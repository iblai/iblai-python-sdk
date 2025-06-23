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
[**credentials_orgs_users_assignments_destroy**](CredentialsApi.md#credentials_orgs_users_assignments_destroy) | **DELETE** /api/credentials/orgs/{org}/users/{user_id}/assignments/{assignment_id} | 
[**credentials_orgs_users_assignments_groups_create**](CredentialsApi.md#credentials_orgs_users_assignments_groups_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/assignments/groups/ | 
[**credentials_orgs_users_assignments_groups_retrieve**](CredentialsApi.md#credentials_orgs_users_assignments_groups_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/assignments/groups/ | 
[**credentials_orgs_users_assignments_users_create**](CredentialsApi.md#credentials_orgs_users_assignments_users_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/assignments/users/ | 
[**credentials_orgs_users_assignments_users_retrieve**](CredentialsApi.md#credentials_orgs_users_assignments_users_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/assignments/users/ | 
[**credentials_orgs_users_course_assertions_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/course-assertions-over-time/ | 
[**credentials_orgs_users_course_credentials_list**](CredentialsApi.md#credentials_orgs_users_course_credentials_list) | **GET** /api/credentials/orgs/{org}/users/{user_id}/course-credentials/ | 
[**credentials_orgs_users_create**](CredentialsApi.md#credentials_orgs_users_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/ | 
[**credentials_orgs_users_credentials_over_time_retrieve**](CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/credentials-over-time/ | 
[**credentials_orgs_users_destroy**](CredentialsApi.md#credentials_orgs_users_destroy) | **DELETE** /api/credentials/orgs/{org}/users/{user_id}/{entity_id} | 
[**credentials_orgs_users_images_create**](CredentialsApi.md#credentials_orgs_users_images_create) | **POST** /api/credentials/orgs/{org}/users/{user_id}/images/ | 
[**credentials_orgs_users_images_retrieve**](CredentialsApi.md#credentials_orgs_users_images_retrieve) | **GET** /api/credentials/orgs/{org}/users/{user_id}/images/ | 
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



Endpoint to issue credential assertions in bulk for a specific credential.  This endpoint allows issuing credential assertions to multiple users at once.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  POST Request Body:     A JSON object containing:     - users (list): List of usernames to issue the credential to     - Additional metadata required for issuing the credential  Returns:     A JSON response containing:     {         \"skipped\": [\"username1\", \"username3\"],  // Users that were skipped (e.g., already have the credential)         \"issued\": [\"username2\", \"username4\"]    // Users that were successfully issued the credential     }  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs

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



Endpoint to issue and retrieve credential assertions for a specific credential.  This endpoint allows issuing new credential assertions and retrieving existing assertions for a specific credential.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  Methods:     POST: Issue a new credential assertion     GET: Retrieve assertions for a specific credential  POST Request Body:     A JSON object containing recipient information and any additional metadata     required for issuing the credential.  Returns:     POST: A JSON response containing the created assertion using the AssertionSerializer format     GET: A paginated list of assertions using the AssertionSerializer format  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs

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
> OvertimeWithChangeInfo credentials_orgs_users_assertions_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



Get all credentials of a given tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.overtime_with_change_info import OvertimeWithChangeInfo
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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
 **end_date** | **str**| end date. ISO 8601 | [optional] 
 **format** | **str**| Format  * &#x60;json&#x60; - json | [optional] [default to json]
 **include_main_platform** | **bool**| Include main platform data | [optional] [default to True]
 **start_date** | **str**| start date. ISO 8601 | [optional] 

### Return type

[**OvertimeWithChangeInfo**](OvertimeWithChangeInfo.md)

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
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve(org, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)



Endpoint to retrieve all credential assertions for a user within an organization.  This endpoint provides access to all credential assertions (issued credentials) for a specific user within an organization, with support for filtering.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID to retrieve assertions for  Query Parameters:     course (str, optional): Filter by course ID     include_revoked (bool, optional): Include revoked assertions (default: false)     include_expired (bool, optional): Include expired assertions (default: false)     exclude_main_tenant_assertions (bool, optional): Exclude assertions from the main tenant (default: false)  Returns:     A paginated response using the AssertionSerializer format  Error Responses:     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the user or organization doesn't exist     500 Internal Server Error: If an unexpected error occurs

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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
page = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_assertions_retrieve(org, user_id, course=course, exclude_main_tenant_assertions=exclude_main_tenant_assertions, include_expired=include_expired, include_revoked=include_revoked, page=page, page_size=page_size)
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
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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



Endpoint to retrieve and update a specific credential assertion.  This endpoint allows retrieving details of a specific credential assertion and updating its status (e.g., revoking it).  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The assertion entity ID  Methods:     GET: Retrieve assertion details     PUT: Update assertion status (e.g., revoke)  PUT Request Body:     A JSON object containing:     - revoked (bool): Set to true to revoke the assertion     - revocationReason (str): Reason for revocation (required when revoking)  Returns:     GET: A JSON response containing the assertion details using the AssertionSerializer format     PUT: A JSON response containing the updated assertion using the AssertionSerializer format  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the assertion doesn't exist     500 Internal Server Error: If an unexpected error occurs

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
> PaginatedAssertionsResponse credentials_orgs_users_assertions_retrieve3(entity_id, org, user_id)



Endpoint to issue and retrieve credential assertions for a specific credential.  This endpoint allows issuing new credential assertions and retrieving existing assertions for a specific credential.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  Methods:     POST: Issue a new credential assertion     GET: Retrieve assertions for a specific credential  POST Request Body:     A JSON object containing recipient information and any additional metadata     required for issuing the credential.  Returns:     POST: A JSON response containing the created assertion using the AssertionSerializer format     GET: A paginated list of assertions using the AssertionSerializer format  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse
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

[**PaginatedAssertionsResponse**](PaginatedAssertionsResponse.md)

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



Endpoint to retrieve and update a specific credential assertion.  This endpoint allows retrieving details of a specific credential assertion and updating its status (e.g., revoking it).  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The assertion entity ID  Methods:     GET: Retrieve assertion details     PUT: Update assertion status (e.g., revoke)  PUT Request Body:     A JSON object containing:     - revoked (bool): Set to true to revoke the assertion     - revocationReason (str): Reason for revocation (required when revoking)  Returns:     GET: A JSON response containing the assertion details using the AssertionSerializer format     PUT: A JSON response containing the updated assertion using the AssertionSerializer format  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the assertion doesn't exist     500 Internal Server Error: If an unexpected error occurs

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

# **credentials_orgs_users_assignments_destroy**
> credentials_orgs_users_assignments_destroy(assignment_id, org, user_id)



Delete a credential assignment using its entity_id. Only platform admins and department admins can delete assignments.

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
assignment_id = 'assignment_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.credentials_orgs_users_assignments_destroy(assignment_id, org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | 
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

# **credentials_orgs_users_assignments_groups_create**
> credentials_orgs_users_assignments_groups_create(org, user_id)



Create group assignment with department access validation

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

try:
    api_instance.credentials_orgs_users_assignments_groups_create(org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_create: %s\n" % e)
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

# **credentials_orgs_users_assignments_groups_retrieve**
> credentials_orgs_users_assignments_groups_retrieve(org, user_id)



Get group assignments with department-aware filtering

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

try:
    api_instance.credentials_orgs_users_assignments_groups_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_groups_retrieve: %s\n" % e)
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

# **credentials_orgs_users_assignments_users_create**
> credentials_orgs_users_assignments_users_create(org, user_id)



Create assignments with department access validation

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

try:
    api_instance.credentials_orgs_users_assignments_users_create(org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_create: %s\n" % e)
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

# **credentials_orgs_users_assignments_users_retrieve**
> credentials_orgs_users_assignments_users_retrieve(org, user_id)



Get assignments and their corresponding assertions based on user role: - Regular users: get only their own assignments - Platform admins: get assignments for all users in their platform - Department admins: get assignments for users in their department groups

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

try:
    api_instance.credentials_orgs_users_assignments_users_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_assignments_users_retrieve: %s\n" % e)
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

# **credentials_orgs_users_course_assertions_over_time_retrieve**
> OverTime credentials_orgs_users_course_assertions_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_course_assertions_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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
> credentials_orgs_users_course_credentials_list(org, user_id, page=page, page_size=page_size)



Endpoint to retrieve the credentials of a given tenant grouped by course.  This endpoint provides access to credential data grouped by course for a specific organization/tenant, with support for pagination and filtering.  Path Parameters:     org (str): The organization/tenant identifier  Query Parameters:     limit (int, optional): Number of results per page (default: 10)     offset (int, optional): Starting position for pagination     search (str, optional): Search term e.g course_id  Returns:     A paginated response using the CourseCredentialSerializer format.  Error Responses:     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this data     404 Not Found: If the organization doesn't exist     500 Internal Server Error: If an unexpected error occurs

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
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_instance.credentials_orgs_users_course_credentials_list(org, user_id, page=page, page_size=page_size)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_course_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

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



API View for managing credentials across a platform.  This endpoint allows creating and retrieving credentials for a specific organization/tenant, with support for filtering, searching, and pagination.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Query Parameters:     # Platform identification     platform_org (str, optional): Alternative platform identifier (takes precedence over URL org)      # Pagination     page (int, optional): Page number (default: 1)     page_size (int, optional): Items per page (default: 10, max: 100)      # Filtering and search     search (str, optional): Search term to filter credentials by name or description     course (str, optional): Course ID to filter credentials associated with a specific course     program (str, optional): Program ID to filter credentials associated with a specific program  Methods:     GET: Retrieve credentials with filtering and pagination     POST: Create a new credential  POST Request Body:     A JSON object containing credential details:     - name (str): Credential name     - description (str, optional): Credential description     - issuer (str): Issuer entity ID     - credential_type (str, optional): Type of credential     - html_template (str, optional): HTML template for credential rendering     - css_template (str, optional): CSS template for credential styling     - icon_image (str, optional): URL to credential icon     - background_image (str, optional): URL to credential background     - thumbnail_image (str, optional): URL to credential thumbnail     - criteria_url (str, optional): URL to credential criteria     - criteria_text (str, optional): Text description of credential criteria     - issuing_signal (str, optional): Signal that triggers credential issuance  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {                 \"next\": \"URL to next page\",                 \"previous\": \"URL to previous page\",                 \"count\": 42,                 \"data\": [                     {credential object},                     {credential object},                     ...                 ],                 \"num_pages\": 5,                 \"page_number\": 1,                 \"max_page_size\": 100             }         }      POST: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Created\"},             \"result\": {credential object}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the platform doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires CredentialAssignmentPermission     - Only public credentials are returned by default

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
> OverTime credentials_orgs_users_credentials_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)



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
department_id = 56 # int | When `department_mode=1` is passed, it allows to filter data for only user content groups for the specified department  (optional)
end_date = 'end_date_example' # str | end date. ISO 8601 (optional)
format = json # str | Format  * `json` - json (optional) (default to json)
include_main_platform = True # bool | Include main platform data (optional) (default to True)
start_date = 'start_date_example' # str | start date. ISO 8601 (optional)

try:
    api_response = api_instance.credentials_orgs_users_credentials_over_time_retrieve(org, user_id, department_id=department_id, end_date=end_date, format=format, include_main_platform=include_main_platform, start_date=start_date)
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
 **department_id** | **int**| When &#x60;department_mode&#x3D;1&#x60; is passed, it allows to filter data for only user content groups for the specified department  | [optional] 
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



API View for managing individual credentials.  This endpoint allows retrieving, updating, and deleting specific credentials identified by their entity_id.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  Methods:     GET: Retrieve a specific credential     PUT: Update a specific credential     DELETE: Delete a specific credential  PUT Request Body:     A JSON object containing credential details to update:     - name (str, optional): Credential name     - description (str, optional): Credential description     - credential_type (str, optional): Type of credential     - html_template (str, optional): HTML template for credential rendering     - css_template (str, optional): CSS template for credential styling     - icon_image (str, optional): URL to credential icon     - background_image (str, optional): URL to credential background     - thumbnail_image (str, optional): URL to credential thumbnail     - criteria_url (str, optional): URL to credential criteria     - criteria_text (str, optional): Text description of credential criteria     - issuing_signal (str, optional): Signal that triggers credential issuance  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {credential object}         }      PUT: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Updated\"},             \"result\": {credential object}         }      DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires CredentialAssignmentPermission     - Users can only manage credentials they have permission to access

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

# **credentials_orgs_users_images_create**
> UploadedImage credentials_orgs_users_images_create(org, user_id, uploaded_image=uploaded_image)



API View for managing uploaded images for credentials.  This endpoint allows uploading new images and retrieving existing images for use with credentials (icons, backgrounds, thumbnails, etc.).  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Query Parameters:     query (str, required for GET): Search term to filter images by name  Methods:     GET: Retrieve images matching a search query     POST: Upload a new image  POST Request Body:     Multipart form data containing:     - image (file, required): The image file to upload     - name (str, optional): A descriptive name for the image  Returns:     GET: A JSON array of image objects:         [             {                 \"id\": 123,                 \"name\": \"Logo\",                 \"image\": \"https://example.com/media/uploaded_images/logo.png\"             },             {                 \"id\": 124,                 \"name\": \"Background\",                 \"image\": \"https://example.com/media/uploaded_images/background.jpg\"             },             ...         ]      POST: A JSON object containing the uploaded image details:         {             \"id\": 125,             \"name\": \"Certificate Icon\",             \"image\": \"https://example.com/media/uploaded_images/certificate-icon.png\"         }  Error Responses:     400 Bad Request: If the request data is invalid or missing required parameters     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can upload and retrieve images

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
uploaded_image = iblai.UploadedImage() # UploadedImage |  (optional)

try:
    api_response = api_instance.credentials_orgs_users_images_create(org, user_id, uploaded_image=uploaded_image)
    print("The response of CredentialsApi->credentials_orgs_users_images_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **uploaded_image** | [**UploadedImage**](UploadedImage.md)|  | [optional] 

### Return type

[**UploadedImage**](UploadedImage.md)

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

# **credentials_orgs_users_images_retrieve**
> UploadedImage credentials_orgs_users_images_retrieve(org, user_id)



API View for managing uploaded images for credentials.  This endpoint allows uploading new images and retrieving existing images for use with credentials (icons, backgrounds, thumbnails, etc.).  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Query Parameters:     query (str, required for GET): Search term to filter images by name  Methods:     GET: Retrieve images matching a search query     POST: Upload a new image  POST Request Body:     Multipart form data containing:     - image (file, required): The image file to upload     - name (str, optional): A descriptive name for the image  Returns:     GET: A JSON array of image objects:         [             {                 \"id\": 123,                 \"name\": \"Logo\",                 \"image\": \"https://example.com/media/uploaded_images/logo.png\"             },             {                 \"id\": 124,                 \"name\": \"Background\",                 \"image\": \"https://example.com/media/uploaded_images/background.jpg\"             },             ...         ]      POST: A JSON object containing the uploaded image details:         {             \"id\": 125,             \"name\": \"Certificate Icon\",             \"image\": \"https://example.com/media/uploaded_images/certificate-icon.png\"         }  Error Responses:     400 Bad Request: If the request data is invalid or missing required parameters     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can upload and retrieve images

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.uploaded_image import UploadedImage
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
    api_response = api_instance.credentials_orgs_users_images_retrieve(org, user_id)
    print("The response of CredentialsApi->credentials_orgs_users_images_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_orgs_users_images_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UploadedImage**](UploadedImage.md)

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

# **credentials_orgs_users_issuers_authority_create**
> IssuerAuthority credentials_orgs_users_issuers_authority_create(org, user_id, issuer_authority)



API View for managing issuer authorities (signatories).  This endpoint allows creating authorities/signatories that can be associated with issuers or specific credentials.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Methods:     POST: Create a new issuer authority  POST Request Body:     A JSON object containing authority details:     - name (str, required): Name of the signatory     - title (str, required): Title of the signatory     - signature (str, required): URL to the signature image     - org (str, optional): Organization identifier to associate with an issuer     - entityId (str, optional): Issuer entity ID to associate with     - credential (str, optional): Credential entity ID to associate with  Returns:     POST: A JSON response containing the created authority:         {             \"data\": {                 \"name\": \"John Smith\",                 \"title\": \"President\",                 \"signature\": \"https://example.com/signatures/john-smith.png\"             }         }  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the issuer or credential doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage authorities

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



API View for managing credential issuers.  This endpoint allows creating and retrieving issuers for a specific organization/tenant, with support for filtering and pagination.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Query Parameters:     q (str, optional): Search term to filter issuers by name     limit (int, optional): Number of results per page (default: 50)     offset (int, optional): Starting position for pagination  Methods:     GET: Retrieve issuers with filtering and pagination     POST: Create a new issuer  POST Request Body:     A JSON object containing issuer details:     - name (str): Issuer name     - iconImage (str, optional): URL to issuer icon     - email (str, optional): Contact email for the issuer     - url (str, optional): Website URL for the issuer     - allowed_template_tags (array, optional): List of allowed template tags  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {                 \"next\": \"URL to next page\",                 \"previous\": \"URL to previous page\",                 \"count\": 10,                 \"data\": [                     {issuer object},                     {issuer object},                     ...                 ],                 \"num_pages\": 1,                 \"page_number\": 1,                 \"max_page_size\": 1000             }         }      POST: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Created\"},             \"result\": {issuer object}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the platform doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage issuers

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



API View for managing individual issuers.  This endpoint allows retrieving, updating, and deleting specific issuers identified by their entity_id or org identifier.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The issuer entity ID or org identifier  Methods:     GET: Retrieve a specific issuer     PUT: Update a specific issuer     DELETE: Delete a specific issuer  PUT Request Body:     A JSON object containing issuer details to update:     - name (str, optional): Issuer name     - iconImage (str, optional): URL to issuer icon     - email (str, optional): Contact email for the issuer     - url (str, optional): Website URL for the issuer     - allowed_template_tags (array, optional): List of allowed template tags  Returns:     GET: A JSON response containing the issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/logo.png\",                 \"allowed_template_tags\": [...]             }         ]      PUT: A JSON response containing the updated issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/new-logo.png\",                 \"allowed_template_tags\": [...]             }         ]      DELETE: A JSON response indicating success:         {             \"status\": {\"success\": true, \"description\": \"Deleted\"}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the issuer doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage issuers

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



API View for managing credential issuers.  This endpoint allows creating and retrieving issuers for a specific organization/tenant, with support for filtering and pagination.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request  Query Parameters:     q (str, optional): Search term to filter issuers by name     limit (int, optional): Number of results per page (default: 50)     offset (int, optional): Starting position for pagination  Methods:     GET: Retrieve issuers with filtering and pagination     POST: Create a new issuer  POST Request Body:     A JSON object containing issuer details:     - name (str): Issuer name     - iconImage (str, optional): URL to issuer icon     - email (str, optional): Contact email for the issuer     - url (str, optional): Website URL for the issuer     - allowed_template_tags (array, optional): List of allowed template tags  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {                 \"next\": \"URL to next page\",                 \"previous\": \"URL to previous page\",                 \"count\": 10,                 \"data\": [                     {issuer object},                     {issuer object},                     ...                 ],                 \"num_pages\": 1,                 \"page_number\": 1,                 \"max_page_size\": 1000             }         }      POST: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Created\"},             \"result\": {issuer object}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the platform doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage issuers

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



API View for managing individual issuers.  This endpoint allows retrieving, updating, and deleting specific issuers identified by their entity_id or org identifier.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The issuer entity ID or org identifier  Methods:     GET: Retrieve a specific issuer     PUT: Update a specific issuer     DELETE: Delete a specific issuer  PUT Request Body:     A JSON object containing issuer details to update:     - name (str, optional): Issuer name     - iconImage (str, optional): URL to issuer icon     - email (str, optional): Contact email for the issuer     - url (str, optional): Website URL for the issuer     - allowed_template_tags (array, optional): List of allowed template tags  Returns:     GET: A JSON response containing the issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/logo.png\",                 \"allowed_template_tags\": [...]             }         ]      PUT: A JSON response containing the updated issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/new-logo.png\",                 \"allowed_template_tags\": [...]             }         ]      DELETE: A JSON response indicating success:         {             \"status\": {\"success\": true, \"description\": \"Deleted\"}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the issuer doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage issuers

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



API View for managing individual issuers.  This endpoint allows retrieving, updating, and deleting specific issuers identified by their entity_id or org identifier.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The issuer entity ID or org identifier  Methods:     GET: Retrieve a specific issuer     PUT: Update a specific issuer     DELETE: Delete a specific issuer  PUT Request Body:     A JSON object containing issuer details to update:     - name (str, optional): Issuer name     - iconImage (str, optional): URL to issuer icon     - email (str, optional): Contact email for the issuer     - url (str, optional): Website URL for the issuer     - allowed_template_tags (array, optional): List of allowed template tags  Returns:     GET: A JSON response containing the issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/logo.png\",                 \"allowed_template_tags\": [...]             }         ]      PUT: A JSON response containing the updated issuer details:         [             {                 \"name\": \"Example University\",                 \"org\": \"example-university\",                 \"entityId\": \"abc123\",                 \"signatories\": [...],                 \"url\": \"https://example.com\",                 \"iconImage\": \"https://example.com/new-logo.png\",                 \"allowed_template_tags\": [...]             }         ]      DELETE: A JSON response indicating success:         {             \"status\": {\"success\": true, \"description\": \"Deleted\"}         }  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the issuer doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires IsAdminUserOrStudentDRFMixin     - Only authenticated users with appropriate permissions can manage issuers

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



Get all credentials for a platform with search and pagination support.  Query Parameters: - platform_org: Platform org ID (takes precedence over URL org) - page: Page number (default: 1) - page_size: Items per page (default: 10, max: 100) - search: Search term to filter credentials - course: Course ID to filter credentials - program: Program ID to filter credentials

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



API View for managing individual credentials.  This endpoint allows retrieving, updating, and deleting specific credentials identified by their entity_id.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  Methods:     GET: Retrieve a specific credential     PUT: Update a specific credential     DELETE: Delete a specific credential  PUT Request Body:     A JSON object containing credential details to update:     - name (str, optional): Credential name     - description (str, optional): Credential description     - credential_type (str, optional): Type of credential     - html_template (str, optional): HTML template for credential rendering     - css_template (str, optional): CSS template for credential styling     - icon_image (str, optional): URL to credential icon     - background_image (str, optional): URL to credential background     - thumbnail_image (str, optional): URL to credential thumbnail     - criteria_url (str, optional): URL to credential criteria     - criteria_text (str, optional): Text description of credential criteria     - issuing_signal (str, optional): Signal that triggers credential issuance  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {credential object}         }      PUT: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Updated\"},             \"result\": {credential object}         }      DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires CredentialAssignmentPermission     - Users can only manage credentials they have permission to access

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



API View for managing individual credentials.  This endpoint allows retrieving, updating, and deleting specific credentials identified by their entity_id.  Path Parameters:     org (str): The organization/tenant identifier     user_id (str): The user ID making the request     entity_id (str): The credential entity ID  Methods:     GET: Retrieve a specific credential     PUT: Update a specific credential     DELETE: Delete a specific credential  PUT Request Body:     A JSON object containing credential details to update:     - name (str, optional): Credential name     - description (str, optional): Credential description     - credential_type (str, optional): Type of credential     - html_template (str, optional): HTML template for credential rendering     - css_template (str, optional): CSS template for credential styling     - icon_image (str, optional): URL to credential icon     - background_image (str, optional): URL to credential background     - thumbnail_image (str, optional): URL to credential thumbnail     - criteria_url (str, optional): URL to credential criteria     - criteria_text (str, optional): Text description of credential criteria     - issuing_signal (str, optional): Signal that triggers credential issuance  Returns:     GET: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Ok\"},             \"result\": {credential object}         }      PUT: A JSON response containing:         {             \"status\": {\"success\": true, \"description\": \"Updated\"},             \"result\": {credential object}         }      DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid     401 Unauthorized: If the user is not authenticated     403 Forbidden: If the user does not have permission to access this resource     404 Not Found: If the credential doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Requires CredentialAssignmentPermission     - Users can only manage credentials they have permission to access

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
> Assertion credentials_public_assertions_retrieve(entity_id)



Public endpoint to retrieve a specific credential assertion by its entity ID.  This endpoint allows public access to view a specific credential assertion without authentication.  Path Parameters:     entity_id (str): The assertion entity ID  Returns:     A JSON response containing the assertion details using the AssertionSerializer format  Error Responses:     404 Not Found:         - If the assertion doesn't exist: Empty response with 404 status         - If the assertion has been revoked: JSON with error detail and revocation reason     500 Internal Server Error: If an unexpected error occurs

### Example


```python
import iblai
from iblai.models.assertion import Assertion
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.CredentialsApi(api_client)
entity_id = 'entity_id_example' # str | 

try:
    api_response = api_instance.credentials_public_assertions_retrieve(entity_id)
    print("The response of CredentialsApi->credentials_public_assertions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling CredentialsApi->credentials_public_assertions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

[**Assertion**](Assertion.md)

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

