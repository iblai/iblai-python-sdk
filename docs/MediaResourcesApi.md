# iblai.MediaResourcesApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_orgs_users_media_media_resources_by_item_retrieve**](MediaResourcesApi.md#media_orgs_users_media_media_resources_by_item_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/by_item/ | 
[**media_orgs_users_media_media_resources_create**](MediaResourcesApi.md#media_orgs_users_media_media_resources_create) | **POST** /api/media/orgs/{org}/users/{user_id}/media/media-resources/ | 
[**media_orgs_users_media_media_resources_destroy**](MediaResourcesApi.md#media_orgs_users_media_media_resources_destroy) | **DELETE** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
[**media_orgs_users_media_media_resources_list**](MediaResourcesApi.md#media_orgs_users_media_media_resources_list) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/ | 
[**media_orgs_users_media_media_resources_partial_update**](MediaResourcesApi.md#media_orgs_users_media_media_resources_partial_update) | **PATCH** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
[**media_orgs_users_media_media_resources_retrieve**](MediaResourcesApi.md#media_orgs_users_media_media_resources_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
[**media_orgs_users_media_media_resources_search_retrieve**](MediaResourcesApi.md#media_orgs_users_media_media_resources_search_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/search/ | 
[**media_orgs_users_media_media_resources_update**](MediaResourcesApi.md#media_orgs_users_media_media_resources_update) | **PUT** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 


# **media_orgs_users_media_media_resources_by_item_retrieve**
> media_orgs_users_media_media_resources_by_item_retrieve(item_id, item_type, org, user_id, course_id=course_id, search=search, unit_id=unit_id)



Get media resources for a specific item. The item_type determines which resources are returned based on the provided item_id.

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
api_instance = iblai.MediaResourcesApi(api_client)
item_id = 'item_id_example' # str | ID of the item
item_type = 'item_type_example' # str | Type of item. Valid values: course, unit, resource, course_unit, course_resource, unit_resource, all
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_by_item_retrieve(item_id, item_type, org, user_id, course_id=course_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_by_item_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| ID of the item | 
 **item_type** | **str**| Type of item. Valid values: course, unit, resource, course_unit, course_resource, unit_resource, all | 
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources for item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_create**
> media_orgs_users_media_media_resources_create(org, user_id, media_resource, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.media_resource import MediaResource
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
api_instance = iblai.MediaResourcesApi(api_client)
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
media_resource = iblai.MediaResource() # MediaResource | 
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_create(org, user_id, media_resource, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **media_resource** | [**MediaResource**](MediaResource.md)|  | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_destroy**
> media_orgs_users_media_media_resources_destroy(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

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
api_instance = iblai.MediaResourcesApi(api_client)
id = 56 # int | A unique integer value identifying this Media Resource.
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_destroy(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Resource. | 
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_list**
> media_orgs_users_media_media_resources_list(org, user_id, course_id=course_id, item_id=item_id, page=page, page_size=page_size, search=search, unit_id=unit_id)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

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
api_instance = iblai.MediaResourcesApi(api_client)
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_list(org, user_id, course_id=course_id, item_id=item_id, page=page, page_size=page_size, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_partial_update**
> media_orgs_users_media_media_resources_partial_update(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id, patched_media_resource=patched_media_resource)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_media_resource import PatchedMediaResource
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
api_instance = iblai.MediaResourcesApi(api_client)
id = 56 # int | A unique integer value identifying this Media Resource.
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)
patched_media_resource = iblai.PatchedMediaResource() # PatchedMediaResource |  (optional)

try:
    api_instance.media_orgs_users_media_media_resources_partial_update(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id, patched_media_resource=patched_media_resource)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Resource. | 
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 
 **patched_media_resource** | [**PatchedMediaResource**](PatchedMediaResource.md)|  | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_retrieve**
> media_orgs_users_media_media_resources_retrieve(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

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
api_instance = iblai.MediaResourcesApi(api_client)
id = 56 # int | A unique integer value identifying this Media Resource.
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_retrieve(id, org, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Resource. | 
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_search_retrieve**
> media_orgs_users_media_media_resources_search_retrieve(org, q, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)



Search media resources by title, description, or IDs. Supports filtering results by course_id, unit_id, and item_id.

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
api_instance = iblai.MediaResourcesApi(api_client)
org = 'org_example' # str | Organization identifier
q = 'q_example' # str | Search query string
user_id = 'user_id_example' # str | User identifier
course_id = 'course_id_example' # str | Filter results by course ID (optional)
item_id = 'item_id_example' # str | Filter results by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter results by unit ID (optional)

try:
    api_instance.media_orgs_users_media_media_resources_search_retrieve(org, q, user_id, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Organization identifier | 
 **q** | **str**| Search query string | 
 **user_id** | **str**| User identifier | 
 **course_id** | **str**| Filter results by course ID | [optional] 
 **item_id** | **str**| Filter results by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter results by unit ID | [optional] 

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
**200** | Successfully searched media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_orgs_users_media_media_resources_update**
> media_orgs_users_media_media_resources_update(id, org, user_id, media_resource, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)



List and filter media resources. Supports filtering by course_id, unit_id, item_id and searching across multiple fields.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.media_resource import MediaResource
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
api_instance = iblai.MediaResourcesApi(api_client)
id = 56 # int | A unique integer value identifying this Media Resource.
org = 'org_example' # str | Organization identifier
user_id = 'user_id_example' # str | User identifier
media_resource = iblai.MediaResource() # MediaResource | 
course_id = 'course_id_example' # str | Filter by course ID (e.g., course-v1:main+NB101+2025-T1) (optional)
item_id = 'item_id_example' # str | Filter by item ID (optional)
search = 'search_example' # str | Search across title, description, course_id, unit_id, item_id, and file_url (optional)
unit_id = 'unit_id_example' # str | Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) (optional)

try:
    api_instance.media_orgs_users_media_media_resources_update(id, org, user_id, media_resource, course_id=course_id, item_id=item_id, search=search, unit_id=unit_id)
except Exception as e:
    print("Exception when calling MediaResourcesApi->media_orgs_users_media_media_resources_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Resource. | 
 **org** | **str**| Organization identifier | 
 **user_id** | **str**| User identifier | 
 **media_resource** | [**MediaResource**](MediaResource.md)|  | 
 **course_id** | **str**| Filter by course ID (e.g., course-v1:main+NB101+2025-T1) | [optional] 
 **item_id** | **str**| Filter by item ID | [optional] 
 **search** | **str**| Search across title, description, course_id, unit_id, item_id, and file_url | [optional] 
 **unit_id** | **str**| Filter by unit ID (e.g., block-v1:main+NB101+2025-T1+type@vertical+block@12345) | [optional] 

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
**200** | Successfully retrieved media resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

