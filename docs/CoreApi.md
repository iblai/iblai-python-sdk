# iblai.CoreApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_lti1p3_provider_lti_keys_create**](CoreApi.md#core_lti1p3_provider_lti_keys_create) | **POST** /api/core/lti/1p3/provider/lti-keys/ | 
[**core_lti1p3_provider_lti_keys_destroy**](CoreApi.md#core_lti1p3_provider_lti_keys_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_keys_list**](CoreApi.md#core_lti1p3_provider_lti_keys_list) | **GET** /api/core/lti/1p3/provider/lti-keys/ | 
[**core_lti1p3_provider_lti_keys_retrieve**](CoreApi.md#core_lti1p3_provider_lti_keys_retrieve) | **GET** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_keys_update**](CoreApi.md#core_lti1p3_provider_lti_keys_update) | **PUT** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
[**core_lti1p3_provider_lti_tools_create**](CoreApi.md#core_lti1p3_provider_lti_tools_create) | **POST** /api/core/lti/1p3/provider/lti-tools/ | 
[**core_lti1p3_provider_lti_tools_destroy**](CoreApi.md#core_lti1p3_provider_lti_tools_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_lti1p3_provider_lti_tools_list**](CoreApi.md#core_lti1p3_provider_lti_tools_list) | **GET** /api/core/lti/1p3/provider/lti-tools/ | 
[**core_lti1p3_provider_lti_tools_retrieve**](CoreApi.md#core_lti1p3_provider_lti_tools_retrieve) | **GET** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_lti1p3_provider_lti_tools_update**](CoreApi.md#core_lti1p3_provider_lti_tools_update) | **PUT** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
[**core_orgs_dark_mode_logo_create_create**](CoreApi.md#core_orgs_dark_mode_logo_create_create) | **POST** /api/core/orgs/{org}/dark-mode-logo/create/ | 
[**core_orgs_dark_mode_logo_retrieve**](CoreApi.md#core_orgs_dark_mode_logo_retrieve) | **GET** /api/core/orgs/{org}/dark-mode-logo/ | 
[**core_orgs_favicon_create_create**](CoreApi.md#core_orgs_favicon_create_create) | **POST** /api/core/orgs/{org}/favicon/create/ | 
[**core_orgs_favicon_retrieve**](CoreApi.md#core_orgs_favicon_retrieve) | **GET** /api/core/orgs/{org}/favicon/ | 
[**core_orgs_logo_create_create**](CoreApi.md#core_orgs_logo_create_create) | **POST** /api/core/orgs/{org}/logo/create/ | 
[**core_orgs_logo_retrieve**](CoreApi.md#core_orgs_logo_retrieve) | **GET** /api/core/orgs/{org}/logo/ | 
[**core_orgs_metadata_partial_update**](CoreApi.md#core_orgs_metadata_partial_update) | **PATCH** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_retrieve**](CoreApi.md#core_orgs_metadata_retrieve) | **GET** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_update**](CoreApi.md#core_orgs_metadata_update) | **PUT** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_redirect_tokens_create**](CoreApi.md#core_orgs_redirect_tokens_create) | **POST** /api/core/orgs/{org}/redirect-tokens/ | 
[**core_orgs_redirect_tokens_delete_destroy**](CoreApi.md#core_orgs_redirect_tokens_delete_destroy) | **DELETE** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/delete | 
[**core_orgs_redirect_tokens_retrieve**](CoreApi.md#core_orgs_redirect_tokens_retrieve) | **GET** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/ | 
[**core_orgs_thumbnail_create_create**](CoreApi.md#core_orgs_thumbnail_create_create) | **POST** /api/core/orgs/{org}/thumbnail/create/ | 
[**core_orgs_thumbnail_retrieve**](CoreApi.md#core_orgs_thumbnail_retrieve) | **GET** /api/core/orgs/{org}/thumbnail/ | 


# **core_lti1p3_provider_lti_keys_create**
> LtiKey core_lti1p3_provider_lti_keys_create(lti_key)



Create a new LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
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
api_instance = iblai.CoreApi(api_client)
lti_key = iblai.LtiKey() # LtiKey | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_create(lti_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lti_key** | [**LtiKey**](LtiKey.md)|  | 

### Return type

[**LtiKey**](LtiKey.md)

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

# **core_lti1p3_provider_lti_keys_destroy**
> core_lti1p3_provider_lti_keys_destroy(id, platform_key)



Delete an LTI Provider Key  **DANGER:** Deleting a key will also delete all Tools that reference that Key. If you need to delete a Key you should first create a new one and update all Tools to reference the new Key before deleting the old one.

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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_instance.core_lti1p3_provider_lti_keys_destroy(id, platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

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

# **core_lti1p3_provider_lti_keys_list**
> List[LtiKey] core_lti1p3_provider_lti_keys_list(platform_key)



List your LTI Provider Key's

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
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
api_instance = iblai.CoreApi(api_client)
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_list(platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform Key | 

### Return type

[**List[LtiKey]**](LtiKey.md)

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

# **core_lti1p3_provider_lti_keys_retrieve**
> LtiKey core_lti1p3_provider_lti_keys_retrieve(id, platform_key)



Get details about a specific LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_retrieve(id, platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

[**LtiKey**](LtiKey.md)

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

# **core_lti1p3_provider_lti_keys_update**
> LtiKey core_lti1p3_provider_lti_keys_update(id, lti_key)



Update an LTI Provider Key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_key import LtiKey
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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
lti_key = iblai.LtiKey() # LtiKey | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_keys_update(id, lti_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_keys_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_keys_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **lti_key** | [**LtiKey**](LtiKey.md)|  | 

### Return type

[**LtiKey**](LtiKey.md)

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

# **core_lti1p3_provider_lti_tools_create**
> LtiTool core_lti1p3_provider_lti_tools_create(lti_tool)



Create a new LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
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
api_instance = iblai.CoreApi(api_client)
lti_tool = iblai.LtiTool() # LtiTool | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_create(lti_tool)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lti_tool** | [**LtiTool**](LtiTool.md)|  | 

### Return type

[**LtiTool**](LtiTool.md)

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

# **core_lti1p3_provider_lti_tools_destroy**
> core_lti1p3_provider_lti_tools_destroy(id, platform_key)



Delete an LTI Tool

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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_instance.core_lti1p3_provider_lti_tools_destroy(id, platform_key)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

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

# **core_lti1p3_provider_lti_tools_list**
> List[LtiTool] core_lti1p3_provider_lti_tools_list(platform_key)



List your LTI Tool's

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
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
api_instance = iblai.CoreApi(api_client)
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_list(platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform Key | 

### Return type

[**List[LtiTool]**](LtiTool.md)

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

# **core_lti1p3_provider_lti_tools_retrieve**
> LtiTool core_lti1p3_provider_lti_tools_retrieve(id, platform_key)



Get details about a specific LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | Platform Key

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_retrieve(id, platform_key)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**| Platform Key | 

### Return type

[**LtiTool**](LtiTool.md)

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

# **core_lti1p3_provider_lti_tools_update**
> LtiTool core_lti1p3_provider_lti_tools_update(id, lti_tool)



Update an LTI Tool

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.lti_tool import LtiTool
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
api_instance = iblai.CoreApi(api_client)
id = 'id_example' # str | 
lti_tool = iblai.LtiTool() # LtiTool | 

try:
    api_response = api_instance.core_lti1p3_provider_lti_tools_update(id, lti_tool)
    print("The response of CoreApi->core_lti1p3_provider_lti_tools_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_lti1p3_provider_lti_tools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **lti_tool** | [**LtiTool**](LtiTool.md)|  | 

### Return type

[**LtiTool**](LtiTool.md)

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

# **core_orgs_dark_mode_logo_create_create**
> ImageUpload core_orgs_dark_mode_logo_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_dark_mode_logo_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_dark_mode_logo_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_dark_mode_logo_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

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

# **core_orgs_dark_mode_logo_retrieve**
> Dict[str, object] core_orgs_dark_mode_logo_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_dark_mode_logo_retrieve(org)
    print("The response of CoreApi->core_orgs_dark_mode_logo_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_dark_mode_logo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **core_orgs_favicon_create_create**
> ImageUpload core_orgs_favicon_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_favicon_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_favicon_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_favicon_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

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

# **core_orgs_favicon_retrieve**
> Dict[str, object] core_orgs_favicon_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_favicon_retrieve(org)
    print("The response of CoreApi->core_orgs_favicon_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_favicon_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **core_orgs_logo_create_create**
> ImageUpload core_orgs_logo_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_logo_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_logo_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_logo_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

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

# **core_orgs_logo_retrieve**
> Dict[str, object] core_orgs_logo_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_logo_retrieve(org)
    print("The response of CoreApi->core_orgs_logo_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_logo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **core_orgs_metadata_partial_update**
> PlatformPublicMetadata core_orgs_metadata_partial_update(org, patched_platform_public_metadata=patched_platform_public_metadata)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_platform_public_metadata import PatchedPlatformPublicMetadata
from iblai.models.platform_public_metadata import PlatformPublicMetadata
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
patched_platform_public_metadata = iblai.PatchedPlatformPublicMetadata() # PatchedPlatformPublicMetadata |  (optional)

try:
    api_response = api_instance.core_orgs_metadata_partial_update(org, patched_platform_public_metadata=patched_platform_public_metadata)
    print("The response of CoreApi->core_orgs_metadata_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_platform_public_metadata** | [**PatchedPlatformPublicMetadata**](PatchedPlatformPublicMetadata.md)|  | [optional] 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

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

# **core_orgs_metadata_retrieve**
> PlatformPublicMetadata core_orgs_metadata_retrieve(org)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_public_metadata import PlatformPublicMetadata
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_metadata_retrieve(org)
    print("The response of CoreApi->core_orgs_metadata_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

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

# **core_orgs_metadata_update**
> PlatformPublicMetadata core_orgs_metadata_update(org, platform_public_metadata=platform_public_metadata)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_public_metadata import PlatformPublicMetadata
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
platform_public_metadata = iblai.PlatformPublicMetadata() # PlatformPublicMetadata |  (optional)

try:
    api_response = api_instance.core_orgs_metadata_update(org, platform_public_metadata=platform_public_metadata)
    print("The response of CoreApi->core_orgs_metadata_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_metadata_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **platform_public_metadata** | [**PlatformPublicMetadata**](PlatformPublicMetadata.md)|  | [optional] 

### Return type

[**PlatformPublicMetadata**](PlatformPublicMetadata.md)

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

# **core_orgs_redirect_tokens_create**
> RedirectTokenResponse core_orgs_redirect_tokens_create(org, redirect_token_request)



Creates redirect tokens for a URL specified by for a platform

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.redirect_token_request import RedirectTokenRequest
from iblai.models.redirect_token_response import RedirectTokenResponse
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token_request = iblai.RedirectTokenRequest() # RedirectTokenRequest | 

try:
    api_response = api_instance.core_orgs_redirect_tokens_create(org, redirect_token_request)
    print("The response of CoreApi->core_orgs_redirect_tokens_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token_request** | [**RedirectTokenRequest**](RedirectTokenRequest.md)|  | 

### Return type

[**RedirectTokenResponse**](RedirectTokenResponse.md)

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

# **core_orgs_redirect_tokens_delete_destroy**
> core_orgs_redirect_tokens_delete_destroy(org, redirect_token)



Delete specific token

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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token = 'redirect_token_example' # str | 

try:
    api_instance.core_orgs_redirect_tokens_delete_destroy(org, redirect_token)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_delete_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token** | **str**|  | 

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

# **core_orgs_redirect_tokens_retrieve**
> RedirectTokenResponse core_orgs_redirect_tokens_retrieve(org, redirect_token)



Returns Redirect URL for the token specified.  ``` Requires user to be a member of the platform with the token passed ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.redirect_token_response import RedirectTokenResponse
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
redirect_token = 'redirect_token_example' # str | 

try:
    api_response = api_instance.core_orgs_redirect_tokens_retrieve(org, redirect_token)
    print("The response of CoreApi->core_orgs_redirect_tokens_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_redirect_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **redirect_token** | **str**|  | 

### Return type

[**RedirectTokenResponse**](RedirectTokenResponse.md)

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

# **core_orgs_thumbnail_create_create**
> ImageUpload core_orgs_thumbnail_create_create(org, image_upload)



Upload a new platform logo

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.image_upload import ImageUpload
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
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 
image_upload = iblai.ImageUpload() # ImageUpload | 

try:
    api_response = api_instance.core_orgs_thumbnail_create_create(org, image_upload)
    print("The response of CoreApi->core_orgs_thumbnail_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_thumbnail_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **image_upload** | [**ImageUpload**](ImageUpload.md)|  | 

### Return type

[**ImageUpload**](ImageUpload.md)

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

# **core_orgs_thumbnail_retrieve**
> Dict[str, object] core_orgs_thumbnail_retrieve(org)



Get platform logo

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CoreApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.core_orgs_thumbnail_retrieve(org)
    print("The response of CoreApi->core_orgs_thumbnail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CoreApi->core_orgs_thumbnail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

**Dict[str, object]**

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

