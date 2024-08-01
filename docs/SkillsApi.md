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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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

