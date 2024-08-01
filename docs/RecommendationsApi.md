# iblai.RecommendationsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendations_orgs_users_retrieve**](RecommendationsApi.md#recommendations_orgs_users_retrieve) | **GET** /api/recommendations/orgs/{org}/users/{user_id}/ | 


# **recommendations_orgs_users_retrieve**
> RecommendationSearchAPI recommendations_orgs_users_retrieve(org, user_id)



API endpoint that returns a search api url prepopulated with context data See http://localhost:8000/api/schema/swagger-ui/#/recommendations

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommendation_search_api import RecommendationSearchAPI
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
api_instance = iblai.RecommendationsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.recommendations_orgs_users_retrieve(org, user_id)
    print("The response of RecommendationsApi->recommendations_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RecommendationsApi->recommendations_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**RecommendationSearchAPI**](RecommendationSearchAPI.md)

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

