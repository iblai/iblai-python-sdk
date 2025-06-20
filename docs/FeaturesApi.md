# iblai.FeaturesApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**features_apps_list**](FeaturesApi.md#features_apps_list) | **GET** /api/features/apps/ | 
[**features_apps_update_create**](FeaturesApi.md#features_apps_update_create) | **POST** /api/features/apps/update/ | 
[**features_apps_update_trial_status_create**](FeaturesApi.md#features_apps_update_trial_status_create) | **POST** /api/features/apps/update-trial-status/ | 
[**features_bulk_config_create**](FeaturesApi.md#features_bulk_config_create) | **POST** /api/features/bulk-config/ | 
[**features_config_create**](FeaturesApi.md#features_config_create) | **POST** /api/features/config/ | 
[**features_config_retrieve**](FeaturesApi.md#features_config_retrieve) | **GET** /api/features/config/ | 


# **features_apps_list**
> PaginatedUserAppList features_apps_list(page=page, page_size=page_size)



Returns a list of the apps that the user has access to.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_user_app_list import PaginatedUserAppList
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
api_instance = iblai.FeaturesApi(api_client)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.features_apps_list(page=page, page_size=page_size)
    print("The response of FeaturesApi->features_apps_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FeaturesApi->features_apps_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedUserAppList**](PaginatedUserAppList.md)

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

# **features_apps_update_create**
> OnboardingStatusUpdate features_apps_update_create(onboarding_status_update)



Updates the user onboarding completed status

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.onboarding_status_update import OnboardingStatusUpdate
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
api_instance = iblai.FeaturesApi(api_client)
onboarding_status_update = iblai.OnboardingStatusUpdate() # OnboardingStatusUpdate | 

try:
    api_response = api_instance.features_apps_update_create(onboarding_status_update)
    print("The response of FeaturesApi->features_apps_update_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FeaturesApi->features_apps_update_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboarding_status_update** | [**OnboardingStatusUpdate**](OnboardingStatusUpdate.md)|  | 

### Return type

[**OnboardingStatusUpdate**](OnboardingStatusUpdate.md)

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

# **features_apps_update_trial_status_create**
> ActivateUserFreeTrial features_apps_update_trial_status_create(activate_user_free_trial)



Activates free trial for the user  Set free_trial_started to True| false for the user app  App URL or ID is required as well as the platform key

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.activate_user_free_trial import ActivateUserFreeTrial
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
api_instance = iblai.FeaturesApi(api_client)
activate_user_free_trial = iblai.ActivateUserFreeTrial() # ActivateUserFreeTrial | 

try:
    api_response = api_instance.features_apps_update_trial_status_create(activate_user_free_trial)
    print("The response of FeaturesApi->features_apps_update_trial_status_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling FeaturesApi->features_apps_update_trial_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_user_free_trial** | [**ActivateUserFreeTrial**](ActivateUserFreeTrial.md)|  | 

### Return type

[**ActivateUserFreeTrial**](ActivateUserFreeTrial.md)

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

# **features_bulk_config_create**
> features_bulk_config_create()



POST Bulk update user feature config  NOTE: Will not create user feature configs  Params: platform_key  config (OR) feature values

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
api_instance = iblai.FeaturesApi(api_client)

try:
    api_instance.features_bulk_config_create()
except Exception as e:
    print("Exception when calling FeaturesApi->features_bulk_config_create: %s\n" % e)
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

# **features_config_create**
> features_config_create()



POST Update user feature config  Params: user_id/username/email platform_key  config (OR) feature values

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
api_instance = iblai.FeaturesApi(api_client)

try:
    api_instance.features_config_create()
except Exception as e:
    print("Exception when calling FeaturesApi->features_config_create: %s\n" % e)
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

# **features_config_retrieve**
> features_config_retrieve()



Query user feature config  Params: user_id/username/email platform_key

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
api_instance = iblai.FeaturesApi(api_client)

try:
    api_instance.features_config_retrieve()
except Exception as e:
    print("Exception when calling FeaturesApi->features_config_retrieve: %s\n" % e)
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

