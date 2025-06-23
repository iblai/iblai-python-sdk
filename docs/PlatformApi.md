# iblai.PlatformApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platform_orgs_courses_count_retrieve**](PlatformApi.md#platform_orgs_courses_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/count | 
[**platform_orgs_courses_grades_retrieve**](PlatformApi.md#platform_orgs_courses_grades_retrieve) | **GET** /api/platform/orgs/{org}/courses/grades | 
[**platform_orgs_courses_progress_average_days_to_complete_retrieve**](PlatformApi.md#platform_orgs_courses_progress_average_days_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/average-days-to-complete | 
[**platform_orgs_courses_progress_average_time_to_complete_retrieve**](PlatformApi.md#platform_orgs_courses_progress_average_time_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/average-time-to-complete | 
[**platform_orgs_courses_progress_completed_retrieve**](PlatformApi.md#platform_orgs_courses_progress_completed_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/completed | 
[**platform_orgs_courses_progress_completion_rate_retrieve**](PlatformApi.md#platform_orgs_courses_progress_completion_rate_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/completion-rate | 
[**platform_orgs_courses_progress_in_progress_retrieve**](PlatformApi.md#platform_orgs_courses_progress_in_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/in-progress | 
[**platform_orgs_courses_progress_retrieve**](PlatformApi.md#platform_orgs_courses_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/ | 
[**platform_orgs_courses_progress_started_retrieve**](PlatformApi.md#platform_orgs_courses_progress_started_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/started | 
[**platform_orgs_courses_users_grades_passed_retrieve**](PlatformApi.md#platform_orgs_courses_users_grades_passed_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/grades/passed | 
[**platform_orgs_courses_users_progress_days_to_complete_retrieve**](PlatformApi.md#platform_orgs_courses_users_progress_days_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress/days-to-complete | 
[**platform_orgs_courses_users_progress_retrieve**](PlatformApi.md#platform_orgs_courses_users_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress | 
[**platform_orgs_courses_users_time_count_retrieve**](PlatformApi.md#platform_orgs_courses_users_time_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/time/count | 
[**platform_orgs_courses_users_videos_count_retrieve**](PlatformApi.md#platform_orgs_courses_users_videos_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/videos/count | 
[**platform_orgs_courses_videos_retrieve**](PlatformApi.md#platform_orgs_courses_videos_retrieve) | **GET** /api/platform/orgs/{org}/courses/videos | 
[**platform_orgs_courses_videos_retrieve2**](PlatformApi.md#platform_orgs_courses_videos_retrieve2) | **GET** /api/platform/orgs/{org}/courses/{course_id}/videos/ | 
[**platform_orgs_progress_completed_retrieve**](PlatformApi.md#platform_orgs_progress_completed_retrieve) | **GET** /api/platform/orgs/{org}/progress/completed | 
[**platform_orgs_progress_completion_rate_retrieve**](PlatformApi.md#platform_orgs_progress_completion_rate_retrieve) | **GET** /api/platform/orgs/{org}/progress/completion-rate | 
[**platform_orgs_progress_in_progress_retrieve**](PlatformApi.md#platform_orgs_progress_in_progress_retrieve) | **GET** /api/platform/orgs/{org}/progress/in-progress | 
[**platform_orgs_progress_started_retrieve**](PlatformApi.md#platform_orgs_progress_started_retrieve) | **GET** /api/platform/orgs/{org}/progress/started | 
[**platform_orgs_retrieve**](PlatformApi.md#platform_orgs_retrieve) | **GET** /api/platform/orgs/{org}/ | 
[**platform_orgs_time_count_retrieve**](PlatformApi.md#platform_orgs_time_count_retrieve) | **GET** /api/platform/orgs/{org}/time/count | 
[**platform_orgs_users_active_count_retrieve**](PlatformApi.md#platform_orgs_users_active_count_retrieve) | **GET** /api/platform/orgs/{org}/users/active/count | 
[**platform_orgs_users_count_retrieve**](PlatformApi.md#platform_orgs_users_count_retrieve) | **GET** /api/platform/orgs/{org}/users/count | 
[**platform_orgs_users_courses_completed_count_retrieve**](PlatformApi.md#platform_orgs_users_courses_completed_count_retrieve) | **GET** /api/platform/orgs/{org}/users/courses-completed/count | 


# **platform_orgs_courses_count_retrieve**
> Count platform_orgs_courses_count_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)



Get total count of courses on the platform.  This endpoint returns the total number of courses available on the platform.  Returns:     The total count of courses on the platform.

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
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_count_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PlatformApi->platform_orgs_courses_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

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

# **platform_orgs_courses_grades_retrieve**
> platform_orgs_courses_grades_retrieve(org)



List grading information on a per-course basis.  This endpoint provides grading statistics for all courses, including average grades and completion rates.  Returns:     A list of courses with their associated grading metrics.

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_courses_grades_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_grades_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_average_days_to_complete_retrieve**
> platform_orgs_courses_progress_average_days_to_complete_retrieve(course_id, org)



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

try:
    api_instance.platform_orgs_courses_progress_average_days_to_complete_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_average_days_to_complete_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_average_time_to_complete_retrieve**
> platform_orgs_courses_progress_average_time_to_complete_retrieve(course_id, org)



Average time used to complete a course in secs  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run

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

try:
    api_instance.platform_orgs_courses_progress_average_time_to_complete_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_average_time_to_complete_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_completed_retrieve**
> platform_orgs_courses_progress_completed_retrieve(course_id, org)



Get completion count statistics.  This endpoint returns completion counts at different levels: - Platform level: Total users who have completed at least one course - Course level: Total completions for a specific course - Learner level: Total courses completed by a specific learner  Query Parameters:     course_id (str, optional): Filter by course ID     user_id (str, optional): Filter by username or email  Returns:     A count of completions based on the specified filters.

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

try:
    api_instance.platform_orgs_courses_progress_completed_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_completed_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_completion_rate_retrieve**
> platform_orgs_courses_progress_completion_rate_retrieve(course_id, org)



Average of total completed units

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

try:
    api_instance.platform_orgs_courses_progress_completion_rate_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_completion_rate_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_in_progress_retrieve**
> platform_orgs_courses_progress_in_progress_retrieve(course_id, org)



In Progress means any unit completion in the past 30 days  For platform :  Total users who have atleast a course in_progress on the platform For course : Total users For learner : Total courses in progress  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run     2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)

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

try:
    api_instance.platform_orgs_courses_progress_in_progress_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_in_progress_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_retrieve**
> platform_orgs_courses_progress_retrieve(course_id, org)



Completion information per enrolled user  Gives Percentage of units completed in course  Query Params course_id <required> user_id <optional>

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

try:
    api_instance.platform_orgs_courses_progress_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_progress_started_retrieve**
> platform_orgs_courses_progress_started_retrieve(course_id, org)



Started means an enrollment  For platform :  Total users who have atleast an enrollment For course : Total users enrolled For learner : Total courses in progress  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run     2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)

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

try:
    api_instance.platform_orgs_courses_progress_started_retrieve(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_progress_started_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_courses_users_grades_passed_retrieve**
> platform_orgs_courses_users_grades_passed_retrieve(course_id, org, user_id)



Base class for API views that return a single count value.  This class formats the response as {\"data\": {value_key: count}} where value_key is configurable (defaults to \"count\").  Attributes:     value_key: The key used in the response for the count value

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
> PerlearnerCourseProgress platform_orgs_courses_users_progress_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_users_progress_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> Count platform_orgs_courses_users_time_count_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.platform_orgs_courses_users_time_count_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> VideosCount platform_orgs_courses_users_videos_count_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_users_videos_count_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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

# **platform_orgs_courses_videos_retrieve**
> WatchedVideosPerCourse platform_orgs_courses_videos_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)



Get video watch statistics on a per-course basis.  This endpoint provides a list of courses with aggregated video watch metrics, including total views and completion percentages.  Returns:     A list of courses with:     - Course identification (ID and name)     - Video watch count     - Percentage of total videos watched

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.watched_videos_per_course import WatchedVideosPerCourse
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
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.platform_orgs_courses_videos_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PlatformApi->platform_orgs_courses_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_videos_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**WatchedVideosPerCourse**](WatchedVideosPerCourse.md)

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

# **platform_orgs_courses_videos_retrieve2**
> platform_orgs_courses_videos_retrieve2(course_id, org)



Count of total videos in a course  Query Params course_id  e.g course-v1:Org+Course4+Run

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

try:
    api_instance.platform_orgs_courses_videos_retrieve2(course_id, org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_courses_videos_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 

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

# **platform_orgs_progress_completed_retrieve**
> platform_orgs_progress_completed_retrieve(org)



Get completion count statistics.  This endpoint returns completion counts at different levels: - Platform level: Total users who have completed at least one course - Course level: Total completions for a specific course - Learner level: Total courses completed by a specific learner  Query Parameters:     course_id (str, optional): Filter by course ID     user_id (str, optional): Filter by username or email  Returns:     A count of completions based on the specified filters.

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_progress_completed_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_progress_completed_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_progress_completion_rate_retrieve**
> platform_orgs_progress_completion_rate_retrieve(org)



Average of total completed units

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_progress_completion_rate_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_progress_completion_rate_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_progress_in_progress_retrieve**
> platform_orgs_progress_in_progress_retrieve(org)



In Progress means any unit completion in the past 30 days  For platform :  Total users who have atleast a course in_progress on the platform For course : Total users For learner : Total courses in progress  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run     2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_progress_in_progress_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_progress_in_progress_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_progress_started_retrieve**
> platform_orgs_progress_started_retrieve(org)



Started means an enrollment  For platform :  Total users who have atleast an enrollment For course : Total users enrolled For learner : Total courses in progress  Query Params     1. course_id <optional> e.g course-v1:Org+Course4+Run     2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email)

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_progress_started_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_progress_started_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_retrieve**
> platform_orgs_retrieve(org)



Get a list of registered users on the platform.  This endpoint provides a list of all registered users with basic profile information including username, name, email, and registration date.  Returns:     A list of registered users with their profile information.

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_time_count_retrieve**
> platform_orgs_time_count_retrieve(org)



Total time spent count on the platform within specified range or all time  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default result is all time

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
org = 'org_example' # str | 

try:
    api_instance.platform_orgs_time_count_retrieve(org)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_time_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **platform_orgs_users_active_count_retrieve**
> OverTimeWithTotal platform_orgs_users_active_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get count of active users on the platform.  This endpoint returns the number of users who have had activity on the platform, either for all time or within a specified date range.  Query Parameters:     start_date (str, optional): Start date for filtering (ISO format)     end_date (str, optional): End date for filtering (ISO format)  Returns:     The count of active users and change metrics compared to previous periods.  Default behavior returns the count for all time if no date range is specified.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time_with_total import OverTimeWithTotal
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
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.platform_orgs_users_active_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PlatformApi->platform_orgs_users_active_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_users_active_count_retrieve: %s\n" % e)
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

[**OverTimeWithTotal**](OverTimeWithTotal.md)

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

# **platform_orgs_users_count_retrieve**
> OverTimeWithTotal platform_orgs_users_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get count of registered users on the platform.  This endpoint returns the number of users registered on the platform, either for all time or within a specified date range.  Query Parameters:     start_date (str, optional): Start date for filtering (ISO format)     end_date (str, optional): End date for filtering (ISO format)  Returns:     The count of registered users and change metrics compared to previous periods.  Default behavior returns the count for all time if no date range is specified.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time_with_total import OverTimeWithTotal
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
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.platform_orgs_users_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PlatformApi->platform_orgs_users_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_users_count_retrieve: %s\n" % e)
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

[**OverTimeWithTotal**](OverTimeWithTotal.md)

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

# **platform_orgs_users_courses_completed_count_retrieve**
> OverTimeWithTotal platform_orgs_users_courses_completed_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Count of users who have completed a course on the platform within specified range or all time  Query Params 1. start_date e.g 2020-10-01 2. end_date e.g 2020-10-10  Default is all time

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time_with_total import OverTimeWithTotal
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
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.platform_orgs_users_courses_completed_count_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PlatformApi->platform_orgs_users_courses_completed_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformApi->platform_orgs_users_courses_completed_count_retrieve: %s\n" % e)
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

[**OverTimeWithTotal**](OverTimeWithTotal.md)

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

