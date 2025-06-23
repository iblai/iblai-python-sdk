# iblai.RolesApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_platform_orgs_roles_users_desired_roles_retrieve**](RolesApi.md#roles_platform_orgs_roles_users_desired_roles_retrieve) | **GET** /api/roles/platform/orgs/{org}/roles/users/{username}/desired-roles/ | 
[**roles_platform_orgs_roles_users_reported_roles_retrieve**](RolesApi.md#roles_platform_orgs_roles_users_reported_roles_retrieve) | **GET** /api/roles/platform/orgs/{org}/roles/users/{username}/reported-roles/ | 


# **roles_platform_orgs_roles_users_desired_roles_retrieve**
> DesiredRole roles_platform_orgs_roles_users_desired_roles_retrieve(org, username)



Retrieve a user's desired role information.  This endpoint returns the role and skills that a user has indicated they want to develop or acquire. This represents the user's career goals and learning objectives.  Path Parameters:     org (str): The platform/organization identifier     username (str): The username of the user to retrieve role information for  Returns:     The user's desired role information including:     - Target role title     - Skills needed for the role     - Current progress toward skill acquisition  Error Responses:     400 Bad Request: If the user doesn't exist in the platform or has no desired role     404 Not Found: If the specified platform doesn't exist

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.desired_role import DesiredRole
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
api_instance = iblai.RolesApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.roles_platform_orgs_roles_users_desired_roles_retrieve(org, username)
    print("The response of RolesApi->roles_platform_orgs_roles_users_desired_roles_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->roles_platform_orgs_roles_users_desired_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**DesiredRole**](DesiredRole.md)

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

# **roles_platform_orgs_roles_users_reported_roles_retrieve**
> ReportedRole roles_platform_orgs_roles_users_reported_roles_retrieve(org, username)



Retrieve a user's reported role information.  This endpoint returns the role and skills that a user has reported having in their profile. This represents the user's current skills and professional role.  Path Parameters:     org (str): The platform/organization identifier     username (str): The username of the user to retrieve role information for  Returns:     The user's reported role information including:     - Role title     - Skills associated with the role     - Experience level  Error Responses:     400 Bad Request: If the user doesn't exist in the platform or has no reported role     404 Not Found: If the specified platform doesn't exist

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.reported_role import ReportedRole
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
api_instance = iblai.RolesApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 

try:
    api_response = api_instance.roles_platform_orgs_roles_users_reported_roles_retrieve(org, username)
    print("The response of RolesApi->roles_platform_orgs_roles_users_reported_roles_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->roles_platform_orgs_roles_users_reported_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**ReportedRole**](ReportedRole.md)

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

