import logging
import requests
import typing as t


from iblai.helpers.constants import DEFAULT_BASE_URL


log = logging.getLogger(__name__)


def create_mentor(
    tenant: str, username: str, settings: dict[str, str], api_token: str, base_url: t.Optional[str] = None
) -> dict[str, t.Any] | None:
    """
    Create a new mentor with the provided settings.
    """
    request_base = base_url
    if not base_url:
        request_base = DEFAULT_BASE_URL
    
    headers = {"Authorization": f"Api-Token {api_token}"}
    resp = requests.post(
        f"{request_base}/api/ai-mentor/orgs/{tenant}/users/{username}/mentor-with-settings/",
        headers=headers,
        json=settings,
    )
    if resp and resp.ok:
        return resp.json()
    else:
        log.error(
            "Failed to create mentor (status=%s): %s",
            resp.status_code,
            resp.text,
        )

