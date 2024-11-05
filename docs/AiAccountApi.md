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
[**ai_account_orgs_users_free_trial_list**](AiAccountApi.md#ai_account_orgs_users_free_trial_list) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/free-trial | 


# **ai_account_orgs_credential_create**
> LLMCredentialResponse ai_account_orgs_credential_create(org, credential_request)



This is for creating llm credentials for a tenant.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.  Returns:      400: When the data is not valid, when the name already exists for the same tenant.      400: When the name already exists for the same tenant.      400: When the name already exists for the same tenant.      201 : Llm credential details.  Example :      POST : /api/ai-account/orgs/main/credential/ .      Request:       {                         \"name\": \"openai\",                         \"value\": {                             \"key\": \"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"                         },                         \"platform\": \"main\"                     }       Response:       {                         \"name\": \"openai\",                         \"value\": {                             \"key\": \"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"                         },                         \"platform\": \"main\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential_request import CredentialRequest
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
credential_request = iblai.CredentialRequest() # CredentialRequest | 

try:
    api_response = api_instance.ai_account_orgs_credential_create(org, credential_request)
    print("The response of AiAccountApi->ai_account_orgs_credential_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_credential_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **credential_request** | [**CredentialRequest**](CredentialRequest.md)|  | 

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
> LLMCredentialResponse ai_account_orgs_credential_partial_update(org, patched_credential_request=patched_credential_request)



This is for updating llm credentials for a tenant.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.      NotFound: When the name passed is not found.  Returns:      400: When the data is not valid, when the name already exists for the same tenant.      400: When the name already exists for the same tenant.      400: When the name already exists for the same tenant.      200 : Llm credential details.  Example :      POST : /api/ai-account/orgs/main/credential/ .      Request:       {                         \"name\": \"openai\",                         \"value\": {                             \"key\": \"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"                         },                         \"platform\": \"main\"                     }       Response:       {                         \"name\": \"openai\",                         \"value\": {                             \"key\": \"sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"                         },                         \"platform\": \"main\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_credential_response import LLMCredentialResponse
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
    api_response = api_instance.ai_account_orgs_credential_partial_update(org, patched_credential_request=patched_credential_request)
    print("The response of AiAccountApi->ai_account_orgs_credential_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_credential_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_credential_request** | [**PatchedCredentialRequest**](PatchedCredentialRequest.md)|  | [optional] 

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



This is for getting list of llm credentials for a tenant.  You can also filter the llm credentials by passing a query parameter name=<llm_name>.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.      NotFound: When the llm name passed in the paramter is not found.   Returns:      400: When the data is not valid.      200 : List of llm credentials.  Example :      GET : /api/ai-account/orgs/main/credential/ .      Response:       [                         {                             \"name\": \"openai\",                             \"value\": {                                 \"key\": \"sk-xxxxxxxxxxxxxxxxxxxxx\"                             },                             \"platform\": \"main\"                         },                         {                             \"name\": \"google\",                             \"value\": {                                 \"type\": \"service_account\",                                 \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                 \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"token_uri\": \"https://oauth2.googleapis.com/token\",                                 \"project_id\": \"xxxxxxxxxxxxxx\",                                 \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                                 \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"universe_domain\": \"googleapis.com\",                                 \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                                 \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                             },                             \"platform\": \"main\"                         }                     ]

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
name = 'name_example' # str | Name of the credential provider (optional)

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
 **name** | **str**| Name of the credential provider | [optional] 

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



This is for creating integration credentials for a tenant.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.  Returns:      400: When the data is not valid, when the name already exists for the same tenant.      400: When the name already exists for the same tenant.      201 : Tntegration credential details.  Example :      POST : /api/ai-account/orgs/main/integration-credential/ .      Request:       {                         \"name\": \"google-drive\",                         \"value\": {                             \"type\": \"service_account\",                             \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                             \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"token_uri\": \"https://oauth2.googleapis.com/token\",                             \"project_id\": \"xxxxxxxxxxxxxx\",                             \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                             \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"universe_domain\": \"googleapis.com\",                             \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                             \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                         },                         \"platform\": \"main\"                     }       Response:       {                         \"name\": \"google-drive\",                         \"value\": {                             \"type\": \"service_account\",                             \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                             \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"token_uri\": \"https://oauth2.googleapis.com/token\",                             \"project_id\": \"xxxxxxxxxxxxxx\",                             \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                             \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"universe_domain\": \"googleapis.com\",                             \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                             \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                         },                         \"platform\": \"main\"                     }

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
credential_request = iblai.CredentialRequest() # CredentialRequest | 

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



This is for updating Integration credentials for a tenant.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.      NotFound: When the name passed is not found.  Returns:      400: When the data is not valid, when the name already exists for the same tenant.      400: When the name already exists for the same tenant.      200 : Llm redential details.  Example :      POST : /api/ai-account/orgs/main/integration-credential/ .      Request:       {                         \"name\": \"google-drive\",                         \"value\": {                             \"type\": \"service_account\",                             \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                             \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"token_uri\": \"https://oauth2.googleapis.com/token\",                             \"project_id\": \"xxxxxxxxxxxxxx\",                             \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                             \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"universe_domain\": \"googleapis.com\",                             \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                             \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                         },                         \"platform\": \"main\"                     }       Response:       {                         \"name\": \"google-drive\",                         \"value\": {                             \"type\": \"service_account\",                             \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                             \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"token_uri\": \"https://oauth2.googleapis.com/token\",                             \"project_id\": \"xxxxxxxxxxxxxx\",                             \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                             \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                             \"universe_domain\": \"googleapis.com\",                             \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                             \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                         }                         \"platform\": \"main\"                     }

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



This is for getting  a list of integration credentials for a tenant.  You can also filter the integration credentials by passing a query parameter name=<llm_name>.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.      NotFound: When the  name passed in the paramter is not found.   Returns:      400: When the data is not valid.      200 : List of integration credentials.  Example :      GET : /api/ai-account/orgs/main/integration-credential/ .      Response:       [                         {                             \"name\": \"google-drive\",                             \"value\": {                                 \"type\": \"service_account\",                                 \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                 \"client_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"token_uri\": \"https://oauth2.googleapis.com/token\",                                 \"project_id\": \"xxxxxxxxxxxxxx\",                                 \"private_key\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"client_email\": \"xxx-xxx-sa@xx-xxxx.iam.gserviceaccount.com\",                                 \"private_key_id\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\",                                 \"universe_domain\": \"googleapis.com\",                                 \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/xxxxxxxx.com\",                                 \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                             },                             \"platform\": \"main\"                         }                     ]

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
name = 'name_example' # str | Name of the credential provider (optional)

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
 **name** | **str**| Name of the credential provider | [optional] 

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



This is for  adding platform metadata. In order to use google as your LLM provider, you need to specify `google_project` (your google cloud project id) and `google_location`, which defaults to `us-central1`  Accessible to tenant admins only.  Raises:      NotFound: When platfom metadata is not found.  Returns:      201 : Platform metadata details.  Example :      GET : /api/ai-account/orgs/main/platform-metadata/ .      Request:        {                         \"data\": {                             \"llms\": {                                 \"google\": {                                     \"credential\": {                                         \"type\": \"service_account\",                                         \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                         \"client_id\": \"\",                                         \"token_uri\": \"https://oauth2.googleapis.com/token\",                                         \"project_id\": \"NO PROJECT ID IS PROVIDED\",                                         \"private_key\": \"\",                                         \"client_email\": \"\",                                         \"private_key_id\": \"\",                                         \"universe_domain\": \"googleapis.com\",                                         \"client_x509_cert_url\": \"\",                                         \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",                                     },                                     \"llm_options\": {\"temperature\": 0.7},                                 },                                 \"openai\": {                                     \"credential\": {\"key\": \"NO KEY IS PROVIDED\"},                                     \"llm_options\": {\"temperature\": 0.7},                                 },                             },                         },                     }      Response:       {                         \"metadata\": {                             \"llms\": {                                 \"google\": {                                     \"credential\": {                                         \"type\": \"service_account\",                                         \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                         \"client_id\": \"\",                                         \"token_uri\": \"https://oauth2.googleapis.com/token\",                                         \"project_id\": \"NO PROJECT ID IS PROVIDED\",                                         \"private_key\": \"\",                                         \"client_email\": \"\",                                         \"private_key_id\": \"\",                                         \"universe_domain\": \"googleapis.com\",                                         \"client_x509_cert_url\": \"\",                                         \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",                                     },                                     \"llm_options\": {\"temperature\": 0.7},                                 },                                 \"openai\": {                                     \"credential\": {\"key\": \"NO KEY IS PROVIDED\"},                                     \"llm_options\": {\"temperature\": 0.7},                                 },                             },                             \"active_llm\": \"openai\",                         }                     }

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



This is for getting platform metadata.  Accessible to tenant admins only.  Raises:      NotFound: When platfom metadata is not found.  Returns:      200 : Platform metadata details.  Example :      GET : /api/ai-account/orgs/main/platform-metadata/ .      Response:       {                         \"metadata\": {                             \"services\": {                                 \"google\": {                                     \"credential\": {                                         \"type\": \"service_account\",                                         \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                         \"client_id\": \"\",                                         \"token_uri\": \"https://oauth2.googleapis.com/token\",                                         \"project_id\": \"NO PROJECT ID IS PROVIDED\",                                         \"private_key\": \"\",                                         \"client_email\": \"\",                                         \"private_key_id\": \"\",                                         \"universe_domain\": \"googleapis.com\",                                         \"client_x509_cert_url\": \"\",                                         \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                                     },                                     \"llm_options\": {                                         \"temperature\": 0.7                                     }                                 },                                 \"openai\": {                                     \"credential\": {                                         \"key\": \"NO KEY IS PROVIDED\"                                     },                                     \"llm_options\": {                                         \"temperature\": 0.7                                     }                                 }                             },                             \"active_llm\": \"openai\",                             \"active_stt\": \"google\",                             \"active_tts\": \"google\"                         }                     }

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



This is for  updating platform metadata.  Accessible to tenant admins only.  Raises:      NotFound: When platfom metadata is not found.  Returns:      200 : Platform metadata details.  Example :      GET : /api/ai-account/orgs/main/platform-metadata/ .      Request:        {                         \"active_llm\": \"openai\",                         \"llms\": [\"google\", \"openai\"]                     }      Response:       {                         \"metadata\": {                             \"services\": {                                 \"google\": {                                     \"credential\": {                                         \"type\": \"service_account\",                                         \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",                                         \"client_id\": \"\",                                         \"token_uri\": \"https://oauth2.googleapis.com/token\",                                         \"project_id\": \"NO PROJECT ID IS PROVIDED\",                                         \"private_key\": \"\",                                         \"client_email\": \"\",                                         \"private_key_id\": \"\",                                         \"universe_domain\": \"googleapis.com\",                                         \"client_x509_cert_url\": \"\",                                         \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\"                                     },                                     \"llm_options\": {                                         \"temperature\": 0.7                                     }                                 },                                 \"openai\": {                                     \"credential\": {                                         \"key\": \"NO KEY IS PROVIDED\"                                     },                                     \"llm_options\": {                                         \"temperature\": 0.7                                     }                                 }                             },                             \"active_llm\": \"openai\",                             \"active_stt\": \"google\",                             \"active_tts\": \"google\"                         }                     }

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



This is for getting weekly tokens.  You can also filter the list  by passing a query parameter username=<username> and session_id=<session_id>.  Accessible to tenant admins only.  Raises:      NotFound: When organization is not found.      NotFound: When session id is not found.   Returns:      400: When the data is not valid.      200 : List of tokens.  Example :      GET : /api/ai-account/orgs/main/tokens/ .      Response:       [                         {                             \"date\": \"2024-02-05\",                             \"completion_tokens\": 2147483647,                             \"prompt_tokens\": 123456785                         }                     ]

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
session_id = 'session_id_example' # str | session id of the user's chat (optional)
username = 'username_example' # str | Username of the user (optional)

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
 **session_id** | **str**| session id of the user&#39;s chat | [optional] 
 **username** | **str**| Username of the user | [optional] 

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
> UseMainCreds ai_account_orgs_use_default_llm_key_create(org, use_main_creds)



Endpoint to enable or disable the usage of the tenant llm key  Accessible to tenant admins only.  Returns:      200: No response data.      400: When data is not valid.  Example:          POST: /api/ai-mentor/orgs/main/use-main-llm-key/          Response:      {                         \"message\": \"Tenant is now using the main credentials\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
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
use_main_creds = iblai.UseMainCreds() # UseMainCreds | 

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

[**UseMainCreds**](UseMainCreds.md)

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
> UseMainCreds ai_account_orgs_use_free_trial_create(org, use_main_creds)



Endpoint to enable or disable free trial for a tenant.  Accessible to tenant admins only.  Returns:      200: No response data.      400: When data is not valid.  Example:          POST: /api/ai-mentor/orgs/main/use-main-llm-key/          Request: {                     \"enable\": true                     \"disable\": false                     \"metadata\": {                         \"key\": \"value\"                     }         }          Response:      {                         \"message\": \"Tenant is now using the main credentials\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
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
use_main_creds = iblai.UseMainCreds() # UseMainCreds | 

try:
    api_response = api_instance.ai_account_orgs_use_free_trial_create(org, use_main_creds)
    print("The response of AiAccountApi->ai_account_orgs_use_free_trial_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_use_free_trial_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **use_main_creds** | [**UseMainCreds**](UseMainCreds.md)|  | 

### Return type

[**UseMainCreds**](UseMainCreds.md)

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

# **ai_account_orgs_users_default_llm_key_usage_retrieve**
> MainCreds ai_account_orgs_users_default_llm_key_usage_retrieve(org, user_id)



Endpoint to enable or disable the usage of the tenant llm key  Accessible to tenant admins only.  Returns:      200: No response data.      400: When data is not valid.  Example:          POST: /api/ai-mentor/orgs/main/use-main-llm-key/          Response:    {                         \"use_main_credentials\": true                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.main_creds import MainCreds
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
    api_response = api_instance.ai_account_orgs_users_default_llm_key_usage_retrieve(org, user_id)
    print("The response of AiAccountApi->ai_account_orgs_users_default_llm_key_usage_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_users_default_llm_key_usage_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MainCreds**](MainCreds.md)

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

# **ai_account_orgs_users_free_trial_list**
> List[LLMCredentialResponse] ai_account_orgs_users_free_trial_list(org, user_id)



This is for getting list of free trial status for a tenant.  Accessible to tenant admins only.  Raises:      NotFound: When tenant key is not found.      NotFound: When the name passed in the paramter is not found.   Returns:      400: When the data is not valid.      200 : List of free trial credentials.  Example :      GET : /api/ai-account/orgs/main/free-trial/ .  Response:     {         is_in_free_trial: true     }

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
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_account_orgs_users_free_trial_list(org, user_id)
    print("The response of AiAccountApi->ai_account_orgs_users_free_trial_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAccountApi->ai_account_orgs_users_free_trial_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[LLMCredentialResponse]**](LLMCredentialResponse.md)

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

