# iblai.CommerceApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_association_stripe_callback_retrieve**](CommerceApi.md#provider_association_stripe_callback_retrieve) | **GET** /api/provider-association/stripe/callback/{launch_id}/ | 
[**providers_apple_associate_account_create**](CommerceApi.md#providers_apple_associate_account_create) | **POST** /api/providers/apple/associate-account/ | 
[**providers_apple_hook_create**](CommerceApi.md#providers_apple_hook_create) | **POST** /api/providers/apple/hook/ | 
[**providers_apple_subscription_status_create**](CommerceApi.md#providers_apple_subscription_status_create) | **POST** /api/providers/apple/subscription-status/ | 
[**providers_apple_validate_transaction_id_create**](CommerceApi.md#providers_apple_validate_transaction_id_create) | **POST** /api/providers/apple/validate-transaction-id/ | 
[**providers_aws_create_organization_create**](CommerceApi.md#providers_aws_create_organization_create) | **POST** /api/providers/aws/create-organization/ | 
[**providers_aws_domain_status_retrieve**](CommerceApi.md#providers_aws_domain_status_retrieve) | **GET** /api/providers/aws/domain-status/ | 
[**providers_aws_launch_tenant_create**](CommerceApi.md#providers_aws_launch_tenant_create) | **POST** /api/providers/aws/launch-tenant/ | 
[**providers_aws_sync_domain_records_create**](CommerceApi.md#providers_aws_sync_domain_records_create) | **POST** /api/providers/aws/sync-domain-records/ | 
[**providers_aws_sync_domain_records_retrieve**](CommerceApi.md#providers_aws_sync_domain_records_retrieve) | **GET** /api/providers/aws/sync-domain-records/ | 
[**providers_gcp_create_organization_create**](CommerceApi.md#providers_gcp_create_organization_create) | **POST** /api/providers/gcp/create-organization/ | 
[**providers_gcp_create_organization_create2**](CommerceApi.md#providers_gcp_create_organization_create2) | **POST** /api/providers/gcp/create-organization/{product_id}/ | 
[**providers_gcp_hook_create**](CommerceApi.md#providers_gcp_hook_create) | **POST** /api/providers/gcp/hook/ | 
[**providers_gcp_launch_tenant_create**](CommerceApi.md#providers_gcp_launch_tenant_create) | **POST** /api/providers/gcp/launch-tenant/ | 
[**providers_gcp_validate_signup_token_create**](CommerceApi.md#providers_gcp_validate_signup_token_create) | **POST** /api/providers/gcp/validate-signup-token/ | 
[**providers_google_pay_get_account_retrieve**](CommerceApi.md#providers_google_pay_get_account_retrieve) | **GET** /api/providers/google-pay/get-account/{bundle_id} | 
[**providers_google_pay_hook_create**](CommerceApi.md#providers_google_pay_hook_create) | **POST** /api/providers/google-pay/hook/ | 
[**providers_google_pay_validate_transaction_id_create**](CommerceApi.md#providers_google_pay_validate_transaction_id_create) | **POST** /api/providers/google-pay/validate-transaction-id/ | 
[**providers_stripe_create_organization_create**](CommerceApi.md#providers_stripe_create_organization_create) | **POST** /api/providers/stripe/create-organization/ | 
[**provision_create**](CommerceApi.md#provision_create) | **POST** /api/provision/{config_name}/ | 
[**service_launch_tenant_create**](CommerceApi.md#service_launch_tenant_create) | **POST** /api/service/launch/tenant/ | 
[**service_manage_user_create**](CommerceApi.md#service_manage_user_create) | **POST** /api/service/manage/user/ | 
[**service_manage_user_role_create**](CommerceApi.md#service_manage_user_role_create) | **POST** /api/service/manage/user/role/ | 
[**service_orgs_stripe_course_payment_callback_retrieve**](CommerceApi.md#service_orgs_stripe_course_payment_callback_retrieve) | **GET** /api/service/orgs/{platform_key}/stripe/course-payment-callback/ | 
[**service_orgs_users_stripe_checkout_session_create**](CommerceApi.md#service_orgs_users_stripe_checkout_session_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/checkout-session/ | 
[**service_orgs_users_stripe_customer_portal_create**](CommerceApi.md#service_orgs_users_stripe_customer_portal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/customer-portal/ | 
[**service_orgs_users_stripe_products_manage_create**](CommerceApi.md#service_orgs_users_stripe_products_manage_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/products/manage/ | 
[**service_orgs_users_stripe_products_retrieve**](CommerceApi.md#service_orgs_users_stripe_products_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/products/ | 
[**service_orgs_users_stripe_subscription_renewal_create**](CommerceApi.md#service_orgs_users_stripe_subscription_renewal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/subscription-renewal/ | 
[**service_orgs_users_stripe_subscriptions_retrieve**](CommerceApi.md#service_orgs_users_stripe_subscriptions_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/subscriptions/ | 
[**service_platforms_stripe_context_retrieve**](CommerceApi.md#service_platforms_stripe_context_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/context/ | 
[**service_platforms_stripe_credit_topup_callback_retrieve**](CommerceApi.md#service_platforms_stripe_credit_topup_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/credit-topup-callback/{checkout_session_id}/ | 
[**service_platforms_stripe_pricing_page_callback_retrieve**](CommerceApi.md#service_platforms_stripe_pricing_page_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-callback/ | 
[**service_platforms_stripe_pricing_page_callback_retrieve2**](CommerceApi.md#service_platforms_stripe_pricing_page_callback_retrieve2) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-callback/{checkout_session_id}/ | 
[**service_platforms_stripe_pricing_page_session_retrieve**](CommerceApi.md#service_platforms_stripe_pricing_page_session_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-session/ | 
[**service_stripe_checkout_free_trial_create**](CommerceApi.md#service_stripe_checkout_free_trial_create) | **POST** /api/service/stripe/checkout/free-trial/ | 
[**service_stripe_checkout_retrieve**](CommerceApi.md#service_stripe_checkout_retrieve) | **GET** /api/service/stripe/checkout/{checkout_uuid}/ | 
[**service_stripe_new_user_checkout_create**](CommerceApi.md#service_stripe_new_user_checkout_create) | **POST** /api/service/stripe/new-user-checkout/ | 
[**service_tenant_validation_create**](CommerceApi.md#service_tenant_validation_create) | **POST** /api/service/tenant/validation/ | 
[**service_token_retrieve**](CommerceApi.md#service_token_retrieve) | **GET** /api/service/token/ | 
[**service_user_validation_create**](CommerceApi.md#service_user_validation_create) | **POST** /api/service/user/validation/ | 


# **provider_association_stripe_callback_retrieve**
> AiAccountOrgsUseDefaultLlmKeyCreate200Response provider_association_stripe_callback_retrieve(launch_id)

Handle callbacks from Stripe after successful checkout.

Updates:
- Platform launch state
- Association configuration status

### Example


```python
import iblai
from iblai.models.ai_account_orgs_use_default_llm_key_create200_response import AiAccountOrgsUseDefaultLlmKeyCreate200Response
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
launch_id = 'launch_id_example' # str | 

try:
    api_response = api_instance.provider_association_stripe_callback_retrieve(launch_id)
    print("The response of CommerceApi->provider_association_stripe_callback_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->provider_association_stripe_callback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launch_id** | **str**|  | 

### Return type

[**AiAccountOrgsUseDefaultLlmKeyCreate200Response**](AiAccountOrgsUseDefaultLlmKeyCreate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_apple_associate_account_create**
> AssociateAccountResponse providers_apple_associate_account_create(associate_apple_account)

Associate an Apple account with a user known user

### Example


```python
import iblai
from iblai.models.associate_account_response import AssociateAccountResponse
from iblai.models.associate_apple_account import AssociateAppleAccount
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
associate_apple_account = iblai.AssociateAppleAccount() # AssociateAppleAccount | 

try:
    api_response = api_instance.providers_apple_associate_account_create(associate_apple_account)
    print("The response of CommerceApi->providers_apple_associate_account_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_apple_associate_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associate_apple_account** | [**AssociateAppleAccount**](AssociateAppleAccount.md)|  | 

### Return type

[**AssociateAccountResponse**](AssociateAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_apple_hook_create**
> providers_apple_hook_create()

View to handle apple webhooks

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_apple_hook_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_apple_hook_create: %s\n" % e)
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

# **providers_apple_subscription_status_create**
> AppleSubscriptionStatusView providers_apple_subscription_status_create(apple_subscription_status_request=apple_subscription_status_request)

Returns information about a user subscription status

### Example


```python
import iblai
from iblai.models.apple_subscription_status_request import AppleSubscriptionStatusRequest
from iblai.models.apple_subscription_status_view import AppleSubscriptionStatusView
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
apple_subscription_status_request = iblai.AppleSubscriptionStatusRequest() # AppleSubscriptionStatusRequest |  (optional)

try:
    api_response = api_instance.providers_apple_subscription_status_create(apple_subscription_status_request=apple_subscription_status_request)
    print("The response of CommerceApi->providers_apple_subscription_status_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_apple_subscription_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_subscription_status_request** | [**AppleSubscriptionStatusRequest**](AppleSubscriptionStatusRequest.md)|  | [optional] 

### Return type

[**AppleSubscriptionStatusView**](AppleSubscriptionStatusView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_apple_validate_transaction_id_create**
> BaseResponse providers_apple_validate_transaction_id_create(apple_verify_transaction_id)

Checks if a provided transaction_id is valid

### Example


```python
import iblai
from iblai.models.apple_verify_transaction_id import AppleVerifyTransactionId
from iblai.models.base_response import BaseResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
apple_verify_transaction_id = iblai.AppleVerifyTransactionId() # AppleVerifyTransactionId | 

try:
    api_response = api_instance.providers_apple_validate_transaction_id_create(apple_verify_transaction_id)
    print("The response of CommerceApi->providers_apple_validate_transaction_id_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_apple_validate_transaction_id_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_verify_transaction_id** | [**AppleVerifyTransactionId**](AppleVerifyTransactionId.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_aws_create_organization_create**
> providers_aws_create_organization_create()

Serves a view that redirects to the AWS marketplace create organization page

Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the
URL of the AWS marketplace create organization page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_aws_create_organization_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_aws_create_organization_create: %s\n" % e)
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

# **providers_aws_domain_status_retrieve**
> providers_aws_domain_status_retrieve()

API endpoint to get domain setup status

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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_aws_domain_status_retrieve()
except Exception as e:
    print("Exception when calling CommerceApi->providers_aws_domain_status_retrieve: %s\n" % e)
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

# **providers_aws_launch_tenant_create**
> TenantLaunchResponse providers_aws_launch_tenant_create(aws_tenant_launch_request)

Proxy to the Platform launch API

We cannot expose launching a tenant to an authorized user hence the need for the API

The API validates the x_amzn_marketplace_token and then proxies the request to the Platform Launch API

### Example


```python
import iblai
from iblai.models.aws_tenant_launch_request import AWSTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
aws_tenant_launch_request = iblai.AWSTenantLaunchRequest() # AWSTenantLaunchRequest | 

try:
    api_response = api_instance.providers_aws_launch_tenant_create(aws_tenant_launch_request)
    print("The response of CommerceApi->providers_aws_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_aws_launch_tenant_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_tenant_launch_request** | [**AWSTenantLaunchRequest**](AWSTenantLaunchRequest.md)|  | 

### Return type

[**TenantLaunchResponse**](TenantLaunchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**417** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_aws_sync_domain_records_create**
> providers_aws_sync_domain_records_create()

API endpoint to get/update CNAME records for domain setup

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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_aws_sync_domain_records_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_aws_sync_domain_records_create: %s\n" % e)
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

# **providers_aws_sync_domain_records_retrieve**
> providers_aws_sync_domain_records_retrieve()

API endpoint to get/update CNAME records for domain setup

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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_aws_sync_domain_records_retrieve()
except Exception as e:
    print("Exception when calling CommerceApi->providers_aws_sync_domain_records_retrieve: %s\n" % e)
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

# **providers_gcp_create_organization_create**
> providers_gcp_create_organization_create()

Serves a view that redirects to the GCP marketplace create organization page

Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the URL of the GCP marketplace create organization
page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_gcp_create_organization_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_gcp_create_organization_create: %s\n" % e)
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

# **providers_gcp_create_organization_create2**
> providers_gcp_create_organization_create2(product_id)

Serves a view that redirects to the GCP marketplace create organization page

Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the URL of the GCP marketplace create organization
page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
product_id = 'product_id_example' # str | 

try:
    api_instance.providers_gcp_create_organization_create2(product_id)
except Exception as e:
    print("Exception when calling CommerceApi->providers_gcp_create_organization_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

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

# **providers_gcp_hook_create**
> providers_gcp_hook_create()

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_gcp_hook_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_gcp_hook_create: %s\n" % e)
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

# **providers_gcp_launch_tenant_create**
> TenantLaunchResponse providers_gcp_launch_tenant_create(gcp_tenant_launch_request)

Proxy to the Platform launch API

We cannot expose launching a tenant to an authorized user hence the need for the API

The API validates the x_gcp_marketplace_token and then proxies the request to the Platform Launc API

### Example


```python
import iblai
from iblai.models.gcp_tenant_launch_request import GCPTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
gcp_tenant_launch_request = iblai.GCPTenantLaunchRequest() # GCPTenantLaunchRequest | 

try:
    api_response = api_instance.providers_gcp_launch_tenant_create(gcp_tenant_launch_request)
    print("The response of CommerceApi->providers_gcp_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_gcp_launch_tenant_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_tenant_launch_request** | [**GCPTenantLaunchRequest**](GCPTenantLaunchRequest.md)|  | 

### Return type

[**TenantLaunchResponse**](TenantLaunchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**417** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_gcp_validate_signup_token_create**
> VerifyGCPMarketPlaceResponse providers_gcp_validate_signup_token_create(verify_gcp_market_place_request)

### Example


```python
import iblai
from iblai.models.verify_gcp_market_place_request import VerifyGCPMarketPlaceRequest
from iblai.models.verify_gcp_market_place_response import VerifyGCPMarketPlaceResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
verify_gcp_market_place_request = iblai.VerifyGCPMarketPlaceRequest() # VerifyGCPMarketPlaceRequest | 

try:
    api_response = api_instance.providers_gcp_validate_signup_token_create(verify_gcp_market_place_request)
    print("The response of CommerceApi->providers_gcp_validate_signup_token_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_gcp_validate_signup_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_gcp_market_place_request** | [**VerifyGCPMarketPlaceRequest**](VerifyGCPMarketPlaceRequest.md)|  | 

### Return type

[**VerifyGCPMarketPlaceResponse**](VerifyGCPMarketPlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_pay_get_account_retrieve**
> GooglePayAccountResponse providers_google_pay_get_account_retrieve(bundle_id)

Google Allows us to pass an obfuscated account id to be sent to during a subscription purchase

### Example


```python
import iblai
from iblai.models.google_pay_account_response import GooglePayAccountResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
bundle_id = 'bundle_id_example' # str | 

try:
    api_response = api_instance.providers_google_pay_get_account_retrieve(bundle_id)
    print("The response of CommerceApi->providers_google_pay_get_account_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_google_pay_get_account_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 

### Return type

[**GooglePayAccountResponse**](GooglePayAccountResponse.md)

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

# **providers_google_pay_hook_create**
> providers_google_pay_hook_create()

View to handle Google Pay webhooks

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.providers_google_pay_hook_create()
except Exception as e:
    print("Exception when calling CommerceApi->providers_google_pay_hook_create: %s\n" % e)
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

# **providers_google_pay_validate_transaction_id_create**
> BaseResponse providers_google_pay_validate_transaction_id_create(google_pay_verify_token)

Associate a Google Pay account with a known user

### Example


```python
import iblai
from iblai.models.base_response import BaseResponse
from iblai.models.google_pay_verify_token import GooglePayVerifyToken
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
google_pay_verify_token = iblai.GooglePayVerifyToken() # GooglePayVerifyToken | 

try:
    api_response = api_instance.providers_google_pay_validate_transaction_id_create(google_pay_verify_token)
    print("The response of CommerceApi->providers_google_pay_validate_transaction_id_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_google_pay_validate_transaction_id_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_pay_verify_token** | [**GooglePayVerifyToken**](GooglePayVerifyToken.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_stripe_create_organization_create**
> TenantLaunchResponse providers_stripe_create_organization_create(stripe_new_user_tenant_launch_request)

Proxy to the Platform launch API

We cannot expose launching a tenant to an unauthorized user hence the need for the API

The API validates the stripe_checkout_id and then proxies the request to the Platform Launch API

### Example


```python
import iblai
from iblai.models.stripe_new_user_tenant_launch_request import StripeNewUserTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
stripe_new_user_tenant_launch_request = iblai.StripeNewUserTenantLaunchRequest() # StripeNewUserTenantLaunchRequest | 

try:
    api_response = api_instance.providers_stripe_create_organization_create(stripe_new_user_tenant_launch_request)
    print("The response of CommerceApi->providers_stripe_create_organization_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->providers_stripe_create_organization_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_new_user_tenant_launch_request** | [**StripeNewUserTenantLaunchRequest**](StripeNewUserTenantLaunchRequest.md)|  | 

### Return type

[**TenantLaunchResponse**](TenantLaunchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**417** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_create**
> provision_create(config_name)

POST
Update platform provisioning config

request body:
{"config_name": "demo_config}

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
api_instance = iblai.CommerceApi(api_client)
config_name = 'config_name_example' # str | 

try:
    api_instance.provision_create(config_name)
except Exception as e:
    print("Exception when calling CommerceApi->provision_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_name** | **str**|  | 

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

# **service_launch_tenant_create**
> TenantLaunchResponse service_launch_tenant_create(tenant_launch_request)

User/tenant creation API

To create using any payment provider, ensure you use the StudentToken Authentication Mechanism
 and also include the correct `provider_key` in the request body:

```
    apple_transaction_id: str
    stripe_checkout_id: str
    x_gcp_marketplace_token: str
    aws_transaction_id: str
    google_pay_transaction_id: str
```

To create a tenant without a payment provider, call the API without ny of the above provider keys in the request body

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
api_instance = iblai.CommerceApi(api_client)
tenant_launch_request = iblai.TenantLaunchRequest() # TenantLaunchRequest | 

try:
    api_response = api_instance.service_launch_tenant_create(tenant_launch_request)
    print("The response of CommerceApi->service_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_launch_tenant_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.service_manage_user_create()
except Exception as e:
    print("Exception when calling CommerceApi->service_manage_user_create: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.service_manage_user_role_create()
except Exception as e:
    print("Exception when calling CommerceApi->service_manage_user_role_create: %s\n" % e)
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

Handle course payment callback after successful Stripe checkout.
Enrolls the user in the purchased course.

URL Parameters:
    - stripe_checkout_id: The local Checkout Session UUID

Response:
    - Redirect: Successfully processed course enrollment
    - 404: Checkout session not found
    - 400: Invalid checkout session or product
    - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_orgs_stripe_course_payment_callback_retrieve(platform_key)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_stripe_course_payment_callback_retrieve: %s\n" % e)
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

Stripe checkout session API View for user upgrade

Request the following fields:

- tenant
- sku
- mode
- success_url
- cancel_url

Response:
{
    "redirect_to": "https://checkout.stripe.com/xxx/xxxx/xxxx",
}

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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_checkout_session_request = iblai.StripeCheckoutSessionRequest() # StripeCheckoutSessionRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_checkout_session_create(org, user_id, stripe_checkout_session_request)
    print("The response of CommerceApi->service_orgs_users_stripe_checkout_session_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_checkout_session_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_customer_portal_request = iblai.StripeCustomerPortalRequest() # StripeCustomerPortalRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_customer_portal_create(org, user_id, stripe_customer_portal_request)
    print("The response of CommerceApi->service_orgs_users_stripe_customer_portal_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_customer_portal_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.service_orgs_users_stripe_products_manage_create(org, user_id)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_products_manage_create: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.service_orgs_users_stripe_products_retrieve(org, user_id)
    print("The response of CommerceApi->service_orgs_users_stripe_products_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_products_retrieve: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
stripe_subscription_renewal_request = iblai.StripeSubscriptionRenewalRequest() # StripeSubscriptionRenewalRequest | 

try:
    api_response = api_instance.service_orgs_users_stripe_subscription_renewal_create(org, user_id, stripe_subscription_renewal_request)
    print("The response of CommerceApi->service_orgs_users_stripe_subscription_renewal_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_subscription_renewal_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.CommerceApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.service_orgs_users_stripe_subscriptions_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling CommerceApi->service_orgs_users_stripe_subscriptions_retrieve: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.service_platforms_stripe_context_retrieve(platform_key)
    print("The response of CommerceApi->service_platforms_stripe_context_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_platforms_stripe_context_retrieve: %s\n" % e)
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

Handle  callback after successful Stripe checkout for credit top up.
Redirects user to another page, ensures user credit is updated accordingly.

URL Parameters:
    - stripe_checkout_id: The Checkout Session UUID

Response:
    - Redirect: Successfully validated and sending to next page
    - 404: Checkout session not found
    - 400: Invalid checkout session or product
    - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
checkout_session_id = 'checkout_session_id_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_platforms_stripe_credit_topup_callback_retrieve(checkout_session_id, platform_key)
except Exception as e:
    print("Exception when calling CommerceApi->service_platforms_stripe_credit_topup_callback_retrieve: %s\n" % e)
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
> service_platforms_stripe_pricing_page_callback_retrieve(platform_key)

Handle  callback after successful Stripe checkout.
Redirects user to another page, ensures user subscription is updated accordingly.

URL Parameters:
    - stripe_checkout_id: The local Checkout Session UUID

Response:
    - Redirect: Successfully validated and sending to next page
    - 404: Checkout session not found
    - 400: Invalid checkout session or product
    - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_platforms_stripe_pricing_page_callback_retrieve(platform_key)
except Exception as e:
    print("Exception when calling CommerceApi->service_platforms_stripe_pricing_page_callback_retrieve: %s\n" % e)
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

# **service_platforms_stripe_pricing_page_callback_retrieve2**
> service_platforms_stripe_pricing_page_callback_retrieve2(checkout_session_id, platform_key)

Handle  callback after successful Stripe checkout.
Redirects user to another page, ensures user subscription is updated accordingly.

URL Parameters:
    - stripe_checkout_id: The local Checkout Session UUID

Response:
    - Redirect: Successfully validated and sending to next page
    - 404: Checkout session not found
    - 400: Invalid checkout session or product
    - 500: Server error during processing

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
checkout_session_id = 'checkout_session_id_example' # str | 
platform_key = 'platform_key_example' # str | 

try:
    api_instance.service_platforms_stripe_pricing_page_callback_retrieve2(checkout_session_id, platform_key)
except Exception as e:
    print("Exception when calling CommerceApi->service_platforms_stripe_pricing_page_callback_retrieve2: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.service_platforms_stripe_pricing_page_session_retrieve(platform_key)
    print("The response of CommerceApi->service_platforms_stripe_pricing_page_session_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_platforms_stripe_pricing_page_session_retrieve: %s\n" % e)
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

Stripe free trial checkout session. No user auth

Request the following fields:

- success_url
- cancel_url
- product

Response:
{
    "redirect_to": "https://checkout.stripe.com/xxx/xxxx/xxxx",
}

### Example


```python
import iblai
from iblai.models.stripe_checkout_session_response import StripeCheckoutSessionResponse
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)
stripe_checkout_session_response = iblai.StripeCheckoutSessionResponse() # StripeCheckoutSessionResponse | 

try:
    api_response = api_instance.service_stripe_checkout_free_trial_create(stripe_checkout_session_response)
    print("The response of CommerceApi->service_stripe_checkout_free_trial_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_stripe_checkout_free_trial_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.CommerceApi(api_client)
checkout_uuid = 'checkout_uuid_example' # str | 

try:
    api_instance.service_stripe_checkout_retrieve(checkout_uuid)
except Exception as e:
    print("Exception when calling CommerceApi->service_stripe_checkout_retrieve: %s\n" % e)
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

# **service_stripe_new_user_checkout_create**
> StripeCheckoutSessionResponse service_stripe_new_user_checkout_create(stripe_checkout_session_request)

Stripe checkout session API View for new users (first-time subscription)

Request the following fields:

- user_id, username, or email (user identifier)
- tenant (tenant type to create after successful checkout)
- sku
- mode (choices: "subscription", "payment", "setup")
- success_url
- cancel_url
- period (optional): Billing period - "weekly", "monthly", or "yearly" (defaults to "monthly")
- skip_card (optional): Skip card collection for free plans
- is_free_trial (optional): Enable free trial mode

Response:
{
    "redirect_to": "https://checkout.stripe.com/xxx/xxxx/xxxx",
}

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
api_instance = iblai.CommerceApi(api_client)
stripe_checkout_session_request = iblai.StripeCheckoutSessionRequest() # StripeCheckoutSessionRequest | 

try:
    api_response = api_instance.service_stripe_new_user_checkout_create(stripe_checkout_session_request)
    print("The response of CommerceApi->service_stripe_new_user_checkout_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CommerceApi->service_stripe_new_user_checkout_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_checkout_session_request** | [**StripeCheckoutSessionRequest**](StripeCheckoutSessionRequest.md)|  | 

### Return type

[**StripeCheckoutSessionResponse**](StripeCheckoutSessionResponse.md)

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

# **service_tenant_validation_create**
> service_tenant_validation_create()

Check if tenant exists or not

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.service_tenant_validation_create()
except Exception as e:
    print("Exception when calling CommerceApi->service_tenant_validation_create: %s\n" % e)
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

GET
Gets site hash_key from
or
Gets site_id form hash_key

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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.service_token_retrieve()
except Exception as e:
    print("Exception when calling CommerceApi->service_token_retrieve: %s\n" % e)
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
api_instance = iblai.CommerceApi(api_client)

try:
    api_instance.service_user_validation_create()
except Exception as e:
    print("Exception when calling CommerceApi->service_user_validation_create: %s\n" % e)
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

