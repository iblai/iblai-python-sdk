import logging
import requests
import typing as t


from iblai.helpers.constants import DEFAULT_BASE_URL, DEFAULT_TIMEOUT


log = logging.getLogger(__name__)


def invite_user_to_platform(
    tenant: str, email: str, api_token: str, base_url: t.Optional[str] = None,
) -> dict[str, t.Any] | None:
    """
    Invite user to platform by email
    """
    request_base = (base_url or DEFAULT_BASE_URL).rstrip("/")

    data = {
        "platform_key": tenant,
        "email": email
    }
    headers = {
        "Authorization": f"Api-Token {api_token}",
    }

    response = requests.post(
        f"{request_base}/api/ibl/catalog/invitations/platform/",
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
    else:
        log.error(
            "Failed to invite user (status=%s): %s",
            response.status_code,
            response.text
        )
        return None
