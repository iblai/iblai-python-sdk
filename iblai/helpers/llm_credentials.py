import logging
import requests
import typing as t


from iblai.helpers.constants import DEFAULT_BASE_URL, DEFAULT_TIMEOUT


log = logging.getLogger(__name__)


def add_llm_credential(
    credential_name: str, credential_value: str, tenant: str, api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Create llm credential for a tenant via the API.
    If the credential already exists, it will be updated with the new value.
    """
    request_base = (base_url or DEFAULT_BASE_URL).rstrip("/")

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
        json=data,
        timeout=DEFAULT_TIMEOUT
    )

    if response and response.ok:
        try:
            return response.json()
        except (ValueError, TypeError) as e:
            log.error("Failed to parse response as JSON: %s", str(e))
            return None

    # Handle duplicate credential — update the existing one
    if response.status_code == 400:
        try:
            error_data = response.json()
            non_field_errors = error_data.get("non_field_errors", [])
            if any("unique set" in str(e).lower() for e in non_field_errors):
                log.info("Credential '%s' already exists, updating...", credential_name)
                update_response = requests.patch(
                    f"{request_base}/api/ai-account/orgs/{tenant}/credential/{credential_name}/",
                    headers=headers,
                    json={"value": {"key": credential_value}},
                    timeout=DEFAULT_TIMEOUT
                )
                if update_response and update_response.ok:
                    try:
                        return update_response.json()
                    except (ValueError, TypeError) as e:
                        log.error("Failed to parse update response as JSON: %s", str(e))
                        return None
                else:
                    log.error(
                        "Failed to update existing credential (status=%s): %s",
                        update_response.status_code,
                        update_response.text,
                    )
                    return None
        except (ValueError, TypeError):
            pass

    log.error(
        "Failed to add LLM credentials (status=%s): %s",
        response.status_code,
        response.text,
    )
    return None


def get_llm_credentials(
    tenant: str, api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Get llm credential for a tenant via the API.
    """
    request_base = (base_url or DEFAULT_BASE_URL).rstrip("/")

    headers = {
        "Authorization": f"Api-Token {api_token}"
    }
    response = requests.get(
        f"{request_base}/api/ai-account/orgs/{tenant}/credential/",
        headers=headers,
        timeout=DEFAULT_TIMEOUT
    )

    if response and response.ok:
        try:
            return response.json()
        except (ValueError, TypeError) as e:
            log.error("Failed to parse response as JSON: %s", str(e))
            return None
    else:
        log.error(
            "Failed to query LLM credentials (status=%s): %s",
            response.status_code,
            response.text,
        )
        return None
