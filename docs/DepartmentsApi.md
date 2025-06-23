# iblai.DepartmentsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**departments_orgs_retrieve**](DepartmentsApi.md#departments_orgs_retrieve) | **GET** /api/departments/orgs/{org}/ | 


# **departments_orgs_retrieve**
> GroupList departments_orgs_retrieve(org, department_id=department_id, departments=departments, end_date=end_date, format=format, include_main_platform=include_main_platform, is_enrolled=is_enrolled, length=length, location=location, page=page, pathway=pathway, program=program, start_date=start_date)



Get a list of departments with metrics and filtering options.  This endpoint provides a paginated list of departments with aggregated metrics about learner performance, course completions, and skill acquisition.  Query Parameters:     page (int, optional): Page number for pagination     length (int, optional): Number of items per page     program (str, optional): Filter by program     pathway (str, optional): Filter by pathway     departments (list, optional): Filter by department ids     department_id (str, optional): Filter by department id     location (str, optional): Filter by location     is_enrolled (bool, optional): Filter for departments with enrolled users     start_date (date, optional): Filter by learner join date (start range)     end_date (date, optional): Filter by learner join date (end range)  Returns:     A paginated list of departments with comprehensive metrics.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.group_list import GroupList
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
api_instance = iblai.DepartmentsApi(api_client)
org = 'org_example' # str | 
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
departments = ['departments_example'] # List[str] | Departments search string. Single string or list of strings. e.g 'sample_department' or `['department', 'another department']`  (optional)
end_date = '2013-10-20' # date | Filter by learners date_joined. Start date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
is_enrolled = True # bool | Filter for users who have at least an enro;lment (optional)
length = 56 # int | Size of data to return (optional)
location = 'location_example' # str | Location search string (optional)
page = 56 # int | Page offset (optional)
pathway = 'pathway_example' # str | Pathway string (optional)
program = 'program_example' # str | Program search string (optional)
start_date = '2013-10-20' # date | Filter by learners date_joined. Start date. ISO 8601 (optional)

try:
    api_response = api_instance.departments_orgs_retrieve(org, department_id=department_id, departments=departments, end_date=end_date, format=format, include_main_platform=include_main_platform, is_enrolled=is_enrolled, length=length, location=location, page=page, pathway=pathway, program=program, start_date=start_date)
    print("The response of DepartmentsApi->departments_orgs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling DepartmentsApi->departments_orgs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **departments** | [**List[str]**](str.md)| Departments search string. Single string or list of strings. e.g &#39;sample_department&#39; or &#x60;[&#39;department&#39;, &#39;another department&#39;]&#x60;  | [optional] 
 **end_date** | **date**| Filter by learners date_joined. Start date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **is_enrolled** | **bool**| Filter for users who have at least an enro;lment | [optional] 
 **length** | **int**| Size of data to return | [optional] 
 **location** | **str**| Location search string | [optional] 
 **page** | **int**| Page offset | [optional] 
 **pathway** | **str**| Pathway string | [optional] 
 **program** | **str**| Program search string | [optional] 
 **start_date** | **date**| Filter by learners date_joined. Start date. ISO 8601 | [optional] 

### Return type

[**GroupList**](GroupList.md)

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

