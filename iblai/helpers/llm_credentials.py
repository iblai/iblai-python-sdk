import logging
import requests
import typing as t


from iblai.helpers.constants import DEFAULT_BASE_URL


log = logging.getLogger(__name__)


def add_llm_credential(
    credential_name: str, credential_value: str, tenant: str, api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Create llm credential for a tenant via the API.
    """
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    data = {
        "name": credential_name,
        "value": {"key": credential_value},
        "platform": "main"
    }
    headers = {
        "Authorization": f"Api-Token {api_token}"
    }
    response = requests.post(
        f"{request_base}/api/ai-account/orgs/{tenant}/credential/",
        headers=headers,
        json=data
    )

    if response and response.ok:
        return response.json()
    else:
        log.error(
            "Failed to add LLM credentials (status=%s): %s",
            response.status_code,
            response.text,
        )


def get_llm_credentials(
    tenant: str, api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Get llm credential for a tenant via the API.
    """
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    headers = {
        "Authorization": f"Api-Token {api_token}"
    }
    response = requests.get(
        f"{request_base}/api/ai-account/orgs/{tenant}/credential/",
        headers=headers
    )

    if response and response.ok:
        return response.json()
    else:
        log.error(
            "Failed to query LLM credentials (status=%s): %s",
            response.status_code,
            response.text,
        )
