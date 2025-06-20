# iblai.SkillsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skills_orgs_skills_list**](SkillsApi.md#skills_orgs_skills_list) | **GET** /api/skills/orgs/{org}/skills | 
[**skills_orgs_skills_percentile_list**](SkillsApi.md#skills_orgs_skills_percentile_list) | **GET** /api/skills/orgs/{org}/skills/percentile/ | 
[**skills_orgs_skills_percentile_retrieve**](SkillsApi.md#skills_orgs_skills_percentile_retrieve) | **GET** /api/skills/orgs/{org}/skills/{skill_id}/percentile/ | 
[**skills_orgs_skills_retrieve**](SkillsApi.md#skills_orgs_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/{skill_name}/ | 
[**skills_orgs_skills_thresholds_create**](SkillsApi.md#skills_orgs_skills_thresholds_create) | **POST** /api/skills/orgs/{org}/skills/thresholds/ | 
[**skills_orgs_skills_thresholds_destroy**](SkillsApi.md#skills_orgs_skills_thresholds_destroy) | **DELETE** /api/skills/orgs/{org}/skills/thresholds/ | 
[**skills_orgs_skills_thresholds_partial_update**](SkillsApi.md#skills_orgs_skills_thresholds_partial_update) | **PATCH** /api/skills/orgs/{org}/skills/thresholds/ | 
[**skills_orgs_skills_thresholds_retrieve**](SkillsApi.md#skills_orgs_skills_thresholds_retrieve) | **GET** /api/skills/orgs/{org}/skills/thresholds/ | 
[**skills_orgs_skills_users_desired_skills_retrieve**](SkillsApi.md#skills_orgs_skills_users_desired_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/desired-skills/ | 
[**skills_orgs_skills_users_point_percentile_retrieve**](SkillsApi.md#skills_orgs_skills_users_point_percentile_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/point-percentile/ | 
[**skills_orgs_skills_users_reported_skills_retrieve**](SkillsApi.md#skills_orgs_skills_users_reported_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/reported-skills/ | 
[**skills_orgs_skills_users_retrieve**](SkillsApi.md#skills_orgs_skills_users_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/ | 


# **skills_orgs_skills_list**
> List[SkillInfo] skills_orgs_skills_list(org)



List all available skills on the platform.  This endpoint returns information about all skills that can be acquired on the platform.  Path Parameters:     org (str): The platform/organization identifier  Returns:     A list of all skills with basic information about each skill.  Access Control:     - Platform admins can access this information     - All authenticated users can access this information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill_info import SkillInfo
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_list(org)
    print("The response of SkillsApi->skills_orgs_skills_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[SkillInfo]**](SkillInfo.md)

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

# **skills_orgs_skills_percentile_list**
> List[PointsPercentile] skills_orgs_skills_percentile_list(org)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.points_percentile import PointsPercentile
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_percentile_list(org)
    print("The response of SkillsApi->skills_orgs_skills_percentile_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_percentile_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**List[PointsPercentile]**](PointsPercentile.md)

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

# **skills_orgs_skills_percentile_retrieve**
> PointsPercentile skills_orgs_skills_percentile_retrieve(org, skill_id)



Retrieve percentile distribution for a specific skill.  This endpoint returns the percentile distribution of points earned by users for a specific skill.  Path Parameters:     skill_id (int): The ID of the skill to retrieve percentile information for     org (str, optional): The platform/organization identifier to filter results  Returns:     A list of percentile breakpoints for the specified skill.  Error Responses:     404 Not Found: If the specified skill doesn't exist  Access Control:     - Platform admins can access this information     - All authenticated users can access this information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.points_percentile import PointsPercentile
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
skill_id = 56 # int | 

try:
    api_response = api_instance.skills_orgs_skills_percentile_retrieve(org, skill_id)
    print("The response of SkillsApi->skills_orgs_skills_percentile_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_percentile_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **skill_id** | **int**|  | 

### Return type

[**PointsPercentile**](PointsPercentile.md)

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

# **skills_orgs_skills_retrieve**
> SkillDetail skills_orgs_skills_retrieve(org, skill_name)



Retrieve detailed information about a specific skill.  This endpoint returns comprehensive information about a specific skill, including its description, categories, and related courses.  Path Parameters:     org (str): The platform/organization identifier     skill_name (str): The name of the skill to retrieve details for  Returns:     Detailed information about the specified skill.  Error Responses:     404 Not Found: If the specified skill doesn't exist  Access Control:     - Platform admins can access this information     - All authenticated users can access this information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill_detail import SkillDetail
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
skill_name = 'skill_name_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_retrieve(org, skill_name)
    print("The response of SkillsApi->skills_orgs_skills_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **skill_name** | **str**|  | 

### Return type

[**SkillDetail**](SkillDetail.md)

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

# **skills_orgs_skills_thresholds_create**
> SkillThreshold skills_orgs_skills_thresholds_create(org, skill_threshold)



Manage skill thresholds for a platform.  This endpoint allows platform administrators to view, create, update, and delete skill thresholds. Skill thresholds define the minimum points required to consider a skill as acquired or mastered.  Path Parameters:     org (str): The platform/organization identifier  Methods:     GET: Retrieve all skill thresholds for the platform     POST: Create a new skill threshold     PATCH: Update an existing skill threshold     DELETE: Delete all skill thresholds for the platform  Request Body (POST):     name (str, required): The name of the threshold level (e.g., \"Beginner\", \"Intermediate\")     threshold (int, required): The minimum points required to reach this threshold  Request Body (PATCH):     name (str, required): The name of the existing threshold to update     threshold (int, required): The new minimum points value for this threshold  Returns:     GET: A list of all skill thresholds for the platform     POST/PATCH: The created or updated skill threshold with format:         {             \"name\": \"threshold_name\",             \"threshold\": threshold_value         }     DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     404 Not Found: If the specified platform doesn't exist or the threshold                   to update cannot be found  Access Control:     - Only platform administrators can access this endpoint

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill_threshold import SkillThreshold
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
skill_threshold = iblai.SkillThreshold() # SkillThreshold | 

try:
    api_response = api_instance.skills_orgs_skills_thresholds_create(org, skill_threshold)
    print("The response of SkillsApi->skills_orgs_skills_thresholds_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_thresholds_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **skill_threshold** | [**SkillThreshold**](SkillThreshold.md)|  | 

### Return type

[**SkillThreshold**](SkillThreshold.md)

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

# **skills_orgs_skills_thresholds_destroy**
> skills_orgs_skills_thresholds_destroy(org)



Manage skill thresholds for a platform.  This endpoint allows platform administrators to view, create, update, and delete skill thresholds. Skill thresholds define the minimum points required to consider a skill as acquired or mastered.  Path Parameters:     org (str): The platform/organization identifier  Methods:     GET: Retrieve all skill thresholds for the platform     POST: Create a new skill threshold     PATCH: Update an existing skill threshold     DELETE: Delete all skill thresholds for the platform  Request Body (POST):     name (str, required): The name of the threshold level (e.g., \"Beginner\", \"Intermediate\")     threshold (int, required): The minimum points required to reach this threshold  Request Body (PATCH):     name (str, required): The name of the existing threshold to update     threshold (int, required): The new minimum points value for this threshold  Returns:     GET: A list of all skill thresholds for the platform     POST/PATCH: The created or updated skill threshold with format:         {             \"name\": \"threshold_name\",             \"threshold\": threshold_value         }     DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     404 Not Found: If the specified platform doesn't exist or the threshold                   to update cannot be found  Access Control:     - Only platform administrators can access this endpoint

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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.skills_orgs_skills_thresholds_destroy(org)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_thresholds_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

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

# **skills_orgs_skills_thresholds_partial_update**
> SkillThreshold skills_orgs_skills_thresholds_partial_update(org, patched_skill_threshold=patched_skill_threshold)



Manage skill thresholds for a platform.  This endpoint allows platform administrators to view, create, update, and delete skill thresholds. Skill thresholds define the minimum points required to consider a skill as acquired or mastered.  Path Parameters:     org (str): The platform/organization identifier  Methods:     GET: Retrieve all skill thresholds for the platform     POST: Create a new skill threshold     PATCH: Update an existing skill threshold     DELETE: Delete all skill thresholds for the platform  Request Body (POST):     name (str, required): The name of the threshold level (e.g., \"Beginner\", \"Intermediate\")     threshold (int, required): The minimum points required to reach this threshold  Request Body (PATCH):     name (str, required): The name of the existing threshold to update     threshold (int, required): The new minimum points value for this threshold  Returns:     GET: A list of all skill thresholds for the platform     POST/PATCH: The created or updated skill threshold with format:         {             \"name\": \"threshold_name\",             \"threshold\": threshold_value         }     DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     404 Not Found: If the specified platform doesn't exist or the threshold                   to update cannot be found  Access Control:     - Only platform administrators can access this endpoint

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_skill_threshold import PatchedSkillThreshold
from iblai.models.skill_threshold import SkillThreshold
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
patched_skill_threshold = iblai.PatchedSkillThreshold() # PatchedSkillThreshold |  (optional)

try:
    api_response = api_instance.skills_orgs_skills_thresholds_partial_update(org, patched_skill_threshold=patched_skill_threshold)
    print("The response of SkillsApi->skills_orgs_skills_thresholds_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_thresholds_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_skill_threshold** | [**PatchedSkillThreshold**](PatchedSkillThreshold.md)|  | [optional] 

### Return type

[**SkillThreshold**](SkillThreshold.md)

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

# **skills_orgs_skills_thresholds_retrieve**
> SkillThreshold skills_orgs_skills_thresholds_retrieve(org)



Manage skill thresholds for a platform.  This endpoint allows platform administrators to view, create, update, and delete skill thresholds. Skill thresholds define the minimum points required to consider a skill as acquired or mastered.  Path Parameters:     org (str): The platform/organization identifier  Methods:     GET: Retrieve all skill thresholds for the platform     POST: Create a new skill threshold     PATCH: Update an existing skill threshold     DELETE: Delete all skill thresholds for the platform  Request Body (POST):     name (str, required): The name of the threshold level (e.g., \"Beginner\", \"Intermediate\")     threshold (int, required): The minimum points required to reach this threshold  Request Body (PATCH):     name (str, required): The name of the existing threshold to update     threshold (int, required): The new minimum points value for this threshold  Returns:     GET: A list of all skill thresholds for the platform     POST/PATCH: The created or updated skill threshold with format:         {             \"name\": \"threshold_name\",             \"threshold\": threshold_value         }     DELETE: No content (204)  Error Responses:     400 Bad Request: If the request data is invalid or missing required fields     404 Not Found: If the specified platform doesn't exist or the threshold                   to update cannot be found  Access Control:     - Only platform administrators can access this endpoint

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.skill_threshold import SkillThreshold
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_thresholds_retrieve(org)
    print("The response of SkillsApi->skills_orgs_skills_thresholds_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_thresholds_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

[**SkillThreshold**](SkillThreshold.md)

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

# **skills_orgs_skills_users_desired_skills_retrieve**
> DesiredSkill skills_orgs_skills_users_desired_skills_retrieve(org, user_id)



Retrieve a user's desired skills.  This endpoint returns the skills that a user has indicated they want to develop or acquire through the platform.  Path Parameters:     org (str): The platform/organization identifier     user_id (str): The username of the user to retrieve skill information for  Returns:     The user's desired skills information.  Error Responses:     400 Bad Request: If the user doesn't exist in the platform or has no desired skills     404 Not Found: If the specified platform doesn't exist  Access Control:     - Platform admins can access any user's information     - Users can access their own information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.desired_skill import DesiredSkill
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_users_desired_skills_retrieve(org, user_id)
    print("The response of SkillsApi->skills_orgs_skills_users_desired_skills_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_users_desired_skills_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**DesiredSkill**](DesiredSkill.md)

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

# **skills_orgs_skills_users_point_percentile_retrieve**
> UserSkillPointsPercentile skills_orgs_skills_users_point_percentile_retrieve(org, user_id)



Retrieve a user's total skill points and percentile ranking.  This endpoint returns the total skill points a user has earned across all skills and their percentile ranking compared to other users on the platform.  Path Parameters:     org (str): The platform/organization identifier     user_id (str): The username of the user to retrieve information for  Returns:     The user's total skill points and percentile ranking information:     - Username     - Total points earned across all skills     - Percentile ranking compared to other users  Access Control:     - Platform admins can access any user's information     - Users can access their own information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_skill_points_percentile import UserSkillPointsPercentile
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_users_point_percentile_retrieve(org, user_id)
    print("The response of SkillsApi->skills_orgs_skills_users_point_percentile_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_users_point_percentile_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserSkillPointsPercentile**](UserSkillPointsPercentile.md)

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

# **skills_orgs_skills_users_reported_skills_retrieve**
> ReportedSkill skills_orgs_skills_users_reported_skills_retrieve(org, user_id)



Retrieve a user's self-reported skills.  This endpoint returns the skills that a user has reported having prior to or outside of the platform learning experience.  Path Parameters:     org (str): The platform/organization identifier     user_id (str): The username of the user to retrieve skill information for  Returns:     The user's self-reported skills information.  Error Responses:     400 Bad Request: If the user doesn't exist in the platform or has no reported skills     404 Not Found: If the specified platform doesn't exist  Access Control:     - Platform admins can access any user's information     - Users can access their own information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.reported_skill import ReportedSkill
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_users_reported_skills_retrieve(org, user_id)
    print("The response of SkillsApi->skills_orgs_skills_users_reported_skills_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_users_reported_skills_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ReportedSkill**](ReportedSkill.md)

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

# **skills_orgs_skills_users_retrieve**
> UserSkill skills_orgs_skills_users_retrieve(org, user_id)



Retrieve a user's skill information.  This endpoint returns information about skills that a user has acquired through the platform. It can return all skills or filter by a specific skill.  Path Parameters:     org (str): The platform/organization identifier     user_id (str): The username of the user to retrieve skill information for  Query Parameters:     skill_name (str, optional): Filter results to a specific skill  Returns:     When skill_name is provided:         Details about the specific skill including points earned and percentile ranking      When skill_name is not provided:         A list of all skills the user has acquired with their points  Access Control:     - Platform admins can access any user's skill information     - Users can access their own skill information

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_skill import UserSkill
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
api_instance = iblai.SkillsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.skills_orgs_skills_users_retrieve(org, user_id)
    print("The response of SkillsApi->skills_orgs_skills_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SkillsApi->skills_orgs_skills_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserSkill**](UserSkill.md)

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

