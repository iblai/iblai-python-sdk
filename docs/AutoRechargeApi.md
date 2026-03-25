# iblai.AutoRechargeApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_recharge_trigger_create**](AutoRechargeApi.md#auto_recharge_trigger_create) | **POST** /auto-recharge/trigger/ | Trigger auto-recharge or manual top-up


# **auto_recharge_trigger_create**
> AutoRechargeTriggerResponse auto_recharge_trigger_create(auto_recharge_trigger_request=auto_recharge_trigger_request)

Trigger auto-recharge or manual top-up

With amount_usd: manual top-up (charge that amount, add credits; no threshold/limit/cooldown). Without amount_usd: run auto-recharge once if enabled and balance below threshold. Returns 400 if skipped or failed (e.g. no payment method, cooldown). Pass platform_key in request body.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.auto_recharge_trigger_request import AutoRechargeTriggerRequest
from iblai.models.auto_recharge_trigger_response import AutoRechargeTriggerResponse
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
api_instance = iblai.AutoRechargeApi(api_client)
auto_recharge_trigger_request = iblai.AutoRechargeTriggerRequest() # AutoRechargeTriggerRequest |  (optional)

try:
    # Trigger auto-recharge or manual top-up
    api_response = api_instance.auto_recharge_trigger_create(auto_recharge_trigger_request=auto_recharge_trigger_request)
    print("The response of AutoRechargeApi->auto_recharge_trigger_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AutoRechargeApi->auto_recharge_trigger_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_recharge_trigger_request** | [**AutoRechargeTriggerRequest**](AutoRechargeTriggerRequest.md)|  | [optional] 

### Return type

[**AutoRechargeTriggerResponse**](AutoRechargeTriggerResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

