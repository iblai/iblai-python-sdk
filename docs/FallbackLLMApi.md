# iblai.FallbackLLMApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_account_orgs_fallback_llm_create**](FallbackLLMApi.md#ai_account_orgs_fallback_llm_create) | **POST** /api/ai-account/orgs/{org}/fallback-llm/ | Create fallback LLM configuration
[**ai_account_orgs_fallback_llm_destroy**](FallbackLLMApi.md#ai_account_orgs_fallback_llm_destroy) | **DELETE** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Delete fallback LLM configuration
[**ai_account_orgs_fallback_llm_partial_update**](FallbackLLMApi.md#ai_account_orgs_fallback_llm_partial_update) | **PATCH** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Partially update fallback LLM configuration
[**ai_account_orgs_fallback_llm_retrieve**](FallbackLLMApi.md#ai_account_orgs_fallback_llm_retrieve) | **GET** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Get fallback LLM configuration
[**ai_account_orgs_fallback_llm_update**](FallbackLLMApi.md#ai_account_orgs_fallback_llm_update) | **PUT** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Update fallback LLM configuration


# **ai_account_orgs_fallback_llm_create**
> FallbackLLM ai_account_orgs_fallback_llm_create(org, fallback_llm_create)

Create fallback LLM configuration


        Create a new fallback LLM configuration.

        - For model scope: specify source_model_name
        - For provider scope: only source_provider_name is needed
        - Leave tenant_key empty for global configuration
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.fallback_llm import FallbackLLM
from iblai.models.fallback_llm_create import FallbackLLMCreate
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
api_instance = iblai.FallbackLLMApi(api_client)
org = 'org_example' # str | 
fallback_llm_create = iblai.FallbackLLMCreate() # FallbackLLMCreate | 

try:
    # Create fallback LLM configuration
    api_response = api_instance.ai_account_orgs_fallback_llm_create(org, fallback_llm_create)
    print("The response of FallbackLLMApi->ai_account_orgs_fallback_llm_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FallbackLLMApi->ai_account_orgs_fallback_llm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **fallback_llm_create** | [**FallbackLLMCreate**](FallbackLLMCreate.md)|  | 

### Return type

[**FallbackLLM**](FallbackLLM.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Validation error |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_account_orgs_fallback_llm_destroy**
> ai_account_orgs_fallback_llm_destroy(id, org)

Delete fallback LLM configuration

Delete a fallback LLM configuration.

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
api_instance = iblai.FallbackLLMApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    # Delete fallback LLM configuration
    api_instance.ai_account_orgs_fallback_llm_destroy(id, org)
except Exception as e:
    print("Exception when calling FallbackLLMApi->ai_account_orgs_fallback_llm_destroy: %s\n" % e)
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
**204** | Deleted successfully |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_account_orgs_fallback_llm_partial_update**
> FallbackLLM ai_account_orgs_fallback_llm_partial_update(id, org, patched_fallback_llm_update=patched_fallback_llm_update)

Partially update fallback LLM configuration

Partially update an existing fallback LLM configuration.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.fallback_llm import FallbackLLM
from iblai.models.patched_fallback_llm_update import PatchedFallbackLLMUpdate
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
api_instance = iblai.FallbackLLMApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 
patched_fallback_llm_update = iblai.PatchedFallbackLLMUpdate() # PatchedFallbackLLMUpdate |  (optional)

try:
    # Partially update fallback LLM configuration
    api_response = api_instance.ai_account_orgs_fallback_llm_partial_update(id, org, patched_fallback_llm_update=patched_fallback_llm_update)
    print("The response of FallbackLLMApi->ai_account_orgs_fallback_llm_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FallbackLLMApi->ai_account_orgs_fallback_llm_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 
 **patched_fallback_llm_update** | [**PatchedFallbackLLMUpdate**](PatchedFallbackLLMUpdate.md)|  | [optional] 

### Return type

[**FallbackLLM**](FallbackLLM.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Validation error |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_account_orgs_fallback_llm_retrieve**
> FallbackLLM ai_account_orgs_fallback_llm_retrieve(id, org)

Get fallback LLM configuration

Retrieve a specific fallback LLM configuration.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.fallback_llm import FallbackLLM
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
api_instance = iblai.FallbackLLMApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 

try:
    # Get fallback LLM configuration
    api_response = api_instance.ai_account_orgs_fallback_llm_retrieve(id, org)
    print("The response of FallbackLLMApi->ai_account_orgs_fallback_llm_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FallbackLLMApi->ai_account_orgs_fallback_llm_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 

### Return type

[**FallbackLLM**](FallbackLLM.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_account_orgs_fallback_llm_update**
> FallbackLLM ai_account_orgs_fallback_llm_update(id, org, fallback_llm_update)

Update fallback LLM configuration

Update an existing fallback LLM configuration.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.fallback_llm import FallbackLLM
from iblai.models.fallback_llm_update import FallbackLLMUpdate
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
api_instance = iblai.FallbackLLMApi(api_client)
id = 'id_example' # str | 
org = 'org_example' # str | 
fallback_llm_update = iblai.FallbackLLMUpdate() # FallbackLLMUpdate | 

try:
    # Update fallback LLM configuration
    api_response = api_instance.ai_account_orgs_fallback_llm_update(id, org, fallback_llm_update)
    print("The response of FallbackLLMApi->ai_account_orgs_fallback_llm_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FallbackLLMApi->ai_account_orgs_fallback_llm_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **org** | **str**|  | 
 **fallback_llm_update** | [**FallbackLLMUpdate**](FallbackLLMUpdate.md)|  | 

### Return type

[**FallbackLLM**](FallbackLLM.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Validation error |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

