# iblai.NotificationApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_v1_campaigns_unsubscribe_retrieve**](NotificationApi.md#notification_v1_campaigns_unsubscribe_retrieve) | **GET** /api/notification/v1/campaigns/unsubscribe/{unsubscribe_hash}/ | 
[**notification_v1_orgs_campaigns_enable_create**](NotificationApi.md#notification_v1_orgs_campaigns_enable_create) | **POST** /api/notification/v1/orgs/{platform_key}/campaigns/enable/ | 
[**notification_v1_orgs_campaigns_exclude_create**](NotificationApi.md#notification_v1_orgs_campaigns_exclude_create) | **POST** /api/notification/v1/orgs/{platform_key}/campaigns/exclude/ | 
[**notification_v1_orgs_mark_all_as_read_create**](NotificationApi.md#notification_v1_orgs_mark_all_as_read_create) | **POST** /api/notification/v1/orgs/{platform_key}/mark-all-as-read | 
[**notification_v1_orgs_notifications_bulk_update_partial_update**](NotificationApi.md#notification_v1_orgs_notifications_bulk_update_partial_update) | **PATCH** /api/notification/v1/orgs/{org}/notifications/bulk-update/ | 
[**notification_v1_orgs_notifications_retrieve**](NotificationApi.md#notification_v1_orgs_notifications_retrieve) | **GET** /api/notification/v1/orgs/{org}/notifications/ | 
[**notification_v1_orgs_notifications_update**](NotificationApi.md#notification_v1_orgs_notifications_update) | **PUT** /api/notification/v1/orgs/{org}/notifications/ | 
[**notification_v1_orgs_users_notifications_bulk_update_partial_update**](NotificationApi.md#notification_v1_orgs_users_notifications_bulk_update_partial_update) | **PATCH** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/bulk-update/ | 
[**notification_v1_orgs_users_notifications_count_retrieve**](NotificationApi.md#notification_v1_orgs_users_notifications_count_retrieve) | **GET** /api/notification/v1/orgs/{org}/users/{user_id}/notifications-count/ | 
[**notification_v1_orgs_users_notifications_destroy**](NotificationApi.md#notification_v1_orgs_users_notifications_destroy) | **DELETE** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/{notification_id}/ | 
[**notification_v1_orgs_users_notifications_retrieve**](NotificationApi.md#notification_v1_orgs_users_notifications_retrieve) | **GET** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/ | 
[**notification_v1_orgs_users_notifications_update**](NotificationApi.md#notification_v1_orgs_users_notifications_update) | **PUT** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/ | 


# **notification_v1_campaigns_unsubscribe_retrieve**
> NotificationV1CampaignsUnsubscribeRetrieve200Response notification_v1_campaigns_unsubscribe_retrieve(unsubscribe_hash)



Unsubscribe from a campaign using a hash

### Example


```python
import iblai
from iblai.models.notification_v1_campaigns_unsubscribe_retrieve200_response import NotificationV1CampaignsUnsubscribeRetrieve200Response
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.NotificationApi(api_client)
unsubscribe_hash = 'unsubscribe_hash_example' # str | 

try:
    api_response = api_instance.notification_v1_campaigns_unsubscribe_retrieve(unsubscribe_hash)
    print("The response of NotificationApi->notification_v1_campaigns_unsubscribe_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_campaigns_unsubscribe_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_hash** | **str**|  | 

### Return type

[**NotificationV1CampaignsUnsubscribeRetrieve200Response**](NotificationV1CampaignsUnsubscribeRetrieve200Response.md)

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

# **notification_v1_orgs_campaigns_enable_create**
> NotificationV1CampaignsUnsubscribeRetrieve200Response notification_v1_orgs_campaigns_enable_create(platform_key, campaign_enablement=campaign_enablement)



Re-enable campaigns for a user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.campaign_enablement import CampaignEnablement
from iblai.models.notification_v1_campaigns_unsubscribe_retrieve200_response import NotificationV1CampaignsUnsubscribeRetrieve200Response
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
api_instance = iblai.NotificationApi(api_client)
platform_key = 'platform_key_example' # str | 
campaign_enablement = iblai.CampaignEnablement() # CampaignEnablement |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_campaigns_enable_create(platform_key, campaign_enablement=campaign_enablement)
    print("The response of NotificationApi->notification_v1_orgs_campaigns_enable_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_campaigns_enable_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **campaign_enablement** | [**CampaignEnablement**](CampaignEnablement.md)|  | [optional] 

### Return type

[**NotificationV1CampaignsUnsubscribeRetrieve200Response**](NotificationV1CampaignsUnsubscribeRetrieve200Response.md)

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

# **notification_v1_orgs_campaigns_exclude_create**
> NotificationV1CampaignsUnsubscribeRetrieve200Response notification_v1_orgs_campaigns_exclude_create(platform_key, campaign_exclusion=campaign_exclusion)



Exclude a user from specified campaigns

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.campaign_exclusion import CampaignExclusion
from iblai.models.notification_v1_campaigns_unsubscribe_retrieve200_response import NotificationV1CampaignsUnsubscribeRetrieve200Response
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
api_instance = iblai.NotificationApi(api_client)
platform_key = 'platform_key_example' # str | 
campaign_exclusion = iblai.CampaignExclusion() # CampaignExclusion |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_campaigns_exclude_create(platform_key, campaign_exclusion=campaign_exclusion)
    print("The response of NotificationApi->notification_v1_orgs_campaigns_exclude_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_campaigns_exclude_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **campaign_exclusion** | [**CampaignExclusion**](CampaignExclusion.md)|  | [optional] 

### Return type

[**NotificationV1CampaignsUnsubscribeRetrieve200Response**](NotificationV1CampaignsUnsubscribeRetrieve200Response.md)

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

# **notification_v1_orgs_mark_all_as_read_create**
> MarkAllReadResponse notification_v1_orgs_mark_all_as_read_create(platform_key, mark_all_read_request=mark_all_read_request)



Mark all notifications as read for a user. Optionally provide specific notification IDs.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mark_all_read_request import MarkAllReadRequest
from iblai.models.mark_all_read_response import MarkAllReadResponse
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
api_instance = iblai.NotificationApi(api_client)
platform_key = 'platform_key_example' # str | 
mark_all_read_request = iblai.MarkAllReadRequest() # MarkAllReadRequest |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_mark_all_as_read_create(platform_key, mark_all_read_request=mark_all_read_request)
    print("The response of NotificationApi->notification_v1_orgs_mark_all_as_read_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_mark_all_as_read_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **mark_all_read_request** | [**MarkAllReadRequest**](MarkAllReadRequest.md)|  | [optional] 

### Return type

[**MarkAllReadResponse**](MarkAllReadResponse.md)

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

# **notification_v1_orgs_notifications_bulk_update_partial_update**
> Notification notification_v1_orgs_notifications_bulk_update_partial_update(org, patched_notification=patched_notification)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
from iblai.models.patched_notification import PatchedNotification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
patched_notification = iblai.PatchedNotification() # PatchedNotification |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_notifications_bulk_update_partial_update(org, patched_notification=patched_notification)
    print("The response of NotificationApi->notification_v1_orgs_notifications_bulk_update_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_notifications_bulk_update_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **patched_notification** | [**PatchedNotification**](PatchedNotification.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **notification_v1_orgs_notifications_retrieve**
> Notification notification_v1_orgs_notifications_retrieve(org, channel=channel, end_date=end_date, exclude_channel=exclude_channel, start_date=start_date, status=status)



Get notifications for a user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
channel = 'channel_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
exclude_channel = 'exclude_channel_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_notifications_retrieve(org, channel=channel, end_date=end_date, exclude_channel=exclude_channel, start_date=start_date, status=status)
    print("The response of NotificationApi->notification_v1_orgs_notifications_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_notifications_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **channel** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **exclude_channel** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **notification_v1_orgs_notifications_update**
> Notification notification_v1_orgs_notifications_update(org, notification)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
notification = iblai.Notification() # Notification | 

try:
    api_response = api_instance.notification_v1_orgs_notifications_update(org, notification)
    print("The response of NotificationApi->notification_v1_orgs_notifications_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_notifications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **notification** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

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

# **notification_v1_orgs_users_notifications_bulk_update_partial_update**
> Notification notification_v1_orgs_users_notifications_bulk_update_partial_update(org, user_id, patched_notification=patched_notification)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
from iblai.models.patched_notification import PatchedNotification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_notification = iblai.PatchedNotification() # PatchedNotification |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_users_notifications_bulk_update_partial_update(org, user_id, patched_notification=patched_notification)
    print("The response of NotificationApi->notification_v1_orgs_users_notifications_bulk_update_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_users_notifications_bulk_update_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_notification** | [**PatchedNotification**](PatchedNotification.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **notification_v1_orgs_users_notifications_count_retrieve**
> NotificationCount notification_v1_orgs_users_notifications_count_retrieve(org, user_id, channel=channel, status=status)



Get notifications count for a user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification_count import NotificationCount
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
channel = 'channel_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_users_notifications_count_retrieve(org, user_id, channel=channel, status=status)
    print("The response of NotificationApi->notification_v1_orgs_users_notifications_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_users_notifications_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **channel** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**NotificationCount**](NotificationCount.md)

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

# **notification_v1_orgs_users_notifications_destroy**
> notification_v1_orgs_users_notifications_destroy(notification_id, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

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
api_instance = iblai.NotificationApi(api_client)
notification_id = 'notification_id_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.notification_v1_orgs_users_notifications_destroy(notification_id, org, user_id)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_users_notifications_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 
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

# **notification_v1_orgs_users_notifications_retrieve**
> Notification notification_v1_orgs_users_notifications_retrieve(org, user_id, channel=channel, end_date=end_date, exclude_channel=exclude_channel, start_date=start_date, status=status)



Get notifications for a user

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
channel = 'channel_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)
exclude_channel = 'exclude_channel_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    api_response = api_instance.notification_v1_orgs_users_notifications_retrieve(org, user_id, channel=channel, end_date=end_date, exclude_channel=exclude_channel, start_date=start_date, status=status)
    print("The response of NotificationApi->notification_v1_orgs_users_notifications_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_users_notifications_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **channel** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 
 **exclude_channel** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**Notification**](Notification.md)

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

# **notification_v1_orgs_users_notifications_update**
> Notification notification_v1_orgs_users_notifications_update(org, user_id, notification)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification import Notification
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
api_instance = iblai.NotificationApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
notification = iblai.Notification() # Notification | 

try:
    api_response = api_instance.notification_v1_orgs_users_notifications_update(org, user_id, notification)
    print("The response of NotificationApi->notification_v1_orgs_users_notifications_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationApi->notification_v1_orgs_users_notifications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **notification** | [**Notification**](Notification.md)|  | 

### Return type

[**Notification**](Notification.md)

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

