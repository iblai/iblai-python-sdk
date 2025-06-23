# iblai.AiMarketingApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_marketing_orgs_users_heygen_videos_create**](AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_create) | **POST** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/ | 
[**ai_marketing_orgs_users_heygen_videos_list**](AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_list) | **GET** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/ | 
[**ai_marketing_orgs_users_heygen_videos_retrieve**](AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_retrieve) | **GET** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/{name}/ | 


# **ai_marketing_orgs_users_heygen_videos_create**
> HeygenMarketingVideoList ai_marketing_orgs_users_heygen_videos_create(org, user_id, heygen_marketing_video_list=heygen_marketing_video_list)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_marketing_video_list import HeygenMarketingVideoList
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
api_instance = iblai.AiMarketingApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
heygen_marketing_video_list = iblai.HeygenMarketingVideoList() # HeygenMarketingVideoList |  (optional)

try:
    api_response = api_instance.ai_marketing_orgs_users_heygen_videos_create(org, user_id, heygen_marketing_video_list=heygen_marketing_video_list)
    print("The response of AiMarketingApi->ai_marketing_orgs_users_heygen_videos_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMarketingApi->ai_marketing_orgs_users_heygen_videos_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **heygen_marketing_video_list** | [**HeygenMarketingVideoList**](HeygenMarketingVideoList.md)|  | [optional] 

### Return type

[**HeygenMarketingVideoList**](HeygenMarketingVideoList.md)

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

# **ai_marketing_orgs_users_heygen_videos_list**
> PaginatedHeygenMarketingVideoListList ai_marketing_orgs_users_heygen_videos_list(org, user_id, page=page, page_size=page_size)



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
api_instance = iblai.AiMarketingApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.ai_marketing_orgs_users_heygen_videos_list(org, user_id, page=page, page_size=page_size)
    print("The response of AiMarketingApi->ai_marketing_orgs_users_heygen_videos_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMarketingApi->ai_marketing_orgs_users_heygen_videos_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

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

# **ai_marketing_orgs_users_heygen_videos_retrieve**
> HeygenMarketingVideoDetail ai_marketing_orgs_users_heygen_videos_retrieve(name, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.heygen_marketing_video_detail import HeygenMarketingVideoDetail
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
api_instance = iblai.AiMarketingApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_marketing_orgs_users_heygen_videos_retrieve(name, org, user_id)
    print("The response of AiMarketingApi->ai_marketing_orgs_users_heygen_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMarketingApi->ai_marketing_orgs_users_heygen_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**HeygenMarketingVideoDetail**](HeygenMarketingVideoDetail.md)

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

