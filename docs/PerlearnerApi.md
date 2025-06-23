# iblai.PerlearnerApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**perlearner_orgs_learners_retrieve**](PerlearnerApi.md#perlearner_orgs_learners_retrieve) | **GET** /api/perlearner/orgs/{org}/learners | 
[**perlearner_orgs_users_activity_retrieve**](PerlearnerApi.md#perlearner_orgs_users_activity_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/activity/ | 
[**perlearner_orgs_users_courses_grading_cutoffs_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_grading_cutoffs_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/cutoffs | 
[**perlearner_orgs_users_courses_grading_detail_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_grading_detail_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/detail | 
[**perlearner_orgs_users_courses_grading_summary_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_grading_summary_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/summary | 
[**perlearner_orgs_users_courses_overview_engagement_index_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_overview_engagement_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/engagement-index | 
[**perlearner_orgs_users_courses_overview_grade_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_overview_grade_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/grade | 
[**perlearner_orgs_users_courses_overview_performance_index_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_overview_performance_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/performance-index | 
[**perlearner_orgs_users_courses_overview_time_over_time_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_overview_time_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/time/over-time | 
[**perlearner_orgs_users_courses_videos_over_time_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_videos_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos/over-time | 
[**perlearner_orgs_users_courses_videos_retrieve**](PerlearnerApi.md#perlearner_orgs_users_courses_videos_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos | 
[**perlearner_orgs_users_grades_per_course_retrieve**](PerlearnerApi.md#perlearner_orgs_users_grades_per_course_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/grades/per-course | 
[**perlearner_orgs_users_info_retrieve**](PerlearnerApi.md#perlearner_orgs_users_info_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/info | 
[**perlearner_orgs_users_last_access_retrieve**](PerlearnerApi.md#perlearner_orgs_users_last_access_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/last-access | 
[**perlearner_orgs_users_overview_engagement_index_retrieve**](PerlearnerApi.md#perlearner_orgs_users_overview_engagement_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/engagement-index | 
[**perlearner_orgs_users_overview_grades_average_retrieve**](PerlearnerApi.md#perlearner_orgs_users_overview_grades_average_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/grades/average | 
[**perlearner_orgs_users_overview_performance_index_retrieve**](PerlearnerApi.md#perlearner_orgs_users_overview_performance_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/performance-index | 
[**perlearner_orgs_users_overview_time_over_time_retrieve**](PerlearnerApi.md#perlearner_orgs_users_overview_time_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/time/over-time | 
[**perlearner_orgs_users_retrieve**](PerlearnerApi.md#perlearner_orgs_users_retrieve) | **GET** /api/perlearner/orgs/{org}/users | 
[**perlearner_orgs_users_videos_over_time_retrieve**](PerlearnerApi.md#perlearner_orgs_users_videos_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/videos/over-time | 
[**perlearner_orgs_users_videos_per_course_retrieve**](PerlearnerApi.md#perlearner_orgs_users_videos_per_course_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/videos/per-course | 


# **perlearner_orgs_learners_retrieve**
> NewPerLearnerList perlearner_orgs_learners_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, is_enrolled=is_enrolled, length=length, location=location, page=page, platform=platform, program=program, search=search, start_date=start_date)



Enhanced API endpoint for listing learners with comprehensive filtering.  This endpoint provides a paginated list of learners with detailed metrics and supports advanced filtering options. It uses DM token authentication and respects department-based access controls.  Query Parameters:     page (int): Page number for pagination     length (int): Number of items per page     search (str): Filter by username, email, or full name     program (str): Filter by program     location (str): Filter by location     is_enrolled (bool): Filter for users with enrollments     platform (str): Filter by platform     start_date (date): Filter by join date (start range)     end_date (date): Filter by join date (end range)  Returns:     A paginated list of learners with comprehensive metrics including:     - Course enrollments and completions     - Time spent on platform     - Pathway progress     - Certificate and skill information     - Location data  Access Control:     - Platform admins can see all learners     - Department admins can only see learners in their departments

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.new_per_learner_list import NewPerLearnerList
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = '2013-10-20' # date | Learner date_joined end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
is_enrolled = True # bool | Filter for users who have at least an enrollment (optional)
length = 56 # int | Size of data to return (optional)
location = 'location_example' # str | Location search string (optional)
page = 56 # int | Page offset (optional)
platform = 'platform_example' # str | Platform search string (optional)
program = 'program_example' # str | Program search string (optional)
search = 'search_example' # str | Search string for learner. email, username or full name (optional)
start_date = '2013-10-20' # date | Learner date_joined start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_learners_retrieve(org, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, is_enrolled=is_enrolled, length=length, location=location, page=page, platform=platform, program=program, search=search, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_learners_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_learners_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **date**| Learner date_joined end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **is_enrolled** | **bool**| Filter for users who have at least an enrollment | [optional] 
 **length** | **int**| Size of data to return | [optional] 
 **location** | **str**| Location search string | [optional] 
 **page** | **int**| Page offset | [optional] 
 **platform** | **str**| Platform search string | [optional] 
 **program** | **str**| Program search string | [optional] 
 **search** | **str**| Search string for learner. email, username or full name | [optional] 
 **start_date** | **date**| Learner date_joined start date. ISO 8601 | [optional] 

### Return type

[**NewPerLearnerList**](NewPerLearnerList.md)

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

# **perlearner_orgs_users_activity_retrieve**
> ActivityAPI perlearner_orgs_users_activity_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



Provides information on user enrollments  Params user_id e.g developer@ibleducation.com| developer

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.activity_api import ActivityAPI
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.perlearner_orgs_users_activity_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PerlearnerApi->perlearner_orgs_users_activity_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_activity_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**ActivityAPI**](ActivityAPI.md)

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

# **perlearner_orgs_users_courses_grading_cutoffs_retrieve**
> PerlearnerGradeWithCutOff perlearner_orgs_users_courses_grading_cutoffs_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Provides about a learner current grade in a course with the course cut Kwargs 1. course_id e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_grade_with_cut_off import PerlearnerGradeWithCutOff
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_grading_cutoffs_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_grading_cutoffs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_grading_cutoffs_retrieve: %s\n" % e)
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

[**PerlearnerGradeWithCutOff**](PerlearnerGradeWithCutOff.md)

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

# **perlearner_orgs_users_courses_grading_detail_retrieve**
> DetailedGradeView perlearner_orgs_users_courses_grading_detail_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.detailed_grade_view import DetailedGradeView
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_grading_detail_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_grading_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_grading_detail_retrieve: %s\n" % e)
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

[**DetailedGradeView**](DetailedGradeView.md)

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

# **perlearner_orgs_users_courses_grading_summary_retrieve**
> PerlearnerGradeSummary perlearner_orgs_users_courses_grading_summary_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Query Params 1. course_id e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_grade_summary import PerlearnerGradeSummary
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_grading_summary_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_grading_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_grading_summary_retrieve: %s\n" % e)
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

[**PerlearnerGradeSummary**](PerlearnerGradeSummary.md)

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

# **perlearner_orgs_users_courses_overview_engagement_index_retrieve**
> Value perlearner_orgs_users_courses_overview_engagement_index_retrieve(course_id, org, user_id)



Average of days with atleast an activity within ENGAGEMENT_INDEX_PERIOD consecutive days for a learner in a course

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.value import Value
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.perlearner_orgs_users_courses_overview_engagement_index_retrieve(course_id, org, user_id)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_overview_engagement_index_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_overview_engagement_index_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Value**](Value.md)

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

# **perlearner_orgs_users_courses_overview_grade_retrieve**
> PerlearnerGradeWithCutOff perlearner_orgs_users_courses_overview_grade_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Provides about a learner current grade in a course with the course cut Kwargs 1. course_id e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_grade_with_cut_off import PerlearnerGradeWithCutOff
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_overview_grade_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_overview_grade_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_overview_grade_retrieve: %s\n" % e)
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

[**PerlearnerGradeWithCutOff**](PerlearnerGradeWithCutOff.md)

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

# **perlearner_orgs_users_courses_overview_performance_index_retrieve**
> Value perlearner_orgs_users_courses_overview_performance_index_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Evaluates performance index for platform, per course, per user and per user-per course  Query Params course_id <optional> learner_id <optional>

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.value import Value
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_overview_performance_index_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_overview_performance_index_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_overview_performance_index_retrieve: %s\n" % e)
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

[**Value**](Value.md)

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

# **perlearner_orgs_users_courses_overview_time_over_time_retrieve**
> OverTimeWithTotal perlearner_orgs_users_courses_overview_time_over_time_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent within a course in secs on a per-day basis  Kwargs 1. course_id  e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email) Query Params 3. start_date e.g 2020-10-01 4. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_overview_time_over_time_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_overview_time_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_overview_time_over_time_retrieve: %s\n" % e)
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

# **perlearner_orgs_users_courses_videos_over_time_retrieve**
> OverTimeWithTotal perlearner_orgs_users_courses_videos_over_time_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get video watch counts over time.  This endpoint provides daily counts of videos watched over a specified time period, with options to filter by course or user.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)     course_id (str, optional): Filter by course ID     user_id (str, optional): Filter by username or email  Returns:     Daily video watch counts over the specified time period.  Default time range is the last 7 days if no dates are specified.  Access Control:     - Platform admins can access any video watch data     - Learners can access their own video watch data

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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_courses_videos_over_time_retrieve(course_id, org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_videos_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_videos_over_time_retrieve: %s\n" % e)
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

# **perlearner_orgs_users_courses_videos_retrieve**
> PerLearnerCourseVideosWatched perlearner_orgs_users_courses_videos_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



List of videos within a course a learner has watched  Kwargs 1. course_id e.g course-v1:Org+Course4+Run 2. user_id e.g developer@ibleducation.com or dev123 (username|email)  Default result when no query param is added is [], 0

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.per_learner_course_videos_watched import PerLearnerCourseVideosWatched
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
api_instance = iblai.PerlearnerApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.perlearner_orgs_users_courses_videos_retrieve(course_id, org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PerlearnerApi->perlearner_orgs_users_courses_videos_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_courses_videos_retrieve: %s\n" % e)
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

[**PerLearnerCourseVideosWatched**](PerLearnerCourseVideosWatched.md)

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

# **perlearner_orgs_users_grades_per_course_retrieve**
> PerlearnerGradingPerCourseAPI perlearner_orgs_users_grades_per_course_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



Summary Grading Information for a learner on a per-enrollment basis  Query Params 1. user_id e.g developer@ibleducation.com or dev123 (username|email)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_grading_per_course_api import PerlearnerGradingPerCourseAPI
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.perlearner_orgs_users_grades_per_course_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PerlearnerApi->perlearner_orgs_users_grades_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_grades_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**PerlearnerGradingPerCourseAPI**](PerlearnerGradingPerCourseAPI.md)

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

# **perlearner_orgs_users_info_retrieve**
> LearnerInformationAPI perlearner_orgs_users_info_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform, meta=meta, search=search)



Retrieve detailed information about a specific learner.  This endpoint returns personal and activity information about a learner, including profile data, activity metrics, and location information.  Path Parameters:     user_id (str): The username or email of the learner  Query Parameters:     meta (bool): Include additional analytics information when true  Returns:     Detailed learner information including:     - Profile data (username, name, email)     - Registration and activity dates     - Activity metrics (assessments, time spent, videos watched)     - Location and browser information (when available)  Access Control:     - Platform admins can access any learner     - Learners can access their own information     - Department admins can access learners in their departments

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.learner_information_api import LearnerInformationAPI
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
meta = n # str | Include extra analytics information?  * `y` - y * `yes` - yes * `true` - true * `True` - True * `n` - n * `no` - no * `false` - false * `False` - False (optional) (default to n)
search = 'search_example' # str |  (optional)

try:
    api_response = api_instance.perlearner_orgs_users_info_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform, meta=meta, search=search)
    print("The response of PerlearnerApi->perlearner_orgs_users_info_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_info_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **meta** | **str**| Include extra analytics information?  * &#x60;y&#x60; - y * &#x60;yes&#x60; - yes * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;n&#x60; - n * &#x60;no&#x60; - no * &#x60;false&#x60; - false * &#x60;False&#x60; - False | [optional] [default to n]
 **search** | **str**|  | [optional] 

### Return type

[**LearnerInformationAPI**](LearnerInformationAPI.md)

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

# **perlearner_orgs_users_last_access_retrieve**
> PerLearnerLastAccess perlearner_orgs_users_last_access_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



Last course accessed by a learner, includes upto unit information as well

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.per_learner_last_access import PerLearnerLastAccess
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.perlearner_orgs_users_last_access_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PerlearnerApi->perlearner_orgs_users_last_access_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_last_access_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**PerLearnerLastAccess**](PerLearnerLastAccess.md)

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

# **perlearner_orgs_users_overview_engagement_index_retrieve**
> Value perlearner_orgs_users_overview_engagement_index_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Average of days with atleast an activity within ENGAGEMENT_INDEX_PERIOD consecutive days

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.value import Value
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_overview_engagement_index_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_overview_engagement_index_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_overview_engagement_index_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Value**](Value.md)

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

# **perlearner_orgs_users_overview_grades_average_retrieve**
> Average perlearner_orgs_users_overview_grades_average_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)



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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.perlearner_orgs_users_overview_grades_average_retrieve(org, user_id, department_id=department_id, format=format, include_main_platform=include_main_platform)
    print("The response of PerlearnerApi->perlearner_orgs_users_overview_grades_average_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_overview_grades_average_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
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

# **perlearner_orgs_users_overview_performance_index_retrieve**
> Value perlearner_orgs_users_overview_performance_index_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Evaluates performance index for platform, per course, per user and per user-per course  Query Params course_id <optional> learner_id <optional>

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.value import Value
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_overview_performance_index_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_overview_performance_index_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_overview_performance_index_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**Value**](Value.md)

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

# **perlearner_orgs_users_overview_time_over_time_retrieve**
> OverTimeWithTotal perlearner_orgs_users_overview_time_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Time spent in secs on a per-day basis  Query Params 1. course_id <optional> e.g course-v1:Org+Course4+Run 2. user_id <optional> e.g developer@ibleducation.com or dev123 (username|email) 3. start_date e.g 2020-10-01 4. end_date e.g 2020-10-10  Default result when no query param is added is last_7_days (today inclusive)

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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_overview_time_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_overview_time_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_overview_time_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
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

# **perlearner_orgs_users_retrieve**
> PerlearnerUserList perlearner_orgs_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)



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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)
search = 'search_example' # str | Search string for learner (optional)

try:
    api_response = api_instance.perlearner_orgs_users_retrieve(org, department_id=department_id, format=format, include_main_platform=include_main_platform, length=length, page=page, search=search)
    print("The response of PerlearnerApi->perlearner_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_retrieve: %s\n" % e)
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

# **perlearner_orgs_users_videos_over_time_retrieve**
> OverTimeWithTotal perlearner_orgs_users_videos_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get video watch counts over time.  This endpoint provides daily counts of videos watched over a specified time period, with options to filter by course or user.  Query Parameters:     start_date (str, optional): Start date for the time range (ISO format)     end_date (str, optional): End date for the time range (ISO format)     course_id (str, optional): Filter by course ID     user_id (str, optional): Filter by username or email  Returns:     Daily video watch counts over the specified time period.  Default time range is the last 7 days if no dates are specified.  Access Control:     - Platform admins can access any video watch data     - Learners can access their own video watch data

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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_videos_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_videos_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_videos_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
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

# **perlearner_orgs_users_videos_per_course_retrieve**
> PerlearnerEngagementVideosWatchedPerCourse perlearner_orgs_users_videos_per_course_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Summary Videos watched data for a learner per enrollment  Query Params 1. user_id e.g developer@ibleducation.com or dev123 (username|email)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.perlearner_engagement_videos_watched_per_course import PerlearnerEngagementVideosWatchedPerCourse
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
api_instance = iblai.PerlearnerApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.perlearner_orgs_users_videos_per_course_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of PerlearnerApi->perlearner_orgs_users_videos_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerlearnerApi->perlearner_orgs_users_videos_per_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**PerlearnerEngagementVideosWatchedPerCourse**](PerlearnerEngagementVideosWatchedPerCourse.md)

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

