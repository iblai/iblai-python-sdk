# iblai.OrgsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgs_scim_v2_department_members_create**](OrgsApi.md#orgs_scim_v2_department_members_create) | **POST** /api/orgs/{org}/scim/v2/DepartmentMembers/ | 
[**orgs_scim_v2_department_members_destroy**](OrgsApi.md#orgs_scim_v2_department_members_destroy) | **DELETE** /api/orgs/{org}/scim/v2/DepartmentMembers/{id}/ | 
[**orgs_scim_v2_department_members_retrieve**](OrgsApi.md#orgs_scim_v2_department_members_retrieve) | **GET** /api/orgs/{org}/scim/v2/DepartmentMembers/ | 
[**orgs_scim_v2_department_members_retrieve2**](OrgsApi.md#orgs_scim_v2_department_members_retrieve2) | **GET** /api/orgs/{org}/scim/v2/DepartmentMembers/{id}/ | 
[**orgs_scim_v2_department_members_update**](OrgsApi.md#orgs_scim_v2_department_members_update) | **PUT** /api/orgs/{org}/scim/v2/DepartmentMembers/{id}/ | 
[**orgs_scim_v2_departments_add_members_create**](OrgsApi.md#orgs_scim_v2_departments_add_members_create) | **POST** /api/orgs/{org}/scim/v2/Departments/{id}/add_members/ | 
[**orgs_scim_v2_departments_create**](OrgsApi.md#orgs_scim_v2_departments_create) | **POST** /api/orgs/{org}/scim/v2/Departments/ | 
[**orgs_scim_v2_departments_destroy**](OrgsApi.md#orgs_scim_v2_departments_destroy) | **DELETE** /api/orgs/{org}/scim/v2/Departments/{id}/ | 
[**orgs_scim_v2_departments_remove_members_create**](OrgsApi.md#orgs_scim_v2_departments_remove_members_create) | **POST** /api/orgs/{org}/scim/v2/Departments/{id}/remove_members/ | 
[**orgs_scim_v2_departments_retrieve**](OrgsApi.md#orgs_scim_v2_departments_retrieve) | **GET** /api/orgs/{org}/scim/v2/Departments/ | 
[**orgs_scim_v2_departments_retrieve2**](OrgsApi.md#orgs_scim_v2_departments_retrieve2) | **GET** /api/orgs/{org}/scim/v2/Departments/{id}/ | 
[**orgs_scim_v2_departments_update**](OrgsApi.md#orgs_scim_v2_departments_update) | **PUT** /api/orgs/{org}/scim/v2/Departments/{id}/ | 
[**orgs_scim_v2_group_members_create**](OrgsApi.md#orgs_scim_v2_group_members_create) | **POST** /api/orgs/{org}/scim/v2/GroupMembers/ | 
[**orgs_scim_v2_group_members_destroy**](OrgsApi.md#orgs_scim_v2_group_members_destroy) | **DELETE** /api/orgs/{org}/scim/v2/GroupMembers/{id}/ | 
[**orgs_scim_v2_group_members_retrieve**](OrgsApi.md#orgs_scim_v2_group_members_retrieve) | **GET** /api/orgs/{org}/scim/v2/GroupMembers/ | 
[**orgs_scim_v2_group_members_retrieve2**](OrgsApi.md#orgs_scim_v2_group_members_retrieve2) | **GET** /api/orgs/{org}/scim/v2/GroupMembers/{id}/ | 
[**orgs_scim_v2_group_members_update**](OrgsApi.md#orgs_scim_v2_group_members_update) | **PUT** /api/orgs/{org}/scim/v2/GroupMembers/{id}/ | 
[**orgs_scim_v2_groups_add_members_create**](OrgsApi.md#orgs_scim_v2_groups_add_members_create) | **POST** /api/orgs/{org}/scim/v2/Groups/{id}/add_members/ | 
[**orgs_scim_v2_groups_create**](OrgsApi.md#orgs_scim_v2_groups_create) | **POST** /api/orgs/{org}/scim/v2/Groups/ | 
[**orgs_scim_v2_groups_destroy**](OrgsApi.md#orgs_scim_v2_groups_destroy) | **DELETE** /api/orgs/{org}/scim/v2/Groups/{id}/ | 
[**orgs_scim_v2_groups_remove_members_create**](OrgsApi.md#orgs_scim_v2_groups_remove_members_create) | **POST** /api/orgs/{org}/scim/v2/Groups/{id}/remove_members/ | 
[**orgs_scim_v2_groups_retrieve**](OrgsApi.md#orgs_scim_v2_groups_retrieve) | **GET** /api/orgs/{org}/scim/v2/Groups/ | 
[**orgs_scim_v2_groups_retrieve2**](OrgsApi.md#orgs_scim_v2_groups_retrieve2) | **GET** /api/orgs/{org}/scim/v2/Groups/{id}/ | 
[**orgs_scim_v2_groups_update**](OrgsApi.md#orgs_scim_v2_groups_update) | **PUT** /api/orgs/{org}/scim/v2/Groups/{id}/ | 
[**orgs_scim_v2_users_create**](OrgsApi.md#orgs_scim_v2_users_create) | **POST** /api/orgs/{org}/scim/v2/Users/ | 
[**orgs_scim_v2_users_destroy**](OrgsApi.md#orgs_scim_v2_users_destroy) | **DELETE** /api/orgs/{org}/scim/v2/Users/{id}/ | 
[**orgs_scim_v2_users_retrieve**](OrgsApi.md#orgs_scim_v2_users_retrieve) | **GET** /api/orgs/{org}/scim/v2/Users/ | 
[**orgs_scim_v2_users_retrieve2**](OrgsApi.md#orgs_scim_v2_users_retrieve2) | **GET** /api/orgs/{org}/scim/v2/Users/{id}/ | 
[**orgs_scim_v2_users_update**](OrgsApi.md#orgs_scim_v2_users_update) | **PUT** /api/orgs/{org}/scim/v2/Users/{id}/ | 


# **orgs_scim_v2_department_members_create**
> orgs_scim_v2_department_members_create(org)



POST /scim/v2/DepartmentMembers Create or update a department member using core logic. SCIM format.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_department_members_create(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_department_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_scim_v2_department_members_destroy**
> orgs_scim_v2_department_members_destroy(id, org)



DELETE /scim/v2/DepartmentMembers/{id} Delete a department member using core logic. SCIM format.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_department_members_destroy(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_department_members_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_department_members_retrieve**
> orgs_scim_v2_department_members_retrieve(org)



GET /scim/v2/DepartmentMembers List all department members in the system.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_department_members_retrieve(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_department_members_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **orgs_scim_v2_department_members_retrieve2**
> orgs_scim_v2_department_members_retrieve2(id, org)



GET /scim/v2/DepartmentMembers/{id} Get department members for a specific department (must belong to the requesting platform/org). SCIM format.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_department_members_retrieve2(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_department_members_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_department_members_update**
> orgs_scim_v2_department_members_update(id, org)



PUT /scim/v2/DepartmentMembers/{id} Update a department member using core logic. SCIM format.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_department_members_update(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_department_members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_add_members_create**
> orgs_scim_v2_departments_add_members_create(id, org)



POST /scim/v2/Departments/{id}/add_members  Add members to a department.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_add_members_create(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_add_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_create**
> orgs_scim_v2_departments_create(org)



POST /scim/v2/Departments  Create a new department in the system.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_create(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_scim_v2_departments_destroy**
> orgs_scim_v2_departments_destroy(id, org)



DELETE /scim/v2/Departments/{id}  Delete a department from the system.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_destroy(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_remove_members_create**
> orgs_scim_v2_departments_remove_members_create(id, org)



POST /scim/v2/Departments/{id}/remove_members  Remove members from a department.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_remove_members_create(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_remove_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_retrieve**
> orgs_scim_v2_departments_retrieve(org)



GET /scim/v2/Departments  List departments in the system. Supports filtering and pagination.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_retrieve(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_retrieve2**
> orgs_scim_v2_departments_retrieve2(id, org)



GET /scim/v2/Departments/{id}  Get details of a specific department.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_retrieve2(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_departments_update**
> orgs_scim_v2_departments_update(id, org)



PUT /scim/v2/Departments/{id}  Update a department's information.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_departments_update(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_departments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_group_members_create**
> orgs_scim_v2_group_members_create(org)



SCIM Group Member endpoints for managing group members in the system.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_group_members_create(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_group_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_scim_v2_group_members_destroy**
> orgs_scim_v2_group_members_destroy(id, org)



SCIM Group Member endpoints for managing group members in the system.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_group_members_destroy(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_group_members_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_group_members_retrieve**
> orgs_scim_v2_group_members_retrieve(org)



SCIM Group Member endpoints for managing group members in the system.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_group_members_retrieve(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_group_members_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **orgs_scim_v2_group_members_retrieve2**
> orgs_scim_v2_group_members_retrieve2(id, org)



SCIM Group Member endpoints for managing group members in the system.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_group_members_retrieve2(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_group_members_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_group_members_update**
> orgs_scim_v2_group_members_update(id, org)



SCIM Group Member endpoints for managing group members in the system.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_group_members_update(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_group_members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_add_members_create**
> orgs_scim_v2_groups_add_members_create(id, org)



POST /scim/v2/groups/{id}/add_members  Add members to a user group.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_add_members_create(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_add_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_create**
> orgs_scim_v2_groups_create(org)



SCIM Group endpoints for managing user groups in the system (SCIM 2.0).

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_create(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_scim_v2_groups_destroy**
> orgs_scim_v2_groups_destroy(id, org)



DELETE /scim/v2/groups/{id}  Delete a user group from the system.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_destroy(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_remove_members_create**
> orgs_scim_v2_groups_remove_members_create(id, org)



POST /scim/v2/groups/{id}/remove_members  Remove members from a user group.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_remove_members_create(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_remove_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_retrieve**
> orgs_scim_v2_groups_retrieve(org)



SCIM Group endpoints for managing user groups in the system (SCIM 2.0).

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_retrieve(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_retrieve2**
> orgs_scim_v2_groups_retrieve2(id, org)



GET /scim/v2/groups/{id}  Get details of a specific user group.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_retrieve2(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_groups_update**
> orgs_scim_v2_groups_update(id, org)



PUT /scim/v2/groups/{id}  Update a user group's information.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_groups_update(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_users_create**
> orgs_scim_v2_users_create(org)



POST /scim/v2/users  Create a new user in the system.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_users_create(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_scim_v2_users_destroy**
> orgs_scim_v2_users_destroy(id, org)



DELETE /scim/v2/users/{id} is not supported.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_users_destroy(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_users_retrieve**
> orgs_scim_v2_users_retrieve(org)



GET /scim/v2/users  List users in the system. Supports filtering and pagination.

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
api_instance = iblai.OrgsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_users_retrieve(org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **orgs_scim_v2_users_retrieve2**
> orgs_scim_v2_users_retrieve2(id, org)



GET /scim/v2/users/{id}  Get details of a specific user.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_users_retrieve2(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_users_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

# **orgs_scim_v2_users_update**
> orgs_scim_v2_users_update(id, org)



PUT /scim/v2/users/{id}  Update a user's information.

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
api_instance = iblai.OrgsApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    api_instance.orgs_scim_v2_users_update(id, org)
except Exception as e:
    print("Exception when calling OrgsApi->orgs_scim_v2_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

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

