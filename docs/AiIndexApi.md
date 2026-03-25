# iblai.AiIndexApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_index_orgs_users_documents_destroy**](AiIndexApi.md#ai_index_orgs_users_documents_destroy) | **DELETE** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
[**ai_index_orgs_users_documents_document_from_pool_create**](AiIndexApi.md#ai_index_orgs_users_documents_document_from_pool_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/document-from-pool/ | 
[**ai_index_orgs_users_documents_pathways_list**](AiIndexApi.md#ai_index_orgs_users_documents_pathways_list) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/pathways/{pathway}/ | 
[**ai_index_orgs_users_documents_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
[**ai_index_orgs_users_documents_search_create**](AiIndexApi.md#ai_index_orgs_users_documents_search_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/search/ | 
[**ai_index_orgs_users_documents_settings_create**](AiIndexApi.md#ai_index_orgs_users_documents_settings_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/settings/ | 
[**ai_index_orgs_users_documents_settings_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_settings_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/settings/ | 
[**ai_index_orgs_users_documents_sources_create**](AiIndexApi.md#ai_index_orgs_users_documents_sources_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/sources/ | 
[**ai_index_orgs_users_documents_tasks_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_tasks_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/tasks/{task_id}/ | 
[**ai_index_orgs_users_documents_train_create**](AiIndexApi.md#ai_index_orgs_users_documents_train_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/ | 
[**ai_index_orgs_users_documents_train_retriever_create**](AiIndexApi.md#ai_index_orgs_users_documents_train_retriever_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/retriever/ | 
[**ai_index_orgs_users_documents_update**](AiIndexApi.md#ai_index_orgs_users_documents_update) | **PUT** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
[**ai_index_orgs_users_resource_data_scrapped_list**](AiIndexApi.md#ai_index_orgs_users_resource_data_scrapped_list) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/resource/data/scrapped/ | 
[**ai_index_orgs_users_resource_data_scrapped_retrieve**](AiIndexApi.md#ai_index_orgs_users_resource_data_scrapped_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/resource/{resource_id}/data/scrapped/ | 
[**ai_index_webhook_scan_create**](AiIndexApi.md#ai_index_webhook_scan_create) | **POST** /api/ai-index/webhook/scan/ | 


# **ai_index_orgs_users_documents_destroy**
> ai_index_orgs_users_documents_destroy(document_id, org, user_id)

Delete a specific document embedding.

This endpoint removes a document embedding from the system,
including untraining it from any associated pathways.

Args:
    request: The HTTP request.
    org: Organization key identifier.
    document_id: The ID of the document embedding to delete.

Returns:
    Response: An empty response with a 204 status code if successful.

Raises:
    NotFound: If the specified document embedding does not exist.

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
api_instance = iblai.AiIndexApi(api_client)
document_id = 'document_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_index_orgs_users_documents_destroy(document_id, org, user_id)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

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
**204** | Document successfully deleted |  -  |
**404** | Document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_document_from_pool_create**
> TrainDocumentViewResponse ai_index_orgs_users_documents_document_from_pool_create(org, user_id, document_from_pool_request)

Train a document from the document pool

Sample request:
```json
{"document_id": 3, "to_pathway": "7c43ec09-3d37-489c-a461-8d73df1d91c7"}
```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.document_from_pool_request import DocumentFromPoolRequest
from iblai.models.train_document_view_response import TrainDocumentViewResponse
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
document_from_pool_request = iblai.DocumentFromPoolRequest() # DocumentFromPoolRequest | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_document_from_pool_create(org, user_id, document_from_pool_request)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_document_from_pool_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_document_from_pool_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **document_from_pool_request** | [**DocumentFromPoolRequest**](DocumentFromPoolRequest.md)|  | 

### Return type

[**TrainDocumentViewResponse**](TrainDocumentViewResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_pathways_list**
> PaginatedRetrieverDocumentEmbeddingList ai_index_orgs_users_documents_pathways_list(org, pathway, user_id, limit=limit, offset=offset, search=search)

Description:
Retrieves a list of document embeddings for a specific pathway with optional search and pagination.

Methods:
- GET: Retrieves document embeddings that match the specified search criteria and are paginated according to offset and limit.

Parameters:
- search (str): Search query to filter document names or URLs.
- offset (int): Offset number for pagination.
- limit (int): Limit number for pagination.

Returns:
- GET: A paginated list of document embeddings with their details.
{
    "count": 10,
    "next": "http://api.example.com/retriever_documents/?offset=10&limit=2",
    "previous": "http://api.example.com/retriever_documents/?offset=0&limit=2",
    "results": [
    {
        "document_name": "Document2",
        "platform_key": "example_platform",
        "pathway": "example_pathway"
    }
    ]
}

Error Responses:
- 400 Bad Request: Invalid query parameters.
- 404 Not Found: No document embeddings found for the specified criteria.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_retriever_document_embedding_list import PaginatedRetrieverDocumentEmbeddingList
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
pathway = 'pathway_example' # str | 
user_id = 'user_id_example' # str | 
limit = 56 # int | limit number (optional)
offset = 56 # int | Offset number (optional)
search = 'search_example' # str | Search query (optional)

try:
    api_response = api_instance.ai_index_orgs_users_documents_pathways_list(org, pathway, user_id, limit=limit, offset=offset, search=search)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_pathways_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_pathways_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **pathway** | **str**|  | 
 **user_id** | **str**|  | 
 **limit** | **int**| limit number | [optional] 
 **offset** | **int**| Offset number | [optional] 
 **search** | **str**| Search query | [optional] 

### Return type

[**PaginatedRetrieverDocumentEmbeddingList**](PaginatedRetrieverDocumentEmbeddingList.md)

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

# **ai_index_orgs_users_documents_retrieve**
> RetrieverDocumentEmbedding ai_index_orgs_users_documents_retrieve(document_id, org, user_id)

Retrieve details of a specific document embedding.

This endpoint returns detailed information about a specific
document embedding identified by its ID.

Args:
    request: The HTTP request.
    org: Organization key identifier.
    document_id: The ID of the document embedding to retrieve.

Returns:
    Response: Detailed information about the document embedding.

Raises:
    NotFound: If the specified document embedding does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retriever_document_embedding import RetrieverDocumentEmbedding
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
api_instance = iblai.AiIndexApi(api_client)
document_id = 'document_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_retrieve(document_id, org, user_id)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**RetrieverDocumentEmbedding**](RetrieverDocumentEmbedding.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_search_create**
> RetrieverResponseSearch ai_index_orgs_users_documents_search_create(org, user_id, retriever_request_search)

Retrieve resource documents similar to the given query.

This endpoint performs a semantic search to find documents that are
relevant to the provided query within the specified pathway.

Args:
    request: The HTTP request containing the search query.
    org: Organization key identifier.

Returns:
    Response: A list of documents relevant to the search query.

Raises:
    ValidationError: If the request data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retriever_request_search import RetrieverRequestSearch
from iblai.models.retriever_response_search import RetrieverResponseSearch
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
retriever_request_search = {"query":"Computational thinking","pathway":"test-pathway"} # RetrieverRequestSearch | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_search_create(org, user_id, retriever_request_search)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_search_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_search_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **retriever_request_search** | [**RetrieverRequestSearch**](RetrieverRequestSearch.md)|  | 

### Return type

[**RetrieverResponseSearch**](RetrieverResponseSearch.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_settings_create**
> DocumentSettingsResponse ai_index_orgs_users_documents_settings_create(document_id, org, user_id, document_settings_response=document_settings_response)

Update document settings with RBAC permission checks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.document_settings_response import DocumentSettingsResponse
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
api_instance = iblai.AiIndexApi(api_client)
document_id = 'document_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
document_settings_response = iblai.DocumentSettingsResponse() # DocumentSettingsResponse |  (optional)

try:
    api_response = api_instance.ai_index_orgs_users_documents_settings_create(document_id, org, user_id, document_settings_response=document_settings_response)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_settings_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_settings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **document_settings_response** | [**DocumentSettingsResponse**](DocumentSettingsResponse.md)|  | [optional] 

### Return type

[**DocumentSettingsResponse**](DocumentSettingsResponse.md)

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

# **ai_index_orgs_users_documents_settings_retrieve**
> DocumentSettingsResponse ai_index_orgs_users_documents_settings_retrieve(document_id, org, user_id)

Retrieve document settings with RBAC permission checks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.document_settings_response import DocumentSettingsResponse
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
api_instance = iblai.AiIndexApi(api_client)
document_id = 'document_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_settings_retrieve(document_id, org, user_id)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**DocumentSettingsResponse**](DocumentSettingsResponse.md)

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

# **ai_index_orgs_users_documents_sources_create**
> List[RetrieverRequestSearchDocument] ai_index_orgs_users_documents_sources_create(org, user_id, retriever_request_search)

Retrieve document sources related to a given query.

This endpoint performs a semantic search to find document sources
that are relevant to the provided query within the specified pathway,
and returns them along with confidence levels.

Args:
    request: The HTTP request containing the search query.
    org: Organization key identifier.

Returns:
    Response: A list of document sources with confidence levels.

Raises:
    ValidationError: If the request data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retriever_request_search import RetrieverRequestSearch
from iblai.models.retriever_request_search_document import RetrieverRequestSearchDocument
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
retriever_request_search = {"query":"Computational thinking","pathway":"test-pathway"} # RetrieverRequestSearch | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_sources_create(org, user_id, retriever_request_search)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_sources_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_sources_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **retriever_request_search** | [**RetrieverRequestSearch**](RetrieverRequestSearch.md)|  | 

### Return type

[**List[RetrieverRequestSearchDocument]**](RetrieverRequestSearchDocument.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_tasks_retrieve**
> CheckDocumentTrainingStatus ai_index_orgs_users_documents_tasks_retrieve(org, task_id, user_id)

Check the status of a document training task.

This endpoint retrieves the current status of an asynchronous
document training task that was previously initiated.

Args:
    request: The HTTP request.
    org: Organization key identifier.
    task_id: The ID of the training task to check.

Returns:
    Response: The current status of the document training task,
             which can be "pending", "completed", or "failed".

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.check_document_training_status import CheckDocumentTrainingStatus
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_tasks_retrieve(org, task_id, user_id)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CheckDocumentTrainingStatus**](CheckDocumentTrainingStatus.md)

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

# **ai_index_orgs_users_documents_train_create**
> TrainDocumentViewResponse ai_index_orgs_users_documents_train_create(org, user_id, type, pathway=pathway, url=url, text=text, translate=translate, file=file, access=access, branch=branch, google_drive_auth_data=google_drive_auth_data, dropbox_auth_data=dropbox_auth_data, crawler_max_depth=crawler_max_depth, crawler_max_pages_limit=crawler_max_pages_limit, crawler_max_concurrency=crawler_max_concurrency, crawler_match_patterns=crawler_match_patterns, crawler_pattern_type=crawler_pattern_type, custom_metadata=custom_metadata, add_to_document_pool=add_to_document_pool, document_pool_only=document_pool_only, user_image_description=user_image_description, github_access_token=github_access_token)

Train a document through a worker process.

This endpoint queues larger documents for training through a worker
process, which is more suitable for handling documents that would
take too long to process directly.

Args:
    request: The HTTP request containing the document information.
    org: Organization key identifier.

Returns:
    Response: A confirmation that the document was queued for training,
             including a task ID for tracking the progress.

Raises:
    ValidationError: If the request data is invalid.
    BadRequest: If there was an error processing the document.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.train_document_view_response import TrainDocumentViewResponse
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
type = 'type_example' # str | Type of document e.g file
pathway = 'pathway_example' # str | Pathway for document to be trained in (optional)
url = 'url_example' # str | Url of the document to be trained (optional)
text = 'text_example' # str | Search text for wikipedia (optional)
translate = False # bool | If file should be translated (optional) (default to False)
file = None # bytearray | File to be trained (optional)
access = 'private' # str | Accessibilityto the file (optional) (default to 'private')
branch = 'branch_example' # str | Branch of the repository (optional)
google_drive_auth_data = None # object | Authentication and scoped details of google drive (optional)
dropbox_auth_data = None # object | Authentication and scoped details of dropbox (optional)
crawler_max_depth = 56 # int | The max depth of the crawler (optional)
crawler_max_pages_limit = 56 # int | The max pages limit of the crawler (optional)
crawler_max_concurrency = 56 # int | The max concurrency of the crawler (optional)
crawler_match_patterns = ['crawler_match_patterns_example'] # List[str] | The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in `crawler_pattern_type`. (optional)
crawler_pattern_type = iblai.CrawlerPatternTypeEnum() # CrawlerPatternTypeEnum | Pattern type for the crawler  * `glob` - Glob * `regex` - Regex (optional)
custom_metadata = None # object | Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. (optional)
add_to_document_pool = False # bool | Adds document to the pool or not. (optional) (default to False)
document_pool_only = False # bool | Only adds document to document pool. Requires pathway to be empty. (optional) (default to False)
user_image_description = 'user_image_description_example' # str | Description of an image submitted by the user for RAG. (optional)
github_access_token = 'github_access_token_example' # str | GitHub access token with repo scope. Required for private repositories. (optional)

try:
    api_response = api_instance.ai_index_orgs_users_documents_train_create(org, user_id, type, pathway=pathway, url=url, text=text, translate=translate, file=file, access=access, branch=branch, google_drive_auth_data=google_drive_auth_data, dropbox_auth_data=dropbox_auth_data, crawler_max_depth=crawler_max_depth, crawler_max_pages_limit=crawler_max_pages_limit, crawler_max_concurrency=crawler_max_concurrency, crawler_match_patterns=crawler_match_patterns, crawler_pattern_type=crawler_pattern_type, custom_metadata=custom_metadata, add_to_document_pool=add_to_document_pool, document_pool_only=document_pool_only, user_image_description=user_image_description, github_access_token=github_access_token)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_train_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_train_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **type** | **str**| Type of document e.g file | 
 **pathway** | **str**| Pathway for document to be trained in | [optional] 
 **url** | **str**| Url of the document to be trained | [optional] 
 **text** | **str**| Search text for wikipedia | [optional] 
 **translate** | **bool**| If file should be translated | [optional] [default to False]
 **file** | **bytearray**| File to be trained | [optional] 
 **access** | **str**| Accessibilityto the file | [optional] [default to &#39;private&#39;]
 **branch** | **str**| Branch of the repository | [optional] 
 **google_drive_auth_data** | [**object**](object.md)| Authentication and scoped details of google drive | [optional] 
 **dropbox_auth_data** | [**object**](object.md)| Authentication and scoped details of dropbox | [optional] 
 **crawler_max_depth** | **int**| The max depth of the crawler | [optional] 
 **crawler_max_pages_limit** | **int**| The max pages limit of the crawler | [optional] 
 **crawler_max_concurrency** | **int**| The max concurrency of the crawler | [optional] 
 **crawler_match_patterns** | [**List[str]**](str.md)| The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in &#x60;crawler_pattern_type&#x60;. | [optional] 
 **crawler_pattern_type** | [**CrawlerPatternTypeEnum**](CrawlerPatternTypeEnum.md)| Pattern type for the crawler  * &#x60;glob&#x60; - Glob * &#x60;regex&#x60; - Regex | [optional] 
 **custom_metadata** | [**object**](object.md)| Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. | [optional] 
 **add_to_document_pool** | **bool**| Adds document to the pool or not. | [optional] [default to False]
 **document_pool_only** | **bool**| Only adds document to document pool. Requires pathway to be empty. | [optional] [default to False]
 **user_image_description** | **str**| Description of an image submitted by the user for RAG. | [optional] 
 **github_access_token** | **str**| GitHub access token with repo scope. Required for private repositories. | [optional] 

### Return type

[**TrainDocumentViewResponse**](TrainDocumentViewResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_train_retriever_create**
> RetreiverTrainViewResponse ai_index_orgs_users_documents_train_retriever_create(org, user_id, pathway, url)

Train a document directly without using a worker.

This endpoint is designed for training smaller documents directly
without queuing them through a worker process. For larger documents,
use the TrainDocumentView endpoint instead.

Args:
    request: The HTTP request containing the document information.
    org: Organization key identifier.

Returns:
    Response: A confirmation that the document was trained successfully.

Raises:
    ValidationError: If the request data is invalid.
    BadRequest: If the document training failed.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retreiver_train_view_response import RetreiverTrainViewResponse
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
pathway = 'pathway_example' # str | Pathway for document to be trained in
url = 'url_example' # str | Url of the document to be trained

try:
    api_response = api_instance.ai_index_orgs_users_documents_train_retriever_create(org, user_id, pathway, url)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_train_retriever_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_train_retriever_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **pathway** | **str**| Pathway for document to be trained in | 
 **url** | **str**| Url of the document to be trained | 

### Return type

[**RetreiverTrainViewResponse**](RetreiverTrainViewResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data or training failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_update**
> RetrieverDocumentEmbedding ai_index_orgs_users_documents_update(document_id, org, user_id, pathway, document_name=document_name, document_type=document_type, url=url, train=train, crawler_max_depth=crawler_max_depth, crawler_max_pages_limit=crawler_max_pages_limit, crawler_max_concurrency=crawler_max_concurrency, crawler_match_patterns=crawler_match_patterns, crawler_pattern_type=crawler_pattern_type, access=access, google_drive_auth_data=google_drive_auth_data, dropbox_auth_data=dropbox_auth_data, custom_metadata=custom_metadata)

Update a specific document embedding.

This endpoint allows updating various properties of a document embedding,
including its name, type, pathway, and training status.

Args:
    request: The HTTP request containing the updated document data.
    org: Organization key identifier.
    document_id: The ID of the document embedding to update.

Returns:
    Response: The updated document embedding information.

Raises:
    BadRequest: If the provided data is invalid.
    NotFound: If the specified document embedding does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retriever_document_embedding import RetrieverDocumentEmbedding
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
api_instance = iblai.AiIndexApi(api_client)
document_id = 'document_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
pathway = 'pathway_example' # str | The pathway to retrain the document in
document_name = 'document_name_example' # str | The name of the document (optional)
document_type = 'document_type_example' # str | The type of the document (optional)
url = 'url_example' # str | The url of the document (optional)
train = True # bool | The type of the document (optional)
crawler_max_depth = 56 # int | The max depth of the crawler (optional)
crawler_max_pages_limit = 56 # int | The max pages limit of the crawler (optional)
crawler_max_concurrency = 56 # int | The max concurrency of the crawler (optional)
crawler_match_patterns = ['crawler_match_patterns_example'] # List[str] | The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in `crawler_pattern_type`. (optional)
crawler_pattern_type = iblai.CrawlerPatternTypeEnum() # CrawlerPatternTypeEnum | Pattern type for the crawler  * `glob` - Glob * `regex` - Regex (optional)
access = iblai.AccessEnum() # AccessEnum | The access of the document.  * `public` - Public * `private` - Private (optional)
google_drive_auth_data = None # object | Authentication and scoped details of google drive. (optional)
dropbox_auth_data = None # object | Authentication and scoped details of dropbox (optional)
custom_metadata = None # object | Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. (optional)

try:
    api_response = api_instance.ai_index_orgs_users_documents_update(document_id, org, user_id, pathway, document_name=document_name, document_type=document_type, url=url, train=train, crawler_max_depth=crawler_max_depth, crawler_max_pages_limit=crawler_max_pages_limit, crawler_max_concurrency=crawler_max_concurrency, crawler_match_patterns=crawler_match_patterns, crawler_pattern_type=crawler_pattern_type, access=access, google_drive_auth_data=google_drive_auth_data, dropbox_auth_data=dropbox_auth_data, custom_metadata=custom_metadata)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **pathway** | **str**| The pathway to retrain the document in | 
 **document_name** | **str**| The name of the document | [optional] 
 **document_type** | **str**| The type of the document | [optional] 
 **url** | **str**| The url of the document | [optional] 
 **train** | **bool**| The type of the document | [optional] 
 **crawler_max_depth** | **int**| The max depth of the crawler | [optional] 
 **crawler_max_pages_limit** | **int**| The max pages limit of the crawler | [optional] 
 **crawler_max_concurrency** | **int**| The max concurrency of the crawler | [optional] 
 **crawler_match_patterns** | [**List[str]**](str.md)| The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in &#x60;crawler_pattern_type&#x60;. | [optional] 
 **crawler_pattern_type** | [**CrawlerPatternTypeEnum**](CrawlerPatternTypeEnum.md)| Pattern type for the crawler  * &#x60;glob&#x60; - Glob * &#x60;regex&#x60; - Regex | [optional] 
 **access** | [**AccessEnum**](AccessEnum.md)| The access of the document.  * &#x60;public&#x60; - Public * &#x60;private&#x60; - Private | [optional] 
 **google_drive_auth_data** | [**object**](object.md)| Authentication and scoped details of google drive. | [optional] 
 **dropbox_auth_data** | [**object**](object.md)| Authentication and scoped details of dropbox | [optional] 
 **custom_metadata** | [**object**](object.md)| Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. | [optional] 

### Return type

[**RetrieverDocumentEmbedding**](RetrieverDocumentEmbedding.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |
**404** | Document not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_resource_data_scrapped_list**
> List[ResourceScrappedData] ai_index_orgs_users_resource_data_scrapped_list(org, user_id, is_archive=is_archive, is_like=is_like, is_video=is_video, search_key=search_key)

Retrieve and filter scraped data from resources.

This endpoint returns a list of scraped data from resources associated
with the specified user, with optional filtering based on query parameters.

Args:
    request: The HTTP request containing filter query parameters.
    org: Organization key identifier.
    user_id: The username of the user whose resources to retrieve.

Returns:
    Response: A list of scraped resource data matching the filter criteria.

Raises:
    BadRequest: If the username is invalid or query parameters are incorrect.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.resource_scrapped_data import ResourceScrappedData
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
is_archive = True # bool |  (optional)
is_like = True # bool |  (optional)
is_video = True # bool |  (optional)
search_key = 'search_key_example' # str |  (optional)

try:
    api_response = api_instance.ai_index_orgs_users_resource_data_scrapped_list(org, user_id, is_archive=is_archive, is_like=is_like, is_video=is_video, search_key=search_key)
    print("The response of AiIndexApi->ai_index_orgs_users_resource_data_scrapped_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_resource_data_scrapped_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **is_archive** | **bool**|  | [optional] 
 **is_like** | **bool**|  | [optional] 
 **is_video** | **bool**|  | [optional] 
 **search_key** | **str**|  | [optional] 

### Return type

[**List[ResourceScrappedData]**](ResourceScrappedData.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid username or query parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_resource_data_scrapped_retrieve**
> ResourceScrappedData ai_index_orgs_users_resource_data_scrapped_retrieve(org, resource_id, user_id)

Retrieve detailed information about a specific scraped resource.

This endpoint returns the complete scraped data for a specific resource
identified by its ID.

Args:
    request: The HTTP request.
    org: Organization key identifier.
    user_id: The username of the user associated with the resource.
    resource_id: The ID of the resource to retrieve.

Returns:
    Response: The complete scraped data for the specified resource.

Raises:
    NotFound: If the specified resource data does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.resource_scrapped_data import ResourceScrappedData
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
api_instance = iblai.AiIndexApi(api_client)
org = 'org_example' # str | 
resource_id = 'resource_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_index_orgs_users_resource_data_scrapped_retrieve(org, resource_id, user_id)
    print("The response of AiIndexApi->ai_index_orgs_users_resource_data_scrapped_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_resource_data_scrapped_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **resource_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ResourceScrappedData**](ResourceScrappedData.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Resource data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_webhook_scan_create**
> ScanWebhookResponse ai_index_webhook_scan_create(scan_webhook_request)

Receive and process file scan status from external security scanning services.

This webhook endpoint receives scan results for files that have been submitted
for security scanning. It processes the results asynchronously and determines
if the files are safe for further processing.

Args:
    request: The HTTP request containing scan result data.

Returns:
    Response: A confirmation that the scan result was received and is being processed.

Raises:
    BadRequest: If the provided scan result data is invalid.

### Example


```python
import iblai
from iblai.models.scan_webhook_request import ScanWebhookRequest
from iblai.models.scan_webhook_response import ScanWebhookResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.AiIndexApi(api_client)
scan_webhook_request = {"file_id":"f12345","filename":"document.pdf","status":"clean","message":"No threats detected"} # ScanWebhookRequest | 

try:
    api_response = api_instance.ai_index_webhook_scan_create(scan_webhook_request)
    print("The response of AiIndexApi->ai_index_webhook_scan_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_webhook_scan_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_webhook_request** | [**ScanWebhookRequest**](ScanWebhookRequest.md)|  | 

### Return type

[**ScanWebhookResponse**](ScanWebhookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

