# iblai.AiAccountApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_account_orgs_credential_create**](AiAccountApi.md#ai_account_orgs_credential_create) | **POST** /api/ai-account/orgs/{org}/credential/ | 
[**ai_account_orgs_credential_partial_update**](AiAccountApi.md#ai_account_orgs_credential_partial_update) | **PATCH** /api/ai-account/orgs/{org}/credential/ | 
[**ai_account_orgs_credential_retrieve**](AiAccountApi.md#ai_account_orgs_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/credential/ | 
[**ai_account_orgs_integration_credential_create**](AiAccountApi.md#ai_account_orgs_integration_credential_create) | **POST** /api/ai-account/orgs/{org}/integration-credential/ | 
[**ai_account_orgs_integration_credential_partial_update**](AiAccountApi.md#ai_account_orgs_integration_credential_partial_update) | **PATCH** /api/ai-account/orgs/{org}/integration-credential/ | 
[**ai_account_orgs_integration_credential_retrieve**](AiAccountApi.md#ai_account_orgs_integration_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/integration-credential/ | 
[**ai_account_orgs_platform_metadata_create**](AiAccountApi.md#ai_account_orgs_platform_metadata_create) | **POST** /api/ai-account/orgs/{org}/platform-metadata/ | 
[**ai_account_orgs_platform_metadata_list**](AiAccountApi.md#ai_account_orgs_platform_metadata_list) | **GET** /api/ai-account/orgs/{org}/platform-metadata/ | 
[**ai_account_orgs_platform_metadata_update**](AiAccountApi.md#ai_account_orgs_platform_metadata_update) | **PUT** /api/ai-account/orgs/{org}/platform-metadata/ | 
[**ai_account_orgs_tokens_list**](AiAccountApi.md#ai_account_orgs_tokens_list) | **GET** /api/ai-account/orgs/{org}/tokens/ | 
[**ai_account_orgs_use_default_llm_key_create**](AiAccountApi.md#ai_account_orgs_use_default_llm_key_create) | **POST** /api/ai-account/orgs/{org}/use-default-llm-key/ | 
[**ai_account_orgs_use_free_trial_create**](AiAccountApi.md#ai_account_orgs_use_free_trial_create) | **POST** /api/ai-account/orgs/{org}/use-free-trial/ | 
[**ai_account_orgs_users_default_llm_key_usage_retrieve**](AiAccountApi.md#ai_account_orgs_users_default_llm_key_usage_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/default-llm-key-usage | 
[**ai_account_orgs_users_free_trial_retrieve**](AiAccountApi.md#ai_account_orgs_users_free_trial_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/free-trial | 


# **ai_account_orgs_credential_create**
> LLMCredentialResponse ai_account_orgs_credential_create(org, llm_credential_request)



Create a new LLM credential for an organization.  Args:     request: The HTTP request containing credential information     org: Organization key identifier  Returns:     Response: Created LLM credential  Raises:     NotFound: When organization is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_credential_request import LLMCredentialRequest
from iblai.models.llm_credential_response import LLMCredentialResponse
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
llm_credential_request = {"name":"openai","value":{"key":"sk-xxxxxxxxxxxxxxxxxxxx"},"platform":"main"} # LLMCredentialRequest | 

try:
    api_response = api_instance.ai_account_orgs_credential_create(org, llm_credential_request)
    print("The response of AiAccountApi->ai_account_orgs_credential_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_credential_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **llm_credential_request** | [**LLMCredentialRequest**](LLMCredentialRequest.md)|  | 

### Return type

[**LLMCredentialResponse**](LLMCredentialResponse.md)

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

# **ai_account_orgs_credential_partial_update**
> LLMCredentialResponse ai_account_orgs_credential_partial_update(org, patched_llm_credential_request=patched_llm_credential_request)



Update an existing LLM credential for an organization.  Args:     request: The HTTP request containing updated credential information     org: Organization key identifier  Returns:     Response: Updated LLM credential  Raises:     NotFound: When organization or credential is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_credential_response import LLMCredentialResponse
from iblai.models.patched_llm_credential_request import PatchedLLMCredentialRequest
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
patched_llm_credential_request = iblai.PatchedLLMCredentialRequest() # PatchedLLMCredentialRequest |  (optional)

try:
    api_response = api_instance.ai_account_orgs_credential_partial_update(org, patched_llm_credential_request=patched_llm_credential_request)
    print("The response of AiAccountApi->ai_account_orgs_credential_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_credential_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_llm_credential_request** | [**PatchedLLMCredentialRequest**](PatchedLLMCredentialRequest.md)|  | [optional] 

### Return type

[**LLMCredentialResponse**](LLMCredentialResponse.md)

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

# **ai_account_orgs_credential_retrieve**
> LLMCredentialResponse ai_account_orgs_credential_retrieve(org, name=name)



Retrieve LLM credentials for an organization.  Query Parameters:     name (optional): Filter results by LLM provider name  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: List of LLM credentials for the organization  Raises:     NotFound: When organization is not found or when no credentials match the filters     ValidationError: When query parameters are invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_credential_response import LLMCredentialResponse
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
name = 'name_example' # str | Filter credentials by provider name (e.g., 'openai', 'google') (optional)

try:
    api_response = api_instance.ai_account_orgs_credential_retrieve(org, name=name)
    print("The response of AiAccountApi->ai_account_orgs_credential_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_credential_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **name** | **str**| Filter credentials by provider name (e.g., &#39;openai&#39;, &#39;google&#39;) | [optional] 

### Return type

[**LLMCredentialResponse**](LLMCredentialResponse.md)

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

# **ai_account_orgs_integration_credential_create**
> IntegrationCredential ai_account_orgs_integration_credential_create(org, credential_request)



Create a new integration credential for an organization.  Args:     request: The HTTP request containing credential information     org: Organization key identifier  Returns:     Response: Created integration credential  Raises:     NotFound: When organization is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_request import CredentialRequest
from iblai.models.integration_credential import IntegrationCredential
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
credential_request = {"name":"google-drive","value":{"type":"service_account","project_id":"project-id","private_key":"-----BEGIN PRIVATE KEY-----\nXXXX\n-----END PRIVATE KEY-----\n","client_email":"service-account@project.iam.gserviceaccount.com"},"platform":"main"} # CredentialRequest | 

try:
    api_response = api_instance.ai_account_orgs_integration_credential_create(org, credential_request)
    print("The response of AiAccountApi->ai_account_orgs_integration_credential_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_integration_credential_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **credential_request** | [**CredentialRequest**](CredentialRequest.md)|  | 

### Return type

[**IntegrationCredential**](IntegrationCredential.md)

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

# **ai_account_orgs_integration_credential_partial_update**
> IntegrationCredential ai_account_orgs_integration_credential_partial_update(org, patched_credential_request=patched_credential_request)



Update an existing integration credential for an organization.  Args:     request: The HTTP request containing updated credential information     org: Organization key identifier  Returns:     Response: Updated integration credential  Raises:     NotFound: When organization or credential is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.integration_credential import IntegrationCredential
from iblai.models.patched_credential_request import PatchedCredentialRequest
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
patched_credential_request = iblai.PatchedCredentialRequest() # PatchedCredentialRequest |  (optional)

try:
    api_response = api_instance.ai_account_orgs_integration_credential_partial_update(org, patched_credential_request=patched_credential_request)
    print("The response of AiAccountApi->ai_account_orgs_integration_credential_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_integration_credential_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_credential_request** | [**PatchedCredentialRequest**](PatchedCredentialRequest.md)|  | [optional] 

### Return type

[**IntegrationCredential**](IntegrationCredential.md)

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

# **ai_account_orgs_integration_credential_retrieve**
> IntegrationCredential ai_account_orgs_integration_credential_retrieve(org, name=name)



Retrieve integration credentials for an organization.  Query Parameters:     name (optional): Filter results by integration service name  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: List of integration credentials for the organization  Raises:     NotFound: When organization is not found or when no credentials match the filters     ValidationError: When query parameters are invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.integration_credential import IntegrationCredential
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
name = 'name_example' # str | Filter credentials by provider name (e.g., 'openai', 'google') (optional)

try:
    api_response = api_instance.ai_account_orgs_integration_credential_retrieve(org, name=name)
    print("The response of AiAccountApi->ai_account_orgs_integration_credential_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_integration_credential_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **name** | **str**| Filter credentials by provider name (e.g., &#39;openai&#39;, &#39;google&#39;) | [optional] 

### Return type

[**IntegrationCredential**](IntegrationCredential.md)

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

# **ai_account_orgs_platform_metadata_create**
> IBLAIPlatformMeta ai_account_orgs_platform_metadata_create(org, iblai_platform_meta_request)



Create or update platform metadata for a specific organization.  Args:     request: The HTTP request containing metadata information     org: Organization key identifier  Returns:     Response: Created/updated platform metadata  Raises:     NotFound: When platform is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.iblai_platform_meta import IBLAIPlatformMeta
from iblai.models.iblai_platform_meta_request import IBLAIPlatformMetaRequest
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
iblai_platform_meta_request = iblai.IBLAIPlatformMetaRequest() # IBLAIPlatformMetaRequest | 

try:
    api_response = api_instance.ai_account_orgs_platform_metadata_create(org, iblai_platform_meta_request)
    print("The response of AiAccountApi->ai_account_orgs_platform_metadata_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_platform_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **iblai_platform_meta_request** | [**IBLAIPlatformMetaRequest**](IBLAIPlatformMetaRequest.md)|  | 

### Return type

[**IBLAIPlatformMeta**](IBLAIPlatformMeta.md)

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

# **ai_account_orgs_platform_metadata_list**
> List[IBLAIPlatformMeta] ai_account_orgs_platform_metadata_list(org)



Retrieve platform metadata for a specific organization.  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: Platform metadata including service configurations and active services  Raises:     NotFound: When platform metadata is not found

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.iblai_platform_meta import IBLAIPlatformMeta
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_account_orgs_platform_metadata_list(org)
    print("The response of AiAccountApi->ai_account_orgs_platform_metadata_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_platform_metadata_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[IBLAIPlatformMeta]**](IBLAIPlatformMeta.md)

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

# **ai_account_orgs_platform_metadata_update**
> List[IBLAIPlatformMeta] ai_account_orgs_platform_metadata_update(org, iblai_platform_meta_update_request=iblai_platform_meta_update_request)



Update specific fields of platform metadata for an organization.  This endpoint allows updating the active LLM provider and available LLMs.  Args:     request: The HTTP request containing update information     org: Organization key identifier  Returns:     Response: Updated platform metadata  Raises:     NotFound: When platform metadata is not found     ValidationError: When request data is invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.iblai_platform_meta import IBLAIPlatformMeta
from iblai.models.iblai_platform_meta_update_request import IBLAIPlatformMetaUpdateRequest
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
iblai_platform_meta_update_request = iblai.IBLAIPlatformMetaUpdateRequest() # IBLAIPlatformMetaUpdateRequest |  (optional)

try:
    api_response = api_instance.ai_account_orgs_platform_metadata_update(org, iblai_platform_meta_update_request=iblai_platform_meta_update_request)
    print("The response of AiAccountApi->ai_account_orgs_platform_metadata_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_platform_metadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **iblai_platform_meta_update_request** | [**IBLAIPlatformMetaUpdateRequest**](IBLAIPlatformMetaUpdateRequest.md)|  | [optional] 

### Return type

[**List[IBLAIPlatformMeta]**](IBLAIPlatformMeta.md)

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

# **ai_account_orgs_tokens_list**
> List[APITokenCost] ai_account_orgs_tokens_list(org, session_id=session_id, username=username)



Retrieve weekly token usage statistics for an organization.  Query Parameters:     username (optional): Filter results by specific username     session_id (optional): Filter results by specific session ID  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: List of weekly token usage records with prompt and completion tokens  Raises:     NotFound: When organization is not found or when no sessions match the filters     ValidationError: When query parameters are invalid

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.api_token_cost import APITokenCost
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | Filter token usage by specific chat session ID (optional)
username = 'username_example' # str | Filter token usage by specific username (optional)

try:
    api_response = api_instance.ai_account_orgs_tokens_list(org, session_id=session_id, username=username)
    print("The response of AiAccountApi->ai_account_orgs_tokens_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**| Filter token usage by specific chat session ID | [optional] 
 **username** | **str**| Filter token usage by specific username | [optional] 

### Return type

[**List[APITokenCost]**](APITokenCost.md)

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

# **ai_account_orgs_use_default_llm_key_create**
> AiAccountOrgsUseDefaultLlmKeyCreate200Response ai_account_orgs_use_default_llm_key_create(org, use_main_creds)



Enable or disable the use of main LLM credentials for an organization.  Request Body:     enable (boolean): Set to true to enable main credentials     disable (boolean): Set to true to disable main credentials  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: Confirmation message  Raises:     ValidationError: When neither enable nor disable is specified

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_account_orgs_use_default_llm_key_create200_response import AiAccountOrgsUseDefaultLlmKeyCreate200Response
from iblai.models.use_main_creds import UseMainCreds
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
use_main_creds = {"enable":true,"disable":false} # UseMainCreds | 

try:
    api_response = api_instance.ai_account_orgs_use_default_llm_key_create(org, use_main_creds)
    print("The response of AiAccountApi->ai_account_orgs_use_default_llm_key_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_use_default_llm_key_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **use_main_creds** | [**UseMainCreds**](UseMainCreds.md)|  | 

### Return type

[**AiAccountOrgsUseDefaultLlmKeyCreate200Response**](AiAccountOrgsUseDefaultLlmKeyCreate200Response.md)

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

# **ai_account_orgs_use_free_trial_create**
> ai_account_orgs_use_free_trial_create(org)



Enable, disable, or update free trial settings for an organization.  Request Body:     enable (boolean): Set to true to enable free trial     disable (boolean): Set to true to disable free trial     metadata (object, optional): Additional metadata for the free trial  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: Confirmation message

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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.ai_account_orgs_use_free_trial_create(org)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_use_free_trial_create: %s\n" % e)
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

# **ai_account_orgs_users_default_llm_key_usage_retrieve**
> ai_account_orgs_users_default_llm_key_usage_retrieve(org, user_id)



Retrieve the status of main LLM credential usage for an organization.  Args:     request: The HTTP request     org: Organization key identifier     user_id: User identifier  Returns:     Response: Status of main LLM credential usage

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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_account_orgs_users_default_llm_key_usage_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_users_default_llm_key_usage_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_account_orgs_users_free_trial_retrieve**
> AiAccountOrgsUsersFreeTrialRetrieve200Response ai_account_orgs_users_free_trial_retrieve(org, user_id)



Retrieve the free trial status for an organization.  Args:     request: The HTTP request     org: Organization key identifier  Returns:     Response: Free trial status (boolean)  Raises:     NotFound: When organization is not found

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_account_orgs_users_free_trial_retrieve200_response import AiAccountOrgsUsersFreeTrialRetrieve200Response
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
api_instance = iblai.AiAccountApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_account_orgs_users_free_trial_retrieve(org, user_id)
    print("The response of AiAccountApi->ai_account_orgs_users_free_trial_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_users_free_trial_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AiAccountOrgsUsersFreeTrialRetrieve200Response**](AiAccountOrgsUsersFreeTrialRetrieve200Response.md)

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

