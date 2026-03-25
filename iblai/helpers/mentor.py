import logging
import requests
import typing as t


from iblai.helpers.constants import DEFAULT_BASE_URL, DEFAULT_TIMEOUT


log = logging.getLogger(__name__)


def create_mentor(
    tenant: str, username: str, settings: dict[str, str], api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Create a new mentor with the provided settings.
    """
    request_base = (base_url or DEFAULT_BASE_URL).rstrip("/")

    headers = {"Authorization": f"Api-Token {api_token}"}
    resp = requests.post(
        f"{request_base}/api/ai-mentor/orgs/{tenant}/users/{username}/mentor-with-settings/",
        headers=headers,
        json=settings,
        timeout=DEFAULT_TIMEOUT
    )
    if resp and resp.ok:
        try:
            return resp.json()
        except (ValueError, TypeError) as e:
            log.error("Failed to parse response as JSON: %s", str(e))
            return None
    else:
        log.error(
            "Failed to create mentor (status=%s): %s",
            resp.status_code,
            resp.text,
        )
        return None
