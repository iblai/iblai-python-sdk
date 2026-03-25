# iblai.CustomDomainsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_domains_by_name_status_update**](CustomDomainsApi.md#custom_domains_by_name_status_update) | **PUT** /api/custom-domains/by-name/{domain_name}/status/ | 
[**custom_domains_create_create**](CustomDomainsApi.md#custom_domains_create_create) | **POST** /api/custom-domains/create/ | 
[**custom_domains_delete_destroy**](CustomDomainsApi.md#custom_domains_delete_destroy) | **DELETE** /api/custom-domains/{domain_id}/delete/ | 
[**custom_domains_deleted_status_create**](CustomDomainsApi.md#custom_domains_deleted_status_create) | **POST** /api/custom-domains/{domain_id}/deleted-status/ | 
[**custom_domains_retrieve**](CustomDomainsApi.md#custom_domains_retrieve) | **GET** /api/custom-domains/ | 
[**custom_domains_status_update**](CustomDomainsApi.md#custom_domains_status_update) | **PUT** /api/custom-domains/{domain_id}/status/ | 


# **custom_domains_by_name_status_update**
> custom_domains_by_name_status_update(domain_name)

API endpoint to update custom domain SPA type by domain name

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
api_instance = iblai.CustomDomainsApi(api_client)
domain_name = 'domain_name_example' # str | 

try:
    api_instance.custom_domains_by_name_status_update(domain_name)
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_by_name_status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 

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

# **custom_domains_create_create**
> custom_domains_create_create()

API endpoint to create a custom domain

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
api_instance = iblai.CustomDomainsApi(api_client)

try:
    api_instance.custom_domains_create_create()
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_create_create: %s\n" % e)
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

# **custom_domains_delete_destroy**
> custom_domains_delete_destroy(domain_id)

API endpoint to hard delete a custom domain

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
api_instance = iblai.CustomDomainsApi(api_client)
domain_id = 56 # int | 

try:
    api_instance.custom_domains_delete_destroy(domain_id)
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_delete_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 

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

# **custom_domains_deleted_status_create**
> custom_domains_deleted_status_create(domain_id)

API endpoint to update the is_deleted status of a custom domain

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
api_instance = iblai.CustomDomainsApi(api_client)
domain_id = 56 # int | 

try:
    api_instance.custom_domains_deleted_status_create(domain_id)
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_deleted_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 

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

# **custom_domains_retrieve**
> custom_domains_retrieve()

API endpoint to get custom domains (public, no authentication or permission checks)

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iblai.CustomDomainsApi(api_client)

try:
    api_instance.custom_domains_retrieve()
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_retrieve: %s\n" % e)
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

# **custom_domains_status_update**
> custom_domains_status_update(domain_id)

API endpoint to update custom domain SPA type

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
api_instance = iblai.CustomDomainsApi(api_client)
domain_id = 56 # int | 

try:
    api_instance.custom_domains_status_update(domain_id)
except Exception as e:
    print("Exception when calling CustomDomainsApi->custom_domains_status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 

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

