# iblai.ProvidersApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_apple_associate_account_create**](ProvidersApi.md#providers_apple_associate_account_create) | **POST** /api/providers/apple/associate-account/ | 
[**providers_apple_hook_create**](ProvidersApi.md#providers_apple_hook_create) | **POST** /api/providers/apple/hook/ | 
[**providers_apple_subscription_status_create**](ProvidersApi.md#providers_apple_subscription_status_create) | **POST** /api/providers/apple/subscription-status/ | 
[**providers_apple_validate_transaction_id_create**](ProvidersApi.md#providers_apple_validate_transaction_id_create) | **POST** /api/providers/apple/validate-transaction-id/ | 
[**providers_aws_create_organization_create**](ProvidersApi.md#providers_aws_create_organization_create) | **POST** /api/providers/aws/create-organization/ | 
[**providers_aws_domain_status_retrieve**](ProvidersApi.md#providers_aws_domain_status_retrieve) | **GET** /api/providers/aws/domain-status/ | 
[**providers_aws_launch_tenant_create**](ProvidersApi.md#providers_aws_launch_tenant_create) | **POST** /api/providers/aws/launch-tenant/ | 
[**providers_aws_sync_domain_records_create**](ProvidersApi.md#providers_aws_sync_domain_records_create) | **POST** /api/providers/aws/sync-domain-records/ | 
[**providers_aws_sync_domain_records_retrieve**](ProvidersApi.md#providers_aws_sync_domain_records_retrieve) | **GET** /api/providers/aws/sync-domain-records/ | 
[**providers_gcp_create_organization_create**](ProvidersApi.md#providers_gcp_create_organization_create) | **POST** /api/providers/gcp/create-organization/ | 
[**providers_gcp_create_organization_create2**](ProvidersApi.md#providers_gcp_create_organization_create2) | **POST** /api/providers/gcp/create-organization/{product_id}/ | 
[**providers_gcp_hook_create**](ProvidersApi.md#providers_gcp_hook_create) | **POST** /api/providers/gcp/hook/ | 
[**providers_gcp_launch_tenant_create**](ProvidersApi.md#providers_gcp_launch_tenant_create) | **POST** /api/providers/gcp/launch-tenant/ | 
[**providers_gcp_validate_signup_token_create**](ProvidersApi.md#providers_gcp_validate_signup_token_create) | **POST** /api/providers/gcp/validate-signup-token/ | 
[**providers_google_pay_get_account_retrieve**](ProvidersApi.md#providers_google_pay_get_account_retrieve) | **GET** /api/providers/google-pay/get-account/{bundle_id} | 
[**providers_google_pay_hook_create**](ProvidersApi.md#providers_google_pay_hook_create) | **POST** /api/providers/google-pay/hook/ | 
[**providers_google_pay_validate_transaction_id_create**](ProvidersApi.md#providers_google_pay_validate_transaction_id_create) | **POST** /api/providers/google-pay/validate-transaction-id/ | 
[**providers_stripe_create_organization_create**](ProvidersApi.md#providers_stripe_create_organization_create) | **POST** /api/providers/stripe/create-organization/ | 


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
api_instance = iblai.ProvidersApi(api_client)
associate_apple_account = iblai.AssociateAppleAccount() # AssociateAppleAccount | 

try:
    api_response = api_instance.providers_apple_associate_account_create(associate_apple_account)
    print("The response of ProvidersApi->providers_apple_associate_account_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_apple_associate_account_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_apple_hook_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_apple_hook_create: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)
apple_subscription_status_request = iblai.AppleSubscriptionStatusRequest() # AppleSubscriptionStatusRequest |  (optional)

try:
    api_response = api_instance.providers_apple_subscription_status_create(apple_subscription_status_request=apple_subscription_status_request)
    print("The response of ProvidersApi->providers_apple_subscription_status_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_apple_subscription_status_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.ProvidersApi(api_client)
apple_verify_transaction_id = iblai.AppleVerifyTransactionId() # AppleVerifyTransactionId | 

try:
    api_response = api_instance.providers_apple_validate_transaction_id_create(apple_verify_transaction_id)
    print("The response of ProvidersApi->providers_apple_validate_transaction_id_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_apple_validate_transaction_id_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_aws_create_organization_create**
> providers_aws_create_organization_create()



Serves a view that redirects to the AWS marketplace create organization page  Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the URL of the AWS marketplace create organization page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_aws_create_organization_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_aws_create_organization_create: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_aws_domain_status_retrieve()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_aws_domain_status_retrieve: %s\n" % e)
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



Proxy to the Platform launch API  We cannot expose launching a tenant to an authorized user hence the need for the API  The API validates the x_amzn_marketplace_token and then proxies the request to the Platform Launch API

### Example


```python
import iblai
from iblai.models.aws_tenant_launch_request import AWSTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)
aws_tenant_launch_request = iblai.AWSTenantLaunchRequest() # AWSTenantLaunchRequest | 

try:
    api_response = api_instance.providers_aws_launch_tenant_create(aws_tenant_launch_request)
    print("The response of ProvidersApi->providers_aws_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_aws_launch_tenant_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_aws_sync_domain_records_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_aws_sync_domain_records_create: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_aws_sync_domain_records_retrieve()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_aws_sync_domain_records_retrieve: %s\n" % e)
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



Serves a view that redirects to the GCP marketplace create organization page  Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the URL of the GCP marketplace create organization page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_gcp_create_organization_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_gcp_create_organization_create: %s\n" % e)
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



Serves a view that redirects to the GCP marketplace create organization page  Set CREATE_ORGANIZATION_URL in GlobalConfigurationFetcher to the URL of the GCP marketplace create organization page

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)
product_id = 'product_id_example' # str | 

try:
    api_instance.providers_gcp_create_organization_create2(product_id)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_gcp_create_organization_create2: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_gcp_hook_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_gcp_hook_create: %s\n" % e)
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



Proxy to the Platform launch API  We cannot expose launching a tenant to an authorized user hence the need for the API  The API validates the x_gcp_marketplace_token and then proxies the request to the Platform Launc API

### Example


```python
import iblai
from iblai.models.gcp_tenant_launch_request import GCPTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)
gcp_tenant_launch_request = iblai.GCPTenantLaunchRequest() # GCPTenantLaunchRequest | 

try:
    api_response = api_instance.providers_gcp_launch_tenant_create(gcp_tenant_launch_request)
    print("The response of ProvidersApi->providers_gcp_launch_tenant_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_gcp_launch_tenant_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.ProvidersApi(api_client)
verify_gcp_market_place_request = iblai.VerifyGCPMarketPlaceRequest() # VerifyGCPMarketPlaceRequest | 

try:
    api_response = api_instance.providers_gcp_validate_signup_token_create(verify_gcp_market_place_request)
    print("The response of ProvidersApi->providers_gcp_validate_signup_token_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_gcp_validate_signup_token_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
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
api_instance = iblai.ProvidersApi(api_client)
bundle_id = 'bundle_id_example' # str | 

try:
    api_response = api_instance.providers_google_pay_get_account_retrieve(bundle_id)
    print("The response of ProvidersApi->providers_google_pay_get_account_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_google_pay_get_account_retrieve: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)

try:
    api_instance.providers_google_pay_hook_create()
except Exception as e:
    print("Exception when calling ProvidersApi->providers_google_pay_hook_create: %s\n" % e)
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
api_instance = iblai.ProvidersApi(api_client)
google_pay_verify_token = iblai.GooglePayVerifyToken() # GooglePayVerifyToken | 

try:
    api_response = api_instance.providers_google_pay_validate_transaction_id_create(google_pay_verify_token)
    print("The response of ProvidersApi->providers_google_pay_validate_transaction_id_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_google_pay_validate_transaction_id_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** |  |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_stripe_create_organization_create**
> TenantLaunchResponse providers_stripe_create_organization_create(stripe_new_user_tenant_launch_request)



Proxy to the Platform launch API  We cannot expose launching a tenant to an unauthorized user hence the need for the API  The API validates the stripe_checkout_id and then proxies the request to the Platform Launch API

### Example


```python
import iblai
from iblai.models.stripe_new_user_tenant_launch_request import StripeNewUserTenantLaunchRequest
from iblai.models.tenant_launch_response import TenantLaunchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.ProvidersApi(api_client)
stripe_new_user_tenant_launch_request = iblai.StripeNewUserTenantLaunchRequest() # StripeNewUserTenantLaunchRequest | 

try:
    api_response = api_instance.providers_stripe_create_organization_create(stripe_new_user_tenant_launch_request)
    print("The response of ProvidersApi->providers_stripe_create_organization_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProvidersApi->providers_stripe_create_organization_create: %s\n" % e)
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**417** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

