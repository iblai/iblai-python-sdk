# iblai.AccessCheckApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_check_retrieve**](AccessCheckApi.md#access_check_retrieve) | **GET** /access-check/{item_type}/{item_id}/ | 


# **access_check_retrieve**
> ItemAccessCheckResponse access_check_retrieve(item_id, item_type, platform_key=platform_key)

Check whether the authenticated user has payment access to an item.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_access_check_response import ItemAccessCheckResponse
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
api_instance = iblai.AccessCheckApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | Platform key. Omit to resolve from request context. (optional)

try:
    api_response = api_instance.access_check_retrieve(item_id, item_type, platform_key=platform_key)
    print("The response of AccessCheckApi->access_check_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccessCheckApi->access_check_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**| Platform key. Omit to resolve from request context. | [optional] 

### Return type

[**ItemAccessCheckResponse**](ItemAccessCheckResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**402** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

