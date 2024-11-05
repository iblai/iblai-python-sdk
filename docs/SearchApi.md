# iblai.SearchApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_ai_search_detail_retrieve**](SearchApi.md#search_ai_search_detail_retrieve) | **GET** /api/search/ai-search/detail/ | 
[**search_ai_search_retrieve**](SearchApi.md#search_ai_search_retrieve) | **GET** /api/search/ai-search/ | 
[**search_catalog_retrieve**](SearchApi.md#search_catalog_retrieve) | **GET** /api/search/catalog/ | 
[**search_documentsearch_retrieve**](SearchApi.md#search_documentsearch_retrieve) | **GET** /api/search/documentsearch/ | 
[**search_es_health_retrieve**](SearchApi.md#search_es_health_retrieve) | **GET** /api/search/es-health/ | 
[**search_personalized_catalog_retrieve**](SearchApi.md#search_personalized_catalog_retrieve) | **GET** /api/search/personalized-catalog/{username}/ | 
[**search_search_retrieve**](SearchApi.md#search_search_retrieve) | **GET** /api/search/search/ | 
[**search_users_orgs_users_retrieve**](SearchApi.md#search_users_orgs_users_retrieve) | **GET** /api/search/users/orgs/{org}/users/{username}/ | 


# **search_ai_search_detail_retrieve**
> QueryEndpoint search_ai_search_detail_retrieve()



### Example


```python
import iblai
from iblai.models.query_endpoint import QueryEndpoint
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)

try:
    api_response = api_instance.search_ai_search_detail_retrieve()
    print("The response of SearchApi->search_ai_search_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_ai_search_detail_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryEndpoint**](QueryEndpoint.md)

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

# **search_ai_search_retrieve**
> QueryEndpoint search_ai_search_retrieve()



### Example


```python
import iblai
from iblai.models.query_endpoint import QueryEndpoint
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)

try:
    api_response = api_instance.search_ai_search_retrieve()
    print("The response of SearchApi->search_ai_search_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_ai_search_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryEndpoint**](QueryEndpoint.md)

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

# **search_catalog_retrieve**
> search_catalog_retrieve()



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)

try:
    api_instance.search_catalog_retrieve()
except Exception as e:
    print("Exception when calling SearchApi->search_catalog_retrieve: %s\n" % e)
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

# **search_documentsearch_retrieve**
> search_documentsearch_retrieve()



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
api_instance = iblai.SearchApi(api_client)

try:
    api_instance.search_documentsearch_retrieve()
except Exception as e:
    print("Exception when calling SearchApi->search_documentsearch_retrieve: %s\n" % e)
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

# **search_es_health_retrieve**
> search_es_health_retrieve()



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)

try:
    api_instance.search_es_health_retrieve()
except Exception as e:
    print("Exception when calling SearchApi->search_es_health_retrieve: %s\n" % e)
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

# **search_personalized_catalog_retrieve**
> search_personalized_catalog_retrieve(username)



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
username = 'username_example' # str | 

try:
    api_instance.search_personalized_catalog_retrieve(username)
except Exception as e:
    print("Exception when calling SearchApi->search_personalized_catalog_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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

# **search_search_retrieve**
> QueryEndpoint search_search_retrieve()



### Example


```python
import iblai
from iblai.models.query_endpoint import QueryEndpoint
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)

try:
    api_response = api_instance.search_search_retrieve()
    print("The response of SearchApi->search_search_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_search_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QueryEndpoint**](QueryEndpoint.md)

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

# **search_users_orgs_users_retrieve**
> search_users_orgs_users_retrieve(org, username)



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
api_instance = iblai.SearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.search_users_orgs_users_retrieve(org, username)
except Exception as e:
    print("Exception when calling SearchApi->search_users_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

