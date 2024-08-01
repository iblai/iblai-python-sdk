# iblai.FinanceApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finance_orgs_products_orders_retrieve**](FinanceApi.md#finance_orgs_products_orders_retrieve) | **GET** /api/finance/orgs/{org}/products/{item_id}/orders | 
[**finance_orgs_products_retrieve**](FinanceApi.md#finance_orgs_products_retrieve) | **GET** /api/finance/orgs/{org}/products | 
[**finance_orgs_products_sales_over_time_retrieve**](FinanceApi.md#finance_orgs_products_sales_over_time_retrieve) | **GET** /api/finance/orgs/{org}/products/{item_id}/sales-over-time | 
[**finance_orgs_revenue_net_over_time_retrieve**](FinanceApi.md#finance_orgs_revenue_net_over_time_retrieve) | **GET** /api/finance/orgs/{org}/revenue/net-over-time | 
[**finance_orgs_revenue_products_retrieve**](FinanceApi.md#finance_orgs_revenue_products_retrieve) | **GET** /api/finance/orgs/{org}/revenue/products | 


# **finance_orgs_products_orders_retrieve**
> Order finance_orgs_products_orders_retrieve(item_id, org, end_date=end_date, start_date=start_date)



Return list of WooCommerce orders for product item_id over optional date range

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.order import Order
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
api_instance = iblai.FinanceApi(api_client)
item_id = 'item_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)
start_date = 'start_date_example' # str | Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)

try:
    api_response = api_instance.finance_orgs_products_orders_retrieve(item_id, org, end_date=end_date, start_date=start_date)
    print("The response of FinanceApi->finance_orgs_products_orders_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FinanceApi->finance_orgs_products_orders_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 
 **start_date** | **str**| Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 

### Return type

[**Order**](Order.md)

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

# **finance_orgs_products_retrieve**
> Product finance_orgs_products_retrieve(org)



Returns table listing products and product info for all or specific org

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.product import Product
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
api_instance = iblai.FinanceApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.finance_orgs_products_retrieve(org)
    print("The response of FinanceApi->finance_orgs_products_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FinanceApi->finance_orgs_products_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**Product**](Product.md)

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

# **finance_orgs_products_sales_over_time_retrieve**
> NetRevenueOverTime finance_orgs_products_sales_over_time_retrieve(item_id, org, end_date=end_date, start_date=start_date)



Returns Net Revenue over time for org and slug

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.net_revenue_over_time import NetRevenueOverTime
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
api_instance = iblai.FinanceApi(api_client)
item_id = 'item_id_example' # str | 
org = 'org_example' # str | 
end_date = 'end_date_example' # str | End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)
start_date = 'start_date_example' # str | Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)

try:
    api_response = api_instance.finance_orgs_products_sales_over_time_retrieve(item_id, org, end_date=end_date, start_date=start_date)
    print("The response of FinanceApi->finance_orgs_products_sales_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FinanceApi->finance_orgs_products_sales_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **org** | **str**|  | 
 **end_date** | **str**| End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 
 **start_date** | **str**| Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 

### Return type

[**NetRevenueOverTime**](NetRevenueOverTime.md)

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

# **finance_orgs_revenue_net_over_time_retrieve**
> NetRevenueOverTime finance_orgs_revenue_net_over_time_retrieve(org, end_date=end_date, start_date=start_date)



Returns Net Revenue over time for org and slug

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.net_revenue_over_time import NetRevenueOverTime
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
api_instance = iblai.FinanceApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)
start_date = 'start_date_example' # str | Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)

try:
    api_response = api_instance.finance_orgs_revenue_net_over_time_retrieve(org, end_date=end_date, start_date=start_date)
    print("The response of FinanceApi->finance_orgs_revenue_net_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FinanceApi->finance_orgs_revenue_net_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 
 **start_date** | **str**| Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 

### Return type

[**NetRevenueOverTime**](NetRevenueOverTime.md)

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

# **finance_orgs_revenue_products_retrieve**
> RevenueByProduct finance_orgs_revenue_products_retrieve(org, end_date=end_date, start_date=start_date)



Returns Revenue by Product + summary for specific org

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.revenue_by_product import RevenueByProduct
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
api_instance = iblai.FinanceApi(api_client)
org = 'org_example' # str | 
end_date = 'end_date_example' # str | End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)
start_date = 'start_date_example' # str | Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. (optional)

try:
    api_response = api_instance.finance_orgs_revenue_products_retrieve(org, end_date=end_date, start_date=start_date)
    print("The response of FinanceApi->finance_orgs_revenue_products_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FinanceApi->finance_orgs_revenue_products_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **end_date** | **str**| End of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 
 **start_date** | **str**| Start of date range, not-inclusive. ISO8601 Date or DateTime. Dates will have 00:00:00 set as the time. | [optional] 

### Return type

[**RevenueByProduct**](RevenueByProduct.md)

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

