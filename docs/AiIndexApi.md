# iblai.AiIndexApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_index_orgs_users_documents_destroy**](AiIndexApi.md#ai_index_orgs_users_documents_destroy) | **DELETE** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
[**ai_index_orgs_users_documents_pathways_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_pathways_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/pathways/{pathway}/ | 
[**ai_index_orgs_users_documents_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
[**ai_index_orgs_users_documents_search_create**](AiIndexApi.md#ai_index_orgs_users_documents_search_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/search/ | 
[**ai_index_orgs_users_documents_sources_create**](AiIndexApi.md#ai_index_orgs_users_documents_sources_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/sources/ | 
[**ai_index_orgs_users_documents_tasks_retrieve**](AiIndexApi.md#ai_index_orgs_users_documents_tasks_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/tasks/{task_id}/ | 
[**ai_index_orgs_users_documents_train_create**](AiIndexApi.md#ai_index_orgs_users_documents_train_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/ | 
[**ai_index_orgs_users_documents_train_retriever_create**](AiIndexApi.md#ai_index_orgs_users_documents_train_retriever_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/retriever/ | 
[**ai_index_orgs_users_documents_train_sessions_create**](AiIndexApi.md#ai_index_orgs_users_documents_train_sessions_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/sessions/{session_id}/ | 
[**ai_index_orgs_users_documents_update**](AiIndexApi.md#ai_index_orgs_users_documents_update) | **PUT** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 


# **ai_index_orgs_users_documents_destroy**
> ai_index_orgs_users_documents_destroy(document_id, org, user_id)



This is for deleting resource document details for a tenant.  Accessible to tenant admins only.  Returns:      404 : When document not found.      204 : No Content.  Example :      DELETE : /api/ai-index/orgs/main/users/johndoe/documents/1/ .      Response:

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_pathways_retrieve**
> RetrieverDocumentEmbedding ai_index_orgs_users_documents_pathways_retrieve(org, pathway, user_id)



This is for getting a list of resource documents for a tenant and pathway.  Accessible to tenant admins only.  Returns:      200 : List of resource documents .  Example :      GET : /api/ai-index/orgs/main/users/johndoe/documents/pathways/test-pathway/      Response:       [{                         \"id\": 1,                         \"document_name\": \"CareerClustersPathways_0\",                         \"document_type\": \"pdf\",                         \"pathway\": \"test-pathway\",                         \"url\": \"https://careertech.org/wp-content/uploads/sites/default/files/CareerClustersPathways_0.pdf\",                         \"tokens\": 46578,                         \"platform_key\": \"main\",                         \"is_trained\": true                     }]

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
org = 'org_example' # str | 
pathway = 'pathway_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_pathways_retrieve(org, pathway, user_id)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_pathways_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_pathways_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **pathway** | **str**|  | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_retrieve**
> RetrieverDocumentEmbedding ai_index_orgs_users_documents_retrieve(document_id, org, user_id)



This is for getting resource document details for a tenant.  Accessible to tenant admins only.  Returns:      404 : When document not found.      200 : Resource document details.  Example :      GET : /api/ai-index/orgs/main/users/johndoe/documents/1/ .      Response:       {                         \"id\": 1,                         \"document_name\": \"CareerClustersPathways_0\",                         \"document_type\": \"pdf\",                         \"pathway\": \"test-pathway\",                         \"url\": \"https://careertech.org/wp-content/uploads/sites/default/files/CareerClustersPathways_0.pdf\",                         \"tokens\": 9223372036854776000,                         \"platform_key\": \"main\",                         \"is_trained\": true                     }

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_search_create**
> RetrieverResponseSearch ai_index_orgs_users_documents_search_create(org, user_id, retriever_request_search)



This is for getting data from resource documents that are similar to the query.  Accessible to tenant admins and students.  Returns:      400 : When request data is not valid.      200 : Object of list of similar data to the query.  Example :      POST : /api/ai-index/orgs/main/users/johndoe/documents/search/.      Request:        {                         \"query\": \"Computational thinking\",                         \"pathway\": \"test-pathway\"                      }      Response:       {                         \"results\": [                             {                                 \"page_content\": \"computational thinking can go from a thought exercise to \"                             },                          ]                     }

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
retriever_request_search = iblai.RetrieverRequestSearch() # RetrieverRequestSearch | 

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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_index_orgs_users_documents_sources_create**
> RetrieverRequestSearchDocument ai_index_orgs_users_documents_sources_create(org, user_id, retriever_request_search)



This is for getting  resource documents urls whose data is similar to the query.  Accessible to tenant admins only.  Returns:      400 : When request data is not valid.      200 : List of document urls whose data is similar to the query.  Example :      POST : /api/ai-index/orgs/main/users/johndoe/documents/sources/.      Request:        {                         \"query\": \"Computational thinking\",                         \"pathway\": \"test-pathway\"                      }      Response:       [                         {                             \"source\": \"https://xxxxxx.com/media/private/mentor-documents/1.1%20Introduction.pdf\",                             \"confidence_level\": 90.38                         }                     ]

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
retriever_request_search = iblai.RetrieverRequestSearch() # RetrieverRequestSearch | 

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

[**RetrieverRequestSearchDocument**](RetrieverRequestSearchDocument.md)

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

# **ai_index_orgs_users_documents_tasks_retrieve**
> CheckDocumentTrainingStatus ai_index_orgs_users_documents_tasks_retrieve(org, task_id, user_id)



This is for checking the document training status.  Accessible to tenant admins only.  Returns:      200 : Document training status.  Example :      GET : /api/ai-index/orgs/main/users/johndoe/documents/pathways/tasks/4194d20c-37d5-4148-882f-f7d2d91f7769/      Response:       {                         \"status\": \"pending\",                         \"message\": \"Training document pending\"                     }

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
> TrainDocumentViewResponse ai_index_orgs_users_documents_train_create(org, user_id, train_document_view_request)



This is for training  documents through the worker, used for larger documents.  Accessible to tenant admins only.  Returns:      400 : When request data is not valid.      200 : Training details.   Example :      POST : /api/ai-index/orgs/main/users/johndoe/documents/train/.      Request:        {                         \"pathway\": \"test-pathway\",                         \"url\": \"https://xxxxxx.com/media/private/mentor-documents/1.1%20Introduction.pdf\",                         \"type\": \"url\",                         \"access\": \"public\"                      }      Response:       {                         \"task_id\": \"4194d20c-37d5-4148-882f-f7d2d91f7769\",                         \"message\": \"Document received, Your request to train is queued\",                         \"tokens\": 877                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.train_document_view_request import TrainDocumentViewRequest
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
train_document_view_request = iblai.TrainDocumentViewRequest() # TrainDocumentViewRequest | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_train_create(org, user_id, train_document_view_request)
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
 **train_document_view_request** | [**TrainDocumentViewRequest**](TrainDocumentViewRequest.md)|  | 

### Return type

[**TrainDocumentViewResponse**](TrainDocumentViewResponse.md)

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

# **ai_index_orgs_users_documents_train_retriever_create**
> RetreiverTrainViewResponse ai_index_orgs_users_documents_train_retriever_create(org, user_id, retreiver_train_view_request)



This is for training  documents directly i.e not through the worker. Use this when training smaller documents.  Accessible to tenant admins only.  Returns:      400 : When request data is not valid.      400 : When document training failed.      200 : When document is already trained.      200 : When document is trained successfully.   Example :      POST : /api/ai-index/orgs/main/users/johndoe/documents/train/retriever/.      Request:        {                         \"pathway\": \"test-pathway\",                         \"url\": \"https://xxxxxx.com/media/private/mentor-documents/1.1%20Introduction.pdf\"                      }      Response:       {                         \"detail\": \"Document trained successfully\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retreiver_train_view_request import RetreiverTrainViewRequest
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
retreiver_train_view_request = iblai.RetreiverTrainViewRequest() # RetreiverTrainViewRequest | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_train_retriever_create(org, user_id, retreiver_train_view_request)
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
 **retreiver_train_view_request** | [**RetreiverTrainViewRequest**](RetreiverTrainViewRequest.md)|  | 

### Return type

[**RetreiverTrainViewResponse**](RetreiverTrainViewResponse.md)

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

# **ai_index_orgs_users_documents_train_sessions_create**
> TrainChatSessionDocumentView ai_index_orgs_users_documents_train_sessions_create(org, session_id, user_id, train_chat_session_document_view_request)



This is for training  chat documents.  Accessible to tenant admins and students.  Returns:      400 : When request data is not valid.      200 : Training details.   Example :      POST : /api/ai-index/orgs/main/users/johndoe/documents/train/sessions/0843d0f4-a7b7-4608-a791-4545dcf9db2a/.      Request:        {                         \"file\": binary                     }      Response:       {                         \"message\": \"Document trained successfully\",                         \"tokens\": 877                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.train_chat_session_document_view import TrainChatSessionDocumentView
from iblai.models.train_chat_session_document_view_request import TrainChatSessionDocumentViewRequest
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
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
train_chat_session_document_view_request = iblai.TrainChatSessionDocumentViewRequest() # TrainChatSessionDocumentViewRequest | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_train_sessions_create(org, session_id, user_id, train_chat_session_document_view_request)
    print("The response of AiIndexApi->ai_index_orgs_users_documents_train_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiIndexApi->ai_index_orgs_users_documents_train_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **train_chat_session_document_view_request** | [**TrainChatSessionDocumentViewRequest**](TrainChatSessionDocumentViewRequest.md)|  | 

### Return type

[**TrainChatSessionDocumentView**](TrainChatSessionDocumentView.md)

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

# **ai_index_orgs_users_documents_update**
> RetrieverDocumentEmbedding ai_index_orgs_users_documents_update(document_id, org, user_id, retriever_document_embedding_request)



This is for updating resource document details for a tenant.  Accessible to tenant admins only.  Returns:      404 : When document not found.      200 : Resource document details.  Example :      PUT : /api/ai-index/orgs/main/users/johndoe/documents/1/.      Request:        {                         \"document_name\": \"Sample\",                         \"document_type\": \"pdf\",                         \"pathway\": \"test-pathway\",                         \"url\": \"https://careertech.org/wp-content/uploads/sites/default/files/CareerClustersPathways_0.pdf\",                         \"platform_key\": \"main\",                         \"train\": true                     }      Response:       {                         \"id\": 1,                         \"document_name\": \"Sample\",                         \"document_type\": \"pdf\",                         \"pathway\": \"test-pathway\",                         \"url\": \"https://careertech.org/wp-content/uploads/sites/default/files/CareerClustersPathways_0.pdf\",                         \"tokens\": 9223372036854776000,                         \"platform_key\": \"main\",                         \"is_trained\": true                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retriever_document_embedding import RetrieverDocumentEmbedding
from iblai.models.retriever_document_embedding_request import RetrieverDocumentEmbeddingRequest
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
retriever_document_embedding_request = iblai.RetrieverDocumentEmbeddingRequest() # RetrieverDocumentEmbeddingRequest | 

try:
    api_response = api_instance.ai_index_orgs_users_documents_update(document_id, org, user_id, retriever_document_embedding_request)
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
 **retriever_document_embedding_request** | [**RetrieverDocumentEmbeddingRequest**](RetrieverDocumentEmbeddingRequest.md)|  | 

### Return type

[**RetrieverDocumentEmbedding**](RetrieverDocumentEmbedding.md)

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

