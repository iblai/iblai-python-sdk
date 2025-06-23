# iblai.CoreApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_consolidated_token_proxy_create**](CoreApi.md#core_consolidated_token_proxy_create) | **POST** /api/core/consolidated-token/proxy/ | 
[**core_departments_create**](CoreApi.md#core_departments_create) | **POST** /api/core/departments/ | 
[**core_departments_destroy**](CoreApi.md#core_departments_destroy) | **DELETE** /api/core/departments/ | 
[**core_departments_members_bulk_create**](CoreApi.md#core_departments_members_bulk_create) | **POST** /api/core/departments/members/bulk/ | 
[**core_departments_members_check_retrieve**](CoreApi.md#core_departments_members_check_retrieve) | **GET** /api/core/departments/members/check/ | 
[**core_departments_members_create**](CoreApi.md#core_departments_members_create) | **POST** /api/core/departments/members/ | 
[**core_departments_members_destroy**](CoreApi.md#core_departments_members_destroy) | **DELETE** /api/core/departments/members/ | 
[**core_departments_members_retrieve**](CoreApi.md#core_departments_members_retrieve) | **GET** /api/core/departments/members/ | 
[**core_departments_retrieve**](CoreApi.md#core_departments_retrieve) | **GET** /api/core/departments/ | 
[**core_domains_whitelist_create**](CoreApi.md#core_domains_whitelist_create) | **POST** /api/core/domains/whitelist/ | 
[**core_domains_whitelist_retrieve**](CoreApi.md#core_domains_whitelist_retrieve) | **GET** /api/core/domains/whitelist/ | 
[**core_heartbeat_celery_beat_retrieve**](CoreApi.md#core_heartbeat_celery_beat_retrieve) | **GET** /api/core/heartbeat/celery-beat/ | 
[**core_heartbeat_celery_retrieve**](CoreApi.md#core_heartbeat_celery_retrieve) | **GET** /api/core/heartbeat/celery/ | 
[**core_launcher_create**](CoreApi.md#core_launcher_create) | **POST** /api/core/launcher/ | 
[**core_launcher_retrieve**](CoreApi.md#core_launcher_retrieve) | **GET** /api/core/launcher/ | 
[**core_lti1p3_provider_lti_keys_create**](CoreApi.md#core_lti1p3_provider_lti_keys_create) | **POST** /api/core/lti/1p3/provider/lti-keys/ | 
[**core_lti1p3_provider_lti_keys_destroy**](CoreApi.md#core_lti1p3_provider_lti_keys_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_keys_list**](CoreApi.md#core_lti1p3_provider_lti_keys_list) | **GET** /api/core/lti/1p3/provider/lti-keys/ | 
[**core_lti1p3_provider_lti_keys_retrieve**](CoreApi.md#core_lti1p3_provider_lti_keys_retrieve) | **GET** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_keys_update**](CoreApi.md#core_lti1p3_provider_lti_keys_update) | **PUT** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_tools_create**](CoreApi.md#core_lti1p3_provider_lti_tools_create) | **POST** /api/core/lti/1p3/provider/lti-tools/ | 
[**core_lti1p3_provider_lti_tools_destroy**](CoreApi.md#core_lti1p3_provider_lti_tools_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_lti1p3_provider_lti_tools_list**](CoreApi.md#core_lti1p3_provider_lti_tools_list) | **GET** /api/core/lti/1p3/provider/lti-tools/ | 
[**core_lti1p3_provider_lti_tools_retrieve**](CoreApi.md#core_lti1p3_provider_lti_tools_retrieve) | **GET** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_lti1p3_provider_lti_tools_update**](CoreApi.md#core_lti1p3_provider_lti_tools_update) | **PUT** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_orgs_dark_mode_logo_create_create**](CoreApi.md#core_orgs_dark_mode_logo_create_create) | **POST** /api/core/orgs/{org}/dark-mode-logo/create/ | 
[**core_orgs_dark_mode_logo_retrieve**](CoreApi.md#core_orgs_dark_mode_logo_retrieve) | **GET** /api/core/orgs/{org}/dark-mode-logo/ | 
[**core_orgs_favicon_create_create**](CoreApi.md#core_orgs_favicon_create_create) | **POST** /api/core/orgs/{org}/favicon/create/ | 
[**core_orgs_favicon_retrieve**](CoreApi.md#core_orgs_favicon_retrieve) | **GET** /api/core/orgs/{org}/favicon/ | 
[**core_orgs_logo_create_create**](CoreApi.md#core_orgs_logo_create_create) | **POST** /api/core/orgs/{org}/logo/create/ | 
[**core_orgs_logo_retrieve**](CoreApi.md#core_orgs_logo_retrieve) | **GET** /api/core/orgs/{org}/logo/ | 
[**core_orgs_metadata_partial_update**](CoreApi.md#core_orgs_metadata_partial_update) | **PATCH** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_retrieve**](CoreApi.md#core_orgs_metadata_retrieve) | **GET** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_update**](CoreApi.md#core_orgs_metadata_update) | **PUT** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_redirect_tokens_create**](CoreApi.md#core_orgs_redirect_tokens_create) | **POST** /api/core/orgs/{org}/redirect-tokens/ | 
[**core_orgs_redirect_tokens_delete_destroy**](CoreApi.md#core_orgs_redirect_tokens_delete_destroy) | **DELETE** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/delete | 
[**core_orgs_redirect_tokens_retrieve**](CoreApi.md#core_orgs_redirect_tokens_retrieve) | **GET** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/ | 
[**core_orgs_thumbnail_create_create**](CoreApi.md#core_orgs_thumbnail_create_create) | **POST** /api/core/orgs/{org}/thumbnail/create/ | 
[**core_orgs_thumbnail_retrieve**](CoreApi.md#core_orgs_thumbnail_retrieve) | **GET** /api/core/orgs/{org}/thumbnail/ | 
[**core_platform_api_tokens_create**](CoreApi.md#core_platform_api_tokens_create) | **POST** /api/core/platform/api-tokens/ | 
[**core_platform_api_tokens_destroy**](CoreApi.md#core_platform_api_tokens_destroy) | **DELETE** /api/core/platform/api-tokens/{name} | 
[**core_platform_api_tokens_list**](CoreApi.md#core_platform_api_tokens_list) | **GET** /api/core/platform/api-tokens/ | 
[**core_platform_config_site_create**](CoreApi.md#core_platform_config_site_create) | **POST** /api/core/platform/config/site/ | 
[**core_platform_config_site_retrieve**](CoreApi.md#core_platform_config_site_retrieve) | **GET** /api/core/platform/config/site/ | 
[**core_platform_create**](CoreApi.md#core_platform_create) | **POST** /api/core/platform/ | 
[**core_platform_retrieve**](CoreApi.md#core_platform_retrieve) | **GET** /api/core/platform/ | 
[**core_platform_users_retrieve**](CoreApi.md#core_platform_users_retrieve) | **GET** /api/core/platform/users/ | 
[**core_rbac_groups_create**](CoreApi.md#core_rbac_groups_create) | **POST** /api/core/rbac/groups/ | Create RBAC group
[**core_rbac_groups_destroy**](CoreApi.md#core_rbac_groups_destroy) | **DELETE** /api/core/rbac/groups/{id}/ | Delete RBAC group
[**core_rbac_groups_list**](CoreApi.md#core_rbac_groups_list) | **GET** /api/core/rbac/groups/ | List RBAC groups
[**core_rbac_groups_partial_update**](CoreApi.md#core_rbac_groups_partial_update) | **PATCH** /api/core/rbac/groups/{id}/ | Partially update RBAC group
[**core_rbac_groups_retrieve**](CoreApi.md#core_rbac_groups_retrieve) | **GET** /api/core/rbac/groups/{id}/ | Retrieve RBAC group
[**core_rbac_groups_update**](CoreApi.md#core_rbac_groups_update) | **PUT** /api/core/rbac/groups/{id}/ | Update RBAC group
[**core_rbac_policies_create**](CoreApi.md#core_rbac_policies_create) | **POST** /api/core/rbac/policies/ | Create RBAC policy
[**core_rbac_policies_destroy**](CoreApi.md#core_rbac_policies_destroy) | **DELETE** /api/core/rbac/policies/{id}/ | Delete RBAC policy
[**core_rbac_policies_list**](CoreApi.md#core_rbac_policies_list) | **GET** /api/core/rbac/policies/ | List RBAC policies
[**core_rbac_policies_partial_update**](CoreApi.md#core_rbac_policies_partial_update) | **PATCH** /api/core/rbac/policies/{id}/ | Partially update RBAC policy
[**core_rbac_policies_retrieve**](CoreApi.md#core_rbac_policies_retrieve) | **GET** /api/core/rbac/policies/{id}/ | Retrieve RBAC policy
[**core_rbac_policies_update**](CoreApi.md#core_rbac_policies_update) | **PUT** /api/core/rbac/policies/{id}/ | Update RBAC policy
[**core_rbac_roles_create**](CoreApi.md#core_rbac_roles_create) | **POST** /api/core/rbac/roles/ | Create RBAC role
[**core_rbac_roles_destroy**](CoreApi.md#core_rbac_roles_destroy) | **DELETE** /api/core/rbac/roles/{id}/ | Delete RBAC role
[**core_rbac_roles_list**](CoreApi.md#core_rbac_roles_list) | **GET** /api/core/rbac/roles/ | List RBAC roles
[**core_rbac_roles_partial_update**](CoreApi.md#core_rbac_roles_partial_update) | **PATCH** /api/core/rbac/roles/{id}/ | Partially update RBAC role
[**core_rbac_roles_retrieve**](CoreApi.md#core_rbac_roles_retrieve) | **GET** /api/core/rbac/roles/{id}/ | Retrieve RBAC role
[**core_rbac_roles_update**](CoreApi.md#core_rbac_roles_update) | **PUT** /api/core/rbac/roles/{id}/ | Update RBAC role
[**core_session_logout_create**](CoreApi.md#core_session_logout_create) | **POST** /api/core/session/logout/ | 
[**core_signals_edx_create**](CoreApi.md#core_signals_edx_create) | **POST** /api/core/signals/edx/ | 
[**core_token_proxy_create**](CoreApi.md#core_token_proxy_create) | **POST** /api/core/token/proxy/ | 
[**core_token_verify_retrieve**](CoreApi.md#core_token_verify_retrieve) | **GET** /api/core/token/verify/ | 
[**core_user_groups_create**](CoreApi.md#core_user_groups_create) | **POST** /api/core/user_groups/ | 
[**core_user_groups_destroy**](CoreApi.md#core_user_groups_destroy) | **DELETE** /api/core/user_groups/ | 
[**core_user_groups_link_bulk_create**](CoreApi.md#core_user_groups_link_bulk_create) | **POST** /api/core/user_groups/link/bulk/ | 
[**core_user_groups_link_create**](CoreApi.md#core_user_groups_link_create) | **POST** /api/core/user_groups/link/ | 
[**core_user_groups_link_destroy**](CoreApi.md#core_user_groups_link_destroy) | **DELETE** /api/core/user_groups/link/ | 
[**core_user_groups_link_retrieve**](CoreApi.md#core_user_groups_link_retrieve) | **GET** /api/core/user_groups/link/ | 
[**core_user_groups_retrieve**](CoreApi.md#core_user_groups_retrieve) | **GET** /api/core/user_groups/ | 
[**core_users_delete_create**](CoreApi.md#core_users_delete_create) | **POST** /api/core/users/delete/ | 
[**core_users_metadata_proxy_retrieve**](CoreApi.md#core_users_metadata_proxy_retrieve) | **GET** /api/core/users/metadata/proxy/ | 
[**core_users_platforms_create**](CoreApi.md#core_users_platforms_create) | **POST** /api/core/users/platforms/ | 
[**core_users_platforms_list**](CoreApi.md#core_users_platforms_list) | **GET** /api/core/users/platforms/ | 
[**core_users_proxy_bulk_create**](CoreApi.md#core_users_proxy_bulk_create) | **POST** /api/core/users/proxy/bulk/ | 
[**core_users_proxy_create**](CoreApi.md#core_users_proxy_create) | **POST** /api/core/users/proxy/ | 
[**core_users_proxy_retrieve**](CoreApi.md#core_users_proxy_retrieve) | **GET** /api/core/users/proxy/ | 
[**core_users_search_retrieve**](CoreApi.md#core_users_search_retrieve) | **GET** /api/core/users/search/ | 


# **core_consolidated_token_proxy_create**
> TokenProxyOutput core_consolidated_token_proxy_create(token_proxy_input)



Create DM and AXD Tokens for user and platform_key  Params: - Any of user_id, username, or email (choose one only, required) - platform_key: str (required)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.token_proxy_input import TokenProxyInput
from iblai.models.token_proxy_output import TokenProxyOutput
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
token_proxy_input = iblai.TokenProxyInput() # TokenProxyInput | 

try:
    api_response = api_instance.core_consolidated_token_proxy_create(token_proxy_input)
    print("The response of CoreApi->core_consolidated_token_proxy_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_consolidated_token_proxy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_proxy_input** | [**TokenProxyInput**](TokenProxyInput.md)|  | 

### Return type

[**TokenProxyOutput**](TokenProxyOutput.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_create**
> core_departments_create()



Create/update a department

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_create()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_destroy**
> core_departments_destroy()



Delete department

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_destroy()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_members_bulk_create**
> core_departments_members_bulk_create()



Add users to department, or update status

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_members_bulk_create()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_members_bulk_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_members_check_retrieve**
> core_departments_members_check_retrieve()



Get department member admin info of requesting user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_members_check_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_members_check_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_members_create**
> core_departments_members_create()



Add single user to department, or update status

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_members_create()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_members_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_members_destroy**
> core_departments_members_destroy()



Delete department member

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_members_destroy()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_members_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_members_retrieve**
> core_departments_members_retrieve()



Show active users in department (paginated)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_members_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_members_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_departments_retrieve**
> core_departments_retrieve()



Show (active) departments associated with a platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_departments_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_departments_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_domains_whitelist_create**
> WhitelistedDomain core_domains_whitelist_create(whitelisted_domain)



Add a new domain to whitelist

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.whitelisted_domain import WhitelistedDomain
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
whitelisted_domain = iblai.WhitelistedDomain() # WhitelistedDomain | 

try:
    api_response = api_instance.core_domains_whitelist_create(whitelisted_domain)
    print("The response of CoreApi->core_domains_whitelist_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_domains_whitelist_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whitelisted_domain** | [**WhitelistedDomain**](WhitelistedDomain.md)|  | 

### Return type

[**WhitelistedDomain**](WhitelistedDomain.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_domains_whitelist_retrieve**
> core_domains_whitelist_retrieve(url, is_active=is_active)



Check if a domain is whitelisted

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
url = 'url_example' # str | 
is_active = True # bool |  (optional)

try:
    api_instance.core_domains_whitelist_retrieve(url, is_active=is_active)
except Exception as e:
    print("Exception when calling CoreApi->core_domains_whitelist_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 
 **is_active** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_heartbeat_celery_beat_retrieve**
> CeleryHeartbeat core_heartbeat_celery_beat_retrieve()



**Use Case**      Celery Beat heartbeat endpoint.  **Example Request**      GET /api/core/heartbeat/celery-beat/  **Response Values**      * 200 on success.     * 500 on failure.

### Example


```python
import iblai
from iblai.models.celery_heartbeat import CeleryHeartbeat
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_response = api_instance.core_heartbeat_celery_beat_retrieve()
    print("The response of CoreApi->core_heartbeat_celery_beat_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_heartbeat_celery_beat_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CeleryHeartbeat**](CeleryHeartbeat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_heartbeat_celery_retrieve**
> core_heartbeat_celery_retrieve()



**Use Case**      Celery heartbeat endpoint.  **Example Request**      GET /api/core/heartbeat/celery/  **Response Values**      * 200 on success.     * 500 on failure.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_heartbeat_celery_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_heartbeat_celery_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_launcher_create**
> PlatformList core_launcher_create(launcher_view_post_request)



POST: Launch a new edX platform  Params: user_id: The ID of the requesting user (required) key: The Deep LMS subdomain (required) name: The edX platform name (\"optional\") org: The edX organization (\"optional\") lms_url: LMS URL (\"optional\") cms_url: CMS URL (\"optional\") portal_url: Portal URL (\"optional\")

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.launcher_view_post_request import LauncherViewPostRequest
from iblai.models.platform_list import PlatformList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
launcher_view_post_request = iblai.LauncherViewPostRequest() # LauncherViewPostRequest | 

try:
    api_response = api_instance.core_launcher_create(launcher_view_post_request)
    print("The response of CoreApi->core_launcher_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_launcher_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_view_post_request** | [**LauncherViewPostRequest**](LauncherViewPostRequest.md)|  | 

### Return type

[**PlatformList**](PlatformList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_launcher_retrieve**
> PlatformList core_launcher_retrieve(key, user_id=user_id)



GET Launch status  Params: key user_id: Optional

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_list import PlatformList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
key = 'key_example' # str | 
user_id = 56 # int |  (optional)

try:
    api_response = api_instance.core_launcher_retrieve(key, user_id=user_id)
    print("The response of CoreApi->core_launcher_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_launcher_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **user_id** | **int**|  | [optional] 

### Return type

[**PlatformList**](PlatformList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_keys_create**
> LtiKey core_lti1p3_provider_lti_keys_create(lti_key)



Create a new LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
lti_key = iblai.LtiKey() # LtiKey | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_create(lti_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lti_key** | [**LtiKey**](LtiKey.md)|  | 

### Return type

[**LtiKey**](LtiKey.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_keys_destroy**
> core_lti1p3_provider_lti_keys_destroy(id, platform_key)



Delete an LTI Provider Key  **DANGER:** Deleting a key will also delete all Tools that reference that Key. If you need to delete a Key you should first create a new one and update all Tools to reference the new Key before deleting the old one.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_instance.core_lti1p3_provider_lti_keys_destroy(id, platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_keys_list**
> List[LtiKey] core_lti1p3_provider_lti_keys_list(platform_key)



List your LTI Provider Key's

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_list(platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform Key | 

### Return type

[**List[LtiKey]**](LtiKey.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_keys_retrieve**
> LtiKey core_lti1p3_provider_lti_keys_retrieve(id, platform_key)



Get details about a specific LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_retrieve(id, platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

[**LtiKey**](LtiKey.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_keys_update**
> LtiKey core_lti1p3_provider_lti_keys_update(id, lti_key)



Update an LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
lti_key = iblai.LtiKey() # LtiKey | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_update(id, lti_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **lti_key** | [**LtiKey**](LtiKey.md)|  | 

### Return type

[**LtiKey**](LtiKey.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_tools_create**
> LtiTool core_lti1p3_provider_lti_tools_create(lti_tool)



Create a new LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
lti_tool = iblai.LtiTool() # LtiTool | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_create(lti_tool)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lti_tool** | [**LtiTool**](LtiTool.md)|  | 

### Return type

[**LtiTool**](LtiTool.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_tools_destroy**
> core_lti1p3_provider_lti_tools_destroy(id, platform_key)



Delete an LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_instance.core_lti1p3_provider_lti_tools_destroy(id, platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_tools_list**
> List[LtiTool] core_lti1p3_provider_lti_tools_list(platform_key)



List your LTI Tool's

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_list(platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform Key | 

### Return type

[**List[LtiTool]**](LtiTool.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_tools_retrieve**
> LtiTool core_lti1p3_provider_lti_tools_retrieve(id, platform_key)



Get details about a specific LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_retrieve(id, platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

[**LtiTool**](LtiTool.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_lti1p3_provider_lti_tools_update**
> LtiTool core_lti1p3_provider_lti_tools_update(id, lti_tool)



Update an LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
lti_tool = iblai.LtiTool() # LtiTool | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_update(id, lti_tool)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **lti_tool** | [**LtiTool**](LtiTool.md)|  | 

### Return type

[**LtiTool**](LtiTool.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_dark_mode_logo_create_create**
> ImageUpload core_orgs_dark_mode_logo_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_dark_mode_logo_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_dark_mode_logo_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_dark_mode_logo_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_dark_mode_logo_retrieve**
> Dict[str, object] core_orgs_dark_mode_logo_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_dark_mode_logo_retrieve(org)
    print("The response of CoreApi->core_orgs_dark_mode_logo_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_dark_mode_logo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_favicon_create_create**
> ImageUpload core_orgs_favicon_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_favicon_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_favicon_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_favicon_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_favicon_retrieve**
> Dict[str, object] core_orgs_favicon_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_favicon_retrieve(org)
    print("The response of CoreApi->core_orgs_favicon_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_favicon_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_logo_create_create**
> ImageUpload core_orgs_logo_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_logo_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_logo_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_logo_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_logo_retrieve**
> Dict[str, object] core_orgs_logo_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_logo_retrieve(org)
    print("The response of CoreApi->core_orgs_logo_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_logo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_metadata_partial_update**
> PlatformPublicMetadata core_orgs_metadata_partial_update(org, patched_platform_public_metadata=patched_platform_public_metadata)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_platform_public_metadata import PatchedPlatformPublicMetadata
from iblai.models.platform_public_metadata import PlatformPublicMetadata
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
patched_platform_public_metadata = iblai.PatchedPlatformPublicMetadata() # PatchedPlatformPublicMetadata |  (optional)

try:
    api_response = api_instance.core_orgs_metadata_partial_update(org, patched_platform_public_metadata=patched_platform_public_metadata)
    print("The response of CoreApi->core_orgs_metadata_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_platform_public_metadata** | [**PatchedPlatformPublicMetadata**](PatchedPlatformPublicMetadata.md)|  | [optional] 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_metadata_retrieve**
> PlatformPublicMetadata core_orgs_metadata_retrieve(org)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_public_metadata import PlatformPublicMetadata
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_metadata_retrieve(org)
    print("The response of CoreApi->core_orgs_metadata_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_metadata_update**
> PlatformPublicMetadata core_orgs_metadata_update(org, platform_public_metadata=platform_public_metadata)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_public_metadata import PlatformPublicMetadata
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
platform_public_metadata = iblai.PlatformPublicMetadata() # PlatformPublicMetadata |  (optional)

try:
    api_response = api_instance.core_orgs_metadata_update(org, platform_public_metadata=platform_public_metadata)
    print("The response of CoreApi->core_orgs_metadata_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **platform_public_metadata** | [**PlatformPublicMetadata**](PlatformPublicMetadata.md)|  | [optional] 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_redirect_tokens_create**
> RedirectTokenResponse core_orgs_redirect_tokens_create(org, redirect_token_request)



Creates redirect tokens for a URL specified by for a platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.redirect_token_request import RedirectTokenRequest
from iblai.models.redirect_token_response import RedirectTokenResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token_request = iblai.RedirectTokenRequest() # RedirectTokenRequest | 

try:
    api_response = api_instance.core_orgs_redirect_tokens_create(org, redirect_token_request)
    print("The response of CoreApi->core_orgs_redirect_tokens_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token_request** | [**RedirectTokenRequest**](RedirectTokenRequest.md)|  | 

### Return type

[**RedirectTokenResponse**](RedirectTokenResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_redirect_tokens_delete_destroy**
> core_orgs_redirect_tokens_delete_destroy(org, redirect_token)



Delete specific token

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token = 'redirect_token_example' # str | 

try:
    api_instance.core_orgs_redirect_tokens_delete_destroy(org, redirect_token)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_delete_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_redirect_tokens_retrieve**
> RedirectTokenResponse core_orgs_redirect_tokens_retrieve(org, redirect_token)



Returns Redirect URL for the token specified.  ``` Requires user to be a member of the platform with the token passed ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.redirect_token_response import RedirectTokenResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token = 'redirect_token_example' # str | 

try:
    api_response = api_instance.core_orgs_redirect_tokens_retrieve(org, redirect_token)
    print("The response of CoreApi->core_orgs_redirect_tokens_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token** | **str**|  | 

### Return type

[**RedirectTokenResponse**](RedirectTokenResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_thumbnail_create_create**
> ImageUpload core_orgs_thumbnail_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_thumbnail_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_thumbnail_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_thumbnail_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_orgs_thumbnail_retrieve**
> Dict[str, object] core_orgs_thumbnail_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_thumbnail_retrieve(org)
    print("The response of CoreApi->core_orgs_thumbnail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_thumbnail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_api_tokens_create**
> PlatformApiKey core_platform_api_tokens_create(platform_api_key)



Create a new Platform Api Key for the target platform

### Example


```python
import iblai
from iblai.models.platform_api_key import PlatformApiKey
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
platform_api_key = iblai.PlatformApiKey() # PlatformApiKey | 

try:
    api_response = api_instance.core_platform_api_tokens_create(platform_api_key)
    print("The response of CoreApi->core_platform_api_tokens_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_api_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_api_key** | [**PlatformApiKey**](PlatformApiKey.md)|  | 

### Return type

[**PlatformApiKey**](PlatformApiKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_api_tokens_destroy**
> core_platform_api_tokens_destroy(name, platform_key)



Delete Platform Api Key by name in the target platform

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
name = 'name_example' # str | 
platform_key = 'platform_key_example' # str | Platform key of target platform

try:
    api_instance.core_platform_api_tokens_destroy(name, platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_api_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **platform_key** | **str**| Platform key of target platform | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_api_tokens_list**
> List[PlatformApiKey] core_platform_api_tokens_list(platform_key)



List Platform API Key's belonging to the target platform

### Example


```python
import iblai
from iblai.models.platform_api_key import PlatformApiKey
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
platform_key = 'platform_key_example' # str | Platform key of target platform

try:
    api_response = api_instance.core_platform_api_tokens_list(platform_key)
    print("The response of CoreApi->core_platform_api_tokens_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_api_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform key of target platform | 

### Return type

[**List[PlatformApiKey]**](PlatformApiKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_config_site_create**
> Dict[str, object] core_platform_config_site_create(request_body=request_body)



GET /site Get site settings.  POST /site Save site settings.  Params: user_id key field_key (POST) value (POST)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
request_body = None # Dict[str, object] |  (optional)

try:
    api_response = api_instance.core_platform_config_site_create(request_body=request_body)
    print("The response of CoreApi->core_platform_config_site_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_config_site_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_config_site_retrieve**
> Dict[str, object] core_platform_config_site_retrieve(key, user_id=user_id)



GET /site Get site settings.  POST /site Save site settings.  Params: user_id key field_key (POST) value (POST)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
key = 'key_example' # str | 
user_id = 56 # int |  (optional)

try:
    api_response = api_instance.core_platform_config_site_retrieve(key, user_id=user_id)
    print("The response of CoreApi->core_platform_config_site_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_config_site_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **user_id** | **int**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_create**
> PlatformList core_platform_create(platform_update_post_request)



Update platform object  Params: user_id  key new_key (If changing platform key) name  Advanced Params (Don't expose these to users) lms_url cms_url portal_url

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_list import PlatformList
from iblai.models.platform_update_post_request import PlatformUpdatePostRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
platform_update_post_request = iblai.PlatformUpdatePostRequest() # PlatformUpdatePostRequest | 

try:
    api_response = api_instance.core_platform_create(platform_update_post_request)
    print("The response of CoreApi->core_platform_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_update_post_request** | [**PlatformUpdatePostRequest**](PlatformUpdatePostRequest.md)|  | 

### Return type

[**PlatformList**](PlatformList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_retrieve**
> PlatformList core_platform_retrieve(key, user_id=user_id)



GET /api/core/platform/ Get main platform info.  POST /api/core/platform/ Save main platform settings.  Params: user_id (optional) key field_key (POST) value (POST)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_list import PlatformList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
key = 'key_example' # str | 
user_id = 56 # int |  (optional)

try:
    api_response = api_instance.core_platform_retrieve(key, user_id=user_id)
    print("The response of CoreApi->core_platform_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **user_id** | **int**|  | [optional] 

### Return type

[**PlatformList**](PlatformList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_platform_users_retrieve**
> UserPlatformManagementListViewGetResponse core_platform_users_retrieve(page=page, page_size=page_size, platform_key=platform_key, platform_org=platform_org, query=query, sort=sort)



Retrieve users associated with platform  Params: platform_key platform_org  query sort  is_admin: Return tenant admin users

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_platform_management_list_view_get_response import UserPlatformManagementListViewGetResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
page = 56 # int |  (optional)
page_size = 56 # int |  (optional)
platform_key = 'platform_key_example' # str |  (optional)
platform_org = 'platform_org_example' # str |  (optional)
query = 'query_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)

try:
    api_response = api_instance.core_platform_users_retrieve(page=page, page_size=page_size, platform_key=platform_key, platform_org=platform_org, query=query, sort=sort)
    print("The response of CoreApi->core_platform_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_platform_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **platform_key** | **str**|  | [optional] 
 **platform_org** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**UserPlatformManagementListViewGetResponse**](UserPlatformManagementListViewGetResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_create**
> RbacGroup core_rbac_groups_create(rbac_group)

Create RBAC group

Create a new RBAC group for a platform. Users can be assigned during creation.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_group import RbacGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
rbac_group = iblai.RbacGroup() # RbacGroup | 

try:
    # Create RBAC group
    api_response = api_instance.core_rbac_groups_create(rbac_group)
    print("The response of CoreApi->core_rbac_groups_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_group** | [**RbacGroup**](RbacGroup.md)|  | 

### Return type

[**RbacGroup**](RbacGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid input data. Common errors include: - Users do not belong to the specified platform - Invalid user IDs provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_destroy**
> core_rbac_groups_destroy(id, platform_key=platform_key)

Delete RBAC group

Delete an RBAC group and all associated group role assignments.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Group.
platform_key = 'platform_key_example' # str | platform key for authorization check (optional)

try:
    # Delete RBAC group
    api_instance.core_rbac_groups_destroy(id, platform_key=platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Group. | 
 **platform_key** | **str**| platform key for authorization check | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Group deleted successfully |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_list**
> PaginatedRbacGroupList core_rbac_groups_list(page=page, page_size=page_size, platform_key=platform_key)

List RBAC groups

Retrieve a list of RBAC groups. Can be filtered by platform_key.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_rbac_group_list import PaginatedRbacGroupList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str | Filter groups by platform key (optional)

try:
    # List RBAC groups
    api_response = api_instance.core_rbac_groups_list(page=page, page_size=page_size, platform_key=platform_key)
    print("The response of CoreApi->core_rbac_groups_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**| Filter groups by platform key | [optional] 

### Return type

[**PaginatedRbacGroupList**](PaginatedRbacGroupList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_partial_update**
> RbacGroup core_rbac_groups_partial_update(id, patched_rbac_group=patched_rbac_group)

Partially update RBAC group

Partially update an existing RBAC group. Platform validation applies for user assignments.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_rbac_group import PatchedRbacGroup
from iblai.models.rbac_group import RbacGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Group.
patched_rbac_group = iblai.PatchedRbacGroup() # PatchedRbacGroup |  (optional)

try:
    # Partially update RBAC group
    api_response = api_instance.core_rbac_groups_partial_update(id, patched_rbac_group=patched_rbac_group)
    print("The response of CoreApi->core_rbac_groups_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Group. | 
 **patched_rbac_group** | [**PatchedRbacGroup**](PatchedRbacGroup.md)|  | [optional] 

### Return type

[**RbacGroup**](RbacGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data. Common errors include: - Users do not belong to the specified platform - Invalid user IDs provided |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_retrieve**
> RbacGroup core_rbac_groups_retrieve(id)

Retrieve RBAC group

Retrieve details of a specific RBAC group including assigned users.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_group import RbacGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Group.

try:
    # Retrieve RBAC group
    api_response = api_instance.core_rbac_groups_retrieve(id)
    print("The response of CoreApi->core_rbac_groups_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Group. | 

### Return type

[**RbacGroup**](RbacGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_groups_update**
> RbacGroup core_rbac_groups_update(id, rbac_group)

Update RBAC group

Update an existing RBAC group. Platform validation applies for user assignments.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_group import RbacGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Group.
rbac_group = iblai.RbacGroup() # RbacGroup | 

try:
    # Update RBAC group
    api_response = api_instance.core_rbac_groups_update(id, rbac_group)
    print("The response of CoreApi->core_rbac_groups_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Group. | 
 **rbac_group** | [**RbacGroup**](RbacGroup.md)|  | 

### Return type

[**RbacGroup**](RbacGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data. Common errors include: - Users do not belong to the specified platform - Invalid user IDs provided |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_create**
> RbacPolicy core_rbac_policies_create(rbac_policy)

Create RBAC policy

Create a new RBAC policy that defines resource access for a role

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_policy import RbacPolicy
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
rbac_policy = iblai.RbacPolicy() # RbacPolicy | 

try:
    # Create RBAC policy
    api_response = api_instance.core_rbac_policies_create(rbac_policy)
    print("The response of CoreApi->core_rbac_policies_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_policy** | [**RbacPolicy**](RbacPolicy.md)|  | 

### Return type

[**RbacPolicy**](RbacPolicy.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid input data. Common errors include: invalid user/group IDs, users/groups not belonging to the platform, or invalid resource paths. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_destroy**
> core_rbac_policies_destroy(id, platform_key=platform_key)

Delete RBAC policy

Delete an RBAC policy.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Policy.
platform_key = 'platform_key_example' # str | platform key for authorization check (optional)

try:
    # Delete RBAC policy
    api_instance.core_rbac_policies_destroy(id, platform_key=platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Policy. | 
 **platform_key** | **str**| platform key for authorization check | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Policy deleted successfully |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_list**
> PaginatedRbacPolicyList core_rbac_policies_list(page=page, page_size=page_size, platform_key=platform_key, role_id=role_id)

List RBAC policies

Retrieve a list of RBAC policies. Can be filtered by platform_key or role_id.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_rbac_policy_list import PaginatedRbacPolicyList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str | Filter policies by platform key (optional)
role_id = 56 # int | Filter policies by role ID (optional)

try:
    # List RBAC policies
    api_response = api_instance.core_rbac_policies_list(page=page, page_size=page_size, platform_key=platform_key, role_id=role_id)
    print("The response of CoreApi->core_rbac_policies_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**| Filter policies by platform key | [optional] 
 **role_id** | **int**| Filter policies by role ID | [optional] 

### Return type

[**PaginatedRbacPolicyList**](PaginatedRbacPolicyList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_partial_update**
> RbacPolicy core_rbac_policies_partial_update(id, patched_rbac_policy=patched_rbac_policy)

Partially update RBAC policy

Partially update an existing RBAC policy. Only provided fields will be updated.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_rbac_policy import PatchedRbacPolicy
from iblai.models.rbac_policy import RbacPolicy
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Policy.
patched_rbac_policy = iblai.PatchedRbacPolicy() # PatchedRbacPolicy |  (optional)

try:
    # Partially update RBAC policy
    api_response = api_instance.core_rbac_policies_partial_update(id, patched_rbac_policy=patched_rbac_policy)
    print("The response of CoreApi->core_rbac_policies_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Policy. | 
 **patched_rbac_policy** | [**PatchedRbacPolicy**](PatchedRbacPolicy.md)|  | [optional] 

### Return type

[**RbacPolicy**](RbacPolicy.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data. Common errors include: invalid user/group IDs, users/groups not belonging to the platform, or invalid resource paths. |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_retrieve**
> RbacPolicy core_rbac_policies_retrieve(id)

Retrieve RBAC policy

Retrieve details of a specific RBAC policy, including role, platform, resources, users, and groups.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_policy import RbacPolicy
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Policy.

try:
    # Retrieve RBAC policy
    api_response = api_instance.core_rbac_policies_retrieve(id)
    print("The response of CoreApi->core_rbac_policies_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Policy. | 

### Return type

[**RbacPolicy**](RbacPolicy.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_policies_update**
> RbacPolicy core_rbac_policies_update(id, rbac_policy)

Update RBAC policy

Update an existing RBAC policy.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_policy import RbacPolicy
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Policy.
rbac_policy = iblai.RbacPolicy() # RbacPolicy | 

try:
    # Update RBAC policy
    api_response = api_instance.core_rbac_policies_update(id, rbac_policy)
    print("The response of CoreApi->core_rbac_policies_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_policies_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Policy. | 
 **rbac_policy** | [**RbacPolicy**](RbacPolicy.md)|  | 

### Return type

[**RbacPolicy**](RbacPolicy.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data. Common errors include: invalid user/group IDs, users/groups not belonging to the platform, or invalid resource paths. |  -  |
**404** | Policy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_create**
> RbacRole core_rbac_roles_create(rbac_role)

Create RBAC role

Create a new RBAC role for a platform.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_role import RbacRole
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
rbac_role = iblai.RbacRole() # RbacRole | 

try:
    # Create RBAC role
    api_response = api_instance.core_rbac_roles_create(rbac_role)
    print("The response of CoreApi->core_rbac_roles_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_role** | [**RbacRole**](RbacRole.md)|  | 

### Return type

[**RbacRole**](RbacRole.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid input data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_destroy**
> core_rbac_roles_destroy(id, platform_key=platform_key)

Delete RBAC role

Delete an RBAC role.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Role.
platform_key = 'platform_key_example' # str | platform key for authorization check (optional)

try:
    # Delete RBAC role
    api_instance.core_rbac_roles_destroy(id, platform_key=platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Role. | 
 **platform_key** | **str**| platform key for authorization check | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Role deleted successfully |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_list**
> PaginatedRbacRoleList core_rbac_roles_list(page=page, page_size=page_size, platform_key=platform_key)

List RBAC roles

Retrieve a list of RBAC roles. Can be filtered by platform_key.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_rbac_role_list import PaginatedRbacRoleList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str | Filter roles by platform key (optional)

try:
    # List RBAC roles
    api_response = api_instance.core_rbac_roles_list(page=page, page_size=page_size, platform_key=platform_key)
    print("The response of CoreApi->core_rbac_roles_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**| Filter roles by platform key | [optional] 

### Return type

[**PaginatedRbacRoleList**](PaginatedRbacRoleList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_partial_update**
> RbacRole core_rbac_roles_partial_update(id, patched_rbac_role=patched_rbac_role)

Partially update RBAC role

Partially update an existing RBAC role.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_rbac_role import PatchedRbacRole
from iblai.models.rbac_role import RbacRole
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Role.
patched_rbac_role = iblai.PatchedRbacRole() # PatchedRbacRole |  (optional)

try:
    # Partially update RBAC role
    api_response = api_instance.core_rbac_roles_partial_update(id, patched_rbac_role=patched_rbac_role)
    print("The response of CoreApi->core_rbac_roles_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Role. | 
 **patched_rbac_role** | [**PatchedRbacRole**](PatchedRbacRole.md)|  | [optional] 

### Return type

[**RbacRole**](RbacRole.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_retrieve**
> RbacRole core_rbac_roles_retrieve(id)

Retrieve RBAC role

Retrieve details of a specific RBAC role.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_role import RbacRole
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Role.

try:
    # Retrieve RBAC role
    api_response = api_instance.core_rbac_roles_retrieve(id)
    print("The response of CoreApi->core_rbac_roles_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Role. | 

### Return type

[**RbacRole**](RbacRole.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_rbac_roles_update**
> RbacRole core_rbac_roles_update(id, rbac_role)

Update RBAC role

Update an existing RBAC role.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.rbac_role import RbacRole
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
id = 56 # int | A unique integer value identifying this RBAC Role.
rbac_role = iblai.RbacRole() # RbacRole | 

try:
    # Update RBAC role
    api_response = api_instance.core_rbac_roles_update(id, rbac_role)
    print("The response of CoreApi->core_rbac_roles_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_rbac_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RBAC Role. | 
 **rbac_role** | [**RbacRole**](RbacRole.md)|  | 

### Return type

[**RbacRole**](RbacRole.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid input data |  -  |
**404** | Role not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_session_logout_create**
> core_session_logout_create()



Invalidate all tokens for the authenticated user

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_session_logout_create()
except Exception as e:
    print("Exception when calling CoreApi->core_session_logout_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_signals_edx_create**
> core_signals_edx_create(edx_signal_receiver_request)



POST signals/edx/

### Example


```python
import iblai
from iblai.models.edx_signal_receiver_request import EdxSignalReceiverRequest
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
edx_signal_receiver_request = iblai.EdxSignalReceiverRequest() # EdxSignalReceiverRequest | 

try:
    api_instance.core_signals_edx_create(edx_signal_receiver_request)
except Exception as e:
    print("Exception when calling CoreApi->core_signals_edx_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edx_signal_receiver_request** | [**EdxSignalReceiverRequest**](EdxSignalReceiverRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_token_proxy_create**
> core_token_proxy_create()



Param: Any of user_id/username/email

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_token_proxy_create()
except Exception as e:
    print("Exception when calling CoreApi->core_token_proxy_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_token_verify_retrieve**
> core_token_verify_retrieve()



Check token user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_token_verify_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_token_verify_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_create**
> core_user_groups_create()



Create/update a user group

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_create()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_destroy**
> core_user_groups_destroy()



Delete user group

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_destroy()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_link_bulk_create**
> core_user_groups_link_bulk_create()



Add users to user group, or update status

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_link_bulk_create()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_link_bulk_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_link_create**
> core_user_groups_link_create()



Add single user to user group, or update status

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_link_create()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_link_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_link_destroy**
> core_user_groups_link_destroy()



Delete user group link

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_link_destroy()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_link_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_link_retrieve**
> core_user_groups_link_retrieve()



Show active users in user group (paginated)  group_id is numeric ID of group

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_link_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_link_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_user_groups_retrieve**
> core_user_groups_retrieve()



Show (active) user groups associated with a platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)

try:
    api_instance.core_user_groups_retrieve()
except Exception as e:
    print("Exception when calling CoreApi->core_user_groups_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_delete_create**
> UserDeleteAPIResponse core_users_delete_create(user_delete_api_request=user_delete_api_request)



Initiates the account deletion process for the authenticated user or specified username.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_delete_api_request import UserDeleteAPIRequest
from iblai.models.user_delete_api_response import UserDeleteAPIResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
user_delete_api_request = iblai.UserDeleteAPIRequest() # UserDeleteAPIRequest |  (optional)

try:
    api_response = api_instance.core_users_delete_create(user_delete_api_request=user_delete_api_request)
    print("The response of CoreApi->core_users_delete_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_delete_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_delete_api_request** | [**UserDeleteAPIRequest**](UserDeleteAPIRequest.md)|  | [optional] 

### Return type

[**UserDeleteAPIResponse**](UserDeleteAPIResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_metadata_proxy_retrieve**
> core_users_metadata_proxy_retrieve(email=email, user_id=user_id, username=username)



Get detailed user information.  Make permission check for platform admins here, then proxy request to edx.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
email = 'email_example' # str |  (optional)
user_id = 56 # int |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_instance.core_users_metadata_proxy_retrieve(email=email, user_id=user_id, username=username)
except Exception as e:
    print("Exception when calling CoreApi->core_users_metadata_proxy_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 
 **user_id** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_platforms_create**
> core_users_platforms_create(user_platform_view_post_request)



Explicitly link platform to user_id  Params: user_id platform_key added_on (optional) expired_on (optional) is_admin (optional) active (optional)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_platform_view_post_request import UserPlatformViewPostRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
user_platform_view_post_request = iblai.UserPlatformViewPostRequest() # UserPlatformViewPostRequest | 

try:
    api_instance.core_users_platforms_create(user_platform_view_post_request)
except Exception as e:
    print("Exception when calling CoreApi->core_users_platforms_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_platform_view_post_request** | [**UserPlatformViewPostRequest**](UserPlatformViewPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_platforms_list**
> List[UserPlatformLink] core_users_platforms_list(email=email, user_id=user_id, username=username)



Retrieve platforms associated with user_id  Params: user_id username email

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_platform_link import UserPlatformLink
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
email = 'email_example' # str |  (optional)
user_id = 56 # int |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.core_users_platforms_list(email=email, user_id=user_id, username=username)
    print("The response of CoreApi->core_users_platforms_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_platforms_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 
 **user_id** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**List[UserPlatformLink]**](UserPlatformLink.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_proxy_bulk_create**
> List[Dict[str, str]] core_users_proxy_bulk_create(user_proxy_bulk_request)



Add proxy users by bulk  Params: users: list of user objects ``` [     {\"user_id\": 1, ...},     {\"user_id\": 2, ...} ] ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_proxy_bulk_request import UserProxyBulkRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
user_proxy_bulk_request = {"users":[{"user_id":1,"username":"test_user1","email":"test_user1@example.com"},{"user_id":2,"username":"test_user2","email":"test_user2@example.com"}]} # UserProxyBulkRequest | 

try:
    api_response = api_instance.core_users_proxy_bulk_create(user_proxy_bulk_request)
    print("The response of CoreApi->core_users_proxy_bulk_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_proxy_bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_proxy_bulk_request** | [**UserProxyBulkRequest**](UserProxyBulkRequest.md)|  | 

### Return type

**List[Dict[str, str]]**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_proxy_create**
> UserProxyPostResponse core_users_proxy_create(user_proxy_post_request)



Add proxy user  Params: user_id username email edx_data data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_proxy_post_request import UserProxyPostRequest
from iblai.models.user_proxy_post_response import UserProxyPostResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
user_proxy_post_request = iblai.UserProxyPostRequest() # UserProxyPostRequest | 

try:
    api_response = api_instance.core_users_proxy_create(user_proxy_post_request)
    print("The response of CoreApi->core_users_proxy_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_proxy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_proxy_post_request** | [**UserProxyPostRequest**](UserProxyPostRequest.md)|  | 

### Return type

[**UserProxyPostResponse**](UserProxyPostResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_proxy_retrieve**
> UserProxyGetResponse core_users_proxy_retrieve(email=email, user_id=user_id, username=username)



Retrieve proxy user information by user_id

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_proxy_get_response import UserProxyGetResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
email = 'email_example' # str |  (optional)
user_id = 56 # int |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.core_users_proxy_retrieve(email=email, user_id=user_id, username=username)
    print("The response of CoreApi->core_users_proxy_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_proxy_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 
 **user_id** | **int**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**UserProxyGetResponse**](UserProxyGetResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_search_retrieve**
> UserSearchViewGetResponse core_users_search_retrieve(page=page, page_size=page_size, query=query, sort=sort)



Retrieve users based on query Not intended for public use with multitenant platforms  Params: query sort

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_search_view_get_response import UserSearchViewGetResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
page = 56 # int |  (optional)
page_size = 56 # int |  (optional)
query = 'query_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)

try:
    api_response = api_instance.core_users_search_retrieve(page=page, page_size=page_size, query=query, sort=sort)
    print("The response of CoreApi->core_users_search_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_users_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **query** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**UserSearchViewGetResponse**](UserSearchViewGetResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

