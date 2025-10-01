# iblai.AnalyticsApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_financial_details_retrieve**](AnalyticsApi.md#analytics_financial_details_retrieve) | **GET** /api/analytics/financial/details/ | 
[**analytics_financial_invoice_retrieve**](AnalyticsApi.md#analytics_financial_invoice_retrieve) | **GET** /api/analytics/financial/invoice/ | 
[**analytics_financial_retrieve**](AnalyticsApi.md#analytics_financial_retrieve) | **GET** /api/analytics/financial/ | 
[**analytics_learners_list_retrieve**](AnalyticsApi.md#analytics_learners_list_retrieve) | **GET** /api/analytics/learners/list/ | 
[**analytics_learners_retrieve**](AnalyticsApi.md#analytics_learners_retrieve) | **GET** /api/analytics/learners/ | 
[**analytics_messages_details_retrieve**](AnalyticsApi.md#analytics_messages_details_retrieve) | **GET** /api/analytics/messages/details/ | 
[**analytics_messages_retrieve**](AnalyticsApi.md#analytics_messages_retrieve) | **GET** /api/analytics/messages/ | 
[**analytics_ratings_retrieve**](AnalyticsApi.md#analytics_ratings_retrieve) | **GET** /api/analytics/ratings/ | 
[**analytics_sessions_details_retrieve**](AnalyticsApi.md#analytics_sessions_details_retrieve) | **GET** /api/analytics/sessions/details/ | 
[**analytics_sessions_retrieve**](AnalyticsApi.md#analytics_sessions_retrieve) | **GET** /api/analytics/sessions/ | 
[**analytics_time_retrieve**](AnalyticsApi.md#analytics_time_retrieve) | **GET** /api/analytics/time/ | 
[**analytics_topics_details_retrieve**](AnalyticsApi.md#analytics_topics_details_retrieve) | **GET** /api/analytics/topics/details/ | 
[**analytics_topics_retrieve**](AnalyticsApi.md#analytics_topics_retrieve) | **GET** /api/analytics/topics/ | 
[**analytics_users_details_retrieve**](AnalyticsApi.md#analytics_users_details_retrieve) | **GET** /api/analytics/users/details/ | 
[**analytics_users_retrieve**](AnalyticsApi.md#analytics_users_retrieve) | **GET** /api/analytics/users/ | 
[**get_content_analytics**](AnalyticsApi.md#get_content_analytics) | **GET** /api/analytics/content/ | Get Content Analytics
[**get_content_details**](AnalyticsApi.md#get_content_details) | **GET** /api/analytics/content/details/{content_id}/ | Get Content Details


# **analytics_financial_details_retrieve**
> FinanceDetailsResponse analytics_financial_details_retrieve(group_by, date_filter=date_filter, end_date=end_date, limit=limit, llm_model=llm_model, mentor_unique_id=mentor_unique_id, metrics=metrics, page=page, platform_key=platform_key, provider=provider, search=search, start_date=start_date, username=username)

Financial Details Analytics API – paginated cost tables with flexible grouping.

This endpoint returns tabular cost metrics aggregated by the dimension
specified via the `group_by` query parameter.  One or more KPI columns
can be requested through the comma-separated `metrics` list while
typical filters (date range, provider, platform_key, user, etc.) narrow the
dataset.  Results are paginated with `page` / `limit`.

**Required query parameters**
- group_by – provider | llm_model | username | mentor | platform
- metrics – csv list of KPI names, e.g. total_cost, sessions

**Shared optional filters**
- start_date, end_date   – ISO yyyy-mm-dd (ignored when all_time=true)
- platform_key           – tenant isolation
- mentor_unique_id       – filter to one mentor
- username               – filter to a learner
- provider / llm_model   – filter to LLM provider / model
- all_time               – true → lifetime totals
- page (default 1), limit (default 50)

**Examples**
--------
1. Cost by provider for the last week
```
   GET /api/v2/analytics/financial/details?
       group_by=provider&
       metrics=total_cost&
       start_date=2025-01-01&
       end_date=2025-01-07&
       page=1&limit=10
```

2. Lifetime cost per user with extra KPIs
   ```
   GET /api/v2/analytics/financial/details?
       group_by=username&
       metrics=total_cost,sessions&
       all_time=true&page=1&limit=50
   ```
3. Cost by LLM model with tenant filter
```
   GET /api/v2/analytics/financial/details?
       group_by=llm_model&
       metrics=total_cost&
       platform_key=web-app&
       start_date=2025-01-01&end_date=2025-01-31
```
Response structure
-------------------
```
{
  "page": 1,
  "limit": 10,
  "total_pages": 1,
  "total_records": 3,
  "rows": [
    {"provider": "openai", "total_cost": 2.5},
    {"provider": "anthropic", "total_cost": 1.0},
    {"provider": "azure",    "total_cost": 0.5}
  ],
  "metrics": [
    {
      "name": "total_cost",
      "unit": "$",
      "description": "Cost for this entity in period"
    }
  ],
  "total_cost": 4.0   // optional grand-total when available
}
``

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.finance_details_response import FinanceDetailsResponse
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
api_instance = iblai.AnalyticsApi(api_client)
group_by = 'group_by_example' # str | Dimension to group by  * `provider` - Group by provider * `llm_model` - Group by LLM model * `username` - Group by username * `mentor` - Group by mentor * `platform` - Group by platform * `action` - Group by actions
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
limit = 20 # int |  (optional) (default to 20)
llm_model = 'llm_model_example' # str |  (optional)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
metrics = 'total_cost' # str | Comma-separated list of metrics (e.g. total_cost,sessions, last_active) (optional) (default to 'total_cost')
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
search = 'search_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.analytics_financial_details_retrieve(group_by, date_filter=date_filter, end_date=end_date, limit=limit, llm_model=llm_model, mentor_unique_id=mentor_unique_id, metrics=metrics, page=page, platform_key=platform_key, provider=provider, search=search, start_date=start_date, username=username)
    print("The response of AnalyticsApi->analytics_financial_details_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_financial_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Dimension to group by  * &#x60;provider&#x60; - Group by provider * &#x60;llm_model&#x60; - Group by LLM model * &#x60;username&#x60; - Group by username * &#x60;mentor&#x60; - Group by mentor * &#x60;platform&#x60; - Group by platform * &#x60;action&#x60; - Group by actions | 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **llm_model** | **str**|  | [optional] 
 **mentor_unique_id** | **str**|  | [optional] 
 **metrics** | **str**| Comma-separated list of metrics (e.g. total_cost,sessions, last_active) | [optional] [default to &#39;total_cost&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**FinanceDetailsResponse**](FinanceDetailsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request – invalid query params |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_financial_invoice_retrieve**
> InvoiceReportResponse analytics_financial_invoice_retrieve(end_date=end_date, include_breakdown=include_breakdown, platform_key=platform_key, start_date=start_date, username=username)

Flexible Invoice Report API – Billing summary with username and platform filtering.

This endpoint generates invoice reports with flexible filtering options:
- Platform admins can view their platform's data and filter by username within their platform
- Super admins can view any combination of username/platform or global summaries

**Key Features:**
- Flexible filtering by username and/or platform_key
- Essential metrics: total cost, sessions, usage period
- Provider breakdown (OpenAI, Anthropic, etc.)
- Top mentors/actions by cost
- Clean, invoice-ready format

**Query Parameters:**
- username: Filter by specific username (optional)
- platform_key: Filter by platform (optional, but required for platform admins)
- start_date, end_date: billing period (defaults to last 30 days)
- include_breakdown: show provider/mentor details (default: true)

**Permission Logic:**
- Platform admins: Must include platform_key matching their permission scope
- Super admins: Can use any combination of filters or none (global summary)

**Examples:**
```
# Platform admin viewing their platform
GET /api/analytics/financial/invoice?platform_key=web-app

# Platform admin viewing specific user in their platform
GET /api/analytics/financial/invoice?platform_key=web-app&username=john.doe

# Super admin viewing specific user across all platforms
GET /api/analytics/financial/invoice?username=john.doe

# Super admin viewing global summary
GET /api/analytics/financial/invoice
```

**Response Structure:**
```json
{
  "entity": {
    "type": "user|platform|global",
    "username": "john.doe",
    "platform_key": "web-app",
    "platform_name": "Web Application",
    "display_name": "John Doe on Web Application"
  },
  "billing_period": {
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "days": 31
  },
  "summary": {
    "total_cost": 245.750,
    "total_sessions": 1250,
    "active_users": 85,
    "cost_per_session": 0.196
  },
  "breakdown": {
    "by_provider": [...],
    "by_mentor": [...],
    "by_action": [...]
  }
}
```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.invoice_report_response import InvoiceReportResponse
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
api_instance = iblai.AnalyticsApi(api_client)
end_date = '2013-10-20' # date | End date for billing period (defaults to today) (optional)
include_breakdown = True # bool | Whether to include provider and mentor breakdown (optional) (default to True)
platform_key = 'platform_key_example' # str | Platform key to filter by (optional, required for platform admins) (optional)
start_date = '2013-10-20' # date | Start date for billing period (defaults to 30 days ago) (optional)
username = 'username_example' # str | Username to generate invoice for (optional) (optional)

try:
    api_response = api_instance.analytics_financial_invoice_retrieve(end_date=end_date, include_breakdown=include_breakdown, platform_key=platform_key, start_date=start_date, username=username)
    print("The response of AnalyticsApi->analytics_financial_invoice_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_financial_invoice_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **date**| End date for billing period (defaults to today) | [optional] 
 **include_breakdown** | **bool**| Whether to include provider and mentor breakdown | [optional] [default to True]
 **platform_key** | **str**| Platform key to filter by (optional, required for platform admins) | [optional] 
 **start_date** | **date**| Start date for billing period (defaults to 30 days ago) | [optional] 
 **username** | **str**| Username to generate invoice for (optional) | [optional] 

### Return type

[**InvoiceReportResponse**](InvoiceReportResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request – invalid parameters |  -  |
**403** | Forbidden – insufficient permissions |  -  |
**404** | No data found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_financial_retrieve**
> BaseFinanceResponse analytics_financial_retrieve(metric, comparison_days=comparison_days, date_filter=date_filter, end_date=end_date, fill_method=fill_method, granularity=granularity, llm_model=llm_model, mentor_unique_id=mentor_unique_id, platform_key=platform_key, provider=provider, show_overtime=show_overtime, start_date=start_date, username=username)

Financial Analytics API - Get comprehensive cost metrics with comparison analysis.

This endpoint provides period-based cost analysis (not cumulative) with support for:
- Multiple time granularities and metrics
- Cross-dimensional filtering
- Percentage change vs comparison periods
- Forward-filled time series

**Examples:**

**Basic Weekly Costs:**
```
GET /api/v2/analytics/financial/?metric=weekly_costs&comparison_days=10
```

**Platform & Mentor Filtered:**
```
# Get total costs for a specific platform and mentor
GET /api/v2/analytics/financial/?metric=total_costs&platform_key=web-app&mentor_unique_id=mentor-123&comparison_days=14
```

**Monthly Costs by Provider:**
```
GET /api/v2/analytics/financial/?metric=monthly_costs&provider=openai&granularity=month&comparison_days=30
```

**Daily Costs for Specific User:**
```
GET /api/v2/analytics/financial/?metric=total_costs&username=user-456&granularity=day&start_date=2025-01-15&end_date=2025-01-21&comparison_days=7
```


**Response Structure:**
```json
{
    "metric": "weekly_costs",
    "value": 12.47,
    "percentage_change": 8.5,
    "overtime": [
        {"date": "2025-01-06", "value": 2.89},
        {"date": "2025-01-13", "value": 3.12}
    ],
    "period_info": {
        "start_date": "2025-01-01",
        "end_date": "2025-01-31",
        "period_days": 31
    },
    "comparison_info": {
        "previous_period_value": 11.50,
        ...
    }
}
```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.base_finance_response import BaseFinanceResponse
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
api_instance = iblai.AnalyticsApi(api_client)
metric = 'metric_example' # str | Type of financial metric to retrieve  * `total_costs` - Total costs for selected timeframe * `weekly_costs` - Costs for current/selected week * `monthly_costs` - Costs for current/selected month
comparison_days = 56 # int | Number of days for comparison period to calculate percentage change (e.g., 10 for 10-day comparison) (optional)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
fill_method = zero # str | Method for filling missing time periods in overtime data  * `zero` - Fill missing periods with zero * `previous` - Fill missing periods with previous value (optional) (default to zero)
granularity = day # str | Time granularity for overtime series data  * `day` - Daily data points * `week` - Weekly data points * `month` - Monthly data points (optional) (default to day)
llm_model = 'llm_model_example' # str | Filter by specific LLM model (e.g., gpt-4o, claude-3-5-sonnet) (optional)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
platform_key = 'platform_key_example' # str |  (optional)
provider = 'provider_example' # str | Filter by AI provider  * `openai` - OpenAI * `anthropic` - Anthropic * `azure` - Azure * `google` - Google * `meta` - Meta * `other` - Other (optional)
show_overtime = True # bool | Whether to include overtime series data in response (optional) (default to True)
start_date = '2013-10-20' # date |  (optional)
username = 'username_example' # str | Filter by specific username - returns costs for this user only (optional)

try:
    api_response = api_instance.analytics_financial_retrieve(metric, comparison_days=comparison_days, date_filter=date_filter, end_date=end_date, fill_method=fill_method, granularity=granularity, llm_model=llm_model, mentor_unique_id=mentor_unique_id, platform_key=platform_key, provider=provider, show_overtime=show_overtime, start_date=start_date, username=username)
    print("The response of AnalyticsApi->analytics_financial_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_financial_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| Type of financial metric to retrieve  * &#x60;total_costs&#x60; - Total costs for selected timeframe * &#x60;weekly_costs&#x60; - Costs for current/selected week * &#x60;monthly_costs&#x60; - Costs for current/selected month | 
 **comparison_days** | **int**| Number of days for comparison period to calculate percentage change (e.g., 10 for 10-day comparison) | [optional] 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **fill_method** | **str**| Method for filling missing time periods in overtime data  * &#x60;zero&#x60; - Fill missing periods with zero * &#x60;previous&#x60; - Fill missing periods with previous value | [optional] [default to zero]
 **granularity** | **str**| Time granularity for overtime series data  * &#x60;day&#x60; - Daily data points * &#x60;week&#x60; - Weekly data points * &#x60;month&#x60; - Monthly data points | [optional] [default to day]
 **llm_model** | **str**| Filter by specific LLM model (e.g., gpt-4o, claude-3-5-sonnet) | [optional] 
 **mentor_unique_id** | **str**|  | [optional] 
 **platform_key** | **str**|  | [optional] 
 **provider** | **str**| Filter by AI provider  * &#x60;openai&#x60; - OpenAI * &#x60;anthropic&#x60; - Anthropic * &#x60;azure&#x60; - Azure * &#x60;google&#x60; - Google * &#x60;meta&#x60; - Meta * &#x60;other&#x60; - Other | [optional] 
 **show_overtime** | **bool**| Whether to include overtime series data in response | [optional] [default to True]
 **start_date** | **date**|  | [optional] 
 **username** | **str**| Filter by specific username - returns costs for this user only | [optional] 

### Return type

[**BaseFinanceResponse**](BaseFinanceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful financial metrics response with period-based cost data |  -  |
**400** | Bad Request - Invalid query parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_learners_list_retrieve**
> LearnerListResponse analytics_learners_list_retrieve(platform_key, date_filter=date_filter, end_date=end_date, granularity=granularity, limit=limit, mentor_unique_id=mentor_unique_id, page=page, search=search, sort_by=sort_by, sort_order=sort_order, start_date=start_date)


        Retrieve a paginated list of learners for a specific platform with their comprehensive
        metrics from the UserPlatformSummary materialized view. This endpoint is accessible only
        to platform administrators and supports search, sorting, and pagination.
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.learner_list_response import LearnerListResponse
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
api_instance = iblai.AnalyticsApi(api_client)
platform_key = 'platform_key_example' # str | Platform key to filter learners by platform
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
limit = 20 # int | Number of learners per page (default: 20, max: 100) (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int | Page number for pagination (default: 1) (optional) (default to 1)
search = 'search_example' # str | Search term to filter learners by username, email, or name (optional)
sort_by = last_activity # str | Field to sort learners by (default: last_activity)  * `username` - Username * `name` - Name * `last_activity` - Last Activity * `total_points` - Total Points * `total_time_spent_seconds` - Time Spent * `total_enrollments` - Enrollments * `total_skills_count` - Skills Count (optional) (default to last_activity)
sort_order = desc # str | Sort order (default: desc)  * `asc` - Ascending * `desc` - Descending (optional) (default to desc)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_learners_list_retrieve(platform_key, date_filter=date_filter, end_date=end_date, granularity=granularity, limit=limit, mentor_unique_id=mentor_unique_id, page=page, search=search, sort_by=sort_by, sort_order=sort_order, start_date=start_date)
    print("The response of AnalyticsApi->analytics_learners_list_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_learners_list_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**| Platform key to filter learners by platform | 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **limit** | **int**| Number of learners per page (default: 20, max: 100) | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**| Page number for pagination (default: 1) | [optional] [default to 1]
 **search** | **str**| Search term to filter learners by username, email, or name | [optional] 
 **sort_by** | **str**| Field to sort learners by (default: last_activity)  * &#x60;username&#x60; - Username * &#x60;name&#x60; - Name * &#x60;last_activity&#x60; - Last Activity * &#x60;total_points&#x60; - Total Points * &#x60;total_time_spent_seconds&#x60; - Time Spent * &#x60;total_enrollments&#x60; - Enrollments * &#x60;total_skills_count&#x60; - Skills Count | [optional] [default to last_activity]
 **sort_order** | **str**| Sort order (default: desc)  * &#x60;asc&#x60; - Ascending * &#x60;desc&#x60; - Descending | [optional] [default to desc]
 **start_date** | **date**|  | [optional] 

### Return type

[**LearnerListResponse**](LearnerListResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of learners with their metrics |  -  |
**400** | Bad Request - Invalid parameters supplied |  -  |
**403** | Forbidden - Platform admin access required |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_learners_retrieve**
> LearnerAnalyticsResponse analytics_learners_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, limit=limit, mentor_unique_id=mentor_unique_id, overtime=overtime, page=page, platform_key=platform_key, start_date=start_date, username=username)

Unified API endpoint for learner analytics.

This endpoint provides either:
1. Cross-platform summary (when only username is provided)
2. Platform-specific detailed data (when username + platform_key are provided)

Query params:
- username (required): Username of the learner
- platform_key (optional): Platform key for platform-specific data
- page (optional): Page number (default: 1)
- limit (optional): Records per page (default: 20, max: 100)

Returns:
- If platform_key provided: Detailed platform metrics
- If no platform_key: Cross-platform summary with pagination

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.learner_analytics_response import LearnerAnalyticsResponse
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
limit = 20 # int | Number of records per page (default: 20, max: 100) (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
overtime = False # bool | Include overtime metrics for the user in the platform (default: false) (optional) (default to False)
page = 1 # int | Page number (default: 1) (optional) (default to 1)
platform_key = 'platform_key_example' # str | Optional platform key - if provided, returns platform-specific detailed data (optional)
start_date = '2013-10-20' # date |  (optional)
username = 'username_example' # str | Username of the learner to get analytics for. Defaults to self if not provided. (optional)

try:
    api_response = api_instance.analytics_learners_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, limit=limit, mentor_unique_id=mentor_unique_id, overtime=overtime, page=page, platform_key=platform_key, start_date=start_date, username=username)
    print("The response of AnalyticsApi->analytics_learners_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_learners_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **limit** | **int**| Number of records per page (default: 20, max: 100) | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **overtime** | **bool**| Include overtime metrics for the user in the platform (default: false) | [optional] [default to False]
 **page** | **int**| Page number (default: 1) | [optional] [default to 1]
 **platform_key** | **str**| Optional platform key - if provided, returns platform-specific detailed data | [optional] 
 **start_date** | **date**|  | [optional] 
 **username** | **str**| Username of the learner to get analytics for. Defaults to self if not provided. | [optional] 

### Return type

[**LearnerAnalyticsResponse**](LearnerAnalyticsResponse.md)

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

# **analytics_messages_details_retrieve**
> ConversationDetailResponse analytics_messages_details_retrieve(session_id, end_date=end_date, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)

Conversation detail endpoint for analytics.

Query params:
- session_id (required): UUID of the session to fetch
- platform_key, mentor_unique_id (optional): further scope
- start_date, end_date (optional): date filter on message timestamps

Returns: summary metadata from conversation_list MV, and a list of
human/ai message pairs in chronological order.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.conversation_detail_response import ConversationDetailResponse
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
api_instance = iblai.AnalyticsApi(api_client)
session_id = 'session_id_example' # str | 
end_date = '2013-10-20' # date |  (optional)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_messages_details_retrieve(session_id, end_date=end_date, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_messages_details_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_messages_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **end_date** | **date**|  | [optional] 
 **mentor_unique_id** | **str**|  | [optional] 
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**ConversationDetailResponse**](ConversationDetailResponse.md)

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

# **analytics_messages_retrieve**
> ConversationListResponse analytics_messages_retrieve(end_date=end_date, limit=limit, max_messages=max_messages, mentor_unique_id=mentor_unique_id, min_messages=min_messages, page=page, platform_key=platform_key, search=search, sentiment=sentiment, start_date=start_date, topic=topic)

Conversation list endpoint for analytics.

Query params (all optional unless specified by permissions):
- platform_key: filter by platform
- mentor_unique_id: filter by mentor
- page: page number (default 1)
- limit: page size (default 20, max 100)
- search: search in user name and first user message
- min_messages, max_messages: message_count range
- sentiment: positive|negative|neutral
- topic: topic name contains
- start_date, end_date: date filter on conversation date

Returns: summary totals, results list (paginated), and pagination metadata.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.conversation_list_response import ConversationListResponse
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
api_instance = iblai.AnalyticsApi(api_client)
end_date = '2013-10-20' # date |  (optional)
limit = 20 # int |  (optional) (default to 20)
max_messages = 56 # int |  (optional)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
min_messages = 56 # int |  (optional)
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str |  (optional)
sentiment = 'sentiment_example' # str | * `positive` - positive * `negative` - negative * `neutral` - neutral (optional)
start_date = '2013-10-20' # date |  (optional)
topic = 'topic_example' # str |  (optional)

try:
    api_response = api_instance.analytics_messages_retrieve(end_date=end_date, limit=limit, max_messages=max_messages, mentor_unique_id=mentor_unique_id, min_messages=min_messages, page=page, platform_key=platform_key, search=search, sentiment=sentiment, start_date=start_date, topic=topic)
    print("The response of AnalyticsApi->analytics_messages_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **max_messages** | **int**|  | [optional] 
 **mentor_unique_id** | **str**|  | [optional] 
 **min_messages** | **int**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **sentiment** | **str**| * &#x60;positive&#x60; - positive * &#x60;negative&#x60; - negative * &#x60;neutral&#x60; - neutral | [optional] 
 **start_date** | **date**|  | [optional] 
 **topic** | **str**|  | [optional] 

### Return type

[**ConversationListResponse**](ConversationListResponse.md)

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

# **analytics_ratings_retrieve**
> RatingsOvertime analytics_ratings_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)

Ratings overtime endpoint.

Query params:
- metric: only 'ratings' is supported (default)
- platform_key, mentor_unique_id: optional filters
- granularity: 'day' (default) or 'hour' (hour only for today)
- start_date, end_date: optional date range; defaults applied if not provided

Returns: { metric: 'ratings', points: [{date, value}, ...] }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ratings_overtime import RatingsOvertime
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
metric = ratings # str | * `ratings` - Ratings over time (optional) (default to ratings)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_ratings_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_ratings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_ratings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **mentor_unique_id** | **str**|  | [optional] 
 **metric** | **str**| * &#x60;ratings&#x60; - Ratings over time | [optional] [default to ratings]
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**RatingsOvertime**](RatingsOvertime.md)

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

# **analytics_sessions_details_retrieve**
> TopicDetails analytics_sessions_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.topic_details import TopicDetails
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
limit = 20 # int |  (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | Search by topic name (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_sessions_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)
    print("The response of AnalyticsApi->analytics_sessions_details_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_sessions_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| Search by topic name | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**TopicDetails**](TopicDetails.md)

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

# **analytics_sessions_retrieve**
> SessionsChart analytics_sessions_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sessions_chart import SessionsChart
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
metric = sessions # str | * `sessions` - Sessions over time * `headline` - Headline metrics for sessions (avg messages per session, avg rating) (optional) (default to sessions)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_sessions_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_sessions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_sessions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **mentor_unique_id** | **str**|  | [optional] 
 **metric** | **str**| * &#x60;sessions&#x60; - Sessions over time * &#x60;headline&#x60; - Headline metrics for sessions (avg messages per session, avg rating) | [optional] [default to sessions]
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**SessionsChart**](SessionsChart.md)

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

# **analytics_time_retrieve**
> AccessTimesHeatmap analytics_time_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)


        Time Analytics API - User activity patterns by time of day and day of week.
        
        Provides heatmap data showing when users are most active, useful for:
        - Understanding peak usage times
        - Capacity planning and resource allocation
        - User behavior analysis
        - Support scheduling optimization
        
        **Key Features:**
        - Day of week patterns (0=Sunday through 6=Saturday)
        - Hour of day activity levels (0-23)
        - Flexible date range filtering
        - Platform and mentor-specific filtering
        - Message count aggregation
        
        **Data Structure:**
        - `day_of_week`: 0-6 (Sunday-Saturday)
        - `hour`: 0-23 (24-hour format)
        - `value`: Message count for that time slot
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.access_times_heatmap import AccessTimesHeatmap
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_time_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_time_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_time_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **mentor_unique_id** | **str**|  | [optional] 
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**AccessTimesHeatmap**](AccessTimesHeatmap.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access times heatmap data with day/hour patterns |  -  |
**400** | Bad Request - Invalid parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_topics_details_retrieve**
> TopicDetails analytics_topics_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.topic_details import TopicDetails
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
limit = 20 # int |  (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | Search by topic name (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_topics_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)
    print("The response of AnalyticsApi->analytics_topics_details_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_topics_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| Search by topic name | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**TopicDetails**](TopicDetails.md)

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

# **analytics_topics_retrieve**
> TopicsOverview analytics_topics_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.topics_overview import TopicsOverview
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
metric = overview # str | * `overview` - Overall topic metrics * `sessions` - Sessions over time * `ratings` - Ratings over time * `highlighted` - Highlighted topics (optional) (default to overview)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_topics_retrieve(date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, metric=metric, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_topics_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_topics_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **mentor_unique_id** | **str**|  | [optional] 
 **metric** | **str**| * &#x60;overview&#x60; - Overall topic metrics * &#x60;sessions&#x60; - Sessions over time * &#x60;ratings&#x60; - Ratings over time * &#x60;highlighted&#x60; - Highlighted topics | [optional] [default to overview]
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**TopicsOverview**](TopicsOverview.md)

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

# **analytics_users_details_retrieve**
> UserDetail analytics_users_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)


        User Details API - Comprehensive user activity details with search and filtering.
        
        Provides detailed user information including:
        - User contact information (email, full name)
        - Activity metrics (message count, last activity)
        - Search functionality across multiple fields
        - Flexible date range filtering
        - CSV export capability
        
        **Key Features:**
        - Full-text search across email, name, and user ID
        - Date range filtering for activity periods
        - Platform and mentor-specific filtering
        - Comprehensive pagination with metadata
        - CSV export for data analysis
        - User aggregation across platforms/mentors
        
        **Search Capabilities:**
        - Email address matching
        - Full name search
        - User ID lookup
        - Partial string matching (case-insensitive)
        
        **Export Options:**
        - JSON response (default)
        - CSV export (?export=csv)
        - Includes all user fields in export
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_detail import UserDetail
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
api_instance = iblai.AnalyticsApi(api_client)
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
limit = 20 # int |  (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | Search by email, full name, or user ID (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_users_details_retrieve(date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date)
    print("The response of AnalyticsApi->analytics_users_details_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_users_details_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| Search by email, full name, or user ID | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated user details with activity metrics |  -  |
**400** | Bad Request - Invalid parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_users_retrieve**
> CurrentUsersResponse analytics_users_retrieve(metric, date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)


        User Analytics API - Comprehensive user activity metrics and trends.
        
        Provides real-time and historical user analytics including:
        - Currently active users (last hour)
        - Active users over time periods (7d, 30d, 90d)
        - Registered user counts and growth
        - Time series charts with customizable granularity
        
        **Key Features:**
        - Real-time active user counting
        - Percentage change calculations vs previous periods
        - Flexible date filtering and granularity
        - Platform and mentor-specific filtering
        - Forward-filled time series data
        
        **Supported Metrics:**
        - `currently_active`: Users active in last hour
        - `active_users`: Unique users in specified period
        - `registered_users`: Total and new user counts
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.current_users_response import CurrentUsersResponse
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
api_instance = iblai.AnalyticsApi(api_client)
metric = 'metric_example' # str | * `currently_active` - Users logged in right now * `active_users` - Active users in a period * `registered_users` - Registered users * `active_users_last_30d` - Active users in the last 30 days
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
platform_key = 'platform_key_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    api_response = api_instance.analytics_users_retrieve(metric, date_filter=date_filter, end_date=end_date, granularity=granularity, mentor_unique_id=mentor_unique_id, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->analytics_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->analytics_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| * &#x60;currently_active&#x60; - Users logged in right now * &#x60;active_users&#x60; - Active users in a period * &#x60;registered_users&#x60; - Registered users * &#x60;active_users_last_30d&#x60; - Active users in the last 30 days | 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **mentor_unique_id** | **str**|  | [optional] 
 **platform_key** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**CurrentUsersResponse**](CurrentUsersResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User analytics metrics with comparison data |  -  |
**400** | Bad Request - Invalid parameters |  -  |
**403** | Forbidden - Insufficient permissions |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_analytics**
> ContentResponse get_content_analytics(metric, date_filter=date_filter, end_date=end_date, granularity=granularity, include_overtime=include_overtime, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, start_date=start_date)

Get Content Analytics


        Retrieve aggregated analytics for catalog content (courses, programs, pathways, skills).
        
        Returns both summary statistics and paginated list of content items with individual analytics.
        When a platform_key is provided, results are filtered to show only content consumed by 
        learners associated with that platform.
        
        **Metrics supported:**
        - `course` or `courses`: Course analytics with time spent
        - `program` or `programs`: Program analytics  
        - `pathway` or `pathways`: Pathway analytics
        - `skill` or `skills`: Skill analytics
        
        **Platform Filtering:**
        - Without platform_key: Shows global analytics across all platforms
        - With platform_key: Shows analytics filtered by platform learners only
        
        **Time Spent Analytics:**
        - Platform-level: Total time spent across all content and average per learner
        - Course-level: Total time spent per course and average per enrolled learner
        - Time values are provided in seconds for precision
        - Overtime: Time series data showing platform time spent over last 7 days (courses only, and include_overtime=true)
        
        **External Content:**
        - Content not owned by the requesting platform but used by its learners is marked as "external"
        - External content has limited metadata exposure for privacy
        

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.content_response import ContentResponse
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
api_instance = iblai.AnalyticsApi(api_client)
metric = 'metric_example' # str | The type of content to retrieve (course, program, pathway, skill)  * `course` - course * `courses` - courses * `program` - program * `programs` - programs * `pathway` - pathway * `pathways` - pathways * `skill` - skill * `skills` - skills
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
granularity = hour # str | * `day` - day * `hour` - hour * `week` - week * `month` - month (optional) (default to hour)
include_overtime = False # bool | Include time spent over time data (optional) (default to False)
limit = 20 # int | Number of items per page (max 100) (optional) (default to 20)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int | Page number for pagination (optional) (default to 1)
platform_key = 'platform_key_example' # str | Optional platform key to filter results by platform (optional)
start_date = '2013-10-20' # date |  (optional)

try:
    # Get Content Analytics
    api_response = api_instance.get_content_analytics(metric, date_filter=date_filter, end_date=end_date, granularity=granularity, include_overtime=include_overtime, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, start_date=start_date)
    print("The response of AnalyticsApi->get_content_analytics:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->get_content_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| The type of content to retrieve (course, program, pathway, skill)  * &#x60;course&#x60; - course * &#x60;courses&#x60; - courses * &#x60;program&#x60; - program * &#x60;programs&#x60; - programs * &#x60;pathway&#x60; - pathway * &#x60;pathways&#x60; - pathways * &#x60;skill&#x60; - skill * &#x60;skills&#x60; - skills | 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **granularity** | **str**| * &#x60;day&#x60; - day * &#x60;hour&#x60; - hour * &#x60;week&#x60; - week * &#x60;month&#x60; - month | [optional] [default to hour]
 **include_overtime** | **bool**| Include time spent over time data | [optional] [default to False]
 **limit** | **int**| Number of items per page (max 100) | [optional] [default to 20]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **platform_key** | **str**| Optional platform key to filter results by platform | [optional] 
 **start_date** | **date**|  | [optional] 

### Return type

[**ContentResponse**](ContentResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_details**
> ContentDetailsResponse get_content_details(content_id, metric, date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date, time_metric=time_metric)

Get Content Details

Retrieve detailed analytics for a specific content item including summary statistics, learner-level data, and optional time series information.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.content_details_response import ContentDetailsResponse
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
api_instance = iblai.AnalyticsApi(api_client)
content_id = 'content_id_example' # str | 
metric = 'metric_example' # str | Content type to fetch (course, program, pathway, skill)  * `course` - course * `courses` - courses * `program` - program * `programs` - programs * `pathway` - pathway * `pathways` - pathways * `skill` - skill * `skills` - skills
date_filter = today # str | * `today` - Today only * `7d` - Last 7 days * `30d` - Last 30 days * `90d` - Last 90 days * `all_time` - All time * `custom` - Custom date range (optional) (default to today)
end_date = '2013-10-20' # date |  (optional)
limit = 10 # int | Number of learner records per page (optional) (default to 10)
mentor_unique_id = 'mentor_unique_id_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)
time_metric = 'time_metric_example' # str | Optional time series metric (enrollments, completions, ratings, time_spent) (optional)

try:
    # Get Content Details
    api_response = api_instance.get_content_details(content_id, metric, date_filter=date_filter, end_date=end_date, limit=limit, mentor_unique_id=mentor_unique_id, page=page, platform_key=platform_key, search=search, start_date=start_date, time_metric=time_metric)
    print("The response of AnalyticsApi->get_content_details:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AnalyticsApi->get_content_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**|  | 
 **metric** | **str**| Content type to fetch (course, program, pathway, skill)  * &#x60;course&#x60; - course * &#x60;courses&#x60; - courses * &#x60;program&#x60; - program * &#x60;programs&#x60; - programs * &#x60;pathway&#x60; - pathway * &#x60;pathways&#x60; - pathways * &#x60;skill&#x60; - skill * &#x60;skills&#x60; - skills | 
 **date_filter** | **str**| * &#x60;today&#x60; - Today only * &#x60;7d&#x60; - Last 7 days * &#x60;30d&#x60; - Last 30 days * &#x60;90d&#x60; - Last 90 days * &#x60;all_time&#x60; - All time * &#x60;custom&#x60; - Custom date range | [optional] [default to today]
 **end_date** | **date**|  | [optional] 
 **limit** | **int**| Number of learner records per page | [optional] [default to 10]
 **mentor_unique_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **platform_key** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 
 **time_metric** | **str**| Optional time series metric (enrollments, completions, ratings, time_spent) | [optional] 

### Return type

[**ContentDetailsResponse**](ContentDetailsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

