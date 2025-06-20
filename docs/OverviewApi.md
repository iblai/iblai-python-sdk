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
> OvertimeWithChangeInfo overview_orgs_active_users_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get active user counts over time.  This endpoint provides daily counts of active users (users with known activity) over a specified time period.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)  Returns:     Daily active user counts over the specified time period, with change metrics     compared to previous periods.  Default time range is the last 7 days if no dates are specified.  An active user is defined as a user with any activity within the past 30 days.

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_active_users_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_active_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_active_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> Average overview_orgs_average_grade_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)



Get average grade value for platform, course, or user.  This endpoint returns the average grade at different levels: - Platform level: Average grade across all courses - Course level: Average grade for a specific course - Learner level: Average grade for a specific learner - Course-learner level: Grade for a specific learner in a specific course  Query Parameters:     course_id (str, optional): Filter by course ID     learner_id (str, optional): Filter by username or email  Returns:     The average grade value based on the specified filters.  Access Control:     - Platform admins can access any grade data     - Learners can access their own grade data

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.overview_orgs_average_grade_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of OverviewApi->overview_orgs_average_grade_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_average_grade_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> CourseCompletionSummaryOvertime overview_orgs_courses_completions_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get course completion summary metrics over time.  This endpoint provides completion statistics across the platform over a specified time period, including daily completion counts and overall metrics.  Query Parameters:     start_date (str): Start date for the time range (ISO format)     end_date (str): End date for the time range (ISO format)  Returns:     Completion data including:     - Daily completion counts over time     - Total unique user count     - Total completion count     - Completion percentage     - Change metrics compared to previous periods  Default time range is the last 7 days if no dates are specified.

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_courses_completions_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_courses_completions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_courses_completions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> PerlearnerUserList overview_orgs_learners_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)



List all learners on the platform with aggregated metrics.  This endpoint returns a paginated list of all learners with key metrics including: - Enrollment counts - Completion counts - Time spent on platform  Query Parameters:     page (int): Page number for pagination     length (int): Number of items per page     search (str): Filter learners by username, email, or name  Returns:     A paginated list of learners with their associated metrics.

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
search = 'search_example' # str | Search string for learner (optional)

try:
    api_response = api_instance.overview_orgs_learners_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)
    print("The response of OverviewApi->overview_orgs_learners_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_learners_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> TimeSpentPerCourse overview_orgs_most_active_courses_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



Get time spent statistics on a per-course basis.  This endpoint provides a paginated list of courses with the total time spent by users in each course.  Query Parameters:     start_date (str, optional): Start date for filtering (ISO format)     end_date (str, optional): End date for filtering (ISO format)     page (int, optional): Page number for pagination     length (int, optional): Number of items per page  Returns:     A paginated list of courses with:     - Course identification (ID and name)     - Total time spent (in seconds)     - Formatted time spent (human-readable)     - Percentage of total platform time

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_most_active_courses_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_most_active_courses_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_most_active_courses_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> OvertimeWithChangeInfo overview_orgs_registered_users_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get registered user counts over time.  This endpoint provides daily counts of new user registrations over a specified time period.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)  Returns:     Daily registration counts over the specified time period, with change metrics     compared to previous periods.  Default time range is the last 7 days if no dates are specified.

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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.overview_orgs_registered_users_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of OverviewApi->overview_orgs_registered_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling OverviewApi->overview_orgs_registered_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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

