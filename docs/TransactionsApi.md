# iblai.TransactionsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_retrieve**](TransactionsApi.md#transactions_retrieve) | **GET** /transactions/ | List transaction history


# **transactions_retrieve**
> CreditTransactionHistory transactions_retrieve(from_date=from_date, platform_key=platform_key, to_date=to_date, transaction_type=transaction_type)

List transaction history

Paginated transaction history for the credit account. Use platform_key query param to list platform account transactions (if permitted). Filter by transaction_type, from_date (YYYY-MM-DD), to_date (YYYY-MM-DD).

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credit_transaction_history import CreditTransactionHistory
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
api_instance = iblai.TransactionsApi(api_client)
from_date = '2013-10-20' # date | Filter from date (YYYY-MM-DD), inclusive. (optional)
platform_key = 'platform_key_example' # str | Platform key. Omit for user's own account. (optional)
to_date = '2013-10-20' # date | Filter to date (YYYY-MM-DD), inclusive. (optional)
transaction_type = 'transaction_type_example' # str | Filter by transaction type.  * `add` - add * `subtract` - subtract * `reserve` - reserve * `release` - release * `rollover` - rollover * `refund` - refund (optional)

try:
    # List transaction history
    api_response = api_instance.transactions_retrieve(from_date=from_date, platform_key=platform_key, to_date=to_date, transaction_type=transaction_type)
    print("The response of TransactionsApi->transactions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling TransactionsApi->transactions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **date**| Filter from date (YYYY-MM-DD), inclusive. | [optional] 
 **platform_key** | **str**| Platform key. Omit for user&#39;s own account. | [optional] 
 **to_date** | **date**| Filter to date (YYYY-MM-DD), inclusive. | [optional] 
 **transaction_type** | **str**| Filter by transaction type.  * &#x60;add&#x60; - add * &#x60;subtract&#x60; - subtract * &#x60;reserve&#x60; - reserve * &#x60;release&#x60; - release * &#x60;rollover&#x60; - rollover * &#x60;refund&#x60; - refund | [optional] 

### Return type

[**CreditTransactionHistory**](CreditTransactionHistory.md)

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

