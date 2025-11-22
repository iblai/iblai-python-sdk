# iblai.AiSearchApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_search_orgs_users_my_mentors_retrieve**](AiSearchApi.md#ai_search_orgs_users_my_mentors_retrieve) | **GET** /api/ai-search/orgs/{org}/users/{username}/my-mentors/ | 
[**create_platform_prompt**](AiSearchApi.md#create_platform_prompt) | **POST** /api/ai-search/prompts/ | Create a new recommendation prompt
[**create_platform_prompt2**](AiSearchApi.md#create_platform_prompt2) | **POST** /api/ai-search/recommendation/prompts/ | Create a new recommendation prompt
[**delete_platform_prompt**](AiSearchApi.md#delete_platform_prompt) | **DELETE** /api/ai-search/prompts/ | Delete a recommendation prompt
[**delete_platform_prompt2**](AiSearchApi.md#delete_platform_prompt2) | **DELETE** /api/ai-search/recommendation/prompts/ | Delete a recommendation prompt
[**list_platform_prompts**](AiSearchApi.md#list_platform_prompts) | **GET** /api/ai-search/prompts/ | List recommendation prompts for a platform
[**list_platform_prompts2**](AiSearchApi.md#list_platform_prompts2) | **GET** /api/ai-search/recommendation/prompts/ | List recommendation prompts for a platform
[**update_platform_prompt**](AiSearchApi.md#update_platform_prompt) | **PUT** /api/ai-search/prompts/ | Update an existing recommendation prompt
[**update_platform_prompt2**](AiSearchApi.md#update_platform_prompt2) | **PUT** /api/ai-search/recommendation/prompts/ | Update an existing recommendation prompt
[**v2_course_recommendations**](AiSearchApi.md#v2_course_recommendations) | **GET** /api/ai-search/recommendations/ | Generate AI-driven course recommendations
[**v2_global_mentor_search**](AiSearchApi.md#v2_global_mentor_search) | **GET** /api/ai-search/mentors/ | Search and filter AI mentors across the platform
[**v2_personalized_mentors**](AiSearchApi.md#v2_personalized_mentors) | **GET** /api/ai-search/personalized-mentors/ | Get mentors created by a specific user


# **ai_search_orgs_users_my_mentors_retrieve**
> MentorSearchResponse ai_search_orgs_users_my_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)

Handle GET requests for my mentors.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_search_response import MentorSearchResponse
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
api_instance = iblai.AiSearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
audience = ['audience_example'] # List[str] | Filter by target audience (optional)
category = ['category_example'] # List[str] | Filter by mentor category (optional)
created_by = 'created_by_example' # str | Filter mentors created by specific user (optional)
featured = True # bool | Filter by featured status (optional)
id = 56 # int | Retrieve a specific mentor by ID (optional)
include_main_public_mentors = False # bool | Include public mentors from main tenant (optional) (default to False)
limit = 12 # int | Number of results per page (optional) (default to 12)
llm = ['llm_example'] # List[str] | Filter by language model type (optional)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_by = 'order_by_example' # str | Field to sort results by ('created_at', 'recently_accessed_at') (optional)
order_direction = 'desc' # str | Sort direction ('asc' or 'desc') (optional) (default to 'desc')
query = 'query_example' # str | Search term to filter mentors by name or description (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
tenant = 'tenant_example' # str | Filter by tenant/organization (optional)
unique_id = 'unique_id_example' # str | Retrieve a specific mentor by UUID (optional)

try:
    api_response = api_instance.ai_search_orgs_users_my_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)
    print("The response of AiSearchApi->ai_search_orgs_users_my_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->ai_search_orgs_users_my_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **audience** | [**List[str]**](str.md)| Filter by target audience | [optional] 
 **category** | [**List[str]**](str.md)| Filter by mentor category | [optional] 
 **created_by** | **str**| Filter mentors created by specific user | [optional] 
 **featured** | **bool**| Filter by featured status | [optional] 
 **id** | **int**| Retrieve a specific mentor by ID | [optional] 
 **include_main_public_mentors** | **bool**| Include public mentors from main tenant | [optional] [default to False]
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **llm** | [**List[str]**](str.md)| Filter by language model type | [optional] 
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_by** | **str**| Field to sort results by (&#39;created_at&#39;, &#39;recently_accessed_at&#39;) | [optional] 
 **order_direction** | **str**| Sort direction (&#39;asc&#39; or &#39;desc&#39;) | [optional] [default to &#39;desc&#39;]
 **query** | **str**| Search term to filter mentors by name or description | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **tenant** | **str**| Filter by tenant/organization | [optional] 
 **unique_id** | **str**| Retrieve a specific mentor by UUID | [optional] 

### Return type

[**MentorSearchResponse**](MentorSearchResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_prompt**
> PlatformPromptResponse create_platform_prompt(platform_prompt=platform_prompt)

Create a new recommendation prompt

Create a new recommendation prompt for a platform and SPA.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt import PlatformPrompt
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)
platform_prompt = {"platform_key":"acme-corp","recommendation_type":"courses","spa_url":"catalog.acme-corp.com","prompt_text":"Focus on technical skills and certifications...","active":true} # PlatformPrompt |  (optional)

try:
    # Create a new recommendation prompt
    api_response = api_instance.create_platform_prompt(platform_prompt=platform_prompt)
    print("The response of AiSearchApi->create_platform_prompt:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->create_platform_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_prompt** | [**PlatformPrompt**](PlatformPrompt.md)|  | [optional] 

### Return type

[**PlatformPromptResponse**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid data |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required |  -  |
**409** | Prompt already exists for this combination |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_prompt2**
> PlatformPromptResponse create_platform_prompt2(platform_prompt=platform_prompt)

Create a new recommendation prompt

Create a new recommendation prompt for a platform and SPA.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt import PlatformPrompt
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)
platform_prompt = {"platform_key":"acme-corp","recommendation_type":"courses","spa_url":"catalog.acme-corp.com","prompt_text":"Focus on technical skills and certifications...","active":true} # PlatformPrompt |  (optional)

try:
    # Create a new recommendation prompt
    api_response = api_instance.create_platform_prompt2(platform_prompt=platform_prompt)
    print("The response of AiSearchApi->create_platform_prompt2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->create_platform_prompt2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_prompt** | [**PlatformPrompt**](PlatformPrompt.md)|  | [optional] 

### Return type

[**PlatformPromptResponse**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid data |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required |  -  |
**409** | Prompt already exists for this combination |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_prompt**
> delete_platform_prompt()

Delete a recommendation prompt

Delete a recommendation prompt by ID. Must provide platform_key to verify ownership. This permanently removes the prompt.

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
api_instance = iblai.AiSearchApi(api_client)

try:
    # Delete a recommendation prompt
    api_instance.delete_platform_prompt()
except Exception as e:
    print("Exception when calling AiSearchApi->delete_platform_prompt: %s\n" % e)
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
**204** | Prompt deleted successfully |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required or platform mismatch |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_prompt2**
> delete_platform_prompt2()

Delete a recommendation prompt

Delete a recommendation prompt by ID. Must provide platform_key to verify ownership. This permanently removes the prompt.

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
api_instance = iblai.AiSearchApi(api_client)

try:
    # Delete a recommendation prompt
    api_instance.delete_platform_prompt2()
except Exception as e:
    print("Exception when calling AiSearchApi->delete_platform_prompt2: %s\n" % e)
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
**204** | Prompt deleted successfully |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required or platform mismatch |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_platform_prompts**
> List[PlatformPromptResponse] list_platform_prompts()

List recommendation prompts for a platform

Get all recommendation prompts for a specific platform. Optionally filter by SPA URL or recommendation type.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)

try:
    # List recommendation prompts for a platform
    api_response = api_instance.list_platform_prompts()
    print("The response of AiSearchApi->list_platform_prompts:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->list_platform_prompts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlatformPromptResponse]**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid parameters |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_platform_prompts2**
> List[PlatformPromptResponse] list_platform_prompts2()

List recommendation prompts for a platform

Get all recommendation prompts for a specific platform. Optionally filter by SPA URL or recommendation type.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)

try:
    # List recommendation prompts for a platform
    api_response = api_instance.list_platform_prompts2()
    print("The response of AiSearchApi->list_platform_prompts2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->list_platform_prompts2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlatformPromptResponse]**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid parameters |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_prompt**
> PlatformPromptResponse update_platform_prompt(platform_prompt=platform_prompt)

Update an existing recommendation prompt

Update an existing prompt by ID. Must provide platform_key to verify ownership.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt import PlatformPrompt
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)
platform_prompt = iblai.PlatformPrompt() # PlatformPrompt |  (optional)

try:
    # Update an existing recommendation prompt
    api_response = api_instance.update_platform_prompt(platform_prompt=platform_prompt)
    print("The response of AiSearchApi->update_platform_prompt:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->update_platform_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_prompt** | [**PlatformPrompt**](PlatformPrompt.md)|  | [optional] 

### Return type

[**PlatformPromptResponse**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required or platform mismatch |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_prompt2**
> PlatformPromptResponse update_platform_prompt2(platform_prompt=platform_prompt)

Update an existing recommendation prompt

Update an existing prompt by ID. Must provide platform_key to verify ownership.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.platform_prompt import PlatformPrompt
from iblai.models.platform_prompt_response import PlatformPromptResponse
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
api_instance = iblai.AiSearchApi(api_client)
platform_prompt = iblai.PlatformPrompt() # PlatformPrompt |  (optional)

try:
    # Update an existing recommendation prompt
    api_response = api_instance.update_platform_prompt2(platform_prompt=platform_prompt)
    print("The response of AiSearchApi->update_platform_prompt2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->update_platform_prompt2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_prompt** | [**PlatformPrompt**](PlatformPrompt.md)|  | [optional] 

### Return type

[**PlatformPromptResponse**](PlatformPromptResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**401** | Authentication required |  -  |
**403** | Admin permissions required or platform mismatch |  -  |
**404** | Prompt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_course_recommendations**
> V2RecommendationResponse v2_course_recommendations(assessment_id=assessment_id, context_type=context_type, difficulty_levels=difficulty_levels, domains=domains, include_main_catalog=include_main_catalog, include_user_history=include_user_history, include_user_skills=include_user_skills, k=k, limit=limit, page=page, page_size=page_size, platform_key=platform_key, platform_org=platform_org, ranking_prompt=ranking_prompt, ranking_strategy=ranking_strategy, recommendation_type=recommendation_type, search_terms=search_terms, spa_url=spa_url, trigger_source=trigger_source, use_llm_ranking=use_llm_ranking, use_rag_search=use_rag_search)

Generate AI-driven course recommendations


        Generate personalized course recommendations using AI that considers the user's
        learning history, organizational goals, and available courses.

        **Authentication Required:**
        - User must be authenticated
        - Platform key must be provided
        - User must have access to the specified platform

        **How It Works:**
        1. Fetches tenant's custom recommendation prompt (if configured)
        2. Analyzes user's course completion history and performance
        3. Reviews available course catalog
        4. Uses AI to match courses to user's needs and organizational goals
        5. Returns 3-5 courses with clear explanations

        **Tenant Prompts:**
        Each organization can configure custom prompts that guide recommendations.
        For example: "Prioritize leadership for sales roles" or "Focus on technical skills."

        **Use Cases:**
        - Manual recommendation requests by users
        - Post-assessment recommendations
        - Milestone-triggered suggestions
        - Learning path planning
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.v2_recommendation_response import V2RecommendationResponse
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
api_instance = iblai.AiSearchApi(api_client)
assessment_id = 'assessment_id_example' # str | Assessment ID if triggered by assessment completion (optional)
context_type = 'context_type_example' # str | Context type for recommendation (e.g., 'assessment_completed', 'milestone_reached') (optional)
difficulty_levels = 'difficulty_levels_example' # str | Filter recommendations to specific difficulty levels (CSV) (optional)
domains = 'domains_example' # str | Filter recommendations to specific domains (CSV) (optional)
include_main_catalog = False # bool | Include items from 'main' tenant catalog IN ADDITION TO platform-specific catalog. By default, only platform-specific data is returned (tenant isolation). Set to True to also include shared 'main' tenant resources. (optional) (default to False)
include_user_history = False # bool | Include user's learning history (completed courses, topics) in the RAG search query. Helps find content that builds on their background. (optional) (default to False)
include_user_skills = False # bool | Include user's skills and badges in the RAG search query. Helps personalize results based on what the user already knows. (optional) (default to False)
k = 20 # int | Number of similar items to retrieve via RAG per tenant (before filtering). Higher values give more options but may be slower. (optional) (default to 20)
limit = 5 # int | Number of course recommendations to return (max 20) (optional) (default to 5)
page = 1 # int | Page number for pagination (starts at 1) (optional) (default to 1)
page_size = 10 # int | Number of recommendations per page (max 100) (optional) (default to 10)
platform_key = 'platform_key_example' # str | Platform key for tenant-scoped recommendations (optional)
platform_org = 'platform_org_example' # str | Platform org identifier (optional - avoids database lookup if provided) (optional)
ranking_prompt = 'ranking_prompt_example' # str | Custom prompt for LLM ranking (only if ranking_strategy='custom'). Define how the LLM should evaluate and order the recommendations. (optional)
ranking_strategy = 'ranking_strategy_example' # str | Strategy for LLM ranking. Only used if use_llm_ranking=True.  * `relevance` - Rank by relevance and value (default) * `difficulty` - Rank by difficulty progression * `personalized` - Personalize to user context and goals * `custom` - Use custom ranking prompt (optional)
recommendation_type = courses # str | Type of resource to recommend. Catalog types (courses/programs/resources/pathways) will use the platform's 'catalog' prompt category if configured.  * `mentors` - Mentor Recommendations * `courses` - Course Recommendations * `programs` - Program Recommendations * `resources` - Resource Recommendations * `pathways` - Pathway Recommendations (optional) (default to courses)
search_terms = 'search_terms_example' # str | Search terms to find similar content (e.g., 'leadership', 'data science'). Used to build the RAG query. (optional)
spa_url = 'spa_url_example' # str | Frontend/SPA identifier (e.g., 'catalog.example.com', 'mentor-ai.ibl.com'). Used to retrieve the correct prompt for that specific frontend. Auto-detected from HTTP_REFERER if not provided. (optional)
trigger_source = 'manual' # str | What triggered this recommendation request (optional) (default to 'manual')
use_llm_ranking = False # bool | Use LLM to rank and personalize RAG results. Adds AI-generated reasoning but increases cost and latency. Only applies if use_rag_search=True. (optional) (default to False)
use_rag_search = True # bool | Use RAG similarity search instead of full LLM catalog review. Faster and more cost-effective. Set to False for legacy LLM-only behavior. (optional) (default to True)

try:
    # Generate AI-driven course recommendations
    api_response = api_instance.v2_course_recommendations(assessment_id=assessment_id, context_type=context_type, difficulty_levels=difficulty_levels, domains=domains, include_main_catalog=include_main_catalog, include_user_history=include_user_history, include_user_skills=include_user_skills, k=k, limit=limit, page=page, page_size=page_size, platform_key=platform_key, platform_org=platform_org, ranking_prompt=ranking_prompt, ranking_strategy=ranking_strategy, recommendation_type=recommendation_type, search_terms=search_terms, spa_url=spa_url, trigger_source=trigger_source, use_llm_ranking=use_llm_ranking, use_rag_search=use_rag_search)
    print("The response of AiSearchApi->v2_course_recommendations:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->v2_course_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assessment_id** | **str**| Assessment ID if triggered by assessment completion | [optional] 
 **context_type** | **str**| Context type for recommendation (e.g., &#39;assessment_completed&#39;, &#39;milestone_reached&#39;) | [optional] 
 **difficulty_levels** | **str**| Filter recommendations to specific difficulty levels (CSV) | [optional] 
 **domains** | **str**| Filter recommendations to specific domains (CSV) | [optional] 
 **include_main_catalog** | **bool**| Include items from &#39;main&#39; tenant catalog IN ADDITION TO platform-specific catalog. By default, only platform-specific data is returned (tenant isolation). Set to True to also include shared &#39;main&#39; tenant resources. | [optional] [default to False]
 **include_user_history** | **bool**| Include user&#39;s learning history (completed courses, topics) in the RAG search query. Helps find content that builds on their background. | [optional] [default to False]
 **include_user_skills** | **bool**| Include user&#39;s skills and badges in the RAG search query. Helps personalize results based on what the user already knows. | [optional] [default to False]
 **k** | **int**| Number of similar items to retrieve via RAG per tenant (before filtering). Higher values give more options but may be slower. | [optional] [default to 20]
 **limit** | **int**| Number of course recommendations to return (max 20) | [optional] [default to 5]
 **page** | **int**| Page number for pagination (starts at 1) | [optional] [default to 1]
 **page_size** | **int**| Number of recommendations per page (max 100) | [optional] [default to 10]
 **platform_key** | **str**| Platform key for tenant-scoped recommendations | [optional] 
 **platform_org** | **str**| Platform org identifier (optional - avoids database lookup if provided) | [optional] 
 **ranking_prompt** | **str**| Custom prompt for LLM ranking (only if ranking_strategy&#x3D;&#39;custom&#39;). Define how the LLM should evaluate and order the recommendations. | [optional] 
 **ranking_strategy** | **str**| Strategy for LLM ranking. Only used if use_llm_ranking&#x3D;True.  * &#x60;relevance&#x60; - Rank by relevance and value (default) * &#x60;difficulty&#x60; - Rank by difficulty progression * &#x60;personalized&#x60; - Personalize to user context and goals * &#x60;custom&#x60; - Use custom ranking prompt | [optional] 
 **recommendation_type** | **str**| Type of resource to recommend. Catalog types (courses/programs/resources/pathways) will use the platform&#39;s &#39;catalog&#39; prompt category if configured.  * &#x60;mentors&#x60; - Mentor Recommendations * &#x60;courses&#x60; - Course Recommendations * &#x60;programs&#x60; - Program Recommendations * &#x60;resources&#x60; - Resource Recommendations * &#x60;pathways&#x60; - Pathway Recommendations | [optional] [default to courses]
 **search_terms** | **str**| Search terms to find similar content (e.g., &#39;leadership&#39;, &#39;data science&#39;). Used to build the RAG query. | [optional] 
 **spa_url** | **str**| Frontend/SPA identifier (e.g., &#39;catalog.example.com&#39;, &#39;mentor-ai.ibl.com&#39;). Used to retrieve the correct prompt for that specific frontend. Auto-detected from HTTP_REFERER if not provided. | [optional] 
 **trigger_source** | **str**| What triggered this recommendation request | [optional] [default to &#39;manual&#39;]
 **use_llm_ranking** | **bool**| Use LLM to rank and personalize RAG results. Adds AI-generated reasoning but increases cost and latency. Only applies if use_rag_search&#x3D;True. | [optional] [default to False]
 **use_rag_search** | **bool**| Use RAG similarity search instead of full LLM catalog review. Faster and more cost-effective. Set to False for legacy LLM-only behavior. | [optional] [default to True]

### Return type

[**V2RecommendationResponse**](V2RecommendationResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request - invalid parameters or missing required fields |  -  |
**401** | Unauthorized - authentication required |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_global_mentor_search**
> V2GlobalMentorSearchResponse v2_global_mentor_search(category=category, created_by=created_by, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, platform_key=platform_key, query=query, subjects=subjects, tenant=tenant, types=types, visibility=visibility)

Search and filter AI mentors across the platform


        Search and filter AI mentors with support for comprehensive filtering, pagination, and detailed mentor information.
        This endpoint supports both anonymous and authenticated users with different access levels.

        **Anonymous Users:**
        - Access to public mentors only (VIEWABLE_BY_ANYONE)
        - Limited search capabilities
        - No personalization

        **Authenticated Users:**
        - Full access based on platform permissions (scoped to requested platform)
        - Personalized results
        - Access to tenant-specific mentors

        **Required Parameters (Authenticated Users):**
        - `platform_key` OR `tenant`: Platform key for RBAC enforcement (required for authenticated requests)
          - Use `platform_key` (preferred) or `tenant` (backward compatibility) - both serve the same purpose
          - If both are provided, `platform_key` takes precedence

        **Available Filters:**
        - `query`: Search term to filter mentors by name or description
        - `tenant`: Filter by tenant/organization platform key(s) - can also be used as alias for `platform_key` (backward compatibility)
        - `category`: Filter by mentor category (comma-separated)
        - `subjects`: Filter by mentor subject (comma-separated)
        - `types`: Filter by mentor type (comma-separated)
        - `llm`: Filter by LLM provider (comma-separated, e.g., GPT-4, Claude)
        - `visibility`: Filter by visibility level (comma-separated: viewable_by_anyone, viewable_by_tenant_students, viewable_by_tenant_admins)
        - `created_by`: Filter mentors created by specific user (for personalized search)
        - `include_main_public_mentors`: Include main tenant public mentors

        **Facets:**
        The response includes facets with aggregated counts for all filterable attributes:
        - categories, subjects, types, llm_providers, visibility
        All facet values can be used as filter parameters in subsequent requests.

        Notes:
        - Detail view is removed; use the ibl_ai_mentor app for mentor details
        - include_main_public_mentors=true shows only VIEWABLE_BY_ANYONE mentors from the main tenant across tenants
        - For authenticated requests, either `platform_key` or `tenant` is required when username is provided
        - `tenant` parameter serves dual purpose: as a filter for multiple tenants, or as an alias for `platform_key` (backward compatibility)
        - Frontend uses `llm` parameter name (backend maps to `llm_provider` automatically)
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.v2_global_mentor_search_response import V2GlobalMentorSearchResponse
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
api_instance = iblai.AiSearchApi(api_client)
category = 'category_example' # str | Mentor category filter (optional)
created_by = 'created_by_example' # str | Filter mentors created by specific user (for personalized search) (optional)
include_main_public_mentors = False # bool | Include main tenant public mentors (VIEWABLE_BY_ANYONE) when true (optional) (default to False)
limit = 56 # int | Number of results per page (optional)
llm = 'llm_example' # str | LLM provider filter (optional)
offset = 56 # int | Number of results to skip (optional)
platform_key = 'platform_key_example' # str | Platform key for RBAC enforcement. Required for authenticated requests. Can also use 'tenant' parameter as an alias (backward compatibility). (optional)
query = 'query_example' # str | Search query for mentors (optional)
subjects = 'subjects_example' # str | Mentor subject filter (optional)
tenant = 'tenant_example' # str | Tenant key(s) (CSV). Can be used as a filter for multiple tenants, or as an alias for 'platform_key' in authenticated requests (backward compatibility). (optional)
types = 'types_example' # str | Mentor type filter (optional)
visibility = 'visibility_example' # str | Mentor visibility filter (viewable_by_anyone, viewable_by_tenant_students, viewable_by_tenant_admins) (optional)

try:
    # Search and filter AI mentors across the platform
    api_response = api_instance.v2_global_mentor_search(category=category, created_by=created_by, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, platform_key=platform_key, query=query, subjects=subjects, tenant=tenant, types=types, visibility=visibility)
    print("The response of AiSearchApi->v2_global_mentor_search:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->v2_global_mentor_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Mentor category filter | [optional] 
 **created_by** | **str**| Filter mentors created by specific user (for personalized search) | [optional] 
 **include_main_public_mentors** | **bool**| Include main tenant public mentors (VIEWABLE_BY_ANYONE) when true | [optional] [default to False]
 **limit** | **int**| Number of results per page | [optional] 
 **llm** | **str**| LLM provider filter | [optional] 
 **offset** | **int**| Number of results to skip | [optional] 
 **platform_key** | **str**| Platform key for RBAC enforcement. Required for authenticated requests. Can also use &#39;tenant&#39; parameter as an alias (backward compatibility). | [optional] 
 **query** | **str**| Search query for mentors | [optional] 
 **subjects** | **str**| Mentor subject filter | [optional] 
 **tenant** | **str**| Tenant key(s) (CSV). Can be used as a filter for multiple tenants, or as an alias for &#39;platform_key&#39; in authenticated requests (backward compatibility). | [optional] 
 **types** | **str**| Mentor type filter | [optional] 
 **visibility** | **str**| Mentor visibility filter (viewable_by_anyone, viewable_by_tenant_students, viewable_by_tenant_admins) | [optional] 

### Return type

[**V2GlobalMentorSearchResponse**](V2GlobalMentorSearchResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request - invalid parameters |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_personalized_mentors**
> V2PersonalizedMentorsResponse v2_personalized_mentors(audience=audience, category=category, limit=limit, llm_providers=llm_providers, offset=offset, order_by=order_by, order_direction=order_direction, platform_key=platform_key, query=query, return_facet=return_facet, tags=tags, tenant=tenant, username=username, visibility=visibility)

Get mentors created by a specific user


        Get mentors created by a specific user within a given organization/platform.
        This endpoint provides a personalized view of the user's own mentors with
        support for filtering, pagination, and detailed mentor information.

        **Authentication Required:**
        - username: Required for personalized mentor access
        - platform_key OR tenant: Required for tenant-specific content (both serve the same purpose)
          - Use `platform_key` (preferred) or `tenant` (backward compatibility)
          - If both are provided, `platform_key` takes precedence

        **Features:**
        - User's own mentors only
        - Personalization data (access counts, last used)
        - Filtering and faceted search
        - Pagination support
        - Detail and list views
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.v2_personalized_mentors_response import V2PersonalizedMentorsResponse
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
api_instance = iblai.AiSearchApi(api_client)
audience = ['audience_example'] # List[str] | Filter by audience (optional)
category = 'category_example' # str | Mentor category filter (optional)
limit = 56 # int | Number of results per page (optional)
llm_providers = ['llm_providers_example'] # List[str] | Filter by LLM provider (optional)
offset = 56 # int | Number of results to skip (optional)
order_by = 'order_by_example' # str | Field to sort by (optional)
order_direction = 'order_direction_example' # str | Sort direction  * `asc` - asc * `desc` - desc (optional)
platform_key = 'platform_key_example' # str | Platform key for authentication. Required for authenticated requests. Can also use 'tenant' parameter as an alias (backward compatibility). (optional)
query = 'query_example' # str | Search query for personalized mentors (optional)
return_facet = True # bool | Include facet data in response (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
tenant = 'tenant_example' # str | Tenant key (alias for 'platform_key' for backward compatibility). Can be used instead of 'platform_key' - both serve the same purpose. (optional)
username = 'username_example' # str | Username for authentication (required for unauthenticated requests) (optional)
visibility = ['visibility_example'] # List[str] | Filter by visibility (optional)

try:
    # Get mentors created by a specific user
    api_response = api_instance.v2_personalized_mentors(audience=audience, category=category, limit=limit, llm_providers=llm_providers, offset=offset, order_by=order_by, order_direction=order_direction, platform_key=platform_key, query=query, return_facet=return_facet, tags=tags, tenant=tenant, username=username, visibility=visibility)
    print("The response of AiSearchApi->v2_personalized_mentors:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiSearchApi->v2_personalized_mentors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience** | [**List[str]**](str.md)| Filter by audience | [optional] 
 **category** | **str**| Mentor category filter | [optional] 
 **limit** | **int**| Number of results per page | [optional] 
 **llm_providers** | [**List[str]**](str.md)| Filter by LLM provider | [optional] 
 **offset** | **int**| Number of results to skip | [optional] 
 **order_by** | **str**| Field to sort by | [optional] 
 **order_direction** | **str**| Sort direction  * &#x60;asc&#x60; - asc * &#x60;desc&#x60; - desc | [optional] 
 **platform_key** | **str**| Platform key for authentication. Required for authenticated requests. Can also use &#39;tenant&#39; parameter as an alias (backward compatibility). | [optional] 
 **query** | **str**| Search query for personalized mentors | [optional] 
 **return_facet** | **bool**| Include facet data in response | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **tenant** | **str**| Tenant key (alias for &#39;platform_key&#39; for backward compatibility). Can be used instead of &#39;platform_key&#39; - both serve the same purpose. | [optional] 
 **username** | **str**| Username for authentication (required for unauthenticated requests) | [optional] 
 **visibility** | [**List[str]**](str.md)| Filter by visibility | [optional] 

### Return type

[**V2PersonalizedMentorsResponse**](V2PersonalizedMentorsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request - invalid parameters |  -  |
**401** | Unauthorized - missing credentials |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Mentor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

