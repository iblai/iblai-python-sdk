# iblai.AnalyticsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_orgs_time_update_create**](AnalyticsApi.md#analytics_orgs_time_update_create) | **POST** /api/analytics/orgs/{org}/time/update/ | 
[**analytics_time_spent_user_retrieve**](AnalyticsApi.md#analytics_time_spent_user_retrieve) | **GET** /api/analytics/time-spent/user/ | Get total time spent for current user


# **analytics_orgs_time_update_create**
> TimeSpentUpdateResponse analytics_orgs_time_update_create(org, time_spent_update_request)



Update time spent tracking data from client-side events.  This endpoint receives time spent data collected on the client side and stores it in the analytics database. It requires a valid authentication token.  Methods:     POST: Submit time spent tracking data    Returns:     A response indicating success or failure:     {         \"success\": true|false,         \"message\": \"Error message if failed\" (optional)     }  Error Responses:     400 Bad Request: If the request data is invalid or the API is disabled  Notes:     This API must be enabled via the ENABLE_TIME_SPENT_UPDATE_API setting.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.time_spent_update_request import TimeSpentUpdateRequest
from iblai.models.time_spent_update_response import TimeSpentUpdateResponse
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
api_instance = iblai.AnalyticsApi(api_client)
org = 'org_example' # str | 
time_spent_update_request = iblai.TimeSpentUpdateRequest() # TimeSpentUpdateRequest | 

try:
    api_response = api_instance.analytics_orgs_time_update_create(org, time_spent_update_request)
    print("The response of AnalyticsApi->analytics_orgs_time_update_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_orgs_time_update_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **time_spent_update_request** | [**TimeSpentUpdateRequest**](TimeSpentUpdateRequest.md)|  | 

### Return type

[**TimeSpentUpdateResponse**](TimeSpentUpdateResponse.md)

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

# **analytics_time_spent_user_retrieve**
> TimeSpentPerUserResponse analytics_time_spent_user_retrieve(course_id=course_id, end_date=end_date, include_main_platform=include_main_platform, learner_id=learner_id, mentor_uuid=mentor_uuid, platform=platform, session_uuid=session_uuid, start_date=start_date, url=url)

Get total time spent for current user

         Returns the total time spent (in seconds) for the current authenticated user.         Can be filtered by platform, date range, course ID, URL, mentor UUID, and session UUID.         

### Example


```python
import iblai
from iblai.models.time_spent_per_user_response import TimeSpentPerUserResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AnalyticsApi(api_client)
course_id = 'course_id_example' # str | Course ID to filter by (can be partial) (optional)
end_date = '2013-10-20' # date | End date for time range (YYYY-MM-DD) (optional)
include_main_platform = True # bool | Whether to include main platform data (optional) (default to True)
learner_id = 'learner_id_example' # str | Username to get data for (admin users only) (optional)
mentor_uuid = 'mentor_uuid_example' # str | Mentor UUID to filter by (optional)
platform = 'platform_example' # str | Platform name or key to filter by (optional)
session_uuid = 'session_uuid_example' # str | Session UUID to filter by (optional)
start_date = '2013-10-20' # date | Start date for time range (YYYY-MM-DD) (optional)
url = 'url_example' # str | URL to filter by (can be partial) (optional)

try:
    # Get total time spent for current user
    api_response = api_instance.analytics_time_spent_user_retrieve(course_id=course_id, end_date=end_date, include_main_platform=include_main_platform, learner_id=learner_id, mentor_uuid=mentor_uuid, platform=platform, session_uuid=session_uuid, start_date=start_date, url=url)
    print("The response of AnalyticsApi->analytics_time_spent_user_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_time_spent_user_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Course ID to filter by (can be partial) | [optional] 
 **end_date** | **date**| End date for time range (YYYY-MM-DD) | [optional] 
 **include_main_platform** | **bool**| Whether to include main platform data | [optional] [default to True]
 **learner_id** | **str**| Username to get data for (admin users only) | [optional] 
 **mentor_uuid** | **str**| Mentor UUID to filter by | [optional] 
 **platform** | **str**| Platform name or key to filter by | [optional] 
 **session_uuid** | **str**| Session UUID to filter by | [optional] 
 **start_date** | **date**| Start date for time range (YYYY-MM-DD) | [optional] 
 **url** | **str**| URL to filter by (can be partial) | [optional] 

### Return type

[**TimeSpentPerUserResponse**](TimeSpentPerUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

