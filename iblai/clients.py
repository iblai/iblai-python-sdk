from .api_client import ApiClient
from .configuration import Configuration


def get_platform_api_client(host: str, key: str) -> ApiClient:
    """Return ApiClient configured to use an Platform Api Key token"""
    config = Configuration(
        host=host,
        api_key={"PlatformApiKeyAuthentication": key},
        api_key_prefix={"PlatformApiKeyAuthentication": "Api-Token"},
    )
    client = ApiClient(config)
    return client
