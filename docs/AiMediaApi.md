# iblai.AiMediaApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_media_orgs_users_heygen_templates_create**](AiMediaApi.md#ai_media_orgs_users_heygen_templates_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/ | 
[**ai_media_orgs_users_heygen_templates_destroy**](AiMediaApi.md#ai_media_orgs_users_heygen_templates_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/{template_name}/ | 
[**ai_media_orgs_users_heygen_templates_list**](AiMediaApi.md#ai_media_orgs_users_heygen_templates_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/ | 
[**ai_media_orgs_users_heygen_video_captions_create**](AiMediaApi.md#ai_media_orgs_users_heygen_video_captions_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-captions/{heygen_marketing_video_id}/ | 
[**ai_media_orgs_users_heygen_video_captions_retrieve**](AiMediaApi.md#ai_media_orgs_users_heygen_video_captions_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-captions/{heygen_marketing_video_id}/ | 
[**ai_media_orgs_users_heygen_video_download_retrieve**](AiMediaApi.md#ai_media_orgs_users_heygen_video_download_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-download/{heygen_marketing_video_id}/ | 
[**ai_media_orgs_users_heygen_videos_create**](AiMediaApi.md#ai_media_orgs_users_heygen_videos_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/ | 
[**ai_media_orgs_users_heygen_videos_destroy**](AiMediaApi.md#ai_media_orgs_users_heygen_videos_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/{heygen_marketing_video_id}/ | 
[**ai_media_orgs_users_heygen_videos_list**](AiMediaApi.md#ai_media_orgs_users_heygen_videos_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/ | 
[**ai_media_orgs_users_heygen_videos_retrieve**](AiMediaApi.md#ai_media_orgs_users_heygen_videos_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/{heygen_marketing_video_id}/ | 
[**ai_media_orgs_users_veo_video_download_retrieve**](AiMediaApi.md#ai_media_orgs_users_veo_video_download_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/video-download/{veo_video_id}/ | 
[**ai_media_orgs_users_veo_videos_create**](AiMediaApi.md#ai_media_orgs_users_veo_videos_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/ | 
[**ai_media_orgs_users_veo_videos_destroy**](AiMediaApi.md#ai_media_orgs_users_veo_videos_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/{veo_video_id}/ | 
[**ai_media_orgs_users_veo_videos_list**](AiMediaApi.md#ai_media_orgs_users_veo_videos_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/ | 
[**ai_media_orgs_users_veo_videos_retrieve**](AiMediaApi.md#ai_media_orgs_users_veo_videos_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/{veo_video_id}/ | 
[**ai_media_orgs_users_video_script_generation_audio_create**](AiMediaApi.md#ai_media_orgs_users_video_script_generation_audio_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/audio/ | 
[**ai_media_orgs_users_video_script_generation_document_create**](AiMediaApi.md#ai_media_orgs_users_video_script_generation_document_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/document/ | 
[**ai_media_orgs_users_video_script_generation_text_create**](AiMediaApi.md#ai_media_orgs_users_video_script_generation_text_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/text/ | 


# **ai_media_orgs_users_heygen_templates_create**
> HeygenTemplateResponseSingle ai_media_orgs_users_heygen_templates_create(org, user_id, heygen_template_request)

Endpoint to add a Heygen template id to an org.

Only platform admins have access to this endpoint.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_template_request import HeygenTemplateRequest
from iblai.models.heygen_template_response_single import HeygenTemplateResponseSingle
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
heygen_template_request = {"template_id":"new_id","name":"template name","preview_image_url":"https://example.com/preview.png"} # HeygenTemplateRequest | 

try:
    api_response = api_instance.ai_media_orgs_users_heygen_templates_create(org, user_id, heygen_template_request)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_templates_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_templates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **heygen_template_request** | [**HeygenTemplateRequest**](HeygenTemplateRequest.md)|  | 

### Return type

[**HeygenTemplateResponseSingle**](HeygenTemplateResponseSingle.md)

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

# **ai_media_orgs_users_heygen_templates_destroy**
> ai_media_orgs_users_heygen_templates_destroy(org, template_name, user_id)

Endpoint to delete a Heygen template id for an org.


The reponse status code is always 204 when no error.


Only platform admins have access to this endpoint.

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
template_name = 'template_name_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_heygen_templates_destroy(org, template_name, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_templates_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **template_name** | **str**|  | 
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

# **ai_media_orgs_users_heygen_templates_list**
> PaginatedHeygenTemplateResponseSingleList ai_media_orgs_users_heygen_templates_list(org, user_id, page=page)

API view to list or append Heygen template ids for a tenant.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_heygen_template_response_single_list import PaginatedHeygenTemplateResponseSingleList
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.ai_media_orgs_users_heygen_templates_list(org, user_id, page=page)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_templates_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_templates_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedHeygenTemplateResponseSingleList**](PaginatedHeygenTemplateResponseSingleList.md)

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

# **ai_media_orgs_users_heygen_video_captions_create**
> HeygenVideoDetail ai_media_orgs_users_heygen_video_captions_create(heygen_marketing_video_id, org, user_id, file)

Endpoint to upload a new caption for a generated video.

Only platform admins have access to this endpoint.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_video_detail import HeygenVideoDetail
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
api_instance = iblai.AiMediaApi(api_client)
heygen_marketing_video_id = 'heygen_marketing_video_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
file = 'file_example' # str | 

try:
    api_response = api_instance.ai_media_orgs_users_heygen_video_captions_create(heygen_marketing_video_id, org, user_id, file)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_video_captions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_video_captions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heygen_marketing_video_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**HeygenVideoDetail**](HeygenVideoDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_media_orgs_users_heygen_video_captions_retrieve**
> ai_media_orgs_users_heygen_video_captions_retrieve(heygen_marketing_video_id, org, user_id)

Endpoint to download caption for a video.

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
api_instance = iblai.AiMediaApi(api_client)
heygen_marketing_video_id = 'heygen_marketing_video_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_heygen_video_captions_retrieve(heygen_marketing_video_id, org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_video_captions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heygen_marketing_video_id** | **str**|  | 
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

# **ai_media_orgs_users_heygen_video_download_retrieve**
> ai_media_orgs_users_heygen_video_download_retrieve(heygen_marketing_video_id, org, user_id)

Endpoint used to download a heygen video.


Only platform admins have access to this endpoint.

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
api_instance = iblai.AiMediaApi(api_client)
heygen_marketing_video_id = 'heygen_marketing_video_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_heygen_video_download_retrieve(heygen_marketing_video_id, org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_video_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heygen_marketing_video_id** | **str**|  | 
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

# **ai_media_orgs_users_heygen_videos_create**
> HeygenVideoDetail ai_media_orgs_users_heygen_videos_create(org, user_id, heygen_video_request)

Endpoint to create a Heygen video

Only platform admins have access to this endpoint.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_video_detail import HeygenVideoDetail
from iblai.models.heygen_video_request import HeygenVideoRequest
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
heygen_video_request = {"name":"video name","data":{},"script":"Hello world. this is a script.","id":35,"video_file":"https://example.com/abcd.mp4","generation_status":"completed"} # HeygenVideoRequest | 

try:
    api_response = api_instance.ai_media_orgs_users_heygen_videos_create(org, user_id, heygen_video_request)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_videos_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_videos_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **heygen_video_request** | [**HeygenVideoRequest**](HeygenVideoRequest.md)|  | 

### Return type

[**HeygenVideoDetail**](HeygenVideoDetail.md)

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

# **ai_media_orgs_users_heygen_videos_destroy**
> ai_media_orgs_users_heygen_videos_destroy(heygen_marketing_video_id, org, user_id)

Endpoint used to delete a heygen video.

Only platform admins have access to this endpoint.

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
api_instance = iblai.AiMediaApi(api_client)
heygen_marketing_video_id = 'heygen_marketing_video_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_heygen_videos_destroy(heygen_marketing_video_id, org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_videos_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heygen_marketing_video_id** | **str**|  | 
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

# **ai_media_orgs_users_heygen_videos_list**
> PaginatedHeygenMarketingVideoListList ai_media_orgs_users_heygen_videos_list(org, user_id, page=page)

Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_heygen_marketing_video_list_list import PaginatedHeygenMarketingVideoListList
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.ai_media_orgs_users_heygen_videos_list(org, user_id, page=page)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_videos_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_videos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedHeygenMarketingVideoListList**](PaginatedHeygenMarketingVideoListList.md)

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

# **ai_media_orgs_users_heygen_videos_retrieve**
> HeygenVideoDetail ai_media_orgs_users_heygen_videos_retrieve(heygen_marketing_video_id, org, user_id)

Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_video_detail import HeygenVideoDetail
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
api_instance = iblai.AiMediaApi(api_client)
heygen_marketing_video_id = 'heygen_marketing_video_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_media_orgs_users_heygen_videos_retrieve(heygen_marketing_video_id, org, user_id)
    print("The response of AiMediaApi->ai_media_orgs_users_heygen_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_heygen_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heygen_marketing_video_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**HeygenVideoDetail**](HeygenVideoDetail.md)

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

# **ai_media_orgs_users_veo_video_download_retrieve**
> ai_media_orgs_users_veo_video_download_retrieve(org, user_id, veo_video_id)

Endpoint used to download a Veo video.


Only platform admins have access to this endpoint.

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
veo_video_id = 'veo_video_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_veo_video_download_retrieve(org, user_id, veo_video_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_veo_video_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **veo_video_id** | **str**|  | 

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

# **ai_media_orgs_users_veo_videos_create**
> VeoVideoDetail ai_media_orgs_users_veo_videos_create(org, user_id, prompt_text, prompt_image=prompt_image, name=name)

Endpoint to create a Veo3 video

Only platform admins have access to this endpoint.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.veo_video_detail import VeoVideoDetail
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
prompt_text = 'prompt_text_example' # str | 
prompt_image = 'prompt_image_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.ai_media_orgs_users_veo_videos_create(org, user_id, prompt_text, prompt_image=prompt_image, name=name)
    print("The response of AiMediaApi->ai_media_orgs_users_veo_videos_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_veo_videos_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **prompt_text** | **str**|  | 
 **prompt_image** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**VeoVideoDetail**](VeoVideoDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_media_orgs_users_veo_videos_destroy**
> ai_media_orgs_users_veo_videos_destroy(org, user_id, veo_video_id)

Endpoint used to delete a veo3 video.

Only platform admins have access to this endpoint.

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
veo_video_id = 'veo_video_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_veo_videos_destroy(org, user_id, veo_video_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_veo_videos_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **veo_video_id** | **str**|  | 

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

# **ai_media_orgs_users_veo_videos_list**
> PaginatedVeoVideoListList ai_media_orgs_users_veo_videos_list(org, user_id, page=page)

Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_veo_video_list_list import PaginatedVeoVideoListList
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.ai_media_orgs_users_veo_videos_list(org, user_id, page=page)
    print("The response of AiMediaApi->ai_media_orgs_users_veo_videos_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_veo_videos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedVeoVideoListList**](PaginatedVeoVideoListList.md)

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

# **ai_media_orgs_users_veo_videos_retrieve**
> VeoVideoDetail ai_media_orgs_users_veo_videos_retrieve(org, user_id, veo_video_id)

Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.veo_video_detail import VeoVideoDetail
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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
veo_video_id = 'veo_video_id_example' # str | 

try:
    api_response = api_instance.ai_media_orgs_users_veo_videos_retrieve(org, user_id, veo_video_id)
    print("The response of AiMediaApi->ai_media_orgs_users_veo_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_veo_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **veo_video_id** | **str**|  | 

### Return type

[**VeoVideoDetail**](VeoVideoDetail.md)

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

# **ai_media_orgs_users_video_script_generation_audio_create**
> ai_media_orgs_users_video_script_generation_audio_create(org, user_id)

Endpoint to generate video scripts from a audio file. The audio file can be one of mp3 and wav.

The request should be a multipart form with your audio file in the `file` field.

Initial Response:
```
{"script": None, "status": "started_generation", "generation_id": "your-generation-id."}
```
This signals the generation has started. You can use the generation id to query video script generation status from this endpoint, using a JSON like below:
```
{"generation_id": "your-generation-id"}
```

Example response:
```
{"script": "hello this is a video script.", "status": "finished", "generation_id": "your-generation-id"}

```

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_video_script_generation_audio_create(org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_video_script_generation_audio_create: %s\n" % e)
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

# **ai_media_orgs_users_video_script_generation_document_create**
> ai_media_orgs_users_video_script_generation_document_create(org, user_id)

    Endpoint to generate video scripts from a document file. The document file can be one of docx, doc, pptx, ppt, txt and pdf.

    The request should be a multipart form with your document file in the `file` field.
Initial Response:
    ```
    {"script": None, "status": "started_generation", "generation_id": "your-generation-id."}
    ```
    This signals the generation has started. You can use the generation id to query video script generation status from this endpoint, using a JSON like below:
    ```
    {"generation_id": "your-generation-id"}
    ```

    Example response:
    ```
    {"script": "hello this is a video script.", "status": "finished", "generation_id": "your-generation-id"}

    ```

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_video_script_generation_document_create(org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_video_script_generation_document_create: %s\n" % e)
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

# **ai_media_orgs_users_video_script_generation_text_create**
> ai_media_orgs_users_video_script_generation_text_create(org, user_id)

Endpoint to generate video scripts from a text.

The request body should be a JSON with your text, like below:
```
{"text": "Generate a script about a campus comedy."}
```

Example response:
```
{"script": "hello this is a video script."}

```

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
api_instance = iblai.AiMediaApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_media_orgs_users_video_script_generation_text_create(org, user_id)
except Exception as e:
    print("Exception when calling AiMediaApi->ai_media_orgs_users_video_script_generation_text_create: %s\n" % e)
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

