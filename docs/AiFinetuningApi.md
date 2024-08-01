# iblai.AiFinetuningApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_finetuning_v1_org_user_datasets_create**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_create) | **POST** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/ | 
[**ai_finetuning_v1_org_user_datasets_destroy**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_destroy) | **DELETE** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
[**ai_finetuning_v1_org_user_datasets_list**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_list) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/ | 
[**ai_finetuning_v1_org_user_datasets_partial_update**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_partial_update) | **PATCH** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
[**ai_finetuning_v1_org_user_datasets_retrieve**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
[**ai_finetuning_v1_org_user_datasets_update**](AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_update) | **PUT** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
[**ai_finetuning_v1_org_user_trainings_create**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_create) | **POST** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/ | 
[**ai_finetuning_v1_org_user_trainings_destroy**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_destroy) | **DELETE** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
[**ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/finetuned-models/ | 
[**ai_finetuning_v1_org_user_trainings_list**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_list) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/ | 
[**ai_finetuning_v1_org_user_trainings_partial_update**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_partial_update) | **PATCH** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
[**ai_finetuning_v1_org_user_trainings_retrieve**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
[**ai_finetuning_v1_org_user_trainings_update**](AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_update) | **PUT** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 


# **ai_finetuning_v1_org_user_datasets_create**
> DataSetCreate ai_finetuning_v1_org_user_datasets_create(org, username, data_set_create)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.data_set_create import DataSetCreate
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
api_instance = iblai.AiFinetuningApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
data_set_create = iblai.DataSetCreate() # DataSetCreate | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_datasets_create(org, username, data_set_create)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_datasets_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **data_set_create** | [**DataSetCreate**](DataSetCreate.md)|  | 

### Return type

[**DataSetCreate**](DataSetCreate.md)

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

# **ai_finetuning_v1_org_user_datasets_destroy**
> ai_finetuning_v1_org_user_datasets_destroy(id, org, username)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this data set.
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.ai_finetuning_v1_org_user_datasets_destroy(id, org, username)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this data set. | 
 **org** | **str**|  | 
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

# **ai_finetuning_v1_org_user_datasets_list**
> PaginatedDataSetList ai_finetuning_v1_org_user_datasets_list(org, username, date_created=date_created, num_data_points=num_data_points, ordering=ordering, page=page, page_size=page_size, retry_attempts=retry_attempts, search=search, status=status)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_data_set_list import PaginatedDataSetList
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
api_instance = iblai.AiFinetuningApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
num_data_points = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
retry_attempts = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `pending` - Pending * `processing` - Processing * `completed` - Completed * `failed` - Failed (optional)

try:
    api_response = api_instance.ai_finetuning_v1_org_user_datasets_list(org, username, date_created=date_created, num_data_points=num_data_points, ordering=ordering, page=page, page_size=page_size, retry_attempts=retry_attempts, search=search, status=status)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_datasets_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **date_created** | **datetime**|  | [optional] 
 **num_data_points** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **retry_attempts** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;pending&#x60; - Pending * &#x60;processing&#x60; - Processing * &#x60;completed&#x60; - Completed * &#x60;failed&#x60; - Failed | [optional] 

### Return type

[**PaginatedDataSetList**](PaginatedDataSetList.md)

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

# **ai_finetuning_v1_org_user_datasets_partial_update**
> DataSet ai_finetuning_v1_org_user_datasets_partial_update(id, org, username, patched_data_set=patched_data_set)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.data_set import DataSet
from iblai.models.patched_data_set import PatchedDataSet
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this data set.
org = 'org_example' # str | 
username = 'username_example' # str | 
patched_data_set = iblai.PatchedDataSet() # PatchedDataSet |  (optional)

try:
    api_response = api_instance.ai_finetuning_v1_org_user_datasets_partial_update(id, org, username, patched_data_set=patched_data_set)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_datasets_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this data set. | 
 **org** | **str**|  | 
 **username** | **str**|  | 
 **patched_data_set** | [**PatchedDataSet**](PatchedDataSet.md)|  | [optional] 

### Return type

[**DataSet**](DataSet.md)

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

# **ai_finetuning_v1_org_user_datasets_retrieve**
> DataSet ai_finetuning_v1_org_user_datasets_retrieve(id, org, username)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.data_set import DataSet
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this data set.
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_datasets_retrieve(id, org, username)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_datasets_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this data set. | 
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**DataSet**](DataSet.md)

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

# **ai_finetuning_v1_org_user_datasets_update**
> DataSet ai_finetuning_v1_org_user_datasets_update(id, org, username, data_set)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.data_set import DataSet
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this data set.
org = 'org_example' # str | 
username = 'username_example' # str | 
data_set = iblai.DataSet() # DataSet | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_datasets_update(id, org, username, data_set)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_datasets_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_datasets_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this data set. | 
 **org** | **str**|  | 
 **username** | **str**|  | 
 **data_set** | [**DataSet**](DataSet.md)|  | 

### Return type

[**DataSet**](DataSet.md)

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

# **ai_finetuning_v1_org_user_trainings_create**
> TrainingCreate ai_finetuning_v1_org_user_trainings_create(org, username, training_create)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.training_create import TrainingCreate
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
api_instance = iblai.AiFinetuningApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
training_create = iblai.TrainingCreate() # TrainingCreate | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_create(org, username, training_create)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **training_create** | [**TrainingCreate**](TrainingCreate.md)|  | 

### Return type

[**TrainingCreate**](TrainingCreate.md)

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

# **ai_finetuning_v1_org_user_trainings_destroy**
> ai_finetuning_v1_org_user_trainings_destroy(id, org, username)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this training.
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.ai_finetuning_v1_org_user_trainings_destroy(id, org, username)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this training. | 
 **org** | **str**|  | 
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

# **ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve**
> Training ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve(org, username)



Retrieves a paginated list of completed fine-tuned models, excluding those without a fine-tuned model. Filtering and pagination is allowed.  NB: This is only a helper endpoint. The same functionality can be achieved with the appropriate filters using the     training list endpoint. Returns:     Response: A paginated response containing the serialized fine-tuned models.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.training import Training
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
api_instance = iblai.AiFinetuningApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve(org, username)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Training**](Training.md)

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

# **ai_finetuning_v1_org_user_trainings_list**
> PaginatedTrainingList ai_finetuning_v1_org_user_trainings_list(org, username, base_model_name=base_model_name, dataset=dataset, date_created=date_created, fine_tuned_model=fine_tuned_model, last_modified=last_modified, ordering=ordering, page=page, page_size=page_size, preprocess_dataset=preprocess_dataset, provider=provider, search=search, status=status)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_training_list import PaginatedTrainingList
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
api_instance = iblai.AiFinetuningApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
base_model_name = 'base_model_name_example' # str |  (optional)
dataset = 'dataset_example' # str |  (optional)
date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
fine_tuned_model = 'fine_tuned_model_example' # str |  (optional)
last_modified = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
preprocess_dataset = True # bool |  (optional)
provider = 'provider_example' # str | * `openai` - Openai (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `pending` - Pending * `processing` - Processing * `completed` - Completed * `cancelled` - Cancelled * `failed` - Failed (optional)

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_list(org, username, base_model_name=base_model_name, dataset=dataset, date_created=date_created, fine_tuned_model=fine_tuned_model, last_modified=last_modified, ordering=ordering, page=page, page_size=page_size, preprocess_dataset=preprocess_dataset, provider=provider, search=search, status=status)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **base_model_name** | **str**|  | [optional] 
 **dataset** | **str**|  | [optional] 
 **date_created** | **datetime**|  | [optional] 
 **fine_tuned_model** | **str**|  | [optional] 
 **last_modified** | **datetime**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **preprocess_dataset** | **bool**|  | [optional] 
 **provider** | **str**| * &#x60;openai&#x60; - Openai | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;pending&#x60; - Pending * &#x60;processing&#x60; - Processing * &#x60;completed&#x60; - Completed * &#x60;cancelled&#x60; - Cancelled * &#x60;failed&#x60; - Failed | [optional] 

### Return type

[**PaginatedTrainingList**](PaginatedTrainingList.md)

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

# **ai_finetuning_v1_org_user_trainings_partial_update**
> TrainingCreate ai_finetuning_v1_org_user_trainings_partial_update(id, org, username, patched_training_create=patched_training_create)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_training_create import PatchedTrainingCreate
from iblai.models.training_create import TrainingCreate
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this training.
org = 'org_example' # str | 
username = 'username_example' # str | 
patched_training_create = iblai.PatchedTrainingCreate() # PatchedTrainingCreate |  (optional)

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_partial_update(id, org, username, patched_training_create=patched_training_create)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this training. | 
 **org** | **str**|  | 
 **username** | **str**|  | 
 **patched_training_create** | [**PatchedTrainingCreate**](PatchedTrainingCreate.md)|  | [optional] 

### Return type

[**TrainingCreate**](TrainingCreate.md)

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

# **ai_finetuning_v1_org_user_trainings_retrieve**
> Training ai_finetuning_v1_org_user_trainings_retrieve(id, org, username)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.training import Training
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this training.
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_retrieve(id, org, username)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this training. | 
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Training**](Training.md)

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

# **ai_finetuning_v1_org_user_trainings_update**
> TrainingCreate ai_finetuning_v1_org_user_trainings_update(id, org, username, training_create)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.training_create import TrainingCreate
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
api_instance = iblai.AiFinetuningApi(api_client)
id = 'id_example' # str | A UUID string identifying this training.
org = 'org_example' # str | 
username = 'username_example' # str | 
training_create = iblai.TrainingCreate() # TrainingCreate | 

try:
    api_response = api_instance.ai_finetuning_v1_org_user_trainings_update(id, org, username, training_create)
    print("The response of AiFinetuningApi->ai_finetuning_v1_org_user_trainings_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiFinetuningApi->ai_finetuning_v1_org_user_trainings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this training. | 
 **org** | **str**|  | 
 **username** | **str**|  | 
 **training_create** | [**TrainingCreate**](TrainingCreate.md)|  | 

### Return type

[**TrainingCreate**](TrainingCreate.md)

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

