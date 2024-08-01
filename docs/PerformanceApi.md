# iblai.PerformanceApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**performance_orgs_courses_grading_average_retrieve**](PerformanceApi.md#performance_orgs_courses_grading_average_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/average | 
[**performance_orgs_courses_grading_average_with_cutoff_retrieve**](PerformanceApi.md#performance_orgs_courses_grading_average_with_cutoff_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/average-with-cutoff | 
[**performance_orgs_courses_grading_detail_retrieve**](PerformanceApi.md#performance_orgs_courses_grading_detail_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/detail | 
[**performance_orgs_courses_grading_per_learner_retrieve**](PerformanceApi.md#performance_orgs_courses_grading_per_learner_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/per-learner | 
[**performance_orgs_courses_grading_summary_retrieve**](PerformanceApi.md#performance_orgs_courses_grading_summary_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/summary | 
[**performance_orgs_grading_average_retrieve**](PerformanceApi.md#performance_orgs_grading_average_retrieve) | **GET** /api/performance/orgs/{org}/grading/average | 
[**performance_orgs_grading_per_course_retrieve**](PerformanceApi.md#performance_orgs_grading_per_course_retrieve) | **GET** /api/performance/orgs/{org}/grading/per-course | 


# **performance_orgs_courses_grading_average_retrieve**
> Average performance_orgs_courses_grading_average_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



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
api_instance = iblai.PerformanceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_courses_grading_average_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_courses_grading_average_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_courses_grading_average_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
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

# **performance_orgs_courses_grading_average_with_cutoff_retrieve**
> AvgCourseGradeWithCutoff performance_orgs_courses_grading_average_with_cutoff_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Returns average course grade and grade cuttoff  e.g ``` {     \"data\": {         \"grade_cutoffs\": {             \"A\": 90,             \"B\": 80,             \"C\": 70,         },         \"average_grade\": 50.0,     } } ```  Kwargs course_id

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.avg_course_grade_with_cutoff import AvgCourseGradeWithCutoff
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
api_instance = iblai.PerformanceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_courses_grading_average_with_cutoff_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_courses_grading_average_with_cutoff_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_courses_grading_average_with_cutoff_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**AvgCourseGradeWithCutoff**](AvgCourseGradeWithCutoff.md)

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

# **performance_orgs_courses_grading_detail_retrieve**
> CourseGradingDetail performance_orgs_courses_grading_detail_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Grading summary for the entire course overview in a tree-like format  Kwargs course_id <required>

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_grading_detail import CourseGradingDetail
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
api_instance = iblai.PerformanceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_courses_grading_detail_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_courses_grading_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_courses_grading_detail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**CourseGradingDetail**](CourseGradingDetail.md)

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

# **performance_orgs_courses_grading_per_learner_retrieve**
> GradingPerUser performance_orgs_courses_grading_per_learner_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Grading information per enrolled user in a course  Kwargs course_id <required>

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.grading_per_user import GradingPerUser
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
api_instance = iblai.PerformanceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_courses_grading_per_learner_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_courses_grading_per_learner_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_courses_grading_per_learner_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**GradingPerUser**](GradingPerUser.md)

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

# **performance_orgs_courses_grading_summary_retrieve**
> CourseGradeSummary performance_orgs_courses_grading_summary_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)



Returns average grades across various assignment types in a course  Query Params course_id  Returns:     dict     {         \"data\": [             {                 \"assignment_type': <str>,                 \"weight\": <float>,                 \"average_weighted_grade\": <float>,                 \"average_section_grade\": <float>             }, ...         ]     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_grade_summary import CourseGradeSummary
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
api_instance = iblai.PerformanceApi(api_client)
course_id = 'course_id_example' # str | 
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_courses_grading_summary_retrieve(course_id, org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_courses_grading_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_courses_grading_summary_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **org** | **str**|  | 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]

### Return type

[**CourseGradeSummary**](CourseGradeSummary.md)

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

# **performance_orgs_grading_average_retrieve**
> Average performance_orgs_grading_average_retrieve(org, format=format, include_main_platform=include_main_platform)



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
api_instance = iblai.PerformanceApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)

try:
    api_response = api_instance.performance_orgs_grading_average_retrieve(org, format=format, include_main_platform=include_main_platform)
    print("The response of PerformanceApi->performance_orgs_grading_average_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_grading_average_retrieve: %s\n" % e)
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

# **performance_orgs_grading_per_course_retrieve**
> PerformanceGradesPerCourse performance_orgs_grading_per_course_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)



Returns grade related performance data per course  Returns:     dict     {         \"data\": [             {                 \"course_id': <str>,                 \"name': <str>,                 \"num_enrollments\": <int>,                 \"num_passed\": <int>,                 \"avg_grade\": <int>             }, ...         ]     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.performance_grades_per_course import PerformanceGradesPerCourse
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
api_instance = iblai.PerformanceApi(api_client)
org = 'org_example' # str | 
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
length = 56 # int | Size of data to return (optional)
page = 56 # int | Page offset (optional)

try:
    api_response = api_instance.performance_orgs_grading_per_course_retrieve(org, format=format, include_main_platform=include_main_platform, length=length, page=page)
    print("The response of PerformanceApi->performance_orgs_grading_per_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PerformanceApi->performance_orgs_grading_per_course_retrieve: %s\n" % e)
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

[**PerformanceGradesPerCourse**](PerformanceGradesPerCourse.md)

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

