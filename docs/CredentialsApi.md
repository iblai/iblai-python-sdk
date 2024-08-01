# iblai.CredentialsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_orgs_users_assertions_bulk_create**](CredentialsApi.md#credentials_orgs_users_assertions_bulk_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/{entity_id}/assertions/bulk/ | 
[**credentials_orgs_users_assertions_create**](CredentialsApi.md#credentials_orgs_users_assertions_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/assertions-over-time/ | 
[**credentials_orgs_users_assertions_retrieve**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/assertions/ | 
[**credentials_orgs_users_assertions_retrieve2**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve2) | **GET** /api/credentials/orgs/{org}/users/{user_id}/assertions/{entity_id} | 
[**credentials_orgs_users_assertions_retrieve3**](CredentialsApi.md#credentials_orgs_users_assertions_retrieve3) | **GET** /api/credentials/orgs/{org}/users/{user_id}/{entity_id}/assertions/ | 
[**credentials_orgs_users_assertions_update**](CredentialsApi.md#credentials_orgs_users_assertions_update) | **PUT** /api/credentials/orgs/{org}/users/{user_id}/assertions/{entity_id} | 
[**credentials_orgs_users_course_assertions_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/course-assertions-over-time/ | 
[**credentials_orgs_users_course_credentials_list**](CredentialsApi.md#credentials_orgs_users_course_credentials_list) | **GET** /api/credentials/orgs/{org}/users/{user_id}/course-credentials/ | 
[**credentials_orgs_users_create**](CredentialsApi.md#credentials_orgs_users_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/ | 
[**credentials_orgs_users_credentials_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/credentials-over-time/ | 
[**credentials_orgs_users_destroy**](CredentialsApi.md#credentials_orgs_users_destroy) | **DELETE** /api/credentials/orgs/{org}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_issuers_authority_create**](CredentialsApi.md#credentials_orgs_users_issuers_authority_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/issuers/authority/ | 
[**credentials_orgs_users_issuers_create**](CredentialsApi.md#credentials_orgs_users_issuers_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/issuers/ | 
[**credentials_orgs_users_issuers_destroy**](CredentialsApi.md#credentials_orgs_users_issuers_destroy) | **DELETE** /api/credentials/orgs/{org}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_retrieve**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/issuers/ | 
[**credentials_orgs_users_issuers_retrieve2**](CredentialsApi.md#credentials_orgs_users_issuers_retrieve2) | **GET** /api/credentials/orgs/{org}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_issuers_update**](CredentialsApi.md#credentials_orgs_users_issuers_update) | **PUT** /api/credentials/orgs/{org}/users/{user_id}/issuers/{entity_id} | 
[**credentials_orgs_users_retrieve**](CredentialsApi.md#credentials_orgs_users_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/ | 
[**credentials_orgs_users_retrieve2**](CredentialsApi.md#credentials_orgs_users_retrieve2) | **GET** /api/credentials/orgs/{org}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_update**](CredentialsApi.md#credentials_orgs_users_update) | **PUT** /api/credentials/orgs/{org}/users/{user_id}/{entity_id} | 
[**credentials_public_assertions_retrieve**](CredentialsApi.md#credentials_public_assertions_retrieve) | **GET** /api/credentials/public/assertions/{entity_id}/ | 


# **credentials_orgs_users_assertions_bulk_create**
> BulkCreateAssertion credentials_orgs_users_assertions_bulk_create(entity_id, org, user_id, bulk_create_assertion)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.bulk_create_assertion import BulkCreateAssertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
bulk_create_assertion = iblai.BulkCreateAssertion() # BulkCreateAssertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_bulk_create(entity_id, org, user_id, bulk_create_assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_bulk_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **bulk_create_assertion** | [**BulkCreateAssertion**](BulkCreateAssertion.md)|  | 

### Return type

[**BulkCreateAssertion**](BulkCreateAssertion.md)

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

# **credentials_orgs_users_assertions_create**
> Assertion credentials_orgs_users_assertions_create(entity_id, org, user_id, assertion)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_create(entity_id, org, user_id, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_over_time_retrieve**
> OverTime credentials_orgs_users_assertions_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_assertions_retrieve**
> Assertion credentials_orgs_users_assertions_retrieve(org, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course = 'course_example' # str |  (optional)
exclude_main_tenant_assertions = True # bool |  (optional)
include_expired = True # bool |  (optional)
include_revoked = True # bool |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve(org, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course** | **str**|  | [optional] 
 **exclude_main_tenant_assertions** | **bool**|  | [optional] 
 **include_expired** | **bool**|  | [optional] 
 **include_revoked** | **bool**|  | [optional] 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_retrieve2**
> Assertion credentials_orgs_users_assertions_retrieve2(entity_id, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve2(entity_id, org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_retrieve3**
> Assertion credentials_orgs_users_assertions_retrieve3(entity_id, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve3(entity_id, org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_retrieve3:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_retrieve3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_assertions_update**
> Assertion credentials_orgs_users_assertions_update(entity_id, org, user_id, assertion)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assertion import Assertion
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
assertion = iblai.Assertion() # Assertion | 

try:
    api_response = api_instance.credentials_orgs_users_assertions_update(entity_id, org, user_id, assertion)
    print("The response of CredentialsApi->credentials_orgs_users_assertions_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assertions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **assertion** | [**Assertion**](Assertion.md)|  | 

### Return type

[**Assertion**](Assertion.md)

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

# **credentials_orgs_users_course_assertions_over_time_retrieve**
> OverTime credentials_orgs_users_course_assertions_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_course_assertions_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_assertions_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_course_credentials_list**
> credentials_orgs_users_course_credentials_list(org, user_id, limit=limit, offset=offset)



Endpoint to retrieve the credentials of a given tenant

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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_instance.credentials_orgs_users_course_credentials_list(org, user_id, limit=limit, offset=offset)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

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

# **credentials_orgs_users_create**
> Credential credentials_orgs_users_create(org, user_id, credential)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_create(org, user_id, credential)
    print("The response of CredentialsApi->credentials_orgs_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_credentials_over_time_retrieve**
> OverTime credentials_orgs_users_credentials_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.over_time import OverTime
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_credentials_over_time_retrieve(org, user_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
    print("The response of CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_credentials_over_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OverTime**](OverTime.md)

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

# **credentials_orgs_users_destroy**
> credentials_orgs_users_destroy(entity_id, org, user_id)



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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.credentials_orgs_users_destroy(entity_id, org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_authority_create**
> IssuerAuthority credentials_orgs_users_issuers_authority_create(org, user_id, issuer_authority)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer_authority import IssuerAuthority
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
issuer_authority = iblai.IssuerAuthority() # IssuerAuthority | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_authority_create(org, user_id, issuer_authority)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_authority_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_authority_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **issuer_authority** | [**IssuerAuthority**](IssuerAuthority.md)|  | 

### Return type

[**IssuerAuthority**](IssuerAuthority.md)

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

# **credentials_orgs_users_issuers_create**
> Issuer credentials_orgs_users_issuers_create(org, q, user_id, issuer)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
q = 'q_example' # str | 
user_id = 'user_id_example' # str | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_create(org, q, user_id, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **q** | **str**|  | 
 **user_id** | **str**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_destroy**
> credentials_orgs_users_issuers_destroy(entity_id, org, user_id)



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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.credentials_orgs_users_issuers_destroy(entity_id, org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
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
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_orgs_users_issuers_retrieve**
> Issuer credentials_orgs_users_issuers_retrieve(org, q, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
q = 'q_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve(org, q, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **q** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_retrieve2**
> Issuer credentials_orgs_users_issuers_retrieve2(entity_id, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_retrieve2(entity_id, org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_issuers_update**
> Issuer credentials_orgs_users_issuers_update(entity_id, org, user_id, issuer)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.issuer import Issuer
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
issuer = iblai.Issuer() # Issuer | 

try:
    api_response = api_instance.credentials_orgs_users_issuers_update(entity_id, org, user_id, issuer)
    print("The response of CredentialsApi->credentials_orgs_users_issuers_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_issuers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **issuer** | [**Issuer**](Issuer.md)|  | 

### Return type

[**Issuer**](Issuer.md)

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

# **credentials_orgs_users_retrieve**
> Credential credentials_orgs_users_retrieve(org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve(org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_retrieve2**
> Credential credentials_orgs_users_retrieve2(entity_id, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.credentials_orgs_users_retrieve2(entity_id, org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_orgs_users_update**
> Credential credentials_orgs_users_update(entity_id, org, user_id, credential)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.credential import Credential
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
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
credential = iblai.Credential() # Credential | 

try:
    api_response = api_instance.credentials_orgs_users_update(entity_id, org, user_id, credential)
    print("The response of CredentialsApi->credentials_orgs_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 

### Return type

[**Credential**](Credential.md)

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

# **credentials_public_assertions_retrieve**
> credentials_public_assertions_retrieve(entity_id)



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 

try:
    api_instance.credentials_public_assertions_retrieve(entity_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_public_assertions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

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

