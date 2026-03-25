# iblai.ReportsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reports_platforms_download_retrieve**](ReportsApi.md#reports_platforms_download_retrieve) | **GET** /api/reports/platforms/{key}/{task_id}/download | Download report
[**reports_platforms_new_create**](ReportsApi.md#reports_platforms_new_create) | **POST** /api/reports/platforms/{key}/new | 
[**reports_platforms_retrieve**](ReportsApi.md#reports_platforms_retrieve) | **GET** /api/reports/platforms/{key}/ | 
[**reports_platforms_retrieve2**](ReportsApi.md#reports_platforms_retrieve2) | **GET** /api/reports/platforms/{key}/{report_name} | 


# **reports_platforms_download_retrieve**
> reports_platforms_download_retrieve(key, task_id, columns=columns, format=format)

Download report

Download a completed report as CSV or JSON. Use the columns parameter to control column order.

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
api_instance = iblai.ReportsApi(api_client)
key = 'key_example' # str | 
task_id = 'task_id_example' # str | 
columns = 'columns_example' # str | Comma-separated column names to control output order. Must be a subset of the report's allowed_result_fields. Omit to use the report's default order. (optional)
format = csv # str | Download format (optional) (default to csv)

try:
    # Download report
    api_instance.reports_platforms_download_retrieve(key, task_id, columns=columns, format=format)
except Exception as e:
    print("Exception when calling ReportsApi->reports_platforms_download_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **task_id** | **str**|  | 
 **columns** | **str**| Comma-separated column names to control output order. Must be a subset of the report&#39;s allowed_result_fields. Omit to use the report&#39;s default order. | [optional] 
 **format** | **str**| Download format | [optional] [default to csv]

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

# **reports_platforms_new_create**
> ReportCreate reports_platforms_new_create(key, report_request=report_request)

Triggers a new report generation.

If the report has been previously requested, it returns the status of the report.
Reports expire after a configured duration.

The request body should include:
- report_name: Name of the report to generate
- learner_id: (optional) ID of the learner to filter by
- course_id: (optional) ID of the course to filter by
- force: (optional) Force generation of a new report even if one exists
- filters: (optional) Additional filters for the report
- departments: (optional) Department IDs to filter by
- mentor: (optional) Mentor unique_id for mentor-specific reports (e.g., ai-mentor-chat-history)
- usergroup_ids: (optional) List of usergroup IDs to filter report data

Required RBAC Permissions:
    1. CanViewAnalytics (kill switch):
       - Action: "Ibl.Analytics/CanViewAnalytics/action"
       - Resource: /platforms/{platform_pk}/

    2. Reports access to at least one user or usergroup:
       - Action: "Ibl.Analytics/Reports/read"
       - Resource: /platforms/{platform_pk}/users/{user_pk}/ OR
                   /platforms/{platform_pk}/usergroups/{group_pk}/
       - Note: User must have access to at least one user or usergroup resource
         with Reports/read permission. Unrestricted access to all users
         (/platforms/{platform_pk}/users/) also satisfies this requirement.

    3. For mentor-specific reports (e.g., ai-mentor-chat-history):
       - Action: "Ibl.Analytics/Reports/read"
       - Resource: /platforms/{platform_pk}/mentors/{mentor_id}/
       - Note: User must have access to at least one mentor via RBAC OR own at least
         one mentor (created_by == username). If a specific mentor_unique_id is
         provided, user must have access to that specific mentor.
       - Raises PermissionDenied if user has no access to any mentors.

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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reports_platforms_retrieve**
> ReportList reports_platforms_retrieve(key)

Returns a list of reports available in the system.

For each report, it includes:
- display_name: Human-readable name of the report
- description: Description of what the report contains
- icon: URL to an icon representing the report
- report_name: Unique identifier for the report
- extra_query_params: Additional parameters that can be passed when creating the report
- result_columns: Columns that will be included in the report results
- status: Current status of the report if it has been previously requested

The status will include details like the report ID, state, and download URL if completed.

Required RBAC Permissions:
    1. CanViewAnalytics (kill switch):
       - Action: "Ibl.Analytics/CanViewAnalytics/action"
       - Resource: /platforms/{platform_pk}/

    2. Reports access to at least one user or usergroup:
       - Action: "Ibl.Analytics/Reports/read"
       - Resource: /platforms/{platform_pk}/users/{user_pk}/ OR
                   /platforms/{platform_pk}/usergroups/{group_pk}/
       - Note: User must have access to at least one user or usergroup resource
         with Reports/read permission. Unrestricted access to all users
         (/platforms/{platform_pk}/users/) also satisfies this requirement.

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
> ReportDetail reports_platforms_retrieve2(key, report_name, mentor_unique_id=mentor_unique_id)

Returns details of a specific report type including its status if previously requested.

Required RBAC Permissions:
    1. CanViewAnalytics (kill switch):
       - Action: "Ibl.Analytics/CanViewAnalytics/action"
       - Resource: /platforms/{platform_pk}/

    2. Reports access to at least one user or usergroup:
       - Action: "Ibl.Analytics/Reports/read"
       - Resource: /platforms/{platform_pk}/users/{user_pk}/ OR
                   /platforms/{platform_pk}/usergroups/{group_pk}/
       - Note: User must have access to at least one user or usergroup resource
         with Reports/read permission. Unrestricted access to all users
         (/platforms/{platform_pk}/users/) also satisfies this requirement.

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
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique ID for mentor-specific reports (e.g., ai-mentor-chat-history). When provided, ownership is validated - mentor owners can access without explicit RBAC permissions. (optional)

try:
    api_response = api_instance.reports_platforms_retrieve2(key, report_name, mentor_unique_id=mentor_unique_id)
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
 **mentor_unique_id** | **str**| Mentor unique ID for mentor-specific reports (e.g., ai-mentor-chat-history). When provided, ownership is validated - mentor owners can access without explicit RBAC permissions. | [optional] 

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

