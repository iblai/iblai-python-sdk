# iblai.PlatformApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_orgs_courses_users_grades_passed_retrieve**](PlatformApi.md#platform_orgs_courses_users_grades_passed_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/grades/passed | 
[**platform_orgs_courses_users_progress_days_to_complete_retrieve**](PlatformApi.md#platform_orgs_courses_users_progress_days_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress/days-to-complete | 
[**platform_orgs_courses_users_progress_retrieve**](PlatformApi.md#platform_orgs_courses_users_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress | 
[**platform_orgs_courses_users_time_count_retrieve**](PlatformApi.md#platform_orgs_courses_users_time_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/time/count | 
[**platform_orgs_courses_users_videos_count_retrieve**](PlatformApi.md#platform_orgs_courses_users_videos_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/videos/count | 


# **platform_orgs_courses_users_grades_passed_retrieve**
> platform_orgs_courses_users_grades_passed_retrieve(course_id, org, user_id)



A GET View that validates QueryParams and returns results to a serializer

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
api_instance = iblai.PlatformApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.platform_orgs_courses_users_grades_passed_retrieve(course_id, org, user_id)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_users_grades_passed_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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

# **platform_orgs_courses_users_progress_days_to_complete_retrieve**
> platform_orgs_courses_users_progress_days_to_complete_retrieve(course_id, org, user_id)



Average days used to complete a course  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run

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
api_instance = iblai.PlatformApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.platform_orgs_courses_users_progress_days_to_complete_retrieve(course_id, org, user_id)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_users_progress_days_to_complete_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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

# **platform_orgs_courses_users_progress_retrieve**
> PerlearnerCourseProgress platform_orgs_courses_users_progress_retrieve(course_id, org, user_id, format=format, include_main_platform=include_main_platform)



Gives Percentage of units completed in course for a specific learner

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_course_progress import PerlearnerCourseProgress
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
api_instance = iblai.PlatformApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_users_progress_retrieve(course_id, org, user_id, format=format, include_main_platform=include_main_platform)
    print("The response of PlatformApi->platform_orgs_courses_users_progress_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_users_progress_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**PerlearnerCourseProgress**](PerlearnerCourseProgress.md)

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

# **platform_orgs_courses_users_time_count_retrieve**
> Count platform_orgs_courses_users_time_count_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent count in seconds within a course by a learner

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.count import Count
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
api_instance = iblai.PlatformApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.platform_orgs_courses_users_time_count_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PlatformApi->platform_orgs_courses_users_time_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_users_time_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Count**](Count.md)

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

# **platform_orgs_courses_users_videos_count_retrieve**
> VideosCount platform_orgs_courses_users_videos_count_retrieve(course_id, org, user_id, format=format, include_main_platform=include_main_platform)



(Total videos watched / Total Course Videos) or Total Videos watched in a course by a learner

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.videos_count import VideosCount
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
api_instance = iblai.PlatformApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_users_videos_count_retrieve(course_id, org, user_id, format=format, include_main_platform=include_main_platform)
    print("The response of PlatformApi->platform_orgs_courses_users_videos_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_users_videos_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**VideosCount**](VideosCount.md)

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

