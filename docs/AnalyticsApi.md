# iblai.AnalyticsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_orgs_time_update_create**](AnalyticsApi.md#analytics_orgs_time_update_create) | **POST** /api/analytics/orgs/{org}/time/update/ | 


# **analytics_orgs_time_update_create**
> TimeSpentUpdateResponse analytics_orgs_time_update_create(org, time_spent_update_request)



Update time spent as received from the client side  ``` Authentication: ManagerAuthToken  Example: Token <token> ```

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

