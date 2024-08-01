# iblai.OverviewApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**overview_orgs_active_users_retrieve**](OverviewApi.md#overview_orgs_active_users_retrieve) | **GET** /api/overview/orgs/{org}/active-users | 
[**overview_orgs_average_grade_retrieve**](OverviewApi.md#overview_orgs_average_grade_retrieve) | **GET** /api/overview/orgs/{org}/average-grade | 
[**overview_orgs_courses_completions_retrieve**](OverviewApi.md#overview_orgs_courses_completions_retrieve) | **GET** /api/overview/orgs/{org}/courses/completions | 
[**overview_orgs_learners_retrieve**](OverviewApi.md#overview_orgs_learners_retrieve) | **GET** /api/overview/orgs/{org}/learners | 
[**overview_orgs_most_active_courses_retrieve**](OverviewApi.md#overview_orgs_most_active_courses_retrieve) | **GET** /api/overview/orgs/{org}/most-active-courses | 
[**overview_orgs_registered_users_retrieve**](OverviewApi.md#overview_orgs_registered_users_retrieve) | **GET** /api/overview/orgs/{org}/registered-users | 


# **overview_orgs_active_users_retrieve**
> OvertimeWithChangeInfo overview_orgs_active_users_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Count of users with known activity within the past 30 days on a per day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive) Returns ``` {     \"data\": {         \"2022-04-26\": 0,         \"2022-04-27\": 0,         \"2022-04-28\": 0,         \"2022-04-29\": 60,         ...         \"2022-05-05\": 0     },     \"total\": 60,     \"meta\": {         \"change_last_seven_days\": 0,         \"change_last_seven_days_percent\": 0.0,         \"change_last_thirty_days\": 0,         \"change_last_thirty_days_percent\": 0.0,         \"change_range\": 0,         \"change_range_percent\": 0.0,         \"total\": 0,     } }

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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_active_users_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_active_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_active_users_retrieve: %s\n" % e)
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

# **overview_orgs_average_grade_retrieve**
> Average overview_orgs_average_grade_retrieve(org, format=format, include_main_platform=include_main_platform)



Average grade value for platform, course, or user.  Query Params course_id <optional>  e.g course-v1:Org+Course4+Run learner_id <optional> e.g std123 , student@email.com

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.average import Average
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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.overview_orgs_average_grade_retrieve(org, format=format, include_main_platform=include_main_platform)
    print("The response of OverviewApi->overview_orgs_average_grade_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_average_grade_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**Average**](Average.md)

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

# **overview_orgs_courses_completions_retrieve**
> CourseCompletionSummaryOvertime overview_orgs_courses_completions_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Course Completion Across the Platform Ovetime with unique User count Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_completion_summary_overtime import CourseCompletionSummaryOvertime
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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_courses_completions_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_courses_completions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_courses_completions_retrieve: %s\n" % e)
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

[**CourseCompletionSummaryOvertime**](CourseCompletionSummaryOvertime.md)

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

# **overview_orgs_learners_retrieve**
> PerlearnerUserList overview_orgs_learners_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)



List of entire learners on the platform with aggregated enrollments, completions and time spent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_user_list import PerlearnerUserList
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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
search = 'search_example' # str | Search string for learner (optional)

try:
    api_response = api_instance.overview_orgs_learners_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)
    print("The response of OverviewApi->overview_orgs_learners_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_learners_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **search** | **str**| Search string for learner | [optional] 

### Return type

[**PerlearnerUserList**](PerlearnerUserList.md)

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

# **overview_orgs_most_active_courses_retrieve**
> TimeSpentPerCourse overview_orgs_most_active_courses_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_most_active_courses_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_most_active_courses_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_most_active_courses_retrieve: %s\n" % e)
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

# **overview_orgs_registered_users_retrieve**
> OvertimeWithChangeInfo overview_orgs_registered_users_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Registered users count on a per day basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

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
api_instance = iblai.OverviewApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_registered_users_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_registered_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_registered_users_retrieve: %s\n" % e)
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

