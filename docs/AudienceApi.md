# iblai.AudienceApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audience_orgs_active_users_over_time_retrieve**](AudienceApi.md#audience_orgs_active_users_over_time_retrieve) | **GET** /api/audience/orgs/{org}/active-users/over-time | 
[**audience_orgs_active_users_per_course_retrieve**](AudienceApi.md#audience_orgs_active_users_per_course_retrieve) | **GET** /api/audience/orgs/{org}/active-users/per-course | 
[**audience_orgs_active_users_users_retrieve**](AudienceApi.md#audience_orgs_active_users_users_retrieve) | **GET** /api/audience/orgs/{org}/active-users/users | 
[**audience_orgs_enrollments_courses_over_time_retrieve**](AudienceApi.md#audience_orgs_enrollments_courses_over_time_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/courses/{course_id}/over-time | 
[**audience_orgs_enrollments_courses_users_retrieve**](AudienceApi.md#audience_orgs_enrollments_courses_users_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/courses/{course_id}/users | 
[**audience_orgs_enrollments_over_time_retrieve**](AudienceApi.md#audience_orgs_enrollments_over_time_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/over-time | 
[**audience_orgs_enrollments_per_course_retrieve**](AudienceApi.md#audience_orgs_enrollments_per_course_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/per-course | 
[**audience_orgs_registered_users_over_time_retrieve**](AudienceApi.md#audience_orgs_registered_users_over_time_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/over-time | 
[**audience_orgs_registered_users_per_course_retrieve**](AudienceApi.md#audience_orgs_registered_users_per_course_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/per-course | 
[**audience_orgs_registered_users_retrieve**](AudienceApi.md#audience_orgs_registered_users_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/ | 


# **audience_orgs_active_users_over_time_retrieve**
> OvertimeWithChangeInfo audience_orgs_active_users_over_time_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_active_users_over_time_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_active_users_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_over_time_retrieve: %s\n" % e)
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

# **audience_orgs_active_users_per_course_retrieve**
> ActiveUsersPerCourse audience_orgs_active_users_per_course_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get active user counts on a per-course basis.  This endpoint provides counts of active users for each course within the specified date range.  Query Parameters:     start_date (str, optional): Start date for filtering (ISO format)     end_date (str, optional): End date for filtering (ISO format)  Returns:     A list of courses with their active user counts.  Default time range is the last 7 days if no dates are specified.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.active_users_per_course import ActiveUsersPerCourse
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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_active_users_per_course_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_active_users_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_per_course_retrieve: %s\n" % e)
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

[**ActiveUsersPerCourse**](ActiveUsersPerCourse.md)

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

# **audience_orgs_active_users_users_retrieve**
> ActiveUsersList audience_orgs_active_users_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page)



Get a list of active users with activity metrics.  This endpoint provides a paginated list of users who have had activity within the specified date range.  Query Parameters:     start_date (str, optional): Start date for filtering (ISO format)     end_date (str, optional): End date for filtering (ISO format)     course_id (str, optional): Filter by course ID     page (int, optional): Page number for pagination     length (int, optional): Number of items per page  Returns:     A paginated list of active users with their activity metrics.  Default time range is the last 7 days if no dates are specified.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.active_users_list import ActiveUsersList
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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.audience_orgs_active_users_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of AudienceApi->audience_orgs_active_users_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_users_retrieve: %s\n" % e)
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

### Return type

[**ActiveUsersList**](ActiveUsersList.md)

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

# **audience_orgs_enrollments_courses_over_time_retrieve**
> OvertimeWithChangeInfo audience_orgs_enrollments_courses_over_time_retrieve(course_id, org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get enrollment or unenrollment counts over time.  This endpoint provides daily counts of new enrollments or unenrollments over a specified time period.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)     course_id (str, optional): Filter by course ID     active (bool): Get enrollments when true, unenrollments when false  Returns:     Daily counts over the specified time period, with change metrics     compared to previous periods.  Default time range is the last 7 days if no dates are specified.

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
api_instance = iblai.AudienceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
active = y # str | Any of `y`, `yes`, `true`. set to false or no for unenrollments   * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to y)
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_courses_over_time_retrieve(course_id, org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_enrollments_courses_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_enrollments_courses_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **active** | **str**| Any of &#x60;y&#x60;, &#x60;yes&#x60;, &#x60;true&#x60;. set to false or no for unenrollments   * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to y]
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

# **audience_orgs_enrollments_courses_users_retrieve**
> EnrollmentsPerUser audience_orgs_enrollments_courses_users_retrieve(course_id, org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



List users enrolled in a specific course.  This endpoint provides a list of users who are enrolled or unenrolled in a specified course.  Query Parameters:     course_id (str): The course ID to get enrollments for     active (bool): Filter for active enrollments when true, inactive when false     page (int, optional): Page number for pagination     length (int, optional): Number of items per page  Returns:     A paginated list of users with:     - Username     - Full name     - Email     - Enrollment timestamp

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.enrollments_per_user import EnrollmentsPerUser
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
api_instance = iblai.AudienceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
active = y # str | Any of `y`, `yes`, `true`. set to false or no for unenrollments   * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to y)
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_courses_users_retrieve(course_id, org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_enrollments_courses_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_enrollments_courses_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **active** | **str**| Any of &#x60;y&#x60;, &#x60;yes&#x60;, &#x60;true&#x60;. set to false or no for unenrollments   * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to y]
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**EnrollmentsPerUser**](EnrollmentsPerUser.md)

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

# **audience_orgs_enrollments_over_time_retrieve**
> OvertimeWithChangeInfo audience_orgs_enrollments_over_time_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get enrollment or unenrollment counts over time.  This endpoint provides daily counts of new enrollments or unenrollments over a specified time period.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)     course_id (str, optional): Filter by course ID     active (bool): Get enrollments when true, unenrollments when false  Returns:     Daily counts over the specified time period, with change metrics     compared to previous periods.  Default time range is the last 7 days if no dates are specified.

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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
active = y # str | Any of `y`, `yes`, `true`. set to false or no for unenrollments   * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to y)
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_over_time_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_enrollments_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_enrollments_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **active** | **str**| Any of &#x60;y&#x60;, &#x60;yes&#x60;, &#x60;true&#x60;. set to false or no for unenrollments   * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to y]
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

# **audience_orgs_enrollments_per_course_retrieve**
> Enrollments audience_orgs_enrollments_per_course_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



List enrollment statistics on a per-course basis.  This endpoint provides enrollment counts for all courses, with options to filter for active or inactive enrollments and to include time-based data.  Query Parameters:     active (bool): Filter for active enrollments when true, inactive when false     start_date (str, optional): Start date for time-based filtering (ISO format)     end_date (str, optional): End date for time-based filtering (ISO format)     page (int, optional): Page number for pagination     length (int, optional): Number of items per page  Returns:     A paginated list of courses with their enrollment counts and percentages.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.enrollments import Enrollments
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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
active = y # str | Any of `y`, `yes`, `true`. set to false or no for unenrollments   * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to y)
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_per_course_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_enrollments_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_enrollments_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **active** | **str**| Any of &#x60;y&#x60;, &#x60;yes&#x60;, &#x60;true&#x60;. set to false or no for unenrollments   * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to y]
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Enrollments**](Enrollments.md)

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

# **audience_orgs_registered_users_over_time_retrieve**
> OvertimeWithChangeInfo audience_orgs_registered_users_over_time_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_over_time_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_registered_users_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_registered_users_over_time_retrieve: %s\n" % e)
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

# **audience_orgs_registered_users_per_course_retrieve**
> Enrollments audience_orgs_registered_users_per_course_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



List enrollment statistics on a per-course basis.  This endpoint provides enrollment counts for all courses, with options to filter for active or inactive enrollments and to include time-based data.  Query Parameters:     active (bool): Filter for active enrollments when true, inactive when false     start_date (str, optional): Start date for time-based filtering (ISO format)     end_date (str, optional): End date for time-based filtering (ISO format)     page (int, optional): Page number for pagination     length (int, optional): Number of items per page  Returns:     A paginated list of courses with their enrollment counts and percentages.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.enrollments import Enrollments
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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
active = y # str | Any of `y`, `yes`, `true`. set to false or no for unenrollments   * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to y)
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_per_course_retrieve(org, active=active, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_registered_users_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_registered_users_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **active** | **str**| Any of &#x60;y&#x60;, &#x60;yes&#x60;, &#x60;true&#x60;. set to false or no for unenrollments   * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to y]
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **length** | **int**| Size of data to return | [optional] 
 **page** | **int**| Page offset | [optional] 
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Enrollments**](Enrollments.md)

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

# **audience_orgs_registered_users_retrieve**
> PerlearnerUserList audience_orgs_registered_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
search = 'search_example' # str | Search string for learner (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)
    print("The response of AudienceApi->audience_orgs_registered_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_registered_users_retrieve: %s\n" % e)
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

