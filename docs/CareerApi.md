# iblai.CareerApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_location_orgs_users_create**](CareerApi.md#career_location_orgs_users_create) | **POST** /api/career/location/orgs/{org}/users/{username}/ | 
[**career_location_orgs_users_retrieve**](CareerApi.md#career_location_orgs_users_retrieve) | **GET** /api/career/location/orgs/{org}/users/{username}/ | 
[**career_location_orgs_users_update**](CareerApi.md#career_location_orgs_users_update) | **PUT** /api/career/location/orgs/{org}/users/{username}/ | 
[**career_locations_orgs_retrieve**](CareerApi.md#career_locations_orgs_retrieve) | **GET** /api/career/locations/orgs/{org}/ | 
[**career_orgs_companies_users_create**](CareerApi.md#career_orgs_companies_users_create) | **POST** /api/career/orgs/{org}/companies/users/{username}/ | 
[**career_orgs_companies_users_destroy**](CareerApi.md#career_orgs_companies_users_destroy) | **DELETE** /api/career/orgs/{org}/companies/users/{username}/ | 
[**career_orgs_companies_users_retrieve**](CareerApi.md#career_orgs_companies_users_retrieve) | **GET** /api/career/orgs/{org}/companies/users/{username}/ | 
[**career_orgs_companies_users_update**](CareerApi.md#career_orgs_companies_users_update) | **PUT** /api/career/orgs/{org}/companies/users/{username}/ | 
[**career_orgs_education_users_create**](CareerApi.md#career_orgs_education_users_create) | **POST** /api/career/orgs/{org}/education/users/{username}/ | 
[**career_orgs_education_users_destroy**](CareerApi.md#career_orgs_education_users_destroy) | **DELETE** /api/career/orgs/{org}/education/users/{username}/ | 
[**career_orgs_education_users_retrieve**](CareerApi.md#career_orgs_education_users_retrieve) | **GET** /api/career/orgs/{org}/education/users/{username}/ | 
[**career_orgs_education_users_update**](CareerApi.md#career_orgs_education_users_update) | **PUT** /api/career/orgs/{org}/education/users/{username}/ | 
[**career_orgs_experience_users_create**](CareerApi.md#career_orgs_experience_users_create) | **POST** /api/career/orgs/{org}/experience/users/{username}/ | 
[**career_orgs_experience_users_destroy**](CareerApi.md#career_orgs_experience_users_destroy) | **DELETE** /api/career/orgs/{org}/experience/users/{username}/ | 
[**career_orgs_experience_users_retrieve**](CareerApi.md#career_orgs_experience_users_retrieve) | **GET** /api/career/orgs/{org}/experience/users/{username}/ | 
[**career_orgs_experience_users_update**](CareerApi.md#career_orgs_experience_users_update) | **PUT** /api/career/orgs/{org}/experience/users/{username}/ | 
[**career_orgs_institutions_users_create**](CareerApi.md#career_orgs_institutions_users_create) | **POST** /api/career/orgs/{org}/institutions/users/{username}/ | 
[**career_orgs_institutions_users_destroy**](CareerApi.md#career_orgs_institutions_users_destroy) | **DELETE** /api/career/orgs/{org}/institutions/users/{username}/ | 
[**career_orgs_institutions_users_retrieve**](CareerApi.md#career_orgs_institutions_users_retrieve) | **GET** /api/career/orgs/{org}/institutions/users/{username}/ | 
[**career_orgs_institutions_users_update**](CareerApi.md#career_orgs_institutions_users_update) | **PUT** /api/career/orgs/{org}/institutions/users/{username}/ | 
[**career_orgs_programs_users_create**](CareerApi.md#career_orgs_programs_users_create) | **POST** /api/career/orgs/{org}/programs/users/{username}/ | 
[**career_orgs_programs_users_destroy**](CareerApi.md#career_orgs_programs_users_destroy) | **DELETE** /api/career/orgs/{org}/programs/users/{username}/ | 
[**career_orgs_programs_users_retrieve**](CareerApi.md#career_orgs_programs_users_retrieve) | **GET** /api/career/orgs/{org}/programs/users/{username}/ | 
[**career_orgs_programs_users_update**](CareerApi.md#career_orgs_programs_users_update) | **PUT** /api/career/orgs/{org}/programs/users/{username}/ | 
[**career_resume_orgs_users_create**](CareerApi.md#career_resume_orgs_users_create) | **POST** /api/career/resume/orgs/{org}/users/{username}/ | 
[**career_resume_orgs_users_retrieve**](CareerApi.md#career_resume_orgs_users_retrieve) | **GET** /api/career/resume/orgs/{org}/users/{username}/ | 
[**career_resume_orgs_users_update**](CareerApi.md#career_resume_orgs_users_update) | **PUT** /api/career/resume/orgs/{org}/users/{username}/ | 


# **career_location_orgs_users_create**
> career_location_orgs_users_create(org, username)



API endpoint for managing user base locations

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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_location_orgs_users_create(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_location_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_location_orgs_users_retrieve**
> career_location_orgs_users_retrieve(org, username)



API endpoint for managing user base locations

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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_location_orgs_users_retrieve(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_location_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_location_orgs_users_update**
> career_location_orgs_users_update(org, username)



API endpoint for managing user base locations

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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_location_orgs_users_update(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_location_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_locations_orgs_retrieve**
> career_locations_orgs_retrieve(org)



Platform-wide location statistics (GET only)

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CareerApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.career_locations_orgs_retrieve(org)
except Exception as e:
    print("Exception when calling CareerApi->career_locations_orgs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **career_orgs_companies_users_create**
> Company career_orgs_companies_users_create(org, username, company)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.company import Company
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
org = 'org_example' # str | 
username = 'username_example' # str | 
company = iblai.Company() # Company | 

try:
    api_response = api_instance.career_orgs_companies_users_create(org, username, company)
    print("The response of CareerApi->career_orgs_companies_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_companies_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **company** | [**Company**](Company.md)|  | 

### Return type

[**Company**](Company.md)

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

# **career_orgs_companies_users_destroy**
> career_orgs_companies_users_destroy(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_orgs_companies_users_destroy(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_companies_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_orgs_companies_users_retrieve**
> Company career_orgs_companies_users_retrieve(org, username)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.company import Company
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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.career_orgs_companies_users_retrieve(org, username)
    print("The response of CareerApi->career_orgs_companies_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_companies_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Company**](Company.md)

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

# **career_orgs_companies_users_update**
> Company career_orgs_companies_users_update(org, username, company)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.company import Company
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
org = 'org_example' # str | 
username = 'username_example' # str | 
company = iblai.Company() # Company | 

try:
    api_response = api_instance.career_orgs_companies_users_update(org, username, company)
    print("The response of CareerApi->career_orgs_companies_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_companies_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **company** | [**Company**](Company.md)|  | 

### Return type

[**Company**](Company.md)

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

# **career_orgs_education_users_create**
> Education career_orgs_education_users_create(org, username, education)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.education import Education
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
org = 'org_example' # str | 
username = 'username_example' # str | 
education = iblai.Education() # Education | 

try:
    api_response = api_instance.career_orgs_education_users_create(org, username, education)
    print("The response of CareerApi->career_orgs_education_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_education_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **education** | [**Education**](Education.md)|  | 

### Return type

[**Education**](Education.md)

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

# **career_orgs_education_users_destroy**
> career_orgs_education_users_destroy(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_orgs_education_users_destroy(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_education_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_orgs_education_users_retrieve**
> Education career_orgs_education_users_retrieve(org, username)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.education import Education
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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.career_orgs_education_users_retrieve(org, username)
    print("The response of CareerApi->career_orgs_education_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_education_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Education**](Education.md)

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

# **career_orgs_education_users_update**
> Education career_orgs_education_users_update(org, username, education)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.education import Education
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
org = 'org_example' # str | 
username = 'username_example' # str | 
education = iblai.Education() # Education | 

try:
    api_response = api_instance.career_orgs_education_users_update(org, username, education)
    print("The response of CareerApi->career_orgs_education_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_education_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **education** | [**Education**](Education.md)|  | 

### Return type

[**Education**](Education.md)

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

# **career_orgs_experience_users_create**
> Experience career_orgs_experience_users_create(org, username, experience)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.experience import Experience
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
org = 'org_example' # str | 
username = 'username_example' # str | 
experience = iblai.Experience() # Experience | 

try:
    api_response = api_instance.career_orgs_experience_users_create(org, username, experience)
    print("The response of CareerApi->career_orgs_experience_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_experience_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **experience** | [**Experience**](Experience.md)|  | 

### Return type

[**Experience**](Experience.md)

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

# **career_orgs_experience_users_destroy**
> career_orgs_experience_users_destroy(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_orgs_experience_users_destroy(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_experience_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_orgs_experience_users_retrieve**
> Experience career_orgs_experience_users_retrieve(org, username)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.experience import Experience
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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.career_orgs_experience_users_retrieve(org, username)
    print("The response of CareerApi->career_orgs_experience_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_experience_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Experience**](Experience.md)

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

# **career_orgs_experience_users_update**
> Experience career_orgs_experience_users_update(org, username, experience)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.experience import Experience
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
org = 'org_example' # str | 
username = 'username_example' # str | 
experience = iblai.Experience() # Experience | 

try:
    api_response = api_instance.career_orgs_experience_users_update(org, username, experience)
    print("The response of CareerApi->career_orgs_experience_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_experience_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **experience** | [**Experience**](Experience.md)|  | 

### Return type

[**Experience**](Experience.md)

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

# **career_orgs_institutions_users_create**
> Institution career_orgs_institutions_users_create(org, username, institution)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.institution import Institution
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
org = 'org_example' # str | 
username = 'username_example' # str | 
institution = iblai.Institution() # Institution | 

try:
    api_response = api_instance.career_orgs_institutions_users_create(org, username, institution)
    print("The response of CareerApi->career_orgs_institutions_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_institutions_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **institution** | [**Institution**](Institution.md)|  | 

### Return type

[**Institution**](Institution.md)

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

# **career_orgs_institutions_users_destroy**
> career_orgs_institutions_users_destroy(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_orgs_institutions_users_destroy(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_institutions_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_orgs_institutions_users_retrieve**
> Institution career_orgs_institutions_users_retrieve(org, username)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.institution import Institution
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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.career_orgs_institutions_users_retrieve(org, username)
    print("The response of CareerApi->career_orgs_institutions_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_institutions_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Institution**](Institution.md)

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

# **career_orgs_institutions_users_update**
> Institution career_orgs_institutions_users_update(org, username, institution)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.institution import Institution
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
org = 'org_example' # str | 
username = 'username_example' # str | 
institution = iblai.Institution() # Institution | 

try:
    api_response = api_instance.career_orgs_institutions_users_update(org, username, institution)
    print("The response of CareerApi->career_orgs_institutions_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_institutions_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **institution** | [**Institution**](Institution.md)|  | 

### Return type

[**Institution**](Institution.md)

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

# **career_orgs_programs_users_create**
> Program career_orgs_programs_users_create(org, username, program)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.program import Program
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
org = 'org_example' # str | 
username = 'username_example' # str | 
program = iblai.Program() # Program | 

try:
    api_response = api_instance.career_orgs_programs_users_create(org, username, program)
    print("The response of CareerApi->career_orgs_programs_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_programs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **program** | [**Program**](Program.md)|  | 

### Return type

[**Program**](Program.md)

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

# **career_orgs_programs_users_destroy**
> career_orgs_programs_users_destroy(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_orgs_programs_users_destroy(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_programs_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_orgs_programs_users_retrieve**
> Program career_orgs_programs_users_retrieve(org, username)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.program import Program
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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.career_orgs_programs_users_retrieve(org, username)
    print("The response of CareerApi->career_orgs_programs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_programs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**Program**](Program.md)

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

# **career_orgs_programs_users_update**
> Program career_orgs_programs_users_update(org, username, program)



### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.program import Program
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
org = 'org_example' # str | 
username = 'username_example' # str | 
program = iblai.Program() # Program | 

try:
    api_response = api_instance.career_orgs_programs_users_update(org, username, program)
    print("The response of CareerApi->career_orgs_programs_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CareerApi->career_orgs_programs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **program** | [**Program**](Program.md)|  | 

### Return type

[**Program**](Program.md)

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

# **career_resume_orgs_users_create**
> career_resume_orgs_users_create(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_resume_orgs_users_create(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_resume_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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
> career_resume_orgs_users_retrieve(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_resume_orgs_users_retrieve(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_resume_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

# **career_resume_orgs_users_update**
> career_resume_orgs_users_update(org, username)



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
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_instance.career_resume_orgs_users_update(org, username)
except Exception as e:
    print("Exception when calling CareerApi->career_resume_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

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

