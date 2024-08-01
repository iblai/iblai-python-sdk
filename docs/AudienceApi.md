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
> OvertimeWithChangeInfo audience_orgs_active_users_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_active_users_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_active_users_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_over_time_retrieve: %s\n" % e)
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

# **audience_orgs_active_users_per_course_retrieve**
> ActiveUsersPerCourse audience_orgs_active_users_per_course_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Count of users with known activity within specified date_range on a per-course basis  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_active_users_per_course_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_active_users_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_per_course_retrieve: %s\n" % e)
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
> ActiveUsersList audience_orgs_active_users_users_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)



List of users with known activity within the specified date range  default is all time  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10 3. course_id <optional> e.g course-v1:Org+Course4+Run  Default result when no query param is added is last_7_days (today inclusive)

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
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.audience_orgs_active_users_users_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of AudienceApi->audience_orgs_active_users_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_active_users_users_retrieve: %s\n" % e)
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
> OvertimeWithChangeInfo audience_orgs_enrollments_courses_over_time_retrieve(course_id, org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Aggregated count of  new enrollments/ unenrollments on a per day basis   Params 1. course_id <optional> e.g course-v1:Org+Course4+Run 2. start_date e.g 2020-10-01 3. end_date e.g 2020-10-10 4. active e.g true/false would mean not active enrollments  Default result when no query param is added is last_7_days (today inclusive)

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_courses_over_time_retrieve(course_id, org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
> EnrollmentsPerUser audience_orgs_enrollments_courses_users_retrieve(course_id, org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



List of users who are enrolled/not enrolled in specified course  Query Params 1. course_id 2. active e.g true/false would mean not active enrollments

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_courses_users_retrieve(course_id, org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
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
> OvertimeWithChangeInfo audience_orgs_enrollments_over_time_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Aggregated count of  new enrollments/ unenrollments on a per day basis   Params 1. course_id <optional> e.g course-v1:Org+Course4+Run 2. start_date e.g 2020-10-01 3. end_date e.g 2020-10-10 4. active e.g true/false would mean not active enrollments  Default result when no query param is added is last_7_days (today inclusive)

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_over_time_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
> Enrollments audience_orgs_enrollments_per_course_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



Aggregated count of active/inactive enrollments on a per course basis Query Params     active e.g true/false would mean not active enrollments

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_enrollments_per_course_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
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
> OvertimeWithChangeInfo audience_orgs_registered_users_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_over_time_retrieve(org, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of AudienceApi->audience_orgs_registered_users_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_registered_users_over_time_retrieve: %s\n" % e)
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

# **audience_orgs_registered_users_per_course_retrieve**
> Enrollments audience_orgs_registered_users_per_course_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)



Aggregated count of active/inactive enrollments on a per course basis Query Params     active e.g true/false would mean not active enrollments

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
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_per_course_retrieve(org, active=active, end_date=end_date, format=format, include_main_platform=include_main_platform, length=length, page=page, start_date=start_date)
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
> PerlearnerUserList audience_orgs_registered_users_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)



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
api_instance = iblai.AudienceApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
search = 'search_example' # str | Search string for learner (optional)

try:
    api_response = api_instance.audience_orgs_registered_users_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)
    print("The response of AudienceApi->audience_orgs_registered_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AudienceApi->audience_orgs_registered_users_retrieve: %s\n" % e)
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

