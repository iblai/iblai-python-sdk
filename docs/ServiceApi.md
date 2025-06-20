# iblai.ServiceApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_launch_tenant_create**](ServiceApi.md#service_launch_tenant_create) | **POST** /api/service/launch/tenant/ | 
[**service_manage_user_create**](ServiceApi.md#service_manage_user_create) | **POST** /api/service/manage/user/ | 
[**service_manage_user_role_create**](ServiceApi.md#service_manage_user_role_create) | **POST** /api/service/manage/user/role/ | 
[**service_orgs_stripe_course_payment_callback_retrieve**](ServiceApi.md#service_orgs_stripe_course_payment_callback_retrieve) | **GET** /api/service/orgs/{platform_key}/stripe/course-payment-callback/ | 
[**service_orgs_users_stripe_checkout_session_create**](ServiceApi.md#service_orgs_users_stripe_checkout_session_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/checkout-session/ | 
[**service_orgs_users_stripe_customer_portal_create**](ServiceApi.md#service_orgs_users_stripe_customer_portal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/customer-portal/ | 
[**service_orgs_users_stripe_products_manage_create**](ServiceApi.md#service_orgs_users_stripe_products_manage_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/products/manage/ | 
[**service_orgs_users_stripe_products_retrieve**](ServiceApi.md#service_orgs_users_stripe_products_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/products/ | 
[**service_orgs_users_stripe_subscription_renewal_create**](ServiceApi.md#service_orgs_users_stripe_subscription_renewal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/subscription-renewal/ | 
[**service_orgs_users_stripe_subscriptions_retrieve**](ServiceApi.md#service_orgs_users_stripe_subscriptions_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/subscriptions/ | 
[**service_platforms_stripe_context_retrieve**](ServiceApi.md#service_platforms_stripe_context_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/context/ | 
[**service_platforms_stripe_credit_topup_callback_retrieve**](ServiceApi.md#service_platforms_stripe_credit_topup_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/credit-topup-callback/{checkout_session_id}/ | 
[**service_platforms_stripe_pricing_page_callback_retrieve**](ServiceApi.md#service_platforms_stripe_pricing_page_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-callback/{checkout_session_id}/ | 
[**service_platforms_stripe_pricing_page_session_retrieve**](ServiceApi.md#service_platforms_stripe_pricing_page_session_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-session/ | 
[**service_stripe_checkout_free_trial_create**](ServiceApi.md#service_stripe_checkout_free_trial_create) | **POST** /api/service/stripe/checkout/free-trial/ | 
[**service_stripe_checkout_retrieve**](ServiceApi.md#service_stripe_checkout_retrieve) | **GET** /api/service/stripe/checkout/{checkout_uuid}/ | 
[**service_tenant_validation_create**](ServiceApi.md#service_tenant_validation_create) | **POST** /api/service/tenant/validation/ | 
[**service_token_retrieve**](ServiceApi.md#service_token_retrieve) | **GET** /api/service/token/ | 
[**service_user_validation_create**](ServiceApi.md#service_user_validation_create) | **POST** /api/service/user/validation/ | 


# **service_launch_tenant_create**
> TenantLaunchResponse service_launch_tenant_create(tenant_launch_request)



User/tenant creation API  To create using any payment provider, ensure you use the StudentToken Authentication Mechanism  and also include the correct `provider_key` in the request body:  ```     apple_transaction_id: str     stripe_checkout_id: str     x_gcp_marketplace_token: str     aws_transaction_id: str     google_pay_transaction_id: str ```  To create a tenant without a payment provider, call the API without ny of the above provider keys in the request body

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tenant_launch_request import TenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
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
api_instance = iblai.ServiceApi(api_client)
tenant_launch_request = iblai.TenantLaunchRequest() # TenantLaunchRequest | 

try:
    api_response = api_instance.service_launch_tenant_create(tenant_launch_request)
    print("The response of ServiceApi->service_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_launch_tenant_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_launch_request** | [**TenantLaunchRequest**](TenantLaunchRequest.md)|  | 

### Return type

[**TenantLaunchResponse**](TenantLaunchResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**417** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_manage_user_create**
> service_manage_user_create()



User creation flow

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
api_instance = iblai.ServiceApi(api_client)

try:
    api_instance.service_manage_user_create()
except Exception as e:
    print("Exception when calling ServiceApi->service_manage_user_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **service_manage_user_role_create**
> service_manage_user_role_create()



Make user tenant admin

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
api_instance = iblai.ServiceApi(api_client)

try:
    api_instance.service_manage_user_role_create()
except Exception as e:
    print("Exception when calling ServiceApi->service_manage_user_role_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **service_orgs_stripe_course_payment_callback_retrieve**
> service_orgs_stripe_course_payment_callback_retrieve(platform_key)



Handle course payment callback after successful Stripe checkout. Enrolls the user in the purchased course.  URL Parameters:     - stripe_checkout_id: The local Checkout Session UUID  Response:     - Redirect: Successfully processed course enrollment     - 404: Checkout session not found     - 400: Invalid checkout session or product     - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ServiceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_orgs_stripe_course_payment_callback_retrieve(platform_key)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_stripe_course_payment_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orgs_users_stripe_checkout_session_create**
> StripeCheckoutSessionResponse service_orgs_users_stripe_checkout_session_create(org, user_id, stripe_checkout_session_request)



Stripe checkout session API View for user upgrade  Request the following fields:  - tenant - sku - mode - success_url - cancel_url  Response: {     \"redirect_to\": \"https://checkout.stripe.com/xxx/xxxx/xxxx\", }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_checkout_session_request import StripeCheckoutSessionRequest
from iblai.models.stripe_checkout_session_response import StripeCheckoutSessionResponse
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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_checkout_session_request = iblai.StripeCheckoutSessionRequest() # StripeCheckoutSessionRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_checkout_session_create(org, user_id, stripe_checkout_session_request)
    print("The response of ServiceApi->service_orgs_users_stripe_checkout_session_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_checkout_session_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **stripe_checkout_session_request** | [**StripeCheckoutSessionRequest**](StripeCheckoutSessionRequest.md)|  | 

### Return type

[**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)

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

# **service_orgs_users_stripe_customer_portal_create**
> StripeCustomerPortalResponse service_orgs_users_stripe_customer_portal_create(org, user_id, stripe_customer_portal_request)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_customer_portal_request import StripeCustomerPortalRequest
from iblai.models.stripe_customer_portal_response import StripeCustomerPortalResponse
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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_customer_portal_request = iblai.StripeCustomerPortalRequest() # StripeCustomerPortalRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_customer_portal_create(org, user_id, stripe_customer_portal_request)
    print("The response of ServiceApi->service_orgs_users_stripe_customer_portal_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_customer_portal_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **stripe_customer_portal_request** | [**StripeCustomerPortalRequest**](StripeCustomerPortalRequest.md)|  | 

### Return type

[**StripeCustomerPortalResponse**](StripeCustomerPortalResponse.md)

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

# **service_orgs_users_stripe_products_manage_create**
> service_orgs_users_stripe_products_manage_create(org, user_id)



Mixin that includes the StudentTokenAuthentication and IsPlatformAdmin

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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.service_orgs_users_stripe_products_manage_create(org, user_id)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_products_manage_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

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

# **service_orgs_users_stripe_products_retrieve**
> StripeLocalProduct service_orgs_users_stripe_products_retrieve(org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_local_product import StripeLocalProduct
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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.service_orgs_users_stripe_products_retrieve(org, user_id)
    print("The response of ServiceApi->service_orgs_users_stripe_products_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_products_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**StripeLocalProduct**](StripeLocalProduct.md)

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

# **service_orgs_users_stripe_subscription_renewal_create**
> StripeSubscriptionRenewalResponse service_orgs_users_stripe_subscription_renewal_create(org, user_id, stripe_subscription_renewal_request)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_subscription_renewal_request import StripeSubscriptionRenewalRequest
from iblai.models.stripe_subscription_renewal_response import StripeSubscriptionRenewalResponse
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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_subscription_renewal_request = iblai.StripeSubscriptionRenewalRequest() # StripeSubscriptionRenewalRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_subscription_renewal_create(org, user_id, stripe_subscription_renewal_request)
    print("The response of ServiceApi->service_orgs_users_stripe_subscription_renewal_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_subscription_renewal_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **stripe_subscription_renewal_request** | [**StripeSubscriptionRenewalRequest**](StripeSubscriptionRenewalRequest.md)|  | 

### Return type

[**StripeSubscriptionRenewalResponse**](StripeSubscriptionRenewalResponse.md)

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

# **service_orgs_users_stripe_subscriptions_retrieve**
> service_orgs_users_stripe_subscriptions_retrieve(org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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
api_instance = iblai.ServiceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.service_orgs_users_stripe_subscriptions_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling ServiceApi->service_orgs_users_stripe_subscriptions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

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

# **service_platforms_stripe_context_retrieve**
> StripeContext service_platforms_stripe_context_retrieve(platform_key)



Create a uuid to help us track internally user initiated checkout

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_context import StripeContext
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
api_instance = iblai.ServiceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.service_platforms_stripe_context_retrieve(platform_key)
    print("The response of ServiceApi->service_platforms_stripe_context_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_platforms_stripe_context_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**StripeContext**](StripeContext.md)

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

# **service_platforms_stripe_credit_topup_callback_retrieve**
> service_platforms_stripe_credit_topup_callback_retrieve(checkout_session_id, platform_key)



Handle  callback after successful Stripe checkout for credit top up. Redirects user to another page, ensures user credit is updated accordingly.  URL Parameters:     - stripe_checkout_id: The Checkout Session UUID  Response:     - Redirect: Successfully validated and sending to next page     - 404: Checkout session not found     - 400: Invalid checkout session or product     - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ServiceApi(api_client)
checkout_session_id = 'checkout_session_id_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_platforms_stripe_credit_topup_callback_retrieve(checkout_session_id, platform_key)
except Exception as e:
    print("Exception when calling ServiceApi->service_platforms_stripe_credit_topup_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 
 **platform_key** | **str**|  | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_platforms_stripe_pricing_page_callback_retrieve**
> service_platforms_stripe_pricing_page_callback_retrieve(checkout_session_id, platform_key)



Handle  callback after successful Stripe checkout. Redirects user to another page, ensures user subscription is updated accordingly.  URL Parameters:     - stripe_checkout_id: The local Checkout Session UUID  Response:     - Redirect: Successfully validated and sending to next page     - 404: Checkout session not found     - 400: Invalid checkout session or product     - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ServiceApi(api_client)
checkout_session_id = 'checkout_session_id_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_platforms_stripe_pricing_page_callback_retrieve(checkout_session_id, platform_key)
except Exception as e:
    print("Exception when calling ServiceApi->service_platforms_stripe_pricing_page_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 
 **platform_key** | **str**|  | 

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_platforms_stripe_pricing_page_session_retrieve**
> StripeBillingPageIdentifierResponse service_platforms_stripe_pricing_page_session_retrieve(platform_key)



Create a uuid to help us track internally user initiated checkout

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.stripe_billing_page_identifier_response import StripeBillingPageIdentifierResponse
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
api_instance = iblai.ServiceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.service_platforms_stripe_pricing_page_session_retrieve(platform_key)
    print("The response of ServiceApi->service_platforms_stripe_pricing_page_session_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_platforms_stripe_pricing_page_session_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**StripeBillingPageIdentifierResponse**](StripeBillingPageIdentifierResponse.md)

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

# **service_stripe_checkout_free_trial_create**
> StripeCheckoutSessionResponse service_stripe_checkout_free_trial_create(stripe_checkout_session_response)



Stripe free trial checkout session. No user auth  Request the following fields:  - success_url - cancel_url - product  Response: {     \"redirect_to\": \"https://checkout.stripe.com/xxx/xxxx/xxxx\", }

### Example


```python
import iblai
from iblai.models.stripe_checkout_session_response import StripeCheckoutSessionResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ServiceApi(api_client)
stripe_checkout_session_response = iblai.StripeCheckoutSessionResponse() # StripeCheckoutSessionResponse | 

try:
    api_response = api_instance.service_stripe_checkout_free_trial_create(stripe_checkout_session_response)
    print("The response of ServiceApi->service_stripe_checkout_free_trial_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceApi->service_stripe_checkout_free_trial_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_checkout_session_response** | [**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)|  | 

### Return type

[**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_stripe_checkout_retrieve**
> service_stripe_checkout_retrieve(checkout_uuid)



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
api_instance = iblai.ServiceApi(api_client)
checkout_uuid = 'checkout_uuid_example' # str | 

try:
    api_instance.service_stripe_checkout_retrieve(checkout_uuid)
except Exception as e:
    print("Exception when calling ServiceApi->service_stripe_checkout_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_uuid** | **str**|  | 

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

# **service_tenant_validation_create**
> service_tenant_validation_create()



Check if tenant exists or not

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ServiceApi(api_client)

try:
    api_instance.service_tenant_validation_create()
except Exception as e:
    print("Exception when calling ServiceApi->service_tenant_validation_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_token_retrieve**
> service_token_retrieve()



GET Gets site hash_key from or Gets site_id form hash_key

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
api_instance = iblai.ServiceApi(api_client)

try:
    api_instance.service_token_retrieve()
except Exception as e:
    print("Exception when calling ServiceApi->service_token_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **service_user_validation_create**
> service_user_validation_create()



Check if tenant exists or not

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
api_instance = iblai.ServiceApi(api_client)

try:
    api_instance.service_user_validation_create()
except Exception as e:
    print("Exception when calling ServiceApi->service_user_validation_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

