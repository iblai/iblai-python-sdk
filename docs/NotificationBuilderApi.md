# iblai.NotificationBuilderApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_v1_orgs_notification_builder_context_retrieve**](NotificationBuilderApi.md#notification_v1_orgs_notification_builder_context_retrieve) | **GET** /api/notification/v1/orgs/{platform_key}/notification-builder/context/ | Get notification context data
[**notification_v1_orgs_notification_builder_preview_create**](NotificationBuilderApi.md#notification_v1_orgs_notification_builder_preview_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/preview/ | Preview notification
[**notification_v1_orgs_notification_builder_recipients_list**](NotificationBuilderApi.md#notification_v1_orgs_notification_builder_recipients_list) | **GET** /api/notification/v1/orgs/{platform_key}/notification-builder/{id}/recipients/ | Get build recipients
[**notification_v1_orgs_notification_builder_send_create**](NotificationBuilderApi.md#notification_v1_orgs_notification_builder_send_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/send/ | Send notification
[**notification_v1_orgs_notification_builder_validate_source_create**](NotificationBuilderApi.md#notification_v1_orgs_notification_builder_validate_source_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/validate_source/ | Validate notification source


# **notification_v1_orgs_notification_builder_context_retrieve**
> ContextResponse notification_v1_orgs_notification_builder_context_retrieve(platform_key)

Get notification context data

Get all context data needed for notification building including templates, channels, and platforms

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.context_response import ContextResponse
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
api_instance = iblai.NotificationBuilderApi(api_client)
platform_key = 'platform_key_example' # str | 

try:
    # Get notification context data
    api_response = api_instance.notification_v1_orgs_notification_builder_context_retrieve(platform_key)
    print("The response of NotificationBuilderApi->notification_v1_orgs_notification_builder_context_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationBuilderApi->notification_v1_orgs_notification_builder_context_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**ContextResponse**](ContextResponse.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_v1_orgs_notification_builder_preview_create**
> PreviewResponse notification_v1_orgs_notification_builder_preview_create(platform_key, notification_preview)

Preview notification

Preview notification recipients and get build ID for sending

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification_preview import NotificationPreview
from iblai.models.preview_response import PreviewResponse
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
api_instance = iblai.NotificationBuilderApi(api_client)
platform_key = 'platform_key_example' # str | 
notification_preview = iblai.NotificationPreview() # NotificationPreview | 

try:
    # Preview notification
    api_response = api_instance.notification_v1_orgs_notification_builder_preview_create(platform_key, notification_preview)
    print("The response of NotificationBuilderApi->notification_v1_orgs_notification_builder_preview_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationBuilderApi->notification_v1_orgs_notification_builder_preview_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **notification_preview** | [**NotificationPreview**](NotificationPreview.md)|  | 

### Return type

[**PreviewResponse**](PreviewResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_v1_orgs_notification_builder_recipients_list**
> List[Recipient] notification_v1_orgs_notification_builder_recipients_list(id, platform_key, page=page, page_size=page_size, search=search)

Get build recipients

Get paginated list of recipients for a notification build

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recipient import Recipient
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
api_instance = iblai.NotificationBuilderApi(api_client)
id = 'id_example' # str | 
platform_key = 'platform_key_example' # str | 
page = 56 # int | Page number (optional)
page_size = 56 # int | Number of items per page (optional)
search = 'search_example' # str | Search recipients by username or email (optional)

try:
    # Get build recipients
    api_response = api_instance.notification_v1_orgs_notification_builder_recipients_list(id, platform_key, page=page, page_size=page_size, search=search)
    print("The response of NotificationBuilderApi->notification_v1_orgs_notification_builder_recipients_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationBuilderApi->notification_v1_orgs_notification_builder_recipients_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **platform_key** | **str**|  | 
 **page** | **int**| Page number | [optional] 
 **page_size** | **int**| Number of items per page | [optional] 
 **search** | **str**| Search recipients by username or email | [optional] 

### Return type

[**List[Recipient]**](Recipient.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_v1_orgs_notification_builder_send_create**
> SendResponse notification_v1_orgs_notification_builder_send_create(platform_key, send_notification)

Send notification

Send notifications to all recipients in a build

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.send_notification import SendNotification
from iblai.models.send_response import SendResponse
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
api_instance = iblai.NotificationBuilderApi(api_client)
platform_key = 'platform_key_example' # str | 
send_notification = iblai.SendNotification() # SendNotification | 

try:
    # Send notification
    api_response = api_instance.notification_v1_orgs_notification_builder_send_create(platform_key, send_notification)
    print("The response of NotificationBuilderApi->notification_v1_orgs_notification_builder_send_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationBuilderApi->notification_v1_orgs_notification_builder_send_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **send_notification** | [**SendNotification**](SendNotification.md)|  | 

### Return type

[**SendResponse**](SendResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notification_v1_orgs_notification_builder_validate_source_create**
> ValidateSourceResponse notification_v1_orgs_notification_builder_validate_source_create(platform_key, notification_source)

Validate notification source

Validate a single notification source (email, username, platform, csv)

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.notification_source import NotificationSource
from iblai.models.validate_source_response import ValidateSourceResponse
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
api_instance = iblai.NotificationBuilderApi(api_client)
platform_key = 'platform_key_example' # str | 
notification_source = iblai.NotificationSource() # NotificationSource | 

try:
    # Validate notification source
    api_response = api_instance.notification_v1_orgs_notification_builder_validate_source_create(platform_key, notification_source)
    print("The response of NotificationBuilderApi->notification_v1_orgs_notification_builder_validate_source_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling NotificationBuilderApi->notification_v1_orgs_notification_builder_validate_source_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **notification_source** | [**NotificationSource**](NotificationSource.md)|  | 

### Return type

[**ValidateSourceResponse**](ValidateSourceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

