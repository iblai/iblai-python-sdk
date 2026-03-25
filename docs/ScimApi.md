# iblai.ScimApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_members**](ScimApi.md#add_group_members) | **POST** /api/orgs/{platform_key}/scim/v2/Groups/{id}/add_members | Add members to an existing RBAC group
[**create_user**](ScimApi.md#create_user) | **POST** /api/orgs/{platform_key}/scim/v2/Users | Create a new user in the system
[**delete_group**](ScimApi.md#delete_group) | **DELETE** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Delete an existing RBAC group
[**delete_group2**](ScimApi.md#delete_group2) | **DELETE** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Delete an existing RBAC group
[**delete_user**](ScimApi.md#delete_user) | **DELETE** /api/orgs/{platform_key}/scim/v2/Users/{id} | Delete a user (not supported)
[**delete_user2**](ScimApi.md#delete_user2) | **DELETE** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Delete a user (not supported)
[**list_groups**](ScimApi.md#list_groups) | **GET** /api/orgs/{platform_key}/scim/v2/Groups | List existing RBAC groups
[**list_users**](ScimApi.md#list_users) | **GET** /api/orgs/{platform_key}/scim/v2/Users | List users in the system
[**manage_group**](ScimApi.md#manage_group) | **POST** /api/orgs/{platform_key}/scim/v2/Groups | Manage existing user group
[**partial_update_group**](ScimApi.md#partial_update_group) | **PATCH** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Partially update an existing RBAC group
[**partial_update_group2**](ScimApi.md#partial_update_group2) | **PATCH** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Partially update an existing RBAC group
[**partial_update_user**](ScimApi.md#partial_update_user) | **PATCH** /api/orgs/{platform_key}/scim/v2/Users/{id} | Partially update an existing user
[**partial_update_user2**](ScimApi.md#partial_update_user2) | **PATCH** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Partially update an existing user
[**remove_group_members**](ScimApi.md#remove_group_members) | **POST** /api/orgs/{platform_key}/scim/v2/Groups/{id}/remove_members | Remove members from an existing RBAC group
[**retrieve_group**](ScimApi.md#retrieve_group) | **GET** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Get details of a specific RBAC group
[**retrieve_group2**](ScimApi.md#retrieve_group2) | **GET** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Get details of a specific RBAC group
[**retrieve_user**](ScimApi.md#retrieve_user) | **GET** /api/orgs/{platform_key}/scim/v2/Users/{id} | Get details of a specific user
[**retrieve_user2**](ScimApi.md#retrieve_user2) | **GET** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Get details of a specific user
[**update_group**](ScimApi.md#update_group) | **PUT** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Update an existing RBAC group
[**update_group2**](ScimApi.md#update_group2) | **PUT** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Update an existing RBAC group
[**update_user**](ScimApi.md#update_user) | **PUT** /api/orgs/{platform_key}/scim/v2/Users/{id} | Update a user
[**update_user2**](ScimApi.md#update_user2) | **PUT** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Update a user


# **add_group_members**
> SCIMGroup add_group_members(id, platform_key, format=format)

Add members to an existing RBAC group

Add members to an existing RBAC group using SCIM patch operations

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Add members to an existing RBAC group
    api_response = api_instance.add_group_members(id, platform_key, format=format)
    print("The response of ScimApi->add_group_members:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->add_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> SCIMUserResponse create_user(platform_key, scim_user_create_request, format=format)

Create a new user in the system

Create a new user in the system for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_create_request import SCIMUserCreateRequest
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
platform_key = 'platform_key_example' # str | 
scim_user_create_request = iblai.SCIMUserCreateRequest() # SCIMUserCreateRequest | 
format = 'format_example' # str |  (optional)

try:
    # Create a new user in the system
    api_response = api_instance.create_user(platform_key, scim_user_create_request, format=format)
    print("The response of ScimApi->create_user:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **scim_user_create_request** | [**SCIMUserCreateRequest**](SCIMUserCreateRequest.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> object delete_group(id, platform_key, format=format)

Delete an existing RBAC group

Delete an existing RBAC group from the system

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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Delete an existing RBAC group
    api_response = api_instance.delete_group(id, platform_key, format=format)
    print("The response of ScimApi->delete_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group2**
> object delete_group2(id, platform_key, format=format)

Delete an existing RBAC group

Delete an existing RBAC group from the system

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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Delete an existing RBAC group
    api_response = api_instance.delete_group2(id, platform_key, format=format)
    print("The response of ScimApi->delete_group2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->delete_group2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id, platform_key, format=format)

Delete a user (not supported)

Delete a user for the specified platform (not supported)

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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Delete a user (not supported)
    api_instance.delete_user(id, platform_key, format=format)
except Exception as e:
    print("Exception when calling ScimApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user2**
> delete_user2(id, platform_key, format=format)

Delete a user (not supported)

Delete a user for the specified platform (not supported)

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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Delete a user (not supported)
    api_instance.delete_user2(id, platform_key, format=format)
except Exception as e:
    print("Exception when calling ScimApi->delete_user2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> List[SCIMGroupListResponse] list_groups(platform_key, format=format)

List existing RBAC groups

List all existing RBAC groups for the specified platform. Only returns groups that have been pre-created in the RBAC system.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group_list_response import SCIMGroupListResponse
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
api_instance = iblai.ScimApi(api_client)
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # List existing RBAC groups
    api_response = api_instance.list_groups(platform_key, format=format)
    print("The response of ScimApi->list_groups:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**List[SCIMGroupListResponse]**](SCIMGroupListResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[SCIMUserListResponse] list_users(platform_key, format=format)

List users in the system

List users in the system for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_list_response import SCIMUserListResponse
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
api_instance = iblai.ScimApi(api_client)
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # List users in the system
    api_response = api_instance.list_users(platform_key, format=format)
    print("The response of ScimApi->list_users:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**List[SCIMUserListResponse]**](SCIMUserListResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manage_group**
> SCIMGroup manage_group(platform_key, scim_group, format=format)

Manage existing user group

Add/remove users from an existing RBAC group for the specified platform. Does not create new groups.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
platform_key = 'platform_key_example' # str | 
scim_group = iblai.SCIMGroup() # SCIMGroup | 
format = 'format_example' # str |  (optional)

try:
    # Manage existing user group
    api_response = api_instance.manage_group(platform_key, scim_group, format=format)
    print("The response of ScimApi->manage_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->manage_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **scim_group** | [**SCIMGroup**](SCIMGroup.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_group**
> SCIMGroup partial_update_group(id, platform_key, format=format, patched_scim_group=patched_scim_group)

Partially update an existing RBAC group

Partially update an existing RBAC group's name, description, and members for the specified platform using PATCH method

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_scim_group import PatchedSCIMGroup
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)
patched_scim_group = iblai.PatchedSCIMGroup() # PatchedSCIMGroup |  (optional)

try:
    # Partially update an existing RBAC group
    api_response = api_instance.partial_update_group(id, platform_key, format=format, patched_scim_group=patched_scim_group)
    print("The response of ScimApi->partial_update_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->partial_update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 
 **patched_scim_group** | [**PatchedSCIMGroup**](PatchedSCIMGroup.md)|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_group2**
> SCIMGroup partial_update_group2(id, platform_key, format=format, patched_scim_group=patched_scim_group)

Partially update an existing RBAC group

Partially update an existing RBAC group's name, description, and members for the specified platform using PATCH method

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_scim_group import PatchedSCIMGroup
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)
patched_scim_group = iblai.PatchedSCIMGroup() # PatchedSCIMGroup |  (optional)

try:
    # Partially update an existing RBAC group
    api_response = api_instance.partial_update_group2(id, platform_key, format=format, patched_scim_group=patched_scim_group)
    print("The response of ScimApi->partial_update_group2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->partial_update_group2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 
 **patched_scim_group** | [**PatchedSCIMGroup**](PatchedSCIMGroup.md)|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_user**
> SCIMUserResponse partial_update_user(id, platform_key, format=format, patched_scim_user_response=patched_scim_user_response)

Partially update an existing user

Partially update an existing user's information using PATCH method

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_scim_user_response import PatchedSCIMUserResponse
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)
patched_scim_user_response = iblai.PatchedSCIMUserResponse() # PatchedSCIMUserResponse |  (optional)

try:
    # Partially update an existing user
    api_response = api_instance.partial_update_user(id, platform_key, format=format, patched_scim_user_response=patched_scim_user_response)
    print("The response of ScimApi->partial_update_user:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->partial_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 
 **patched_scim_user_response** | [**PatchedSCIMUserResponse**](PatchedSCIMUserResponse.md)|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_user2**
> SCIMUserResponse partial_update_user2(id, platform_key, format=format, patched_scim_user_response=patched_scim_user_response)

Partially update an existing user

Partially update an existing user's information using PATCH method

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_scim_user_response import PatchedSCIMUserResponse
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)
patched_scim_user_response = iblai.PatchedSCIMUserResponse() # PatchedSCIMUserResponse |  (optional)

try:
    # Partially update an existing user
    api_response = api_instance.partial_update_user2(id, platform_key, format=format, patched_scim_user_response=patched_scim_user_response)
    print("The response of ScimApi->partial_update_user2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->partial_update_user2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 
 **patched_scim_user_response** | [**PatchedSCIMUserResponse**](PatchedSCIMUserResponse.md)|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_members**
> SCIMGroup remove_group_members(id, platform_key, format=format)

Remove members from an existing RBAC group

Remove members from an existing RBAC group using SCIM patch operations

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Remove members from an existing RBAC group
    api_response = api_instance.remove_group_members(id, platform_key, format=format)
    print("The response of ScimApi->remove_group_members:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->remove_group_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_group**
> SCIMGroup retrieve_group(id, platform_key, format=format)

Get details of a specific RBAC group

Get details of a specific existing RBAC group by unique ID for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Get details of a specific RBAC group
    api_response = api_instance.retrieve_group(id, platform_key, format=format)
    print("The response of ScimApi->retrieve_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->retrieve_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_group2**
> SCIMGroup retrieve_group2(id, platform_key, format=format)

Get details of a specific RBAC group

Get details of a specific existing RBAC group by unique ID for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Get details of a specific RBAC group
    api_response = api_instance.retrieve_group2(id, platform_key, format=format)
    print("The response of ScimApi->retrieve_group2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->retrieve_group2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> SCIMUserResponse retrieve_user(id, platform_key, format=format)

Get details of a specific user

Get details of a specific user by ID for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Get details of a specific user
    api_response = api_instance.retrieve_user(id, platform_key, format=format)
    print("The response of ScimApi->retrieve_user:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->retrieve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user2**
> SCIMUserResponse retrieve_user2(id, platform_key, format=format)

Get details of a specific user

Get details of a specific user by ID for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
format = 'format_example' # str |  (optional)

try:
    # Get details of a specific user
    api_response = api_instance.retrieve_user2(id, platform_key, format=format)
    print("The response of ScimApi->retrieve_user2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->retrieve_user2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> SCIMGroup update_group(id, platform_key, scim_group, format=format)

Update an existing RBAC group

Update an existing RBAC group's name, description, and members for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
scim_group = iblai.SCIMGroup() # SCIMGroup | 
format = 'format_example' # str |  (optional)

try:
    # Update an existing RBAC group
    api_response = api_instance.update_group(id, platform_key, scim_group, format=format)
    print("The response of ScimApi->update_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **scim_group** | [**SCIMGroup**](SCIMGroup.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group2**
> SCIMGroup update_group2(id, platform_key, scim_group, format=format)

Update an existing RBAC group

Update an existing RBAC group's name, description, and members for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_group import SCIMGroup
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
scim_group = iblai.SCIMGroup() # SCIMGroup | 
format = 'format_example' # str |  (optional)

try:
    # Update an existing RBAC group
    api_response = api_instance.update_group2(id, platform_key, scim_group, format=format)
    print("The response of ScimApi->update_group2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->update_group2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **scim_group** | [**SCIMGroup**](SCIMGroup.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMGroup**](SCIMGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> SCIMUserResponse update_user(id, platform_key, scim_user_create_request, format=format)

Update a user

Update a user for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_create_request import SCIMUserCreateRequest
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
scim_user_create_request = iblai.SCIMUserCreateRequest() # SCIMUserCreateRequest | 
format = 'format_example' # str |  (optional)

try:
    # Update a user
    api_response = api_instance.update_user(id, platform_key, scim_user_create_request, format=format)
    print("The response of ScimApi->update_user:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **scim_user_create_request** | [**SCIMUserCreateRequest**](SCIMUserCreateRequest.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user2**
> SCIMUserResponse update_user2(id, platform_key, scim_user_create_request, format=format)

Update a user

Update a user for the specified platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.scim_user_create_request import SCIMUserCreateRequest
from iblai.models.scim_user_response import SCIMUserResponse
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
api_instance = iblai.ScimApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
scim_user_create_request = iblai.SCIMUserCreateRequest() # SCIMUserCreateRequest | 
format = 'format_example' # str |  (optional)

try:
    # Update a user
    api_response = api_instance.update_user2(id, platform_key, scim_user_create_request, format=format)
    print("The response of ScimApi->update_user2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ScimApi->update_user2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **scim_user_create_request** | [**SCIMUserCreateRequest**](SCIMUserCreateRequest.md)|  | 
 **format** | **str**|  | [optional] 

### Return type

[**SCIMUserResponse**](SCIMUserResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/scim+json, application/json
 - **Accept**: application/scim+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

