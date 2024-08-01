# iblai.AiAnalyticsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_analytics_orgs_users_conversation_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_conversation_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/conversation/ | 
[**ai_analytics_orgs_users_costs_model_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_costs_model_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/model/ | 
[**ai_analytics_orgs_users_costs_model_usage_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_costs_model_usage_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/model-usage/ | 
[**ai_analytics_orgs_users_costs_permentor_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_costs_permentor_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/permentor/ | 
[**ai_analytics_orgs_users_costs_peruser_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_costs_peruser_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/peruser/ | 
[**ai_analytics_orgs_users_mentor_detail_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_mentor_detail_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/mentor-detail/ | 
[**ai_analytics_orgs_users_mentor_summary_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_mentor_summary_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/mentor-summary/ | 
[**ai_analytics_orgs_users_sentiment_count_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_sentiment_count_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/sentiment-count/ | 
[**ai_analytics_orgs_users_topics_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_topics_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/topics/ | 
[**ai_analytics_orgs_users_topics_summary_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_topics_summary_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/topics/summary/ | 
[**ai_analytics_orgs_users_traces_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_traces_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/ | 
[**ai_analytics_orgs_users_traces_retrieve2**](AiAnalyticsApi.md#ai_analytics_orgs_users_traces_retrieve2) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/{trace_id}/ | 
[**ai_analytics_orgs_users_traces_scores_create**](AiAnalyticsApi.md#ai_analytics_orgs_users_traces_scores_create) | **POST** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/scores/ | 
[**ai_analytics_orgs_users_traces_scores_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_traces_scores_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/scores/ | 
[**ai_analytics_orgs_users_transcripts_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_transcripts_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/transcripts/ | 
[**ai_analytics_orgs_users_user_feedback_retrieve**](AiAnalyticsApi.md#ai_analytics_orgs_users_user_feedback_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-feedback/ | 


# **ai_analytics_orgs_users_conversation_retrieve**
> ConversationVolume ai_analytics_orgs_users_conversation_retrieve(org, user_id, period=period)



Get the number of conversations for a given period of time  Options include today, yesterday, 7d, 30d, 90d  The start date and end date can also be specified in the format YYYY-MM-DD  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.conversation_volume import ConversationVolume
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
period = '7d' # str |  (optional) (default to '7d')

try:
    api_response = api_instance.ai_analytics_orgs_users_conversation_retrieve(org, user_id, period=period)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_conversation_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_conversation_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **period** | **str**|  | [optional] [default to &#39;7d&#39;]

### Return type

[**ConversationVolume**](ConversationVolume.md)

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

# **ai_analytics_orgs_users_costs_model_retrieve**
> ModelCost ai_analytics_orgs_users_costs_model_retrieve(end_date, org, start_date, user_id)



Retrieve the  model costs for a tenant  Filter parameters for period are start_date and enddate  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.model_cost import ModelCost
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_costs_model_retrieve(end_date, org, start_date, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_costs_model_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_costs_model_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModelCost**](ModelCost.md)

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

# **ai_analytics_orgs_users_costs_model_usage_retrieve**
> ModelUsage ai_analytics_orgs_users_costs_model_usage_retrieve(end_date, org, start_date, user_id)



Retrieve the  model usage data for a tenant  Filter parameters for period are start_date and enddate  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.model_usage import ModelUsage
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_costs_model_usage_retrieve(end_date, org, start_date, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_costs_model_usage_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_costs_model_usage_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModelUsage**](ModelUsage.md)

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

# **ai_analytics_orgs_users_costs_permentor_retrieve**
> TenantMentorTraces ai_analytics_orgs_users_costs_permentor_retrieve(end_date, org, start_date, user_id)



Get the cost of chats per mentor for a tenant.  Filter parameters for period are start_date and end_date  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tenant_mentor_traces import TenantMentorTraces
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_costs_permentor_retrieve(end_date, org, start_date, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_costs_permentor_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_costs_permentor_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 

### Return type

[**TenantMentorTraces**](TenantMentorTraces.md)

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

# **ai_analytics_orgs_users_costs_peruser_retrieve**
> LLMTracesListResponse ai_analytics_orgs_users_costs_peruser_retrieve(end_date, org, start_date, user_id)



Get the cost of chats per user for a tenant.  Filter parameters for period are start_date and end_date  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_traces_list_response import LLMTracesListResponse
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_costs_peruser_retrieve(end_date, org, start_date, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_costs_peruser_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_costs_peruser_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 

### Return type

[**LLMTracesListResponse**](LLMTracesListResponse.md)

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

# **ai_analytics_orgs_users_mentor_detail_retrieve**
> MentorDetailAnalytics ai_analytics_orgs_users_mentor_detail_retrieve(org, user_id)



This view returns analytics for the mentors such as total mentors, total active mentors and ratings for the mentors.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_detail_analytics import MentorDetailAnalytics
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_mentor_detail_retrieve(org, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_mentor_detail_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_mentor_detail_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorDetailAnalytics**](MentorDetailAnalytics.md)

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

# **ai_analytics_orgs_users_mentor_summary_retrieve**
> MentorDetailAnalytics ai_analytics_orgs_users_mentor_summary_retrieve(org, user_id)



This view returns analytics for the mentors such as total mentors, total active mentors and ratings for the mentors.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_detail_analytics import MentorDetailAnalytics
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_mentor_summary_retrieve(org, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_mentor_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_mentor_summary_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorDetailAnalytics**](MentorDetailAnalytics.md)

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

# **ai_analytics_orgs_users_sentiment_count_retrieve**
> UserSentimentCountView ai_analytics_orgs_users_sentiment_count_retrieve(org, user_id, period=period)



Get the number of messages for a given period of time  Filter parameters for period are today, yesterday, 7d, 30d, 90d  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_sentiment_count_view import UserSentimentCountView
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
period = '7d' # str |  (optional) (default to '7d')

try:
    api_response = api_instance.ai_analytics_orgs_users_sentiment_count_retrieve(org, user_id, period=period)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_sentiment_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_sentiment_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **period** | **str**|  | [optional] [default to &#39;7d&#39;]

### Return type

[**UserSentimentCountView**](UserSentimentCountView.md)

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

# **ai_analytics_orgs_users_topics_retrieve**
> Topic ai_analytics_orgs_users_topics_retrieve(org, user_id, period=period, topics=topics, user_ratings=user_ratings, user_sentiments=user_sentiments)



Get all topics relevant to the chat histories of the users in the organization.  Topics can be filtered by period: today, yesterday, 7d, 30d, 90d.  Topics can be filtered by user_sentiments: positive, negative, neutral.  Topics can be filtered by user_ratings: ThumbsUp, ThumbsDown, No Rating.  Accessible to tenant Admins only  An example of a valid request is:  **/orgs/ibl/users/ben/topics/?period=7d&user_sentiments=positive&user_ratings=ThumbsUp**

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.topic import Topic
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
period = 'period_example' # str |  (optional)
topics = ['topics_example'] # List[str] |  (optional)
user_ratings = ['user_ratings_example'] # List[str] |  (optional)
user_sentiments = ['user_sentiments_example'] # List[str] |  (optional)

try:
    api_response = api_instance.ai_analytics_orgs_users_topics_retrieve(org, user_id, period=period, topics=topics, user_ratings=user_ratings, user_sentiments=user_sentiments)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_topics_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_topics_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **period** | **str**|  | [optional] 
 **topics** | [**List[str]**](str.md)|  | [optional] 
 **user_ratings** | [**List[str]**](str.md)|  | [optional] 
 **user_sentiments** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Topic**](Topic.md)

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

# **ai_analytics_orgs_users_topics_summary_retrieve**
> TopicSummaryView ai_analytics_orgs_users_topics_summary_retrieve(org, user_id)



Get the summary of topics relevant to the chat histories of the users in the organization.  This returns the total conversations and the top three topics relevant to the conversations.  Accessible to tenant Admins only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.topic_summary_view import TopicSummaryView
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_topics_summary_retrieve(org, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_topics_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_topics_summary_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TopicSummaryView**](TopicSummaryView.md)

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

# **ai_analytics_orgs_users_traces_retrieve**
> LLMTracesListResponse ai_analytics_orgs_users_traces_retrieve(end_date, org, start_date, user_id, mentor=mentor)



Retrieve the llm summerized traces  for a tenant  Filter parameters for period are start_date and enddate  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_traces_list_response import LLMTracesListResponse
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 
mentor = 'mentor_example' # str | Mentor unique id (optional)

try:
    api_response = api_instance.ai_analytics_orgs_users_traces_retrieve(end_date, org, start_date, user_id, mentor=mentor)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_traces_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_traces_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 
 **mentor** | **str**| Mentor unique id | [optional] 

### Return type

[**LLMTracesListResponse**](LLMTracesListResponse.md)

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

# **ai_analytics_orgs_users_traces_retrieve2**
> LLMTraceDetail ai_analytics_orgs_users_traces_retrieve2(org, trace_id, user_id)



Get the trace detail.  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_trace_detail import LLMTraceDetail
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
trace_id = 'trace_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_traces_retrieve2(org, trace_id, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_traces_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_traces_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **trace_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**LLMTraceDetail**](LLMTraceDetail.md)

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

# **ai_analytics_orgs_users_traces_scores_create**
> LLMScoresViewResponse ai_analytics_orgs_users_traces_scores_create(org, user_id, llm_scores_view_request)



Add message scores for chat.  Filter parameters for period are start_date and enddate  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_scores_view_request import LLMScoresViewRequest
from iblai.models.llm_scores_view_response import LLMScoresViewResponse
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
llm_scores_view_request = iblai.LLMScoresViewRequest() # LLMScoresViewRequest | 

try:
    api_response = api_instance.ai_analytics_orgs_users_traces_scores_create(org, user_id, llm_scores_view_request)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_traces_scores_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_traces_scores_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **llm_scores_view_request** | [**LLMScoresViewRequest**](LLMScoresViewRequest.md)|  | 

### Return type

[**LLMScoresViewResponse**](LLMScoresViewResponse.md)

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

# **ai_analytics_orgs_users_traces_scores_retrieve**
> LLMScoresView ai_analytics_orgs_users_traces_scores_retrieve(end_date, org, start_date, user_id, mentor=mentor)



Get the scores of messages for a tenant.  Filter parameters for period are start_date and end_date  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_scores_view import LLMScoresView
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
api_instance = iblai.AiAnalyticsApi(api_client)
end_date = '2013-10-20T19:20:30+01:00' # datetime | 
org = 'org_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
user_id = 'user_id_example' # str | 
mentor = 'mentor_example' # str | Mentor unique id (optional)

try:
    api_response = api_instance.ai_analytics_orgs_users_traces_scores_retrieve(end_date, org, start_date, user_id, mentor=mentor)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_traces_scores_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_traces_scores_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **datetime**|  | 
 **org** | **str**|  | 
 **start_date** | **datetime**|  | 
 **user_id** | **str**|  | 
 **mentor** | **str**| Mentor unique id | [optional] 

### Return type

[**LLMScoresView**](LLMScoresView.md)

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

# **ai_analytics_orgs_users_transcripts_retrieve**
> ConversationMessage ai_analytics_orgs_users_transcripts_retrieve(org, user_id, end_date=end_date, mentor=mentor, start_date=start_date, topics=topics)



Get the number of messages for a given period of time  Filter parameters for period are today, yesterday, 7d, 30d, 90d  Accessible to tenant Admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.conversation_message import ConversationMessage
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
mentor = 'mentor_example' # str |  (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
topics = 'topics_example' # str |  (optional)

try:
    api_response = api_instance.ai_analytics_orgs_users_transcripts_retrieve(org, user_id, end_date=end_date, mentor=mentor, start_date=start_date, topics=topics)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_transcripts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_transcripts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **datetime**|  | [optional] 
 **mentor** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **topics** | **str**|  | [optional] 

### Return type

[**ConversationMessage**](ConversationMessage.md)

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

# **ai_analytics_orgs_users_user_feedback_retrieve**
> UserChatFeedbackCount ai_analytics_orgs_users_user_feedback_retrieve(org, user_id)



Return the total number of user chat feedback per week

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_chat_feedback_count import UserChatFeedbackCount
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
api_instance = iblai.AiAnalyticsApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_analytics_orgs_users_user_feedback_retrieve(org, user_id)
    print("The response of AiAnalyticsApi->ai_analytics_orgs_users_user_feedback_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiAnalyticsApi->ai_analytics_orgs_users_user_feedback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserChatFeedbackCount**](UserChatFeedbackCount.md)

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

