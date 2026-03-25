# iblai.PlatformsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platforms_items_access_check_retrieve**](PlatformsApi.md#platforms_items_access_check_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/access-check/ | 
[**platforms_items_checkout_callback_retrieve**](PlatformsApi.md#platforms_items_checkout_callback_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/ | Handle checkout callback
[**platforms_items_checkout_callback_retrieve2**](PlatformsApi.md#platforms_items_checkout_callback_retrieve2) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/{checkout_session_id}/ | Handle checkout callback
[**platforms_items_checkout_create**](PlatformsApi.md#platforms_items_checkout_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout/ | Create checkout session
[**platforms_items_checkout_guest_create**](PlatformsApi.md#platforms_items_checkout_guest_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-guest/ | Create guest checkout session
[**platforms_items_paywall_create**](PlatformsApi.md#platforms_items_paywall_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Create or update paywall configuration
[**platforms_items_paywall_destroy**](PlatformsApi.md#platforms_items_paywall_destroy) | **DELETE** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Disable paywall configuration
[**platforms_items_paywall_prices_create**](PlatformsApi.md#platforms_items_paywall_prices_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | Create a price
[**platforms_items_paywall_prices_destroy**](PlatformsApi.md#platforms_items_paywall_prices_destroy) | **DELETE** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Delete a price
[**platforms_items_paywall_prices_list**](PlatformsApi.md#platforms_items_paywall_prices_list) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | List prices
[**platforms_items_paywall_prices_retrieve**](PlatformsApi.md#platforms_items_paywall_prices_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Get price details
[**platforms_items_paywall_prices_update**](PlatformsApi.md#platforms_items_paywall_prices_update) | **PUT** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Update a price
[**platforms_items_paywall_retrieve**](PlatformsApi.md#platforms_items_paywall_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Get paywall configuration
[**platforms_items_paywall_update**](PlatformsApi.md#platforms_items_paywall_update) | **PUT** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Update paywall configuration
[**platforms_items_pricing_retrieve**](PlatformsApi.md#platforms_items_pricing_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/pricing/ | Get public pricing
[**platforms_items_subscribers_list**](PlatformsApi.md#platforms_items_subscribers_list) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/subscribers/ | List item subscribers
[**platforms_items_subscription_cancel_create**](PlatformsApi.md#platforms_items_subscription_cancel_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/subscription/cancel/ | Cancel subscription
[**platforms_items_subscription_retrieve**](PlatformsApi.md#platforms_items_subscription_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/subscription/ | Get user subscription
[**platforms_my_subscriptions_list**](PlatformsApi.md#platforms_my_subscriptions_list) | **GET** /platforms/{platform_key}/my-subscriptions/ | List user subscriptions
[**platforms_paywalls_list**](PlatformsApi.md#platforms_paywalls_list) | **GET** /platforms/{platform_key}/paywalls/ | List all platform paywall configurations
[**platforms_revenue_retrieve**](PlatformsApi.md#platforms_revenue_retrieve) | **GET** /platforms/{platform_key}/revenue/ | Platform sales summary
[**platforms_subscribers_list**](PlatformsApi.md#platforms_subscribers_list) | **GET** /platforms/{platform_key}/subscribers/ | List all platform subscribers


# **platforms_items_access_check_retrieve**
> ItemAccessCheckResponse platforms_items_access_check_retrieve(item_id, item_type, platform_key)

Check whether the authenticated user has payment access to an item on a scoped platform.

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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.platforms_items_access_check_retrieve(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_access_check_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_access_check_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

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

# **platforms_items_checkout_callback_retrieve**
> platforms_items_checkout_callback_retrieve(item_id, item_type, platform_key, return_url=return_url)

Handle checkout callback

Stripe redirects here after checkout. Processes the completed session and redirects to the return URL.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
return_url = 'return_url_example' # str |  (optional)

try:
    # Handle checkout callback
    api_instance.platforms_items_checkout_callback_retrieve(item_id, item_type, platform_key, return_url=return_url)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_checkout_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **return_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_checkout_callback_retrieve2**
> platforms_items_checkout_callback_retrieve2(checkout_session_id, item_id, item_type, platform_key, return_url=return_url)

Handle checkout callback

Stripe redirects here after checkout. Processes the completed session and redirects to the return URL.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.PlatformsApi(api_client)
checkout_session_id = 'checkout_session_id_example' # str | 
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
return_url = 'return_url_example' # str |  (optional)

try:
    # Handle checkout callback
    api_instance.platforms_items_checkout_callback_retrieve2(checkout_session_id, item_id, item_type, platform_key, return_url=return_url)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_checkout_callback_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **return_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_checkout_create**
> CheckoutSessionResponse platforms_items_checkout_create(item_id, item_type, platform_key, checkout_session_create)

Create checkout session

Create a Stripe checkout session for an authenticated user to purchase or subscribe to an item.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.checkout_session_create import CheckoutSessionCreate
from iblai.models.checkout_session_response import CheckoutSessionResponse
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
checkout_session_create = iblai.CheckoutSessionCreate() # CheckoutSessionCreate | 

try:
    # Create checkout session
    api_response = api_instance.platforms_items_checkout_create(item_id, item_type, platform_key, checkout_session_create)
    print("The response of PlatformsApi->platforms_items_checkout_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_checkout_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **checkout_session_create** | [**CheckoutSessionCreate**](CheckoutSessionCreate.md)|  | 

### Return type

[**CheckoutSessionResponse**](CheckoutSessionResponse.md)

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

# **platforms_items_checkout_guest_create**
> CheckoutSessionResponse platforms_items_checkout_guest_create(item_id, item_type, platform_key, checkout_session_create)

Create guest checkout session

Create a Stripe checkout session for a guest user (email required).

### Example


```python
import iblai
from iblai.models.checkout_session_create import CheckoutSessionCreate
from iblai.models.checkout_session_response import CheckoutSessionResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
checkout_session_create = iblai.CheckoutSessionCreate() # CheckoutSessionCreate | 

try:
    # Create guest checkout session
    api_response = api_instance.platforms_items_checkout_guest_create(item_id, item_type, platform_key, checkout_session_create)
    print("The response of PlatformsApi->platforms_items_checkout_guest_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_checkout_guest_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **checkout_session_create** | [**CheckoutSessionCreate**](CheckoutSessionCreate.md)|  | 

### Return type

[**CheckoutSessionResponse**](CheckoutSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_paywall_create**
> ItemPaywallConfig platforms_items_paywall_create(item_id, item_type, platform_key, item_paywall_config_create=item_paywall_config_create)

Create or update paywall configuration

Enable or configure the paywall for an item. Creates a Stripe product on first enable.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_paywall_config import ItemPaywallConfig
from iblai.models.item_paywall_config_create import ItemPaywallConfigCreate
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
item_paywall_config_create = iblai.ItemPaywallConfigCreate() # ItemPaywallConfigCreate |  (optional)

try:
    # Create or update paywall configuration
    api_response = api_instance.platforms_items_paywall_create(item_id, item_type, platform_key, item_paywall_config_create=item_paywall_config_create)
    print("The response of PlatformsApi->platforms_items_paywall_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **item_paywall_config_create** | [**ItemPaywallConfigCreate**](ItemPaywallConfigCreate.md)|  | [optional] 

### Return type

[**ItemPaywallConfig**](ItemPaywallConfig.md)

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

# **platforms_items_paywall_destroy**
> platforms_items_paywall_destroy(item_id, item_type, platform_key)

Disable paywall configuration

Disable the paywall for an item. Does not delete the configuration.

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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # Disable paywall configuration
    api_instance.platforms_items_paywall_destroy(item_id, item_type, platform_key)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_paywall_prices_create**
> ItemPrice platforms_items_paywall_prices_create(item_id, item_type, platform_key, item_price_create)

Create a price

Create a new price tier for an item. Requires paywall to be enabled and Stripe Connect account ready.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_price import ItemPrice
from iblai.models.item_price_create import ItemPriceCreate
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
item_price_create = iblai.ItemPriceCreate() # ItemPriceCreate | 

try:
    # Create a price
    api_response = api_instance.platforms_items_paywall_prices_create(item_id, item_type, platform_key, item_price_create)
    print("The response of PlatformsApi->platforms_items_paywall_prices_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_prices_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **item_price_create** | [**ItemPriceCreate**](ItemPriceCreate.md)|  | 

### Return type

[**ItemPrice**](ItemPrice.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_paywall_prices_destroy**
> platforms_items_paywall_prices_destroy(item_id, item_type, platform_key, price_id)

Delete a price

Soft-delete a price tier and deactivate the corresponding Stripe price.

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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
price_id = 'price_id_example' # str | 

try:
    # Delete a price
    api_instance.platforms_items_paywall_prices_destroy(item_id, item_type, platform_key, price_id)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_prices_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **price_id** | **str**|  | 

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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_paywall_prices_list**
> List[ItemPrice] platforms_items_paywall_prices_list(item_id, item_type, platform_key)

List prices

List active prices for an item's paywall configuration.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_price import ItemPrice
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # List prices
    api_response = api_instance.platforms_items_paywall_prices_list(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_paywall_prices_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_prices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

### Return type

[**List[ItemPrice]**](ItemPrice.md)

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

# **platforms_items_paywall_prices_retrieve**
> ItemPrice platforms_items_paywall_prices_retrieve(item_id, item_type, platform_key, price_id)

Get price details

Retrieve a specific price by ID.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_price import ItemPrice
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
price_id = 'price_id_example' # str | 

try:
    # Get price details
    api_response = api_instance.platforms_items_paywall_prices_retrieve(item_id, item_type, platform_key, price_id)
    print("The response of PlatformsApi->platforms_items_paywall_prices_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_prices_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **price_id** | **str**|  | 

### Return type

[**ItemPrice**](ItemPrice.md)

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

# **platforms_items_paywall_prices_update**
> ItemPrice platforms_items_paywall_prices_update(item_id, item_type, platform_key, price_id, item_price_create)

Update a price

Update a price tier. If pricing fields change and a Stripe price exists, a new Stripe price is created and the old one deactivated.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_price import ItemPrice
from iblai.models.item_price_create import ItemPriceCreate
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
price_id = 'price_id_example' # str | 
item_price_create = iblai.ItemPriceCreate() # ItemPriceCreate | 

try:
    # Update a price
    api_response = api_instance.platforms_items_paywall_prices_update(item_id, item_type, platform_key, price_id, item_price_create)
    print("The response of PlatformsApi->platforms_items_paywall_prices_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_prices_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **price_id** | **str**|  | 
 **item_price_create** | [**ItemPriceCreate**](ItemPriceCreate.md)|  | 

### Return type

[**ItemPrice**](ItemPrice.md)

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

# **platforms_items_paywall_retrieve**
> ItemPaywallConfig platforms_items_paywall_retrieve(item_id, item_type, platform_key)

Get paywall configuration

Retrieve the paywall configuration for an item. Returns default (disabled) config if none exists.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_paywall_config import ItemPaywallConfig
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # Get paywall configuration
    api_response = api_instance.platforms_items_paywall_retrieve(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_paywall_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

### Return type

[**ItemPaywallConfig**](ItemPaywallConfig.md)

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

# **platforms_items_paywall_update**
> ItemPaywallConfig platforms_items_paywall_update(item_id, item_type, platform_key, item_paywall_config_create=item_paywall_config_create)

Update paywall configuration

Same as POST. Update the paywall configuration for an item.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_paywall_config import ItemPaywallConfig
from iblai.models.item_paywall_config_create import ItemPaywallConfigCreate
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
item_paywall_config_create = iblai.ItemPaywallConfigCreate() # ItemPaywallConfigCreate |  (optional)

try:
    # Update paywall configuration
    api_response = api_instance.platforms_items_paywall_update(item_id, item_type, platform_key, item_paywall_config_create=item_paywall_config_create)
    print("The response of PlatformsApi->platforms_items_paywall_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_paywall_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **item_paywall_config_create** | [**ItemPaywallConfigCreate**](ItemPaywallConfigCreate.md)|  | [optional] 

### Return type

[**ItemPaywallConfig**](ItemPaywallConfig.md)

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

# **platforms_items_pricing_retrieve**
> PublicItemPricing platforms_items_pricing_retrieve(item_id, item_type, platform_key)

Get public pricing

Retrieve public pricing information for an item. No authentication required.

### Example


```python
import iblai
from iblai.models.public_item_pricing import PublicItemPricing
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # Get public pricing
    api_response = api_instance.platforms_items_pricing_retrieve(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_pricing_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_pricing_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

### Return type

[**PublicItemPricing**](PublicItemPricing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_subscribers_list**
> PaginatedItemSubscriptionList platforms_items_subscribers_list(item_id, item_type, platform_key, page=page, page_size=page_size, search=search, status=status)

List item subscribers

List all subscribers for an item. Optionally filter by subscription status.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_item_subscription_list import PaginatedItemSubscriptionList
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str |  (optional)
status = 'status_example' # str | * `active` - Active * `free` - Free Tier * `grandfathered` - Grandfathered * `trialing` - Trialing * `past_due` - Past Due * `canceled` - Canceled * `incomplete` - Incomplete (optional)

try:
    # List item subscribers
    api_response = api_instance.platforms_items_subscribers_list(item_id, item_type, platform_key, page=page, page_size=page_size, search=search, status=status)
    print("The response of PlatformsApi->platforms_items_subscribers_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_subscribers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**|  | [optional] 
 **status** | **str**| * &#x60;active&#x60; - Active * &#x60;free&#x60; - Free Tier * &#x60;grandfathered&#x60; - Grandfathered * &#x60;trialing&#x60; - Trialing * &#x60;past_due&#x60; - Past Due * &#x60;canceled&#x60; - Canceled * &#x60;incomplete&#x60; - Incomplete | [optional] 

### Return type

[**PaginatedItemSubscriptionList**](PaginatedItemSubscriptionList.md)

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

# **platforms_items_subscription_cancel_create**
> PortalUrlResponse platforms_items_subscription_cancel_create(item_id, item_type, platform_key)

Cancel subscription

Cancel the current user's subscription. Returns a Stripe customer portal URL for recurring subscriptions, or cancels directly for one-time purchases.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.portal_url_response import PortalUrlResponse
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # Cancel subscription
    api_response = api_instance.platforms_items_subscription_cancel_create(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_subscription_cancel_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_subscription_cancel_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

### Return type

[**PortalUrlResponse**](PortalUrlResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_items_subscription_retrieve**
> ItemSubscription platforms_items_subscription_retrieve(item_id, item_type, platform_key)

Get user subscription

Retrieve the current user's subscription to an item.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.item_subscription import ItemSubscription
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
api_instance = iblai.PlatformsApi(api_client)
item_id = 'item_id_example' # str | 
item_type = 'item_type_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    # Get user subscription
    api_response = api_instance.platforms_items_subscription_retrieve(item_id, item_type, platform_key)
    print("The response of PlatformsApi->platforms_items_subscription_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_items_subscription_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **item_type** | **str**|  | 
 **platform_key** | **str**|  | 

### Return type

[**ItemSubscription**](ItemSubscription.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_my_subscriptions_list**
> PaginatedItemSubscriptionListList platforms_my_subscriptions_list(platform_key, item_type=item_type, page=page, page_size=page_size, search=search, status=status)

List user subscriptions

Paginated list of the current user's subscriptions on a platform. Optionally filter by status or item_type.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_item_subscription_list_list import PaginatedItemSubscriptionListList
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
api_instance = iblai.PlatformsApi(api_client)
platform_key = 'platform_key_example' # str | 
item_type = 'item_type_example' # str | * `mentor` - mentor * `course` - course * `program` - program * `pathway` - pathway (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str |  (optional)
status = 'status_example' # str | * `active` - Active * `free` - Free Tier * `grandfathered` - Grandfathered * `trialing` - Trialing * `past_due` - Past Due * `canceled` - Canceled * `incomplete` - Incomplete (optional)

try:
    # List user subscriptions
    api_response = api_instance.platforms_my_subscriptions_list(platform_key, item_type=item_type, page=page, page_size=page_size, search=search, status=status)
    print("The response of PlatformsApi->platforms_my_subscriptions_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_my_subscriptions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **item_type** | **str**| * &#x60;mentor&#x60; - mentor * &#x60;course&#x60; - course * &#x60;program&#x60; - program * &#x60;pathway&#x60; - pathway | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**|  | [optional] 
 **status** | **str**| * &#x60;active&#x60; - Active * &#x60;free&#x60; - Free Tier * &#x60;grandfathered&#x60; - Grandfathered * &#x60;trialing&#x60; - Trialing * &#x60;past_due&#x60; - Past Due * &#x60;canceled&#x60; - Canceled * &#x60;incomplete&#x60; - Incomplete | [optional] 

### Return type

[**PaginatedItemSubscriptionListList**](PaginatedItemSubscriptionListList.md)

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

# **platforms_paywalls_list**
> PaginatedItemPaywallConfigList platforms_paywalls_list(platform_key, is_enabled=is_enabled, item_type=item_type, page=page, page_size=page_size, search=search)

List all platform paywall configurations

Paginated list of all item paywall configurations on a platform. Filterable by item_type and is_enabled.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_item_paywall_config_list import PaginatedItemPaywallConfigList
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
api_instance = iblai.PlatformsApi(api_client)
platform_key = 'platform_key_example' # str | 
is_enabled = True # bool |  (optional)
item_type = 'item_type_example' # str | * `mentor` - mentor * `course` - course * `program` - program * `pathway` - pathway (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str |  (optional)

try:
    # List all platform paywall configurations
    api_response = api_instance.platforms_paywalls_list(platform_key, is_enabled=is_enabled, item_type=item_type, page=page, page_size=page_size, search=search)
    print("The response of PlatformsApi->platforms_paywalls_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_paywalls_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **is_enabled** | **bool**|  | [optional] 
 **item_type** | **str**| * &#x60;mentor&#x60; - mentor * &#x60;course&#x60; - course * &#x60;program&#x60; - program * &#x60;pathway&#x60; - pathway | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**PaginatedItemPaywallConfigList**](PaginatedItemPaywallConfigList.md)

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

# **platforms_revenue_retrieve**
> PlatformRevenueSummary platforms_revenue_retrieve(platform_key)

Platform sales summary

Aggregate sales volume and count for a platform across all item types.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_revenue_summary import PlatformRevenueSummary
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
api_instance = iblai.PlatformsApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    # Platform sales summary
    api_response = api_instance.platforms_revenue_retrieve(platform_key)
    print("The response of PlatformsApi->platforms_revenue_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_revenue_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**PlatformRevenueSummary**](PlatformRevenueSummary.md)

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

# **platforms_subscribers_list**
> PaginatedItemSubscriptionListList platforms_subscribers_list(platform_key, item_type=item_type, page=page, page_size=page_size, search=search, status=status)

List all platform subscribers

Paginated list of all subscribers across all items on a platform. Filterable by status and item_type.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_item_subscription_list_list import PaginatedItemSubscriptionListList
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
api_instance = iblai.PlatformsApi(api_client)
platform_key = 'platform_key_example' # str | 
item_type = 'item_type_example' # str | * `mentor` - mentor * `course` - course * `program` - program * `pathway` - pathway (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str |  (optional)
status = 'status_example' # str | * `active` - Active * `free` - Free Tier * `grandfathered` - Grandfathered * `trialing` - Trialing * `past_due` - Past Due * `canceled` - Canceled * `incomplete` - Incomplete (optional)

try:
    # List all platform subscribers
    api_response = api_instance.platforms_subscribers_list(platform_key, item_type=item_type, page=page, page_size=page_size, search=search, status=status)
    print("The response of PlatformsApi->platforms_subscribers_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling PlatformsApi->platforms_subscribers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **item_type** | **str**| * &#x60;mentor&#x60; - mentor * &#x60;course&#x60; - course * &#x60;program&#x60; - program * &#x60;pathway&#x60; - pathway | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**|  | [optional] 
 **status** | **str**| * &#x60;active&#x60; - Active * &#x60;free&#x60; - Free Tier * &#x60;grandfathered&#x60; - Grandfathered * &#x60;trialing&#x60; - Trialing * &#x60;past_due&#x60; - Past Due * &#x60;canceled&#x60; - Canceled * &#x60;incomplete&#x60; - Incomplete | [optional] 

### Return type

[**PaginatedItemSubscriptionListList**](PaginatedItemSubscriptionListList.md)

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

