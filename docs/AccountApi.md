# iblai.AccountApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_partial_update**](AccountApi.md#account_partial_update) | **PATCH** /account/ | Partially update auto-recharge preferences
[**account_retrieve**](AccountApi.md#account_retrieve) | **GET** /account/ | Get credit account information
[**account_update**](AccountApi.md#account_update) | **PUT** /account/ | Update auto-recharge preferences


# **account_partial_update**
> CreditAccountInfo account_partial_update(patched_credit_account_auto_recharge_update=patched_credit_account_auto_recharge_update)

Partially update auto-recharge preferences

Same as PUT; partial update of auto-recharge fields.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credit_account_info import CreditAccountInfo
from iblai.models.patched_credit_account_auto_recharge_update import PatchedCreditAccountAutoRechargeUpdate
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
api_instance = iblai.AccountApi(api_client)
patched_credit_account_auto_recharge_update = iblai.PatchedCreditAccountAutoRechargeUpdate() # PatchedCreditAccountAutoRechargeUpdate |  (optional)

try:
    # Partially update auto-recharge preferences
    api_response = api_instance.account_partial_update(patched_credit_account_auto_recharge_update=patched_credit_account_auto_recharge_update)
    print("The response of AccountApi->account_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountApi->account_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_credit_account_auto_recharge_update** | [**PatchedCreditAccountAutoRechargeUpdate**](PatchedCreditAccountAutoRechargeUpdate.md)|  | [optional] 

### Return type

[**CreditAccountInfo**](CreditAccountInfo.md)

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

# **account_retrieve**
> CreditAccountInfo account_retrieve(platform_key=platform_key)

Get credit account information

Return display credits (available_credits, has_credits, account_id) and auto-recharge settings. Pass platform_key (or key) to see platform balance if you are a platform admin.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credit_account_info import CreditAccountInfo
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
api_instance = iblai.AccountApi(api_client)
platform_key = 'platform_key_example' # str | The unique key of the platform to access. If not provided, defaults to 'main' (user's own account). (optional)

try:
    # Get credit account information
    api_response = api_instance.account_retrieve(platform_key=platform_key)
    print("The response of AccountApi->account_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountApi->account_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| The unique key of the platform to access. If not provided, defaults to &#39;main&#39; (user&#39;s own account). | [optional] 

### Return type

[**CreditAccountInfo**](CreditAccountInfo.md)

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

# **account_update**
> CreditAccountInfo account_update(credit_account_auto_recharge_update=credit_account_auto_recharge_update)

Update auto-recharge preferences

Update auto_recharge_threshold_usd, auto_recharge_amount_usd, auto_recharge_enabled, and/or auto_recharge_spending_limit_usd. When enabling auto-recharge, missing values are calculated: if only limit set, amount = 20% of limit; if only amount set, limit = 5x amount; if neither set, defaults are limit=20, amount=4. Pass platform_key in the request body to update platform settings.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credit_account_auto_recharge_update import CreditAccountAutoRechargeUpdate
from iblai.models.credit_account_info import CreditAccountInfo
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
api_instance = iblai.AccountApi(api_client)
credit_account_auto_recharge_update = iblai.CreditAccountAutoRechargeUpdate() # CreditAccountAutoRechargeUpdate |  (optional)

try:
    # Update auto-recharge preferences
    api_response = api_instance.account_update(credit_account_auto_recharge_update=credit_account_auto_recharge_update)
    print("The response of AccountApi->account_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountApi->account_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_account_auto_recharge_update** | [**CreditAccountAutoRechargeUpdate**](CreditAccountAutoRechargeUpdate.md)|  | [optional] 

### Return type

[**CreditAccountInfo**](CreditAccountInfo.md)

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

