import asyncio
import httpx
import json
import logging
import mimetypes
import sys
import typing as t
from pathlib import Path
from websockets.client import connect


from iblai.helpers.constants import DEFAULT_BASE_URL, DEFAULT_WEBSOCKET_URL


log = logging.getLogger(__name__)


async def create_mentor_with_settings(
        tenant: str, username: str, settings: dict[str, str], api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    headers = {
        "Authorization": f"Api-Token {api_token}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{request_base}/api/ai-mentor/orgs/{tenant}/users/{username}/mentor-with-settings/",
            headers=headers,
            json=settings,
        )
        return response


async def create_mentor(
        tenant: str, username: str, settings: dict[str, str], api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:

    mentor_creation_response = await create_mentor_with_settings(
        tenant, username, settings, api_token, base_url=base_url
    )
    if mentor_creation_response.is_success:
        mentor_response_data = mentor_creation_response.json()
        log.info("Successfully created mentor with data: %s", mentor_response_data)
        return mentor_response_data
    else:
        log.error(
            "Failed to create mentor (status=%s): %s",
            mentor_creation_response.status_code,
            mentor_creation_response.text,
        )
    return None


async def upload_document_to_mentor(
    mentor_name: str, file_path: str | Path, tenant: str, username: str, api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    path = Path(file_path)
    payload = {"type": "file", "pathway": mentor_name}
    
    mime_type, encoding = mimetypes.guess_type(path)
    files = [
        (
            "file",
            (
                file_path.name,
                open(path, "rb"),
                mime_type,
            ),
        )
    ]
    headers = {"Authorization": f"Api-Token {api_token}"}
    
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{request_base}/api/ai-index/orgs/{tenant}/users/{username}/documents/train/",
            data=payload,
            files=files,
            headers=headers
        )
        resp_data = resp.json()
        if resp.is_success:
            log.info("Successfully uploaded document for training")
            log.info("Document upload response: %s", resp_data)
            return resp_data
        else:
            log.error(
                "Failed to upload document (status=%s): %s",
                resp.status_code,
                resp.text,
            )


async def wait_for_document_training_to_complete(
    mentor_name: str, 
    tenant: str, 
    username: str, 
    api_token: str, 
    base_url: t.Optional[str] = None,
    max_retries: int = 60,  # 5 minutes with 5-second intervals
    retry_interval: int = 5
) -> bool:
    """
    Wait for document training to complete with timeout protection.
    
    Args:
        mentor_name: Name of the mentor
        tenant: Tenant identifier
        username: Username
        api_token: API token for authentication
        base_url: Optional base URL override
        max_retries: Maximum number of retry attempts (default: 60)
        retry_interval: Seconds to wait between retries (default: 5)
    
    Returns:
        bool: True if training completed successfully, False if timed out
    """
    headers = {"Authorization": f"Api-Token {api_token}"}
    
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    retry_count = 0
    
    async with httpx.AsyncClient() as client:
        while retry_count < max_retries:
            try:
                resp = await client.get(
                    f"{request_base}/api/ai-index/orgs/{tenant}/users/{username}/documents/pathways/{mentor_name}/",
                    headers=headers,
                )

                if resp.is_success:
                    data: list = resp.json()["results"]
                    if all([i["is_trained"] for i in data]):
                        log.info("All documents trained successfully")
                        return True
                else:
                    log.warning(
                        "Failed to check training status (status=%s): %s",
                        resp.status_code,
                        resp.text,
                    )

            except Exception as e:
                log.warning("Error checking training status: %s", str(e))

            retry_count += 1
            if retry_count < max_retries:
                log.info(
                    "Document not trained. Retry %d/%d. Trying again after %d seconds...",
                    retry_count, max_retries, retry_interval
                )
                await asyncio.sleep(retry_interval)
    
    log.error(
        "Document training timed out after %d retries (%d seconds total)",
        max_retries, max_retries * retry_interval
    )
    return False


async def create_chat_session(mentor_name: str, tenant: str, username: str, base_url: t.Optional[str] = None) -> str:
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    # Generate a session id
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{request_base}/api/ai-mentor/orgs/{tenant}/users/{username}/sessions/",
            json={"mentor": mentor_name},
        )
        
        session_id = resp.json().get("session_id")
        log.info("Session id: %s", session_id)
        return session_id


async def chat_with_mentor_async(prompt: str, session_id: str, mentor: str, tenant: str, username: str, api_token: str, base_url: t.Optional[str] = None):
    data = {
        "flow": {
            # `name` is either the unique_id, name or slug  of the mentor in respective order of priority.
            "name": mentor,
            "tenant": tenant,
            "username": username,
            # pathway must be the name of the mentor.
            # `pathway` is the identifier for the vector store path where documents were trained to.
            # Except for special cases, the default pathway name is the name of the mentor
            "pathway": mentor,
        },
        "session_id": session_id,
        # `token` is the access token for the user.
        "token": api_token,
        # `page_content` parameter is optional. it should only be used if you intend
        # to send extra context to the mentor. This is generally the text content of the current webpage.
        # "page_content": "...optional parameter to pass the content of the current web page to the mentor.",
        # `prompt` parameter is the question or message to the mentor
        "prompt": prompt
    }
    
    
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_WEBSOCKET_URL

    ws = await connect(f"{request_base}/ws/langflow/")
    data_without_prompt = {**data}
    data_without_prompt.pop("prompt", "")
    log.info("data without prompt: %s", data_without_prompt)
    await ws.send(json.dumps(data))
    received_data = await ws.recv()
    log.info("%s", received_data)

    # the first message after sending the payload is the status detail.
    # getting a value of `connected` means authentication was successful and
    # the user has permissions to access the said mentor
    log.info("websocket status: %s", json.loads(received_data)["detail"])
    # logger.info("Question: %s", data.get("prompt"))
    await ws.send(json.dumps(data))
    while True:
        try:
            data_rec = await asyncio.wait_for(ws.recv(), timeout=10)
            log.info("received data: %s", data_rec)
            data_json: dict[str, str] = json.loads(data_rec)

            # if `data` is present in the response,
            # then this is a token that needs to be shown to the user.
            data_to_write = data_json.get("data")
            if data_to_write:
                # print the token to the console.
                yield data_to_write
            # if an `eos` value of `True` is received, break the loop.
            # this means the mentor has finished generating the response.
            if data_json.get("eos"):
                log.warning("eos received. breaking out of loop")
                break

        except asyncio.TimeoutError:
            log.warning("timeout error. breaking out of loop")
            break
    await ws.close()

