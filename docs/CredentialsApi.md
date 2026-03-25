# iblai.CredentialsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_exim_credentials_course_export_retrieve**](CredentialsApi.md#credentials_exim_credentials_course_export_retrieve) | **GET** /api/credentials/exim/credentials/course/{course_id}/export/ | 
[**credentials_exim_credentials_course_import_create**](CredentialsApi.md#credentials_exim_credentials_course_import_create) | **POST** /api/credentials/exim/credentials/course/{course_id}/import/ | 
[**credentials_orgs_users_assertions_bulk_create**](CredentialsApi.md#credentials_orgs_users_assertions_bulk_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/bulk/ | 
[**credentials_orgs_users_assertions_bulk_create2**](CredentialsApi.md#credentials_orgs_users_assertions_bulk_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/bulk/ | 
[**credentials_orgs_users_assertions_create**](CredentialsApi.md#credentials_orgs_users_assertions_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_create2**](CredentialsApi.md#credentials_orgs_users_assertions_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions-over-time/ | 
[**credentials_orgs_users_assertions_over_time_retrieve2**](CredentialsApi.md#credentials_orgs_users_assertions_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions-over-time/ | 
[**credentials_orgs_users_assertions_retrieve**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/ | 
[**credentials_orgs_users_assertions_retrieve2**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/{entity_id} | 
[**credentials_orgs_users_assertions_retrieve3**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_retrieve4**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions/ | 
[**credentials_orgs_users_assertions_retrieve5**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve5) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions/{entity_id} | 
[**credentials_orgs_users_assertions_retrieve6**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve6) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_update**](CredentialsApi.md#credentials_orgs_users_assertions_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/{entity_id} | 
[**credentials_orgs_users_assertions_update2**](CredentialsApi.md#credentials_orgs_users_assertions_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/assertions/{entity_id} | 
[**credentials_orgs_users_assignments_destroy**](CredentialsApi.md#credentials_orgs_users_assignments_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/{assignment_id} | 
[**credentials_orgs_users_assignments_destroy2**](CredentialsApi.md#credentials_orgs_users_assignments_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/assignments/{assignment_id} | 
[**credentials_orgs_users_assignments_groups_create**](CredentialsApi.md#credentials_orgs_users_assignments_groups_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/groups/ | 
[**credentials_orgs_users_assignments_groups_create2**](CredentialsApi.md#credentials_orgs_users_assignments_groups_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/assignments/groups/ | 
[**credentials_orgs_users_assignments_groups_retrieve**](CredentialsApi.md#credentials_orgs_users_assignments_groups_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/groups/ | 
[**credentials_orgs_users_assignments_groups_retrieve2**](CredentialsApi.md#credentials_orgs_users_assignments_groups_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assignments/groups/ | 
[**credentials_orgs_users_assignments_users_create**](CredentialsApi.md#credentials_orgs_users_assignments_users_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/users/ | 
[**credentials_orgs_users_assignments_users_create2**](CredentialsApi.md#credentials_orgs_users_assignments_users_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/assignments/users/ | 
[**credentials_orgs_users_assignments_users_retrieve**](CredentialsApi.md#credentials_orgs_users_assignments_users_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/users/ | 
[**credentials_orgs_users_assignments_users_retrieve2**](CredentialsApi.md#credentials_orgs_users_assignments_users_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assignments/users/ | 
[**credentials_orgs_users_course_assertions_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/course-assertions-over-time/ | 
[**credentials_orgs_users_course_assertions_over_time_retrieve2**](CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/course-assertions-over-time/ | 
[**credentials_orgs_users_course_credentials_list**](CredentialsApi.md#credentials_orgs_users_course_credentials_list) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/course-credentials/ | 
[**credentials_orgs_users_course_credentials_list2**](CredentialsApi.md#credentials_orgs_users_course_credentials_list2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/course-credentials/ | 
[**credentials_orgs_users_create**](CredentialsApi.md#credentials_orgs_users_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/ | 
[**credentials_orgs_users_create2**](CredentialsApi.md#credentials_orgs_users_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/ | 
[**credentials_orgs_users_credentials_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/credentials-over-time/ | 
[**credentials_orgs_users_credentials_over_time_retrieve2**](CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/credentials-over-time/ | 
[**credentials_orgs_users_destroy**](CredentialsApi.md#credentials_orgs_users_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_destroy2**](CredentialsApi.md#credentials_orgs_users_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
[**credentials_orgs_users_external_mapping_create**](CredentialsApi.md#credentials_orgs_users_external_mapping_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
[**credentials_orgs_users_external_mapping_create2**](CredentialsApi.md#credentials_orgs_users_external_mapping_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
[**credentials_orgs_users_external_mapping_destroy**](CredentialsApi.md#credentials_orgs_users_external_mapping_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
[**credentials_orgs_users_external_mapping_destroy2**](CredentialsApi.md#credentials_orgs_users_external_mapping_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
[**credentials_orgs_users_external_mapping_retrieve**](CredentialsApi.md#credentials_orgs_users_external_mapping_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
[**credentials_orgs_users_external_mapping_retrieve2**](CredentialsApi.md#credentials_orgs_users_external_mapping_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
[**credentials_orgs_users_images_create**](CredentialsApi.md#credentials_orgs_users_images_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/images/ | 
[**credentials_orgs_users_images_create2**](CredentialsApi.md#credentials_orgs_users_images_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/images/ | 
[**credentials_orgs_users_images_retrieve**](CredentialsApi.md#credentials_orgs_users_images_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/images/ | 
[**credentials_orgs_users_images_retrieve2**](CredentialsApi.md#credentials_orgs_users_images_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/images/ | 
[**credentials_orgs_users_issuers_authority_create**](CredentialsApi.md#credentials_orgs_users_issuers_authority_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/authority/ | 
[**credentials_orgs_users_issuers_authority_create2**](CredentialsApi.md#credentials_orgs_users_issuers_authority_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/issuers/authority/ | 
[**credentials_orgs_users_issuers_create**](CredentialsApi.md#credentials_orgs_users_issuers_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/ | 
[**credentials_orgs_users_issuers_create2**](CredentialsApi.md#credentials_orgs_users_issuers_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/issuers/ | 
[**credentials_orgs_users_issuers_destroy**](CredentialsApi.md#credentials_orgs_users_issuers_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_destroy2**](CredentialsApi.md#credentials_orgs_users_issuers_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_retrieve**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/ | 
[**credentials_orgs_users_issuers_retrieve2**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_retrieve3**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/issuers/ | 
[**credentials_orgs_users_issuers_retrieve4**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_update**](CredentialsApi.md#credentials_orgs_users_issuers_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_update2**](CredentialsApi.md#credentials_orgs_users_issuers_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
[**credentials_orgs_users_provider_config_create**](CredentialsApi.md#credentials_orgs_users_provider_config_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
[**credentials_orgs_users_provider_config_create2**](CredentialsApi.md#credentials_orgs_users_provider_config_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
[**credentials_orgs_users_provider_config_destroy**](CredentialsApi.md#credentials_orgs_users_provider_config_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
[**credentials_orgs_users_provider_config_destroy2**](CredentialsApi.md#credentials_orgs_users_provider_config_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
[**credentials_orgs_users_provider_config_retrieve**](CredentialsApi.md#credentials_orgs_users_provider_config_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
[**credentials_orgs_users_provider_config_retrieve2**](CredentialsApi.md#credentials_orgs_users_provider_config_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
[**credentials_orgs_users_retrieve**](CredentialsApi.md#credentials_orgs_users_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/ | 
[**credentials_orgs_users_retrieve2**](CredentialsApi.md#credentials_orgs_users_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_retrieve3**](CredentialsApi.md#credentials_orgs_users_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/ | 
[**credentials_orgs_users_retrieve4**](CredentialsApi.md#credentials_orgs_users_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
[**credentials_orgs_users_update**](CredentialsApi.md#credentials_orgs_users_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_update2**](CredentialsApi.md#credentials_orgs_users_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
[**credentials_providers_retrieve**](CredentialsApi.md#credentials_providers_retrieve) | **GET** /api/credentials/providers/ | 
[**credentials_public_assertions_retrieve**](CredentialsApi.md#credentials_public_assertions_retrieve) | **GET** /api/credentials/public/assertions/{entity_id}/ | 


# **credentials_exim_credentials_course_export_retrieve**
> credentials_exim_credentials_course_export_retrieve(course_id)

Export credential information for a specific course.

Args:
    request: The HTTP request object
    course_id: Course ID to export credentials for

Returns:
    Response: JSON response with credential data

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
api_instance = iblai.CredentialsApi(api_client)
course_id = 'course_id_example' # str | 

try:
    api_instance.credentials_exim_credentials_course_export_retrieve(course_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_exim_credentials_course_export_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

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

# **credentials_exim_credentials_course_import_create**
> credentials_exim_credentials_course_import_create(course_id)

Import credential information for a specific course.

Args:
    request: The HTTP request object
    course_id: Course ID to import credentials for

Returns:
    Response: JSON response with import results

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
api_instance = iblai.CredentialsApi(api_client)
course_id = 'course_id_example' # str | 

try:
    api_instance.credentials_exim_credentials_course_import_create(course_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_exim_credentials_course_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

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

# **credentials_orgs_users_assertions_bulk_create**
> BulkCreateAssertion credentials_orgs_users_assertions_bulk_create(entity_id, platform_key, user_id, bulk_create_assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.bulk_create_assertion import BulkCreateAssertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
bulk_create_assertion = iblai.BulkCreateAssertion() # BulkCreateAssertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_bulk_create(entity_id, platform_key, user_id, bulk_create_assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_bulk_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **bulk_create_assertion** | [**BulkCreateAssertion**](BulkCreateAssertion.md)|  | 

### Return type

[**BulkCreateAssertion**](BulkCreateAssertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assertions_bulk_create2**
> BulkCreateAssertion credentials_orgs_users_assertions_bulk_create2(entity_id, platform_key, username, bulk_create_assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.bulk_create_assertion import BulkCreateAssertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
bulk_create_assertion = iblai.BulkCreateAssertion() # BulkCreateAssertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_bulk_create2(entity_id, platform_key, username, bulk_create_assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_bulk_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_bulk_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **bulk_create_assertion** | [**BulkCreateAssertion**](BulkCreateAssertion.md)|  | 

### Return type

[**BulkCreateAssertion**](BulkCreateAssertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assertions_create**
> Assertion credentials_orgs_users_assertions_create(entity_id, platform_key, user_id, assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_create(entity_id, platform_key, user_id, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assertions_create2**
> Assertion credentials_orgs_users_assertions_create2(entity_id, platform_key, username, assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_create2(entity_id, platform_key, username, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assertions_over_time_retrieve**
> OvertimeWithChangeInfo credentials_orgs_users_assertions_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OvertimeWithChangeInfo**](OvertimeWithChangeInfo.md)

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

# **credentials_orgs_users_assertions_over_time_retrieve2**
> OvertimeWithChangeInfo credentials_orgs_users_assertions_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OvertimeWithChangeInfo**](OvertimeWithChangeInfo.md)

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

# **credentials_orgs_users_assertions_retrieve**
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve(platform_key, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
course = 'course_example' # str |  (optional)
exclude_main_tenant_assertions = True # bool |  (optional)
include_expired = True # bool |  (optional)
include_revoked = True # bool |  (optional)
page = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve(platform_key, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **course** | **str**|  | [optional] 
 **exclude_main_tenant_assertions** | **bool**|  | [optional] 
 **include_expired** | **bool**|  | [optional] 
 **include_revoked** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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

# **credentials_orgs_users_assertions_retrieve2**
> Assertion credentials_orgs_users_assertions_retrieve2(entity_id, platform_key, user_id)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve2(entity_id, platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_retrieve3**
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve3(entity_id, platform_key, user_id)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve3(entity_id, platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve3:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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

# **credentials_orgs_users_assertions_retrieve4**
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve4(platform_key, username, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
course = 'course_example' # str |  (optional)
exclude_main_tenant_assertions = True # bool |  (optional)
include_expired = True # bool |  (optional)
include_revoked = True # bool |  (optional)
page = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve4(platform_key, username, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve4:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **course** | **str**|  | [optional] 
 **exclude_main_tenant_assertions** | **bool**|  | [optional] 
 **include_expired** | **bool**|  | [optional] 
 **include_revoked** | **bool**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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

# **credentials_orgs_users_assertions_retrieve5**
> Assertion credentials_orgs_users_assertions_retrieve5(entity_id, platform_key, username)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve5(entity_id, platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve5:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_retrieve6**
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve6(entity_id, platform_key, username)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve6(entity_id, platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve6:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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

# **credentials_orgs_users_assertions_update**
> Assertion credentials_orgs_users_assertions_update(entity_id, platform_key, user_id, assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_update(entity_id, platform_key, user_id, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assertions_update2**
> Assertion credentials_orgs_users_assertions_update2(entity_id, platform_key, username, assertion)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_update2(entity_id, platform_key, username, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_update2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_update2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_assignments_destroy**
> credentials_orgs_users_assignments_destroy(assignment_id, platform_key, user_id)

Delete a credential assignment using its entity_id.
Only platform admins and department admins can delete assignments.

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
api_instance = iblai.CredentialsApi(api_client)
assignment_id = 'assignment_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_assignments_destroy(assignment_id, platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_assignments_destroy2**
> credentials_orgs_users_assignments_destroy2(assignment_id, platform_key, username)

Delete a credential assignment using its entity_id.
Only platform admins and department admins can delete assignments.

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
api_instance = iblai.CredentialsApi(api_client)
assignment_id = 'assignment_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_destroy2(assignment_id, platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_assignments_groups_create**
> credentials_orgs_users_assignments_groups_create(platform_key, user_id)

Create group assignment with department access validation

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_assignments_groups_create(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_assignments_groups_create2**
> credentials_orgs_users_assignments_groups_create2(platform_key, username)

Create group assignment with department access validation

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_groups_create2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_assignments_groups_retrieve**
> credentials_orgs_users_assignments_groups_retrieve(platform_key, user_id)

Get group assignments with department-aware filtering

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_assignments_groups_retrieve(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_assignments_groups_retrieve2**
> credentials_orgs_users_assignments_groups_retrieve2(platform_key, username)

Get group assignments with department-aware filtering

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_groups_retrieve2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_assignments_users_create**
> credentials_orgs_users_assignments_users_create(platform_key, user_id)

Create assignments with department access validation

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_assignments_users_create(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_assignments_users_create2**
> credentials_orgs_users_assignments_users_create2(platform_key, username)

Create assignments with department access validation

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_users_create2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_assignments_users_retrieve**
> credentials_orgs_users_assignments_users_retrieve(platform_key, user_id)

Get assignments and their corresponding assertions based on user role:
- Regular users: get only their own assignments
- Platform admins: get assignments for all users in their platform
- Department admins: get assignments for users in their department groups

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_assignments_users_retrieve(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_assignments_users_retrieve2**
> credentials_orgs_users_assignments_users_retrieve2(platform_key, username)

Get assignments and their corresponding assertions based on user role:
- Regular users: get only their own assignments
- Platform admins: get assignments for all users in their platform
- Department admins: get assignments for users in their department groups

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_users_retrieve2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_course_assertions_over_time_retrieve**
> OverTime credentials_orgs_users_course_assertions_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_course_assertions_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_course_assertions_over_time_retrieve2**
> OverTime credentials_orgs_users_course_assertions_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_course_assertions_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_course_credentials_list**
> credentials_orgs_users_course_credentials_list(platform_key, user_id, page=page, page_size=page_size)

DRF view mixin that routes all ORM reads to the read replica.

Falls back to the primary database if the replica is unreachable.

Add as the **first** base class on read-only views/viewsets::

    class MyView(ReadReplicaViewMixin, IsPlatformAdminDRFMixin, APIView):
        ...

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_instance.credentials_orgs_users_course_credentials_list(platform_key, user_id, page=page, page_size=page_size)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

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

# **credentials_orgs_users_course_credentials_list2**
> credentials_orgs_users_course_credentials_list2(platform_key, username, page=page, page_size=page_size)

DRF view mixin that routes all ORM reads to the read replica.

Falls back to the primary database if the replica is unreachable.

Add as the **first** base class on read-only views/viewsets::

    class MyView(ReadReplicaViewMixin, IsPlatformAdminDRFMixin, APIView):
        ...

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_instance.credentials_orgs_users_course_credentials_list2(platform_key, username, page=page, page_size=page_size)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_credentials_list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

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

# **credentials_orgs_users_create**
> Credential credentials_orgs_users_create(platform_key, user_id, credential)

API View for managing credentials across a platform.

This endpoint allows creating and retrieving credentials for a specific organization/tenant,
with support for filtering, searching, and pagination.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request

Query Parameters:
    # Platform identification
    platform_org (str, optional): Alternative platform identifier (takes precedence over URL org)

    # Pagination
    page (int, optional): Page number (default: 1)
    page_size (int, optional): Items per page (default: 10, max: 100)

    # Filtering and search
    search (str, optional): Search term to filter credentials by name or description
    course (str, optional): Course ID to filter credentials associated with a specific course
    program (str, optional): Program ID to filter credentials associated with a specific program

Methods:
    GET: Retrieve credentials with filtering and pagination
    POST: Create a new credential

POST Request Body:
    A JSON object containing credential details:
    - name (str): Credential name
    - description (str, optional): Credential description
    - issuer (str): Issuer entity ID
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {
                "next": "URL to next page",
                "previous": "URL to previous page",
                "count": 42,
                "data": [
                    {credential object},
                    {credential object},
                    ...
                ],
                "num_pages": 5,
                "page_number": 1,
                "max_page_size": 100
            }
        }

    POST: A JSON response containing:
        {
            "status": {"success": true, "description": "Created"},
            "result": {credential object}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the platform doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Only public credentials are returned by default

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_create(platform_key, user_id, credential)
    print("The response of CredentialsApi->credentials_orgs_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_create2**
> Credential credentials_orgs_users_create2(platform_key, username, credential)

API View for managing credentials across a platform.

This endpoint allows creating and retrieving credentials for a specific organization/tenant,
with support for filtering, searching, and pagination.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request

Query Parameters:
    # Platform identification
    platform_org (str, optional): Alternative platform identifier (takes precedence over URL org)

    # Pagination
    page (int, optional): Page number (default: 1)
    page_size (int, optional): Items per page (default: 10, max: 100)

    # Filtering and search
    search (str, optional): Search term to filter credentials by name or description
    course (str, optional): Course ID to filter credentials associated with a specific course
    program (str, optional): Program ID to filter credentials associated with a specific program

Methods:
    GET: Retrieve credentials with filtering and pagination
    POST: Create a new credential

POST Request Body:
    A JSON object containing credential details:
    - name (str): Credential name
    - description (str, optional): Credential description
    - issuer (str): Issuer entity ID
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {
                "next": "URL to next page",
                "previous": "URL to previous page",
                "count": 42,
                "data": [
                    {credential object},
                    {credential object},
                    ...
                ],
                "num_pages": 5,
                "page_number": 1,
                "max_page_size": 100
            }
        }

    POST: A JSON response containing:
        {
            "status": {"success": true, "description": "Created"},
            "result": {credential object}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the platform doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Only public credentials are returned by default

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_create2(platform_key, username, credential)
    print("The response of CredentialsApi->credentials_orgs_users_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_credentials_over_time_retrieve**
> OverTime credentials_orgs_users_credentials_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_credentials_over_time_retrieve(platform_key, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_credentials_over_time_retrieve2**
> OverTime credentials_orgs_users_credentials_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)

Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_credentials_over_time_retrieve2(platform_key, username, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_destroy**
> credentials_orgs_users_destroy(entity_id, platform_key, user_id)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_destroy(entity_id, platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_destroy2**
> credentials_orgs_users_destroy2(entity_id, platform_key, username)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_destroy2(entity_id, platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_external_mapping_create**
> ExternalCredentialMapping credentials_orgs_users_external_mapping_create(platform_key, user_id, external_credential_mapping)

Create or update an external credential mapping.

If a mapping doesn't exist for the credential + platform + provider combination,
it will be created. If it exists, it will be updated.

Request Body:
    {
        "credential_id": "credential-entity-id",  // Required
        "provider_name": "accredible",            // Required
        "external_template_id": "123456",         // Optional
        "metadata": {}                            // Optional
    }

Returns:
    - 201 Created: When creating a new mapping
    - 200 OK: When updating an existing mapping

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.external_credential_mapping import ExternalCredentialMapping
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
external_credential_mapping = iblai.ExternalCredentialMapping() # ExternalCredentialMapping | 

try:
    api_response = api_instance.credentials_orgs_users_external_mapping_create(platform_key, user_id, external_credential_mapping)
    print("The response of CredentialsApi->credentials_orgs_users_external_mapping_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **external_credential_mapping** | [**ExternalCredentialMapping**](ExternalCredentialMapping.md)|  | 

### Return type

[**ExternalCredentialMapping**](ExternalCredentialMapping.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_external_mapping_create2**
> ExternalCredentialMapping credentials_orgs_users_external_mapping_create2(platform_key, username, external_credential_mapping)

Create or update an external credential mapping.

If a mapping doesn't exist for the credential + platform + provider combination,
it will be created. If it exists, it will be updated.

Request Body:
    {
        "credential_id": "credential-entity-id",  // Required
        "provider_name": "accredible",            // Required
        "external_template_id": "123456",         // Optional
        "metadata": {}                            // Optional
    }

Returns:
    - 201 Created: When creating a new mapping
    - 200 OK: When updating an existing mapping

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.external_credential_mapping import ExternalCredentialMapping
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
external_credential_mapping = iblai.ExternalCredentialMapping() # ExternalCredentialMapping | 

try:
    api_response = api_instance.credentials_orgs_users_external_mapping_create2(platform_key, username, external_credential_mapping)
    print("The response of CredentialsApi->credentials_orgs_users_external_mapping_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **external_credential_mapping** | [**ExternalCredentialMapping**](ExternalCredentialMapping.md)|  | 

### Return type

[**ExternalCredentialMapping**](ExternalCredentialMapping.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_external_mapping_destroy**
> credentials_orgs_users_external_mapping_destroy(platform_key, user_id)

Delete an external credential mapping.

Request Body:
    {
        "credential_id": "credential-entity-id",  // Required
        "provider_name": "accredible"             // Required
    }

Returns:
    A JSON response confirming deletion

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_external_mapping_destroy(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_external_mapping_destroy2**
> credentials_orgs_users_external_mapping_destroy2(platform_key, username)

Delete an external credential mapping.

Request Body:
    {
        "credential_id": "credential-entity-id",  // Required
        "provider_name": "accredible"             // Required
    }

Returns:
    A JSON response confirming deletion

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_external_mapping_destroy2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_external_mapping_retrieve**
> ExternalCredentialMapping credentials_orgs_users_external_mapping_retrieve(platform_key, user_id)

Retrieve external credential mappings for the platform.

Query Parameters:
    credential_id (str, optional): Filter by credential entity_id
    provider_name (str, optional): Filter by provider name
    page (int, optional): Page number
    page_size (int, optional): Items per page

Returns all mappings for the platform if the user is an admin.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.external_credential_mapping import ExternalCredentialMapping
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_external_mapping_retrieve(platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_external_mapping_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**ExternalCredentialMapping**](ExternalCredentialMapping.md)

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

# **credentials_orgs_users_external_mapping_retrieve2**
> ExternalCredentialMapping credentials_orgs_users_external_mapping_retrieve2(platform_key, username)

Retrieve external credential mappings for the platform.

Query Parameters:
    credential_id (str, optional): Filter by credential entity_id
    provider_name (str, optional): Filter by provider name
    page (int, optional): Page number
    page_size (int, optional): Items per page

Returns all mappings for the platform if the user is an admin.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.external_credential_mapping import ExternalCredentialMapping
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_external_mapping_retrieve2(platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_external_mapping_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_external_mapping_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**ExternalCredentialMapping**](ExternalCredentialMapping.md)

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

# **credentials_orgs_users_images_create**
> UploadedImage credentials_orgs_users_images_create(platform_key, user_id, uploaded_image=uploaded_image)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
uploaded_image = iblai.UploadedImage() # UploadedImage |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_images_create(platform_key, user_id, uploaded_image=uploaded_image)
    print("The response of CredentialsApi->credentials_orgs_users_images_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **uploaded_image** | [**UploadedImage**](UploadedImage.md)|  | [optional] 

### Return type

[**UploadedImage**](UploadedImage.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_images_create2**
> UploadedImage credentials_orgs_users_images_create2(platform_key, username, uploaded_image=uploaded_image)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
uploaded_image = iblai.UploadedImage() # UploadedImage |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_images_create2(platform_key, username, uploaded_image=uploaded_image)
    print("The response of CredentialsApi->credentials_orgs_users_images_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **uploaded_image** | [**UploadedImage**](UploadedImage.md)|  | [optional] 

### Return type

[**UploadedImage**](UploadedImage.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_images_retrieve**
> UploadedImage credentials_orgs_users_images_retrieve(platform_key, user_id)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_images_retrieve(platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_images_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**UploadedImage**](UploadedImage.md)

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

# **credentials_orgs_users_images_retrieve2**
> UploadedImage credentials_orgs_users_images_retrieve2(platform_key, username)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_images_retrieve2(platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_images_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**UploadedImage**](UploadedImage.md)

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

# **credentials_orgs_users_issuers_authority_create**
> IssuerAuthority credentials_orgs_users_issuers_authority_create(platform_key, user_id, issuer_authority)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer_authority import IssuerAuthority
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
issuer_authority = iblai.IssuerAuthority() # IssuerAuthority | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_authority_create(platform_key, user_id, issuer_authority)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_authority_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_authority_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **issuer_authority** | [**IssuerAuthority**](IssuerAuthority.md)|  | 

### Return type

[**IssuerAuthority**](IssuerAuthority.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_authority_create2**
> IssuerAuthority credentials_orgs_users_issuers_authority_create2(platform_key, username, issuer_authority)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer_authority import IssuerAuthority
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
issuer_authority = iblai.IssuerAuthority() # IssuerAuthority | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_authority_create2(platform_key, username, issuer_authority)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_authority_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_authority_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **issuer_authority** | [**IssuerAuthority**](IssuerAuthority.md)|  | 

### Return type

[**IssuerAuthority**](IssuerAuthority.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_create**
> Issuer credentials_orgs_users_issuers_create(platform_key, q, user_id, issuer)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
q = 'q_example' # str | 
user_id = 56 # int | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_create(platform_key, q, user_id, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **q** | **str**|  | 
 **user_id** | **int**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_create2**
> Issuer credentials_orgs_users_issuers_create2(platform_key, q, username, issuer)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
q = 'q_example' # str | 
username = 'username_example' # str | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_create2(platform_key, q, username, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **q** | **str**|  | 
 **username** | **str**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_destroy**
> credentials_orgs_users_issuers_destroy(entity_id, platform_key, user_id)

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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_issuers_destroy(entity_id, platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_issuers_destroy2**
> credentials_orgs_users_issuers_destroy2(entity_id, platform_key, username)

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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_issuers_destroy2(entity_id, platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_issuers_retrieve**
> Issuer credentials_orgs_users_issuers_retrieve(platform_key, q, user_id)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
q = 'q_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve(platform_key, q, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **q** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_retrieve2**
> Issuer credentials_orgs_users_issuers_retrieve2(entity_id, platform_key, user_id)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve2(entity_id, platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_retrieve3**
> Issuer credentials_orgs_users_issuers_retrieve3(platform_key, q, username)

A GET View that validates QueryParams and returns results to a serializer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
q = 'q_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve3(platform_key, q, username)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve3:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **q** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_retrieve4**
> Issuer credentials_orgs_users_issuers_retrieve4(entity_id, platform_key, username)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve4(entity_id, platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve4:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_update**
> Issuer credentials_orgs_users_issuers_update(entity_id, platform_key, user_id, issuer)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_update(entity_id, platform_key, user_id, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_update2**
> Issuer credentials_orgs_users_issuers_update2(entity_id, platform_key, username, issuer)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_update2(entity_id, platform_key, username, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_update2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_update2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_provider_config_create**
> CredentialProviderConfig credentials_orgs_users_provider_config_create(platform_key, user_id, credential_provider_config)

Create or update a provider configuration.

If a configuration doesn't exist for the platform and provider, it will be created.
If it exists, it will be updated.

Request Body:
    {
        "provider_name": "accredible",  // Required
        "config": {...},                 // Optional
        "enabled": true                  // Optional
    }

Returns:
    - 201 Created: When creating a new configuration
    - 200 OK: When updating an existing configuration

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_provider_config import CredentialProviderConfig
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
credential_provider_config = iblai.CredentialProviderConfig() # CredentialProviderConfig | 

try:
    api_response = api_instance.credentials_orgs_users_provider_config_create(platform_key, user_id, credential_provider_config)
    print("The response of CredentialsApi->credentials_orgs_users_provider_config_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **credential_provider_config** | [**CredentialProviderConfig**](CredentialProviderConfig.md)|  | 

### Return type

[**CredentialProviderConfig**](CredentialProviderConfig.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_provider_config_create2**
> CredentialProviderConfig credentials_orgs_users_provider_config_create2(platform_key, username, credential_provider_config)

Create or update a provider configuration.

If a configuration doesn't exist for the platform and provider, it will be created.
If it exists, it will be updated.

Request Body:
    {
        "provider_name": "accredible",  // Required
        "config": {...},                 // Optional
        "enabled": true                  // Optional
    }

Returns:
    - 201 Created: When creating a new configuration
    - 200 OK: When updating an existing configuration

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_provider_config import CredentialProviderConfig
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
credential_provider_config = iblai.CredentialProviderConfig() # CredentialProviderConfig | 

try:
    api_response = api_instance.credentials_orgs_users_provider_config_create2(platform_key, username, credential_provider_config)
    print("The response of CredentialsApi->credentials_orgs_users_provider_config_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **credential_provider_config** | [**CredentialProviderConfig**](CredentialProviderConfig.md)|  | 

### Return type

[**CredentialProviderConfig**](CredentialProviderConfig.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_provider_config_destroy**
> credentials_orgs_users_provider_config_destroy(platform_key, user_id)

Deactivate a provider configuration (sets enabled=False).

Request Body:
    {
        "provider_name": "accredible"  // Required
    }

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_instance.credentials_orgs_users_provider_config_destroy(platform_key, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

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

# **credentials_orgs_users_provider_config_destroy2**
> credentials_orgs_users_provider_config_destroy2(platform_key, username)

Deactivate a provider configuration (sets enabled=False).

Request Body:
    {
        "provider_name": "accredible"  // Required
    }

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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.credentials_orgs_users_provider_config_destroy2(platform_key, username)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

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

# **credentials_orgs_users_provider_config_retrieve**
> CredentialProviderConfig credentials_orgs_users_provider_config_retrieve(platform_key, user_id)

Retrieve provider configurations for the platform.

Query Parameters:
    provider_name (str, optional): Filter to a specific provider
    page (int, optional): Page number
    page_size (int, optional): Items per page

Returns all configurations for the platform if the user is an admin.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_provider_config import CredentialProviderConfig
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_provider_config_retrieve(platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_provider_config_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**CredentialProviderConfig**](CredentialProviderConfig.md)

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

# **credentials_orgs_users_provider_config_retrieve2**
> CredentialProviderConfig credentials_orgs_users_provider_config_retrieve2(platform_key, username)

Retrieve provider configurations for the platform.

Query Parameters:
    provider_name (str, optional): Filter to a specific provider
    page (int, optional): Page number
    page_size (int, optional): Items per page

Returns all configurations for the platform if the user is an admin.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_provider_config import CredentialProviderConfig
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_provider_config_retrieve2(platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_provider_config_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_provider_config_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**CredentialProviderConfig**](CredentialProviderConfig.md)

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

# **credentials_orgs_users_retrieve**
> Credential credentials_orgs_users_retrieve(platform_key, user_id)

Get all credentials for a platform with search and pagination support.

Query Parameters:
- platform_org: Platform org ID (takes precedence over URL org)
- page: Page number (default: 1)
- page_size: Items per page (default: 10, max: 100)
- search: Search term to filter credentials
- course: Course ID to filter credentials
- program: Program ID to filter credentials

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve(platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_retrieve2**
> Credential credentials_orgs_users_retrieve2(entity_id, platform_key, user_id)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve2(entity_id, platform_key, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_retrieve3**
> Credential credentials_orgs_users_retrieve3(platform_key, username)

Get all credentials for a platform with search and pagination support.

Query Parameters:
- platform_org: Platform org ID (takes precedence over URL org)
- page: Page number (default: 1)
- page_size: Items per page (default: 10, max: 100)
- search: Search term to filter credentials
- course: Course ID to filter credentials
- program: Program ID to filter credentials

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve3(platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve3:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_retrieve4**
> Credential credentials_orgs_users_retrieve4(entity_id, platform_key, username)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve4(entity_id, platform_key, username)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve4:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_update**
> Credential credentials_orgs_users_update(entity_id, platform_key, user_id, credential)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
user_id = 56 # int | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_update(entity_id, platform_key, user_id, credential)
    print("The response of CredentialsApi->credentials_orgs_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **user_id** | **int**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_update2**
> Credential credentials_orgs_users_update2(entity_id, platform_key, username, credential)

API View for managing individual credentials.

This endpoint allows retrieving, updating, and deleting specific credentials
identified by their entity_id.

Path Parameters:
    org (str): The organization/tenant identifier
    user_id (str): The user ID making the request
    entity_id (str): The credential entity ID

Methods:
    GET: Retrieve a specific credential
    PUT: Update a specific credential
    DELETE: Delete a specific credential

PUT Request Body:
    A JSON object containing credential details to update:
    - name (str, optional): Credential name
    - description (str, optional): Credential description
    - credential_type (str, optional): Type of credential
    - html_template (str, optional): HTML template for credential rendering
    - css_template (str, optional): CSS template for credential styling
    - icon_image (str, optional): URL to credential icon
    - background_image (str, optional): URL to credential background
    - thumbnail_image (str, optional): URL to credential thumbnail
    - criteria_url (str, optional): URL to credential criteria
    - criteria_text (str, optional): Text description of credential criteria
    - issuing_signal (str, optional): Signal that triggers credential issuance

Returns:
    GET: A JSON response containing:
        {
            "status": {"success": true, "description": "Ok"},
            "result": {credential object}
        }

    PUT: A JSON response containing:
        {
            "status": {"success": true, "description": "Updated"},
            "result": {credential object}
        }

    DELETE: A JSON response indicating success:
        {
            "status": {"success": true, "description": "Deleted"}
        }

Error Responses:
    400 Bad Request: If the request data is invalid
    401 Unauthorized: If the user is not authenticated
    403 Forbidden: If the user does not have permission to access this resource
    404 Not Found: If the credential doesn't exist
    500 Internal Server Error: If an unexpected error occurs

Access Control:
    - Requires CredentialAssignmentPermission
    - Users can only manage credentials they have permission to access

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
platform_key = 'platform_key_example' # str | 
username = 'username_example' # str | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_update2(entity_id, platform_key, username, credential)
    print("The response of CredentialsApi->credentials_orgs_users_update2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_update2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **platform_key** | **str**|  | 
 **username** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_providers_retrieve**
> credentials_providers_retrieve()

Get list of enabled credential providers with pagination.

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
api_instance = iblai.CredentialsApi(api_client)

try:
    api_instance.credentials_providers_retrieve()
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_providers_retrieve: %s\n" % e)
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

# **credentials_public_assertions_retrieve**
> Assertion credentials_public_assertions_retrieve(entity_id)

Public endpoint to retrieve a specific credential assertion by its entity ID.

This endpoint allows public access to view a specific credential assertion
without authentication.

Path Parameters:
    entity_id (str): The assertion entity ID

Returns:
    A JSON response containing the assertion details using the AssertionSerializer format

Error Responses:
    404 Not Found:
        - If the assertion doesn't exist: Empty response with 404 status
        - If the assertion has been revoked: JSON with error detail and revocation reason
    500 Internal Server Error: If an unexpected error occurs

### Example


```python
import iblai
from iblai.models.assertion import Assertion
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 

try:
    api_response = api_instance.credentials_public_assertions_retrieve(entity_id)
    print("The response of CredentialsApi->credentials_public_assertions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_public_assertions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

[**Assertion**](Assertion.md)

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

