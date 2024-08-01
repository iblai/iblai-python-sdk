# iblai.ReportsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_orgs_list**](ReportsApi.md#reports_orgs_list) | **GET** /api/reports/orgs/{org}/ | 
[**reports_orgs_new_create**](ReportsApi.md#reports_orgs_new_create) | **POST** /api/reports/orgs/{org}/new | 


# **reports_orgs_list**
> List[ReportList] reports_orgs_list(org)



Returns list of report available in the system to download.     `extra_query_params` defines additional query params that can be passed to the report create body If the report has been previously requested, it returns the status of the report

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.report_list import ReportList
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
api_instance = iblai.ReportsApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.reports_orgs_list(org)
    print("The response of ReportsApi->reports_orgs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_orgs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[ReportList]**](ReportList.md)

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

# **reports_orgs_new_create**
> ReportCreate reports_orgs_new_create(org, report_request=report_request)



Triggers a new report generation.  If the report has been previously requested, it returns the status of the report  The current duration for generated report `{settings.REPORT_EXPIRY_SECONDS/3600}` hours.  Given a sample result of the api call  ```json     [       {         \"data\": [           {             \"display_name\": \"User Report 1\",             \"description\": \"A short Description of Report 1\",             \"report_name\": \"report-1\",             \"icon\": \"http://some-icon.png\",             \"extra_query_params\": [               \"course_id\", \"learner_id\"             ],             \"status\": {}           }         ]       }     ] ```  The body of the request would be ```json     {         \"report_name\": \"report-1\",         \"owner\": \"owner-name\"         \"learner_id\": \"learner-id\",         \"course_id\": \"course-id\",     } ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.report_create import ReportCreate
from iblai.models.report_request import ReportRequest
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
api_instance = iblai.ReportsApi(api_client)
org = 'org_example' # str | 
report_request = iblai.ReportRequest() # ReportRequest |  (optional)

try:
    api_response = api_instance.reports_orgs_new_create(org, report_request=report_request)
    print("The response of ReportsApi->reports_orgs_new_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_orgs_new_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **report_request** | [**ReportRequest**](ReportRequest.md)|  | [optional] 

### Return type

[**ReportCreate**](ReportCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

