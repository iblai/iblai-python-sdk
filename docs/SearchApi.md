# iblai.SearchApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_ai_search_retrieve**](SearchApi.md#search_ai_search_retrieve) | **GET** /api/search/ai-search/ | 
[**search_catalog_retrieve**](SearchApi.md#search_catalog_retrieve) | **GET** /api/search/catalog/ | 
[**search_mentors_documents_retrieve**](SearchApi.md#search_mentors_documents_retrieve) | **GET** /api/search/mentors/{mentor_unique_id}/documents/ | 
[**search_mentors_retrieve**](SearchApi.md#search_mentors_retrieve) | **GET** /api/search/mentors/ | 
[**search_orgs_users_mentors_retrieve**](SearchApi.md#search_orgs_users_mentors_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/mentors/ | 
[**search_orgs_users_prompts_retrieve**](SearchApi.md#search_orgs_users_prompts_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/prompts/ | 
[**search_orgs_users_recommended_retrieve**](SearchApi.md#search_orgs_users_recommended_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/recommended/ | 
[**search_personalized_catalog_retrieve**](SearchApi.md#search_personalized_catalog_retrieve) | **GET** /api/search/personalized-catalog/{username}/ | 
[**search_prompts_retrieve**](SearchApi.md#search_prompts_retrieve) | **GET** /api/search/prompts/ | 
[**search_users_orgs_users_retrieve**](SearchApi.md#search_users_orgs_users_retrieve) | **GET** /api/search/users/orgs/{org}/users/{username}/ | 


# **search_ai_search_retrieve**
> MentorSearchResponse search_ai_search_retrieve(audience=audience, category=category, created_by=created_by, filter_facet=filter_facet, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, page=page, page_size=page_size, query=query, tags=tags, tenant=tenant, unique_id=unique_id)



Legacy endpoint for backward compatible mentor search

### Example


```python
import iblai
from iblai.models.mentor_search_response import MentorSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
audience = ['audience_example'] # List[str] | Filter by target audience (optional)
category = ['category_example'] # List[str] | Filter by mentor category (optional)
created_by = 'created_by_example' # str | Filter mentors created by specific user (optional)
filter_facet = False # bool | If present, return only facets without results (optional) (default to False)
id = 56 # int | Retrieve a specific mentor by ID (optional)
limit = 12 # int | Number of results per page (optional) (default to 12)
llm = ['llm_example'] # List[str] | Filter by language model type (optional)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_by = 'order_by_example' # str | Field to sort results by ('created_at', 'recently_accessed_at') (optional)
order_direction = 'desc' # str | Sort direction ('asc' or 'desc') (optional) (default to 'desc')
page = 56 # int | Page number (1-based, used with page_size) (optional)
page_size = 56 # int | Number of results per page (optional)
query = 'query_example' # str | Search term to filter mentors by name or description (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
tenant = 'tenant_example' # str | Filter by tenant/organization (optional)
unique_id = 'unique_id_example' # str | Retrieve a specific mentor by UUID (optional)

try:
    api_response = api_instance.search_ai_search_retrieve(audience=audience, category=category, created_by=created_by, filter_facet=filter_facet, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, page=page, page_size=page_size, query=query, tags=tags, tenant=tenant, unique_id=unique_id)
    print("The response of SearchApi->search_ai_search_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_ai_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience** | [**List[str]**](str.md)| Filter by target audience | [optional] 
 **category** | [**List[str]**](str.md)| Filter by mentor category | [optional] 
 **created_by** | **str**| Filter mentors created by specific user | [optional] 
 **filter_facet** | **bool**| If present, return only facets without results | [optional] [default to False]
 **id** | **int**| Retrieve a specific mentor by ID | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **llm** | [**List[str]**](str.md)| Filter by language model type | [optional] 
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_by** | **str**| Field to sort results by (&#39;created_at&#39;, &#39;recently_accessed_at&#39;) | [optional] 
 **order_direction** | **str**| Sort direction (&#39;asc&#39; or &#39;desc&#39;) | [optional] [default to &#39;desc&#39;]
 **page** | **int**| Page number (1-based, used with page_size) | [optional] 
 **page_size** | **int**| Number of results per page | [optional] 
 **query** | **str**| Search term to filter mentors by name or description | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **tenant** | **str**| Filter by tenant/organization | [optional] 
 **unique_id** | **str**| Retrieve a specific mentor by UUID | [optional] 

### Return type

[**MentorSearchResponse**](MentorSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_catalog_retrieve**
> GlobalCatalogSearchResponse search_catalog_retrieve(allow_skill_search=allow_skill_search, alphabetical=alphabetical, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, order_ascending=order_ascending, order_by=order_by, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, promotion=promotion, query=query, resource_type=resource_type, return_facet=return_facet, return_items=return_items, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, tenant=tenant, topics=topics, update_facet=update_facet)



Search and filter content across the learning catalog.  This endpoint provides a powerful search interface for discovering content across multiple content types (courses, programs, pathways, skills, roles, resources). It supports full-text search, faceted filtering, and pagination.  Query Parameters:     query (str, optional): Search term to filter content by name or description     content (list, optional): Content types to include in results                              (courses, programs, pathways, skills, roles, resources)                              Default: [\"programs\", \"courses\", \"pathways\", \"skills\"]      # Filtering parameters     course_id (str, optional): Filter by specific course ID     program_id (str, optional): Filter by specific program ID     pathway_id (str, optional): Filter by specific pathway ID     skill_id (str, optional): Filter by specific skill ID     subject (list, optional): Filter by subject areas     tenant (list, optional): Filter by tenant/organization     topics (list, optional): Filter by topic areas     tags (list, optional): Filter by tags     level (list, optional): Filter by difficulty level     self_paced (list, optional): Filter by course format (self-paced, instructor-led)     promotion (list, optional): Filter by promotion status     language (list, optional): Filter by content language     certificate (list, optional): Filter by certificate type     program_type (list, optional): Filter by program type     duration (list, optional): Filter by course duration range     price (str, optional): Filter by price/audit status     resource_type (list, optional): Filter by resource type     skills (list, optional): Filter by skills      # Sorting and pagination     order_by (str, optional): Field to sort results by     order_ascending (bool, optional): Sort direction (default: false)     alphabetical (bool, optional): Sort alphabetically by name (default: false)     limit (int, optional): Number of results per page (default: 12, max: 100)     offset (int, optional): Starting position for pagination      # Response options     return_facet (bool, optional): Include facet data in response (default: true)     return_items (bool, optional): Include items in programs/pathways (default: false)     allow_skill_search (bool, optional): Enable skill-based search (default: false)     update_facet (str, optional): Force facet update  Returns:     A JSON response containing:     - results: List of content items with metadata     - count: Total number of matching items     - next: URL for the next page of results (if available)     - previous: URL for the previous page of results (if available)     - current_page: Current page number     - total_pages: Total number of pages     - facets: Aggregated counts for each filter category (if requested)  Each content item contains type-specific fields:     - Courses:         {             \"id\": 123,             \"type\": \"course\",             \"course_id\": \"CS101\",             \"name\": \"Introduction to Computer Science\",             \"description\": \"Learn the fundamentals of computer science\",             \"short_description\": \"CS fundamentals\",             \"image_url\": \"https://example.com/images/cs101.jpg\",             \"level\": \"Beginner\",             \"subject\": \"Computer Science\",             \"topics\": [\"Programming\", \"Algorithms\"],             \"tags\": [\"python\", \"coding\"],             \"language\": \"English\",             \"tenant\": \"example-university\",             \"self_paced\": true,             \"duration\": \"6 weeks\",             \"certificate\": \"Professional Certificate\",             \"price\": \"Free\",             \"skills\": [                 {\"id\": 1, \"name\": \"Python Programming\"},                 {\"id\": 2, \"name\": \"Algorithms\"}             ],             \"url\": \"https://example.com/courses/cs101\"         }      - Programs:         {             \"id\": 456,             \"type\": \"program\",             \"program_id\": \"PROG123\",             \"name\": \"Data Science Program\",             \"description\": \"Comprehensive data science curriculum\",             \"short_description\": \"Learn data science\",             \"image_url\": \"https://example.com/images/datascience.jpg\",             \"level\": \"Intermediate\",             \"subject\": \"Data Science\",             \"topics\": [\"Machine Learning\", \"Statistics\"],             \"program_type\": \"Professional Certificate\",             \"courses\": [                 {\"id\": 123, \"name\": \"Introduction to Python\"},                 {\"id\": 124, \"name\": \"Statistics for Data Science\"}             ],             \"url\": \"https://example.com/programs/prog123\"         }      - Pathways:         {             \"id\": 789,             \"type\": \"pathway\",             \"pathway_id\": \"PATH456\",             \"name\": \"Software Engineering Career Path\",             \"description\": \"Complete pathway to become a software engineer\",             \"image_url\": \"https://example.com/images/swe-path.jpg\",             \"programs\": [                 {\"id\": 456, \"name\": \"Programming Fundamentals\"},                 {\"id\": 457, \"name\": \"Web Development\"}             ],             \"url\": \"https://example.com/pathways/path456\"         }      - Skills:         {             \"id\": 321,             \"type\": \"skill\",             \"name\": \"Machine Learning\",             \"description\": \"Building systems that learn from data\",             \"courses\": [                 {\"id\": 125, \"name\": \"Machine Learning Fundamentals\"}             ],             \"related_skills\": [                 {\"id\": 322, \"name\": \"Deep Learning\"}             ]         }      - Roles:         {             \"id\": 654,             \"type\": \"role\",             \"name\": \"Data Scientist\",             \"description\": \"Professional who analyzes and interprets complex data\",             \"skills\": [                 {\"id\": 321, \"name\": \"Machine Learning\"},                 {\"id\": 323, \"name\": \"Data Analysis\"}             ],             \"recommended_courses\": [                 {\"id\": 125, \"name\": \"Machine Learning Fundamentals\"}             ]         }      - Resources:         {             \"id\": 987,             \"type\": \"resource\",             \"name\": \"Python Cheat Sheet\",             \"description\": \"Quick reference guide for Python\",             \"resource_type\": \"PDF\",             \"url\": \"https://example.com/resources/python-cheatsheet.pdf\",             \"topics\": [\"Programming\", \"Python\"]         }  Error Responses:     500 Internal Server Error: If an unexpected error occurs during processing  Notes:     - Results are cached for performance     - The 'resources' content type is only included by default if IBL_ENABLE_RESOURCES_IN_FACET is true     - For debugging, add ?debug=true to see detailed information about skill matching

### Example


```python
import iblai
from iblai.models.global_catalog_search_response import GlobalCatalogSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
allow_skill_search = False # bool | Enable skill-based search (optional) (default to False)
alphabetical = False # bool | Sort alphabetically by name (optional) (default to False)
certificate = ['certificate_example'] # List[str] | Filter by certificate type (optional)
content = ['content_example'] # List[str] | Content types to include in results (optional)
course_id = 'course_id_example' # str | Filter by specific course ID (optional)
duration = ['duration_example'] # List[str] | Filter by course duration range (optional)
language = ['language_example'] # List[str] | Filter by content language (optional)
level = ['level_example'] # List[str] | Filter by difficulty level (optional)
limit = 12 # int | Number of results per page (optional) (default to 12)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_ascending = False # bool | Sort direction (optional) (default to False)
order_by = 'order_by_example' # str | Field to sort results by (optional)
pathway_id = 'pathway_id_example' # str | Filter by specific pathway ID (optional)
price = 'price_example' # str | Filter by price/audit status (optional)
program_id = 'program_id_example' # str | Filter by specific program ID (optional)
program_type = ['program_type_example'] # List[str] | Filter by program type (optional)
promotion = ['promotion_example'] # List[str] | Filter by promotion status (optional)
query = 'query_example' # str | Search term to filter content by name or description (optional)
resource_type = ['resource_type_example'] # List[str] | Filter by resource type (optional)
return_facet = True # bool | Include facet data in response (optional) (default to True)
return_items = False # bool | Include items in programs/pathways (optional) (default to False)
self_paced = ['self_paced_example'] # List[str] | Filter by course format (optional)
skill_id = 'skill_id_example' # str | Filter by specific skill ID (optional)
skills = ['skills_example'] # List[str] | Filter by skills (optional)
subject = ['subject_example'] # List[str] | Filter by subject areas (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
tenant = ['tenant_example'] # List[str] | Filter by tenant/organization (optional)
topics = ['topics_example'] # List[str] | Filter by topic areas (optional)
update_facet = 'update_facet_example' # str | Force facet update (optional)

try:
    api_response = api_instance.search_catalog_retrieve(allow_skill_search=allow_skill_search, alphabetical=alphabetical, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, order_ascending=order_ascending, order_by=order_by, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, promotion=promotion, query=query, resource_type=resource_type, return_facet=return_facet, return_items=return_items, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, tenant=tenant, topics=topics, update_facet=update_facet)
    print("The response of SearchApi->search_catalog_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_catalog_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_skill_search** | **bool**| Enable skill-based search | [optional] [default to False]
 **alphabetical** | **bool**| Sort alphabetically by name | [optional] [default to False]
 **certificate** | [**List[str]**](str.md)| Filter by certificate type | [optional] 
 **content** | [**List[str]**](str.md)| Content types to include in results | [optional] 
 **course_id** | **str**| Filter by specific course ID | [optional] 
 **duration** | [**List[str]**](str.md)| Filter by course duration range | [optional] 
 **language** | [**List[str]**](str.md)| Filter by content language | [optional] 
 **level** | [**List[str]**](str.md)| Filter by difficulty level | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_ascending** | **bool**| Sort direction | [optional] [default to False]
 **order_by** | **str**| Field to sort results by | [optional] 
 **pathway_id** | **str**| Filter by specific pathway ID | [optional] 
 **price** | **str**| Filter by price/audit status | [optional] 
 **program_id** | **str**| Filter by specific program ID | [optional] 
 **program_type** | [**List[str]**](str.md)| Filter by program type | [optional] 
 **promotion** | [**List[str]**](str.md)| Filter by promotion status | [optional] 
 **query** | **str**| Search term to filter content by name or description | [optional] 
 **resource_type** | [**List[str]**](str.md)| Filter by resource type | [optional] 
 **return_facet** | **bool**| Include facet data in response | [optional] [default to True]
 **return_items** | **bool**| Include items in programs/pathways | [optional] [default to False]
 **self_paced** | [**List[str]**](str.md)| Filter by course format | [optional] 
 **skill_id** | **str**| Filter by specific skill ID | [optional] 
 **skills** | [**List[str]**](str.md)| Filter by skills | [optional] 
 **subject** | [**List[str]**](str.md)| Filter by subject areas | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **tenant** | [**List[str]**](str.md)| Filter by tenant/organization | [optional] 
 **topics** | [**List[str]**](str.md)| Filter by topic areas | [optional] 
 **update_facet** | **str**| Force facet update | [optional] 

### Return type

[**GlobalCatalogSearchResponse**](GlobalCatalogSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_mentors_documents_retrieve**
> DocumentSearchResponse search_mentors_documents_retrieve(mentor_unique_id, access=access, document_type=document_type, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, platform_key=platform_key, query=query, training_status=training_status)



Search and filter documents associated with a specific mentor

### Example


```python
import iblai
from iblai.models.document_search_response import DocumentSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
mentor_unique_id = 'mentor_unique_id_example' # str | 
access = 'access_example' # str | Filter by access level (e.g., 'public', 'private') (optional)
document_type = 'document_type_example' # str | Filter by document type (e.g., 'pdf', 'text') (optional)
limit = 12 # int | Number of results per page (optional) (default to 12)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_by = 'order_by_example' # str | Field to sort results by ('date_created', 'last_modified', 'document_name') (optional)
order_direction = 'desc' # str | Sort direction ('asc' or 'desc') (optional) (default to 'desc')
platform_key = 'platform_key_example' # str | Filter by platform key (optional)
query = 'query_example' # str | Search term to filter documents by name or content (optional)
training_status = 'training_status_example' # str | Filter by training status (e.g., 'trained', 'pending') (optional)

try:
    api_response = api_instance.search_mentors_documents_retrieve(mentor_unique_id, access=access, document_type=document_type, limit=limit, offset=offset, order_by=order_by, order_direction=order_direction, platform_key=platform_key, query=query, training_status=training_status)
    print("The response of SearchApi->search_mentors_documents_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_mentors_documents_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor_unique_id** | **str**|  | 
 **access** | **str**| Filter by access level (e.g., &#39;public&#39;, &#39;private&#39;) | [optional] 
 **document_type** | **str**| Filter by document type (e.g., &#39;pdf&#39;, &#39;text&#39;) | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_by** | **str**| Field to sort results by (&#39;date_created&#39;, &#39;last_modified&#39;, &#39;document_name&#39;) | [optional] 
 **order_direction** | **str**| Sort direction (&#39;asc&#39; or &#39;desc&#39;) | [optional] [default to &#39;desc&#39;]
 **platform_key** | **str**| Filter by platform key | [optional] 
 **query** | **str**| Search term to filter documents by name or content | [optional] 
 **training_status** | **str**| Filter by training status (e.g., &#39;trained&#39;, &#39;pending&#39;) | [optional] 

### Return type

[**DocumentSearchResponse**](DocumentSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**404** | Mentor not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_mentors_retrieve**
> MentorSearchResponse search_mentors_retrieve(audience=audience, category=category, created_by=created_by, featured=featured, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)



Search and filter AI mentors across the platform.  This endpoint provides a powerful search interface for discovering AI mentors with support for filtering, pagination, and detailed mentor information.  Query Parameters:     # Identification parameters (for detail view)     id (int, optional): Retrieve a specific mentor by ID     unique_id (uuid, optional): Retrieve a specific mentor by UUID      # Search and filtering parameters     query (str, optional): Search term to filter mentors by name or description     tenant (str, optional): Filter by tenant/organization     llm (list, optional): Filter by language model type     audience (list, optional): Filter by target audience     category (list, optional): Filter by mentor category     tags (list, optional): Filter by tags     created_by (str, optional): Filter mentors created by specific user      # Sorting and pagination     order_by (str, optional): Field to sort results by ('created_at', 'recently_accessed_at')     order_direction (str, optional): Sort direction ('asc' or 'desc', default: 'desc')     limit (int, optional): Number of results per page (default: 12, max: 100)     offset (int, optional): Starting position for pagination  Returns:     For detail view (when id or unique_id is provided):         A JSON response containing a single mentor's details:         {             \"id\": 123,             \"unique_id\": \"550e8400-e29b-41d4-a716-446655440000\",             \"name\": \"Professor Smith\",             \"description\": \"AI mentor specializing in computer science\",             \"image_url\": \"https://example.com/images/prof-smith.jpg\",             \"llm\": {                 \"id\": 1,                 \"name\": \"GPT-4\",                 \"description\": \"Advanced language model\"             },             \"audience\": {                 \"id\": 2,                 \"name\": \"College Students\",                 \"description\": \"For university-level learners\"             },             \"category\": \"Computer Science\",             \"tags\": [\"programming\", \"algorithms\", \"data structures\"],             \"created_at\": \"2023-01-15T12:00:00Z\",             \"recently_accessed_at\": \"2023-06-20T15:30:00Z\",             \"platform\": {                 \"id\": 1,                 \"name\": \"Example University\",                 \"key\": \"example-university\"             },             \"visibility\": \"public\",             \"settings\": {                 \"temperature\": 0.7,                 \"max_tokens\": 1024,                 \"system_prompt\": \"You are Professor Smith, an expert in computer science...\"             }         }      For list view:         A JSON response containing:         {             \"results\": [                 {                     \"id\": 123,                     \"unique_id\": \"550e8400-e29b-41d4-a716-446655440000\",                     \"name\": \"Professor Smith\",                     \"description\": \"AI mentor specializing in computer science\",                     \"image_url\": \"https://example.com/images/prof-smith.jpg\",                     \"llm\": {\"id\": 1, \"name\": \"GPT-4\"},                     \"audience\": {\"id\": 2, \"name\": \"College Students\"},                     \"category\": \"Computer Science\",                     \"tags\": [\"programming\", \"algorithms\"],                     \"created_at\": \"2023-01-15T12:00:00Z\",                     \"recently_accessed_at\": \"2023-06-20T15:30:00Z\"                 },                 // Additional mentor objects...             ],             \"count\": 50,             \"next\": \"https://api.example.com/api/search/mentors/?limit=12&offset=12\",             \"previous\": null,             \"current_page\": 1,             \"num_pages\": 5,             \"facets\": {                 \"llm\": [                     {\"key\": \"GPT-4\", \"doc_count\": 30},                     {\"key\": \"Claude\", \"doc_count\": 20}                 ],                 \"audience\": [                     {\"key\": \"College Students\", \"doc_count\": 35},                     {\"key\": \"Professionals\", \"doc_count\": 15}                 ],                 \"category\": [                     {\"key\": \"Computer Science\", \"doc_count\": 25},                     {\"key\": \"Mathematics\", \"doc_count\": 15},                     {\"key\": \"Business\", \"doc_count\": 10}                 ]             }         }  Error Responses:     400 Bad Request: If the request parameters are invalid     404 Not Found: If the requested mentor doesn't exist     500 Internal Server Error: If an unexpected error occurs  Notes:     - Results are cached for performance     - Public mentors are visible to all users     - Private mentors are only visible to authorized users

### Example


```python
import iblai
from iblai.models.mentor_search_response import MentorSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
audience = ['audience_example'] # List[str] | Filter by target audience (optional)
category = ['category_example'] # List[str] | Filter by mentor category (optional)
created_by = 'created_by_example' # str | Filter mentors created by specific user (optional)
featured = True # bool | Filter by featured status (optional)
id = 56 # int | Retrieve a specific mentor by ID (optional)
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
    api_response = api_instance.search_mentors_retrieve(audience=audience, category=category, created_by=created_by, featured=featured, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)
    print("The response of SearchApi->search_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience** | [**List[str]**](str.md)| Filter by target audience | [optional] 
 **category** | [**List[str]**](str.md)| Filter by mentor category | [optional] 
 **created_by** | **str**| Filter mentors created by specific user | [optional] 
 **featured** | **bool**| Filter by featured status | [optional] 
 **id** | **int**| Retrieve a specific mentor by ID | [optional] 
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_orgs_users_mentors_retrieve**
> MentorSearchResponse search_orgs_users_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)



Handle GET requests for tenant-specific mentor search.  Args:     request: HTTP request object     org: Tenant/organization key     username: Username of the user making the request  Returns:     Response: DRF Response object with search results

### Example


```python
import iblai
from iblai.models.mentor_search_response import MentorSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
audience = ['audience_example'] # List[str] | Filter by target audience (optional)
category = ['category_example'] # List[str] | Filter by mentor category (optional)
created_by = 'created_by_example' # str | Filter mentors created by specific user (optional)
featured = True # bool | Filter by featured status (optional)
id = 56 # int | Retrieve a specific mentor by ID (optional)
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
    api_response = api_instance.search_orgs_users_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)
    print("The response of SearchApi->search_orgs_users_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_orgs_users_mentors_retrieve: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_orgs_users_prompts_retrieve**
> PromptSearchResponse search_orgs_users_prompts_retrieve(org, username, alphabetical=alphabetical, category=category, filter_facet=filter_facet, language=language, limit=limit, mentor=mentor, offset=offset, order_direction=order_direction, query=query, sort_by=sort_by, style=style, tenant=tenant, tone=tone)



Search and filter AI prompts for a specific user within a tenant.  This endpoint extends the base prompt search functionality but filters results to only show prompts that are available to a specific user within a specific organization/tenant.  Path Parameters:     org (str): The organization/tenant identifier     username (str): The username to filter prompts for  Query Parameters:     Same as PromptSearchView, plus:      # Identification parameters (for detail view)     id (int, optional): Retrieve a specific prompt by ID  Returns:     Same format as PromptSearchView, but filtered to only include prompts     that the specified user has access to within the specified organization.  Error Responses:     400 Bad Request: If the request parameters are invalid     403 Forbidden: If the requested prompt exists but the user doesn't have access     404 Not Found: If the requested prompt doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - Results are filtered based on user's permissions within the organization     - Private prompts are only visible to authorized users

### Example


```python
import iblai
from iblai.models.prompt_search_response import PromptSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
alphabetical = False # bool | Sort alphabetically (optional) (default to False)
category = 'category_example' # str | Filter by prompt category (optional)
filter_facet = True # bool | If true, return only facets without results (optional)
language = 'language_example' # str | Filter by prompt language (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
mentor = 'mentor_example' # str | Filter by mentor UUID (optional)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_direction = 'desc' # str | Sort direction ('asc' or 'desc') (optional) (default to 'desc')
query = 'query_example' # str | Search term to filter prompts by name or content (optional)
sort_by = 'sort_by_example' # str | Field to sort results by (optional)
style = 'style_example' # str | Filter by prompt style (optional)
tenant = 'tenant_example' # str | Filter by tenant/organization (optional)
tone = 'tone_example' # str | Filter by prompt tone (optional)

try:
    api_response = api_instance.search_orgs_users_prompts_retrieve(org, username, alphabetical=alphabetical, category=category, filter_facet=filter_facet, language=language, limit=limit, mentor=mentor, offset=offset, order_direction=order_direction, query=query, sort_by=sort_by, style=style, tenant=tenant, tone=tone)
    print("The response of SearchApi->search_orgs_users_prompts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_orgs_users_prompts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **alphabetical** | **bool**| Sort alphabetically | [optional] [default to False]
 **category** | **str**| Filter by prompt category | [optional] 
 **filter_facet** | **bool**| If true, return only facets without results | [optional] 
 **language** | **str**| Filter by prompt language | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **mentor** | **str**| Filter by mentor UUID | [optional] 
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_direction** | **str**| Sort direction (&#39;asc&#39; or &#39;desc&#39;) | [optional] [default to &#39;desc&#39;]
 **query** | **str**| Search term to filter prompts by name or content | [optional] 
 **sort_by** | **str**| Field to sort results by | [optional] 
 **style** | **str**| Filter by prompt style | [optional] 
 **tenant** | **str**| Filter by tenant/organization | [optional] 
 **tone** | **str**| Filter by prompt tone | [optional] 

### Return type

[**PromptSearchResponse**](PromptSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_orgs_users_recommended_retrieve**
> RecommendedCoursesResponse search_orgs_users_recommended_retrieve(org, username, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, query=query, resource_id=resource_id, resource_type=resource_type, role_id=role_id, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, topics=topics)



Determine whether to serve a detail view or a list view.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommended_courses_response import RecommendedCoursesResponse
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
api_instance = iblai.SearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
certificate = ['certificate_example'] # List[str] | Filter by certificate type (optional)
content = ["courses"] # List[str] | Content types to include in recommendations (courses, programs, pathways, skills, roles, resources) (optional) (default to ["courses"])
course_id = 'course_id_example' # str | Retrieve a specific course by ID (optional)
duration = ['duration_example'] # List[str] | Filter by course duration range (optional)
language = ['language_example'] # List[str] | Filter by content language (optional)
level = ['level_example'] # List[str] | Filter by difficulty level (optional)
limit = 12 # int | Number of results per page (optional) (default to 12)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
pathway_id = 'pathway_id_example' # str | Retrieve a specific pathway by ID (optional)
price = 'price_example' # str | Filter by price/audit status (optional)
program_id = 'program_id_example' # str | Retrieve a specific program by ID (optional)
program_type = ['program_type_example'] # List[str] | Filter by program type (optional)
query = 'query_example' # str | Search term to filter content by name or description (optional)
resource_id = 'resource_id_example' # str | Retrieve a specific resource by ID (optional)
resource_type = ['resource_type_example'] # List[str] | Filter by resource type (optional)
role_id = 'role_id_example' # str | Retrieve a specific role by ID (optional)
self_paced = ['self_paced_example'] # List[str] | Filter by course format (self-paced, instructor-led) (optional)
skill_id = 'skill_id_example' # str | Retrieve a specific skill by ID (optional)
skills = ['skills_example'] # List[str] | Filter by skills (optional)
subject = ['subject_example'] # List[str] | Filter by subject areas (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
topics = ['topics_example'] # List[str] | Filter by topic areas (optional)

try:
    api_response = api_instance.search_orgs_users_recommended_retrieve(org, username, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, query=query, resource_id=resource_id, resource_type=resource_type, role_id=role_id, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, topics=topics)
    print("The response of SearchApi->search_orgs_users_recommended_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_orgs_users_recommended_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **certificate** | [**List[str]**](str.md)| Filter by certificate type | [optional] 
 **content** | [**List[str]**](str.md)| Content types to include in recommendations (courses, programs, pathways, skills, roles, resources) | [optional] [default to [&quot;courses&quot;]]
 **course_id** | **str**| Retrieve a specific course by ID | [optional] 
 **duration** | [**List[str]**](str.md)| Filter by course duration range | [optional] 
 **language** | [**List[str]**](str.md)| Filter by content language | [optional] 
 **level** | [**List[str]**](str.md)| Filter by difficulty level | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **pathway_id** | **str**| Retrieve a specific pathway by ID | [optional] 
 **price** | **str**| Filter by price/audit status | [optional] 
 **program_id** | **str**| Retrieve a specific program by ID | [optional] 
 **program_type** | [**List[str]**](str.md)| Filter by program type | [optional] 
 **query** | **str**| Search term to filter content by name or description | [optional] 
 **resource_id** | **str**| Retrieve a specific resource by ID | [optional] 
 **resource_type** | [**List[str]**](str.md)| Filter by resource type | [optional] 
 **role_id** | **str**| Retrieve a specific role by ID | [optional] 
 **self_paced** | [**List[str]**](str.md)| Filter by course format (self-paced, instructor-led) | [optional] 
 **skill_id** | **str**| Retrieve a specific skill by ID | [optional] 
 **skills** | [**List[str]**](str.md)| Filter by skills | [optional] 
 **subject** | [**List[str]**](str.md)| Filter by subject areas | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **topics** | [**List[str]**](str.md)| Filter by topic areas | [optional] 

### Return type

[**RecommendedCoursesResponse**](RecommendedCoursesResponse.md)

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
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_personalized_catalog_retrieve**
> Dict[str, object] search_personalized_catalog_retrieve(username, allow_skill_search=allow_skill_search, alphabetical=alphabetical, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, order_ascending=order_ascending, order_by=order_by, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, promotion=promotion, query=query, recommended=recommended, resource_id=resource_id, resource_type=resource_type, return_facet=return_facet, return_items=return_items, role_id=role_id, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, tenant=tenant, topics=topics, update_facet=update_facet)



Determine whether to serve a detail view or a list view. If any detail-identifying parameters are present (course_id, program_id, etc.) the detail view is returned; otherwise the aggregated list view is returned.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
username = 'username_example' # str | 
allow_skill_search = False # bool | Enable skill-based search (optional) (default to False)
alphabetical = False # bool | Sort alphabetically by name (optional) (default to False)
certificate = ['certificate_example'] # List[str] | Filter by certificate type (optional)
content = ['content_example'] # List[str] | Content types to include in results (optional)
course_id = 'course_id_example' # str | Retrieve a specific course by ID (optional)
duration = ['duration_example'] # List[str] | Filter by course duration range (optional)
language = ['language_example'] # List[str] | Filter by content language (optional)
level = ['level_example'] # List[str] | Filter by difficulty level (optional)
limit = 12 # int | Number of results per page (optional) (default to 12)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_ascending = False # bool | Sort direction (optional) (default to False)
order_by = 'order_by_example' # str | Field to sort results by (optional)
pathway_id = 'pathway_id_example' # str | Retrieve a specific pathway by ID (optional)
price = 'price_example' # str | Filter by price/audit status (optional)
program_id = 'program_id_example' # str | Retrieve a specific program by ID (optional)
program_type = ['program_type_example'] # List[str] | Filter by program type (optional)
promotion = ['promotion_example'] # List[str] | Filter by promotion status (optional)
query = 'query_example' # str | Search term to filter content by name or description (optional)
recommended = False # bool | Show only recommended content (optional) (default to False)
resource_id = 'resource_id_example' # str | Retrieve a specific resource by ID (optional)
resource_type = ['resource_type_example'] # List[str] | Filter by resource type (optional)
return_facet = True # bool | Include facet data in response (optional) (default to True)
return_items = False # bool | Include items in programs/pathways (optional) (default to False)
role_id = 'role_id_example' # str | Retrieve a specific role by ID (optional)
self_paced = ['self_paced_example'] # List[str] | Filter by course format (optional)
skill_id = 'skill_id_example' # str | Retrieve a specific skill by ID (optional)
skills = ['skills_example'] # List[str] | Filter by skills (optional)
subject = ['subject_example'] # List[str] | Filter by subject areas (optional)
tags = ['tags_example'] # List[str] | Filter by tags (optional)
tenant = ['tenant_example'] # List[str] | Filter by tenant/organization (optional)
topics = ['topics_example'] # List[str] | Filter by topic areas (optional)
update_facet = 'update_facet_example' # str | Force facet update (optional)

try:
    api_response = api_instance.search_personalized_catalog_retrieve(username, allow_skill_search=allow_skill_search, alphabetical=alphabetical, certificate=certificate, content=content, course_id=course_id, duration=duration, language=language, level=level, limit=limit, offset=offset, order_ascending=order_ascending, order_by=order_by, pathway_id=pathway_id, price=price, program_id=program_id, program_type=program_type, promotion=promotion, query=query, recommended=recommended, resource_id=resource_id, resource_type=resource_type, return_facet=return_facet, return_items=return_items, role_id=role_id, self_paced=self_paced, skill_id=skill_id, skills=skills, subject=subject, tags=tags, tenant=tenant, topics=topics, update_facet=update_facet)
    print("The response of SearchApi->search_personalized_catalog_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_personalized_catalog_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **allow_skill_search** | **bool**| Enable skill-based search | [optional] [default to False]
 **alphabetical** | **bool**| Sort alphabetically by name | [optional] [default to False]
 **certificate** | [**List[str]**](str.md)| Filter by certificate type | [optional] 
 **content** | [**List[str]**](str.md)| Content types to include in results | [optional] 
 **course_id** | **str**| Retrieve a specific course by ID | [optional] 
 **duration** | [**List[str]**](str.md)| Filter by course duration range | [optional] 
 **language** | [**List[str]**](str.md)| Filter by content language | [optional] 
 **level** | [**List[str]**](str.md)| Filter by difficulty level | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 12]
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_ascending** | **bool**| Sort direction | [optional] [default to False]
 **order_by** | **str**| Field to sort results by | [optional] 
 **pathway_id** | **str**| Retrieve a specific pathway by ID | [optional] 
 **price** | **str**| Filter by price/audit status | [optional] 
 **program_id** | **str**| Retrieve a specific program by ID | [optional] 
 **program_type** | [**List[str]**](str.md)| Filter by program type | [optional] 
 **promotion** | [**List[str]**](str.md)| Filter by promotion status | [optional] 
 **query** | **str**| Search term to filter content by name or description | [optional] 
 **recommended** | **bool**| Show only recommended content | [optional] [default to False]
 **resource_id** | **str**| Retrieve a specific resource by ID | [optional] 
 **resource_type** | [**List[str]**](str.md)| Filter by resource type | [optional] 
 **return_facet** | **bool**| Include facet data in response | [optional] [default to True]
 **return_items** | **bool**| Include items in programs/pathways | [optional] [default to False]
 **role_id** | **str**| Retrieve a specific role by ID | [optional] 
 **self_paced** | [**List[str]**](str.md)| Filter by course format | [optional] 
 **skill_id** | **str**| Retrieve a specific skill by ID | [optional] 
 **skills** | [**List[str]**](str.md)| Filter by skills | [optional] 
 **subject** | [**List[str]**](str.md)| Filter by subject areas | [optional] 
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **tenant** | [**List[str]**](str.md)| Filter by tenant/organization | [optional] 
 **topics** | [**List[str]**](str.md)| Filter by topic areas | [optional] 
 **update_facet** | **str**| Force facet update | [optional] 

### Return type

**Dict[str, object]**

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

# **search_prompts_retrieve**
> PromptSearchResponse search_prompts_retrieve(alphabetical=alphabetical, category=category, filter_facet=filter_facet, language=language, limit=limit, mentor=mentor, offset=offset, order_direction=order_direction, query=query, sort_by=sort_by, style=style, tenant=tenant, tone=tone)



Search and filter AI prompts across the platform.  This endpoint provides a search interface for discovering AI prompts with support for filtering, pagination, and detailed prompt information.  Query Parameters:     # Identification parameters (for detail view)     id (int, optional): Retrieve a specific prompt by ID      # Search and filtering parameters     query (str, optional): Search term to filter prompts by name or content     category (str, optional): Filter by prompt category     language (str, optional): Filter by prompt language     style (str, optional): Filter by writing style     tone (str, optional): Filter by tone     tenant (str, optional): Filter by tenant/organization     mentor (str, optional): Filter by associated mentor (UUID)      # Sorting and pagination     sort_by (str, optional): Field to sort results by     order_direction (str, optional): Sort direction ('asc' or 'desc', default: 'desc')     alphabetical (bool, optional): Sort alphabetically by name (default: false)     limit (int, optional): Number of results per page (default: 10)     offset (int, optional): Starting position for pagination      # Special parameters     filter_facet (any, optional): If present, return only facets without results  Returns:     For detail view (when id is provided):         A JSON response containing a single prompt's details:         {             \"id\": 456,             \"name\": \"Essay Writing Guide\",             \"content\": \"Write a well-structured essay on the following topic: {{topic}}...\",             \"category\": \"Academic Writing\",             \"language\": \"English\",             \"style\": \"Formal\",             \"tone\": \"Professional\",             \"mentor\": {                 \"id\": 123,                 \"unique_id\": \"550e8400-e29b-41d4-a716-446655440000\",                 \"name\": \"Professor Smith\"             },             \"platform\": {                 \"id\": 1,                 \"name\": \"Example University\",                 \"key\": \"example-university\"             },             \"created_at\": \"2023-02-10T09:15:00Z\",             \"updated_at\": \"2023-05-05T14:20:00Z\",             \"visibility\": \"public\",             \"variables\": [\"topic\", \"length\", \"style\"]         }      For list view:         A JSON response containing:         {             \"results\": [                 {                     \"id\": 456,                     \"name\": \"Essay Writing Guide\",                     \"content\": \"Write a well-structured essay on the following topic: {{topic}}...\",                     \"category\": \"Academic Writing\",                     \"language\": \"English\",                     \"style\": \"Formal\",                     \"tone\": \"Professional\",                     \"mentor\": {\"id\": 123, \"name\": \"Professor Smith\"},                     \"created_at\": \"2023-02-10T09:15:00Z\",                     \"updated_at\": \"2023-05-05T14:20:00Z\"                 },                 // Additional prompt objects...             ],             \"count\": 30,             \"next\": \"?limit=10&offset=10\",             \"previous\": null,             \"current_page\": 1,             \"num_pages\": 3,             \"facets\": {                 \"category\": [                     {\"key\": \"Academic Writing\", \"doc_count\": 15},                     {\"key\": \"Creative Writing\", \"doc_count\": 10},                     {\"key\": \"Technical Documentation\", \"doc_count\": 5}                 ],                 \"language\": [                     {\"key\": \"English\", \"doc_count\": 25},                     {\"key\": \"Spanish\", \"doc_count\": 5}                 ],                 \"style\": [                     {\"key\": \"Formal\", \"doc_count\": 20},                     {\"key\": \"Casual\", \"doc_count\": 10}                 ],                 \"tone\": [                     {\"key\": \"Professional\", \"doc_count\": 15},                     {\"key\": \"Friendly\", \"doc_count\": 10},                     {\"key\": \"Technical\", \"doc_count\": 5}                 ]             }         }  Error Responses:     400 Bad Request: If the request parameters are invalid     403 Forbidden: If the requested prompt exists but is not publicly available     404 Not Found: If the requested prompt doesn't exist     500 Internal Server Error: If an unexpected error occurs  Notes:     - Only publicly available prompts are returned by default     - When filtering by mentor, the mentor ID must be a valid UUID

### Example


```python
import iblai
from iblai.models.prompt_search_response import PromptSearchResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.SearchApi(api_client)
alphabetical = False # bool | Sort alphabetically (optional) (default to False)
category = 'category_example' # str | Filter by prompt category (optional)
filter_facet = True # bool | If true, return only facets without results (optional)
language = 'language_example' # str | Filter by prompt language (optional)
limit = 10 # int | Number of results per page (optional) (default to 10)
mentor = 'mentor_example' # str | Filter by mentor UUID (optional)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
order_direction = 'desc' # str | Sort direction ('asc' or 'desc') (optional) (default to 'desc')
query = 'query_example' # str | Search term to filter prompts by name or content (optional)
sort_by = 'sort_by_example' # str | Field to sort results by (optional)
style = 'style_example' # str | Filter by prompt style (optional)
tenant = 'tenant_example' # str | Filter by tenant/organization (optional)
tone = 'tone_example' # str | Filter by prompt tone (optional)

try:
    api_response = api_instance.search_prompts_retrieve(alphabetical=alphabetical, category=category, filter_facet=filter_facet, language=language, limit=limit, mentor=mentor, offset=offset, order_direction=order_direction, query=query, sort_by=sort_by, style=style, tenant=tenant, tone=tone)
    print("The response of SearchApi->search_prompts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_prompts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alphabetical** | **bool**| Sort alphabetically | [optional] [default to False]
 **category** | **str**| Filter by prompt category | [optional] 
 **filter_facet** | **bool**| If true, return only facets without results | [optional] 
 **language** | **str**| Filter by prompt language | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **mentor** | **str**| Filter by mentor UUID | [optional] 
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **order_direction** | **str**| Sort direction (&#39;asc&#39; or &#39;desc&#39;) | [optional] [default to &#39;desc&#39;]
 **query** | **str**| Search term to filter prompts by name or content | [optional] 
 **sort_by** | **str**| Field to sort results by | [optional] 
 **style** | **str**| Filter by prompt style | [optional] 
 **tenant** | **str**| Filter by tenant/organization | [optional] 
 **tone** | **str**| Filter by prompt tone | [optional] 

### Return type

[**PromptSearchResponse**](PromptSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_orgs_users_retrieve**
> UserSearchResponse search_users_orgs_users_retrieve(org, username, department=department, education__degree=education__degree, education__field_of_study=education__field_of_study, education__institution=education__institution, include_membership_data=include_membership_data, limit=limit, offset=offset, q=q, user_resume__company=user_resume__company, user_resume__industry=user_resume__industry, user_resume__job_title=user_resume__job_title, user_resume__location=user_resume__location, user_resume__skills=user_resume__skills)



Search and filter users within a specific organization/tenant.  This endpoint provides a search interface for discovering users within an organization, with support for filtering by departments, pagination, and faceted filtering.  Path Parameters:     org (str): The organization/tenant identifier     username (str): The username of the user making the request  Query Parameters:     # Search parameters     query (str, optional): Search term to filter users by name, username, or email      # Department filtering     department_mode (bool, optional): Enable department-based filtering (default: false)     user_department (bool, optional): Legacy parameter for department_mode (default: false)     department (list, optional): Filter by specific departments      # Additional filters     role (list, optional): Filter by user role     status (list, optional): Filter by user status (active, inactive)     joined_date (list, optional): Filter by join date range     last_login (list, optional): Filter by last login date range      # Pagination     limit (int, optional): Number of results per page (default: 10)     offset (int, optional): Starting position for pagination  Returns:     A JSON response containing:     ```     {         \"results\": [             {                 \"id\": 123,                 \"username\": \"john.doe\",                 \"email\": \"john.doe@example.com\",                 \"first_name\": \"John\",                 \"last_name\": \"Doe\",                 \"full_name\": \"John Doe\",                 \"profile_image\": \"https://example.com/profiles/john-doe.jpg\",                 \"role\": \"Student\",                 \"departments\": [\"Computer Science\", \"Data Science\"],                 \"status\": \"active\",                 \"joined_date\": \"2023-01-15T12:00:00Z\",                 \"last_login\": \"2023-06-20T15:30:00Z\",                 \"metadata\": {                     \"location\": \"New York\",                     \"title\": \"Software Engineer\",                     \"bio\": \"Experienced software engineer with a passion for education\"                 }             },             // Additional user objects...         ],         \"count\": 50,         \"next\": \"https://api.example.com/api/search/users/example-org/admin/?limit=10&offset=10\",         \"previous\": null,         \"current_page\": 1,         \"total_pages\": 5,         \"facets\": {             \"role\": [                 {\"key\": \"Student\", \"doc_count\": 30},                 {\"key\": \"Instructor\", \"doc_count\": 15},                 {\"key\": \"Admin\", \"doc_count\": 5}             ],             \"department\": [                 {\"key\": \"Computer Science\", \"doc_count\": 20},                 {\"key\": \"Data Science\", \"doc_count\": 15},                 {\"key\": \"Business\", \"doc_count\": 10},                 {\"key\": \"Engineering\", \"doc_count\": 5}             ],             \"status\": [                 {\"key\": \"active\", \"doc_count\": 45},                 {\"key\": \"inactive\", \"doc_count\": 5}             ]         }     }     ``` Error Responses:     400 Bad Request: If the request parameters are invalid     403 Forbidden: If the user doesn't have department admin privileges (when using department_mode)     404 Not Found: If the user or organization doesn't exist     500 Internal Server Error: If an unexpected error occurs  Access Control:     - The requesting user must have an active account in the specified organization     - When department_mode is enabled, the user must be an admin of at least one department     - Department filtering restricts results to users in departments where the requesting user is an admin

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_search_response import UserSearchResponse
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
api_instance = iblai.SearchApi(api_client)
org = 'org_example' # str | 
username = 'username_example' # str | 
department = ['department_example'] # List[str] | Filter by department names (optional)
education__degree = 'education__degree_example' # str | Filter by degree (optional)
education__field_of_study = 'education__field_of_study_example' # str | Filter by field of study (optional)
education__institution = 'education__institution_example' # str | Filter by institution (optional)
include_membership_data = False # bool | Include user group membership data in results (optional) (default to False)
limit = 10 # int | Number of results per page (optional) (default to 10)
offset = 0 # int | Starting position for pagination (optional) (default to 0)
q = 'q_example' # str | Search term to filter users by name, email, or other attributes (optional)
user_resume__company = 'user_resume__company_example' # str | Filter by company (optional)
user_resume__industry = 'user_resume__industry_example' # str | Filter by industry (optional)
user_resume__job_title = 'user_resume__job_title_example' # str | Filter by job title (optional)
user_resume__location = 'user_resume__location_example' # str | Filter by location (optional)
user_resume__skills = 'user_resume__skills_example' # str | Filter by skills (optional)

try:
    api_response = api_instance.search_users_orgs_users_retrieve(org, username, department=department, education__degree=education__degree, education__field_of_study=education__field_of_study, education__institution=education__institution, include_membership_data=include_membership_data, limit=limit, offset=offset, q=q, user_resume__company=user_resume__company, user_resume__industry=user_resume__industry, user_resume__job_title=user_resume__job_title, user_resume__location=user_resume__location, user_resume__skills=user_resume__skills)
    print("The response of SearchApi->search_users_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling SearchApi->search_users_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **username** | **str**|  | 
 **department** | [**List[str]**](str.md)| Filter by department names | [optional] 
 **education__degree** | **str**| Filter by degree | [optional] 
 **education__field_of_study** | **str**| Filter by field of study | [optional] 
 **education__institution** | **str**| Filter by institution | [optional] 
 **include_membership_data** | **bool**| Include user group membership data in results | [optional] [default to False]
 **limit** | **int**| Number of results per page | [optional] [default to 10]
 **offset** | **int**| Starting position for pagination | [optional] [default to 0]
 **q** | **str**| Search term to filter users by name, email, or other attributes | [optional] 
 **user_resume__company** | **str**| Filter by company | [optional] 
 **user_resume__industry** | **str**| Filter by industry | [optional] 
 **user_resume__job_title** | **str**| Filter by job title | [optional] 
 **user_resume__location** | **str**| Filter by location | [optional] 
 **user_resume__skills** | **str**| Filter by skills | [optional] 

### Return type

[**UserSearchResponse**](UserSearchResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

