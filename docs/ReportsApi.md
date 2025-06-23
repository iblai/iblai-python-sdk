# iblai.ReportsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_orgs_new_create**](ReportsApi.md#reports_orgs_new_create) | **POST** /api/reports/orgs/{org}/new | 
[**reports_orgs_retrieve**](ReportsApi.md#reports_orgs_retrieve) | **GET** /api/reports/orgs/{org}/ | 
[**reports_orgs_retrieve2**](ReportsApi.md#reports_orgs_retrieve2) | **GET** /api/reports/orgs/{org}/{report_name} | 
[**reports_platforms_new_create**](ReportsApi.md#reports_platforms_new_create) | **POST** /api/reports/platforms/{key}/new | 
[**reports_platforms_retrieve**](ReportsApi.md#reports_platforms_retrieve) | **GET** /api/reports/platforms/{key}/ | 
[**reports_platforms_retrieve2**](ReportsApi.md#reports_platforms_retrieve2) | **GET** /api/reports/platforms/{key}/{report_name} | 


# **reports_orgs_new_create**
> ReportCreate reports_orgs_new_create(org, report_request=report_request)



Creates and manages report generation requests.  This endpoint allows users to: 1. Request a new report generation 2. Check the status of a previously requested report 3. Force regeneration of an existing report  Reports expire after a configured time period (default is typically 24-48 hours).  Request Parameters:     report_name (str): The identifier of the report to generate     owner (str): The username of the report owner (usually the current user)     learner_id (str, optional): Filter by specific learner     course_id (str, optional): Filter by specific course     start_date (str, optional): Start date for report data (ISO format)     end_date (str, optional): End date for report data (ISO format)     filters (dict, optional): Additional filters specific to the report type     force (bool, optional): Force regeneration even if a valid report exists  Returns:     For new reports:         - report_id: The unique identifier for the report task         - state: The current state of the report (PENDING, RUNNING, etc.)      For completed reports:         - report_id: The unique identifier for the report task         - report_name: The name of the report         - url: Download URL for the report         - state: COMPLETED         - expires: Expiration timestamp for the report      For in-progress reports:         - report_id: The unique identifier for the report task         - state: Current state (PENDING, RUNNING)         - started_on: When the report generation started         - owner: Username of the report owner  Error Responses:     400 Bad Request: Invalid parameters or report configuration     404 Not Found: Report type not found     403 Forbidden: User doesn't have permission for the requested report

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

# **reports_orgs_retrieve**
> ReportList reports_orgs_retrieve(org)



Lists all available reports in the system.  This endpoint returns a list of all reports available to the user, including: - Report metadata (name, description, icon) - Available query parameters for each report - Result columns that will be returned - Current status of any previously requested reports  If a report has been previously requested by the user, its status will be included in the response. Expired reports are automatically cleaned up.  Returns:     A list of report objects with their metadata and status information.

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
    api_response = api_instance.reports_orgs_retrieve(org)
    print("The response of ReportsApi->reports_orgs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_orgs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**ReportList**](ReportList.md)

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

# **reports_orgs_retrieve2**
> ReportDetail reports_orgs_retrieve2(org, report_name)



Retrieves detailed information about a specific report type.  This endpoint provides: - Metadata about the report (name, description, icon) - Available query parameters for the report - Result columns that will be returned - Current status of the most recent report of this type requested by the user  Path Parameters:     report_name (str): The identifier of the report to retrieve details for  Returns:     Detailed information about the report type and its current status if previously requested.  Error Responses:     404 Not Found: If the specified report type doesn't exist

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.report_detail import ReportDetail
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
report_name = 'report_name_example' # str | 

try:
    api_response = api_instance.reports_orgs_retrieve2(org, report_name)
    print("The response of ReportsApi->reports_orgs_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_orgs_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **report_name** | **str**|  | 

### Return type

[**ReportDetail**](ReportDetail.md)

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

# **reports_platforms_new_create**
> ReportCreate reports_platforms_new_create(key, report_request=report_request)



Triggers a new report generation.  If the report has been previously requested, it returns the status of the report. Reports expire after a configured duration.  The request body should include: - report_name: Name of the report to generate - learner_id: (optional) ID of the learner to filter by - course_id: (optional) ID of the course to filter by - force: (optional) Force generation of a new report even if one exists - filters: (optional) Additional filters for the report - departments: (optional) Department IDs to filter by

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
key = 'key_example' # str | 
report_request = iblai.ReportRequest() # ReportRequest |  (optional)

try:
    api_response = api_instance.reports_platforms_new_create(key, report_request=report_request)
    print("The response of ReportsApi->reports_platforms_new_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_platforms_new_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
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

# **reports_platforms_retrieve**
> ReportList reports_platforms_retrieve(key)



Returns a list of reports available in the system.  For each report, it includes: - display_name: Human-readable name of the report - description: Description of what the report contains - icon: URL to an icon representing the report - report_name: Unique identifier for the report - extra_query_params: Additional parameters that can be passed when creating the report - result_columns: Columns that will be included in the report results - status: Current status of the report if it has been previously requested  The status will include details like the report ID, state, and download URL if completed.

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
key = 'key_example' # str | 

try:
    api_response = api_instance.reports_platforms_retrieve(key)
    print("The response of ReportsApi->reports_platforms_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_platforms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**ReportList**](ReportList.md)

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

# **reports_platforms_retrieve2**
> ReportDetail reports_platforms_retrieve2(key, report_name)



Returns details of a specific report type including its status if previously requested.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.report_detail import ReportDetail
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
key = 'key_example' # str | 
report_name = 'report_name_example' # str | 

try:
    api_response = api_instance.reports_platforms_retrieve2(key, report_name)
    print("The response of ReportsApi->reports_platforms_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ReportsApi->reports_platforms_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **report_name** | **str**|  | 

### Return type

[**ReportDetail**](ReportDetail.md)

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

