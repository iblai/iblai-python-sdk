# iblai.V2Api

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_search_orgs_users_my_mentors_retrieve**](V2Api.md#v2_search_orgs_users_my_mentors_retrieve) | **GET** /api/v2/search/orgs/{org}/users/{username}/my-mentors/ | 


# **v2_search_orgs_users_my_mentors_retrieve**
> MentorSearchResponse v2_search_orgs_users_my_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)

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
api_instance = iblai.V2Api(api_client)
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
    api_response = api_instance.v2_search_orgs_users_my_mentors_retrieve(org, username, audience=audience, category=category, created_by=created_by, featured=featured, id=id, include_main_public_mentors=include_main_public_mentors, limit=limit, llm=llm, offset=offset, order_by=order_by, order_direction=order_direction, query=query, tags=tags, tenant=tenant, unique_id=unique_id)
    print("The response of V2Api->v2_search_orgs_users_my_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling V2Api->v2_search_orgs_users_my_mentors_retrieve: %s\n" % e)
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

