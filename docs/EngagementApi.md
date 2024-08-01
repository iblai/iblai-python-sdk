# iblai.EngagementApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**engagement_orgs_activity_retrieve**](EngagementApi.md#engagement_orgs_activity_retrieve) | **GET** /api/engagement/orgs/{org}/activity | 
[**engagement_orgs_course_completion_over_time_retrieve**](EngagementApi.md#engagement_orgs_course_completion_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/course_completion/over-time | 
[**engagement_orgs_course_completion_per_course_retrieve**](EngagementApi.md#engagement_orgs_course_completion_per_course_retrieve) | **GET** /api/engagement/orgs/{org}/course_completion/per-course | 
[**engagement_orgs_courses_time_average_retrieve**](EngagementApi.md#engagement_orgs_courses_time_average_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/average | 
[**engagement_orgs_courses_time_detail_retrieve**](EngagementApi.md#engagement_orgs_courses_time_detail_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/detail | 
[**engagement_orgs_courses_time_over_time_retrieve**](EngagementApi.md#engagement_orgs_courses_time_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/over-time | 
[**engagement_orgs_courses_time_users_detail_retrieve**](EngagementApi.md#engagement_orgs_courses_time_users_detail_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/detail | 
[**engagement_orgs_courses_time_users_over_time_retrieve**](EngagementApi.md#engagement_orgs_courses_time_users_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/over-time | 
[**engagement_orgs_courses_time_users_retrieve**](EngagementApi.md#engagement_orgs_courses_time_users_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users | 
[**engagement_orgs_courses_videos_over_time_retrieve**](EngagementApi.md#engagement_orgs_courses_videos_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/over-time | 
[**engagement_orgs_courses_videos_retrieve**](EngagementApi.md#engagement_orgs_courses_videos_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/ | 
[**engagement_orgs_courses_videos_summary_retrieve**](EngagementApi.md#engagement_orgs_courses_videos_summary_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/summary | 
[**engagement_orgs_courses_videos_users_retrieve**](EngagementApi.md#engagement_orgs_courses_videos_users_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/users | 
[**engagement_orgs_time_average_perlearner_percourse_retrieve**](EngagementApi.md#engagement_orgs_time_average_perlearner_percourse_retrieve) | **GET** /api/engagement/orgs/{org}/time/average-perlearner-percourse | 
[**engagement_orgs_time_average_with_over_time_retrieve**](EngagementApi.md#engagement_orgs_time_average_with_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/time/average-with-over-time | 
[**engagement_orgs_time_over_time_retrieve**](EngagementApi.md#engagement_orgs_time_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/time/over-time | 
[**engagement_orgs_time_per_course_retrieve**](EngagementApi.md#engagement_orgs_time_per_course_retrieve) | **GET** /api/engagement/orgs/{org}/time/per-course | 
[**engagement_orgs_videos_over_time_retrieve**](EngagementApi.md#engagement_orgs_videos_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/videos/over-time | 
[**engagement_orgs_videos_retrieve**](EngagementApi.md#engagement_orgs_videos_retrieve) | **GET** /api/engagement/orgs/{org}/videos/ | 


# **engagement_orgs_activity_retrieve**
> EngagementPerCourse engagement_orgs_activity_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)



Engagement information on a per-course basis

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.engagement_per_course import EngagementPerCourse
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.engagement_orgs_activity_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of EngagementApi->engagement_orgs_activity_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_activity_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 

### Return type

[**EngagementPerCourse**](EngagementPerCourse.md)

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

# **engagement_orgs_course_completion_over_time_retrieve**
> OvertimeWithChangeInfo engagement_orgs_course_completion_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Completion count per user per course across the platform  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_course_completion_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_course_completion_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_course_completion_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OvertimeWithChangeInfo**](OvertimeWithChangeInfo.md)

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

# **engagement_orgs_course_completion_per_course_retrieve**
> CourseCompletionPerCourse engagement_orgs_course_completion_per_course_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)



Aggregated table of enrollments,and completed count on a per-course basis

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_completion_per_course import CourseCompletionPerCourse
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.engagement_orgs_course_completion_per_course_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of EngagementApi->engagement_orgs_course_completion_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_course_completion_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 

### Return type

[**CourseCompletionPerCourse**](CourseCompletionPerCourse.md)

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

# **engagement_orgs_courses_time_average_retrieve**
> AverageOvertime engagement_orgs_courses_time_average_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Average time spent in secs on a per-day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10 3. course_id <optional>  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.average_overtime import AverageOvertime
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_time_average_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_time_average_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_average_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**AverageOvertime**](AverageOvertime.md)

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

# **engagement_orgs_courses_time_detail_retrieve**
> TimeDetail engagement_orgs_courses_time_detail_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Time spent per course in secs in a tree like form  Kwargs course_id e.g course-v1:Org+Course4+Run  Query Params 1. start_date <optional> e.g 2020-10-01 2. end_date <optional> e.g 2020-10-10

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.time_detail import TimeDetail
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.engagement_orgs_courses_time_detail_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of EngagementApi->engagement_orgs_courses_time_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_detail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**TimeDetail**](TimeDetail.md)

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

# **engagement_orgs_courses_time_over_time_retrieve**
> Overtime engagement_orgs_courses_time_over_time_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent per course in secs on a per-day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10 Kwargs 3. course_id  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime import Overtime
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_time_over_time_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_time_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Overtime**](Overtime.md)

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

# **engagement_orgs_courses_time_users_detail_retrieve**
> PerLearnerTimeSpentInCourseTree engagement_orgs_courses_time_users_detail_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent within a course in ordered hierarchical format  Kwargs 1. course_id  e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email) Query Params 3. start_date <optional> e.g 2020-10-01 4. end_date <optional> e.g 2020-10-10

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.per_learner_time_spent_in_course_tree import PerLearnerTimeSpentInCourseTree
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_time_users_detail_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_time_users_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_users_detail_retrieve: %s\n" % e)
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

[**PerLearnerTimeSpentInCourseTree**](PerLearnerTimeSpentInCourseTree.md)

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

# **engagement_orgs_courses_time_users_over_time_retrieve**
> Overtime engagement_orgs_courses_time_users_over_time_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent in secs on a per-day basis  Query Params 1. course_id <optional> e.g course-v1:Org+Course4+Run 2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email) 3. start_date e.g 2020-10-01 4. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime import Overtime
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_time_users_over_time_retrieve(course_id, org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_time_users_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_users_over_time_retrieve: %s\n" % e)
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

[**Overtime**](Overtime.md)

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

# **engagement_orgs_courses_time_users_retrieve**
> TimeSpentByUsersInCourse engagement_orgs_courses_time_users_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



Time spent by users in a course  Query Params course_id  e.g course-v1:Org+Course4+Run

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.time_spent_by_users_in_course import TimeSpentByUsersInCourse
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_time_users_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_time_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_time_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**TimeSpentByUsersInCourse**](TimeSpentByUsersInCourse.md)

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

# **engagement_orgs_courses_videos_over_time_retrieve**
> Overtime engagement_orgs_courses_videos_over_time_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



 Watched Videos count on a per-day basis  Kwargs  1. course_id <optional> e.g course-v1:Org+Course4+Run  2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)   Query Params  3. start_date e.g 2020-10-01  4. end_date e.g 2020-10-10   Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime import Overtime
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_courses_videos_over_time_retrieve(course_id, org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_courses_videos_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_videos_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Overtime**](Overtime.md)

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

# **engagement_orgs_courses_videos_retrieve**
> VideosSpecificCourse engagement_orgs_courses_videos_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Engagement information (video) for a specific course

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.videos_specific_course import VideosSpecificCourse
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.engagement_orgs_courses_videos_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of EngagementApi->engagement_orgs_courses_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**VideosSpecificCourse**](VideosSpecificCourse.md)

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

# **engagement_orgs_courses_videos_summary_retrieve**
> VideosInCourseSummary engagement_orgs_courses_videos_summary_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Returns a Simplified tree structure of videos watched in course Kwargs course_id  e.g course-v1:Org+Course4+Run

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.videos_in_course_summary import VideosInCourseSummary
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.engagement_orgs_courses_videos_summary_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of EngagementApi->engagement_orgs_courses_videos_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_videos_summary_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**VideosInCourseSummary**](VideosInCourseSummary.md)

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

# **engagement_orgs_courses_videos_users_retrieve**
> WatchedVideosPerUser engagement_orgs_courses_videos_users_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



List of users' videos completed records for a specific course  Kwargs course_id  e.g course-v1:Org+Course4+Run

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.watched_videos_per_user import WatchedVideosPerUser
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
api_instance = iblai.EngagementApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.engagement_orgs_courses_videos_users_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of EngagementApi->engagement_orgs_courses_videos_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_courses_videos_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**WatchedVideosPerUser**](WatchedVideosPerUser.md)

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

# **engagement_orgs_time_average_perlearner_percourse_retrieve**
> AverageOvertime engagement_orgs_time_average_perlearner_percourse_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Average time spent by a learner in enrolled courses. Gives a rough estimate of whats the average time that would be spent by a learner in a course  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.average_overtime import AverageOvertime
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_time_average_perlearner_percourse_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_time_average_perlearner_percourse_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_time_average_perlearner_percourse_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**AverageOvertime**](AverageOvertime.md)

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

# **engagement_orgs_time_average_with_over_time_retrieve**
> AverageOvertime engagement_orgs_time_average_with_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Average time spent in secs on a per-day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10 3. course_id <optional>  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.average_overtime import AverageOvertime
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_time_average_with_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_time_average_with_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_time_average_with_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**AverageOvertime**](AverageOvertime.md)

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

# **engagement_orgs_time_over_time_retrieve**
> OvertimeWithChangeInfo engagement_orgs_time_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent in secs on a per-day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_time_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_time_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_time_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OvertimeWithChangeInfo**](OvertimeWithChangeInfo.md)

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

# **engagement_orgs_time_per_course_retrieve**
> TimeSpentPerCourse engagement_orgs_time_per_course_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



Aggregated time spent value on a per course basis

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.time_spent_per_course import TimeSpentPerCourse
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_time_per_course_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_time_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_time_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**TimeSpentPerCourse**](TimeSpentPerCourse.md)

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

# **engagement_orgs_videos_over_time_retrieve**
> Overtime engagement_orgs_videos_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



 Watched Videos count on a per-day basis  Kwargs  1. course_id <optional> e.g course-v1:Org+Course4+Run  2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)   Query Params  3. start_date e.g 2020-10-01  4. end_date e.g 2020-10-10   Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime import Overtime
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.engagement_orgs_videos_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of EngagementApi->engagement_orgs_videos_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_videos_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Overtime**](Overtime.md)

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

# **engagement_orgs_videos_retrieve**
> VideoEngagementPerCourse engagement_orgs_videos_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)



Video Engagement information on a per-course basis

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.video_engagement_per_course import VideoEngagementPerCourse
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
api_instance = iblai.EngagementApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.engagement_orgs_videos_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of EngagementApi->engagement_orgs_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling EngagementApi->engagement_orgs_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 

### Return type

[**VideoEngagementPerCourse**](VideoEngagementPerCourse.md)

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

