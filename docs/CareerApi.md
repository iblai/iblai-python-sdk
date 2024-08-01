# iblai.CareerApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_resume_orgs_users_create**](CareerApi.md#career_resume_orgs_users_create) | **POST** /api/career/resume/orgs/{orgs}/users/{user_id}/ | 
[**career_resume_orgs_users_retrieve**](CareerApi.md#career_resume_orgs_users_retrieve) | **GET** /api/career/resume/orgs/{orgs}/users/{user_id}/ | 


# **career_resume_orgs_users_create**
> career_resume_orgs_users_create(orgs, user_id)



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
api_instance = iblai.CareerApi(api_client)
orgs = 'orgs_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.career_resume_orgs_users_create(orgs, user_id)
except Exception as e:
    print("Exception when calling CareerApi->career_resume_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgs** | **str**|  | 
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

# **career_resume_orgs_users_retrieve**
> career_resume_orgs_users_retrieve(orgs, user_id)



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
api_instance = iblai.CareerApi(api_client)
orgs = 'orgs_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.career_resume_orgs_users_retrieve(orgs, user_id)
except Exception as e:
    print("Exception when calling CareerApi->career_resume_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgs** | **str**|  | 
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

