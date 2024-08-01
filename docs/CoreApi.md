# iblai.CoreApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_orgs_dark_mode_logo_create_create**](CoreApi.md#core_orgs_dark_mode_logo_create_create) | **POST** /api/core/orgs/{org}/dark-mode-logo/create/ | 
[**core_orgs_dark_mode_logo_retrieve**](CoreApi.md#core_orgs_dark_mode_logo_retrieve) | **GET** /api/core/orgs/{org}/dark-mode-logo/ | 
[**core_orgs_favicon_create_create**](CoreApi.md#core_orgs_favicon_create_create) | **POST** /api/core/orgs/{org}/favicon/create/ | 
[**core_orgs_favicon_retrieve**](CoreApi.md#core_orgs_favicon_retrieve) | **GET** /api/core/orgs/{org}/favicon/ | 
[**core_orgs_logo_create_create**](CoreApi.md#core_orgs_logo_create_create) | **POST** /api/core/orgs/{org}/logo/create/ | 
[**core_orgs_logo_retrieve**](CoreApi.md#core_orgs_logo_retrieve) | **GET** /api/core/orgs/{org}/logo/ | 
[**core_orgs_metadata_partial_update**](CoreApi.md#core_orgs_metadata_partial_update) | **PATCH** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_retrieve**](CoreApi.md#core_orgs_metadata_retrieve) | **GET** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_metadata_update**](CoreApi.md#core_orgs_metadata_update) | **PUT** /api/core/orgs/{org}/metadata/ | 
[**core_orgs_thumbnail_create_create**](CoreApi.md#core_orgs_thumbnail_create_create) | **POST** /api/core/orgs/{org}/thumbnail/create/ | 
[**core_orgs_thumbnail_retrieve**](CoreApi.md#core_orgs_thumbnail_retrieve) | **GET** /api/core/orgs/{org}/thumbnail/ | 


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

