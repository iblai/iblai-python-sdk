# iblai.AiPromptApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_prompt_orgs_metadata_create**](AiPromptApi.md#ai_prompt_orgs_metadata_create) | **POST** /api/ai-prompt/orgs/{org}/metadata/ | 
[**ai_prompt_orgs_users_all_chats_memory_create**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
[**ai_prompt_orgs_users_all_chats_memory_destroy**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
[**ai_prompt_orgs_users_all_chats_memory_destroy2**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_destroy2) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/{memory_id}/ | 
[**ai_prompt_orgs_users_all_chats_memory_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
[**ai_prompt_orgs_users_all_chats_memory_update**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
[**ai_prompt_orgs_users_all_chats_memory_update2**](AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_update2) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/{memory_id}/ | 
[**ai_prompt_orgs_users_chat_memory_status_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_chat_memory_status_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/chat-memory-status/ | 
[**ai_prompt_orgs_users_chat_memory_status_update**](AiPromptApi.md#ai_prompt_orgs_users_chat_memory_status_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/chat-memory-status/ | 
[**ai_prompt_orgs_users_languages_create**](AiPromptApi.md#ai_prompt_orgs_users_languages_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/ | 
[**ai_prompt_orgs_users_languages_destroy**](AiPromptApi.md#ai_prompt_orgs_users_languages_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/{language_id}/ | 
[**ai_prompt_orgs_users_languages_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_languages_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/ | 
[**ai_prompt_orgs_users_languages_update**](AiPromptApi.md#ai_prompt_orgs_users_languages_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/{language_id}/ | 
[**ai_prompt_orgs_users_memory_context_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_memory_context_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-context/ | 
[**ai_prompt_orgs_users_memory_context_update**](AiPromptApi.md#ai_prompt_orgs_users_memory_context_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-context/ | 
[**ai_prompt_orgs_users_memory_create**](AiPromptApi.md#ai_prompt_orgs_users_memory_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
[**ai_prompt_orgs_users_memory_destroy**](AiPromptApi.md#ai_prompt_orgs_users_memory_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
[**ai_prompt_orgs_users_memory_destroy2**](AiPromptApi.md#ai_prompt_orgs_users_memory_destroy2) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/{memory_id}/ | 
[**ai_prompt_orgs_users_memory_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_memory_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
[**ai_prompt_orgs_users_memory_status_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_memory_status_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-status/ | 
[**ai_prompt_orgs_users_memory_status_update**](AiPromptApi.md#ai_prompt_orgs_users_memory_status_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-status/ | 
[**ai_prompt_orgs_users_memory_update**](AiPromptApi.md#ai_prompt_orgs_users_memory_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/{memory_id}/ | 
[**ai_prompt_orgs_users_metadata_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_metadata_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/metadata | 
[**ai_prompt_orgs_users_prompt_create**](AiPromptApi.md#ai_prompt_orgs_users_prompt_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/ | 
[**ai_prompt_orgs_users_prompt_destroy**](AiPromptApi.md#ai_prompt_orgs_users_prompt_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
[**ai_prompt_orgs_users_prompt_list**](AiPromptApi.md#ai_prompt_orgs_users_prompt_list) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/ | 
[**ai_prompt_orgs_users_prompt_partial_update**](AiPromptApi.md#ai_prompt_orgs_users_prompt_partial_update) | **PATCH** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
[**ai_prompt_orgs_users_prompt_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_prompt_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
[**ai_prompt_orgs_users_prompt_update**](AiPromptApi.md#ai_prompt_orgs_users_prompt_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
[**ai_prompt_orgs_users_prompts_category_create**](AiPromptApi.md#ai_prompt_orgs_users_prompts_category_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
[**ai_prompt_orgs_users_prompts_category_destroy**](AiPromptApi.md#ai_prompt_orgs_users_prompts_category_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
[**ai_prompt_orgs_users_prompts_category_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_prompts_category_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
[**ai_prompt_orgs_users_sessions_guided_prompts_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_sessions_guided_prompts_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/sessions/{session_id}/guided-prompts/ | 
[**ai_prompt_orgs_users_styles_create**](AiPromptApi.md#ai_prompt_orgs_users_styles_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/ | 
[**ai_prompt_orgs_users_styles_destroy**](AiPromptApi.md#ai_prompt_orgs_users_styles_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/{style_id}/ | 
[**ai_prompt_orgs_users_styles_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_styles_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/ | 
[**ai_prompt_orgs_users_styles_update**](AiPromptApi.md#ai_prompt_orgs_users_styles_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/{style_id}/ | 
[**ai_prompt_orgs_users_tags_create**](AiPromptApi.md#ai_prompt_orgs_users_tags_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/ | 
[**ai_prompt_orgs_users_tags_destroy**](AiPromptApi.md#ai_prompt_orgs_users_tags_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/{tag_id}/ | 
[**ai_prompt_orgs_users_tags_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_tags_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/ | 
[**ai_prompt_orgs_users_tags_update**](AiPromptApi.md#ai_prompt_orgs_users_tags_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/{tag_id}/ | 
[**ai_prompt_orgs_users_tones_create**](AiPromptApi.md#ai_prompt_orgs_users_tones_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/ | 
[**ai_prompt_orgs_users_tones_destroy**](AiPromptApi.md#ai_prompt_orgs_users_tones_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/{tone_id}/ | 
[**ai_prompt_orgs_users_tones_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_tones_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/ | 
[**ai_prompt_orgs_users_tones_update**](AiPromptApi.md#ai_prompt_orgs_users_tones_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/{tone_id}/ | 


# **ai_prompt_orgs_metadata_create**
> Metadata ai_prompt_orgs_metadata_create(org, metadata)



Endpoint for adding prompt metadata.  Accessible to tenant admins and students.  Returns:      200: Metadata Object.      404: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/metadata/      Request:        {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"prompt\": \"testing\"                     }      Response:       {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"prompt\": \"testing\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.metadata import Metadata
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
metadata = iblai.Metadata() # Metadata | 

try:
    api_response = api_instance.ai_prompt_orgs_metadata_create(org, metadata)
    print("The response of AiPromptApi->ai_prompt_orgs_metadata_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **metadata** | [**Metadata**](Metadata.md)|  | 

### Return type

[**Metadata**](Metadata.md)

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

# **ai_prompt_orgs_users_all_chats_memory_create**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_create(org, user_id, user_all_chat_memory_view)



Endpoint for Adding user all chat memory.  Accessible to tenant admins and students.  Returns:      201: user all chat memory Object.      400: When data is not valid.    Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/      Request:        {                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"content\": \"Loves programming\"                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"content\": \"Loves programming\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_all_chat_memory_view import UserAllChatMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_all_chat_memory_view = iblai.UserAllChatMemoryView() # UserAllChatMemoryView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_all_chats_memory_create(org, user_id, user_all_chat_memory_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_all_chats_memory_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_all_chat_memory_view** | [**UserAllChatMemoryView**](UserAllChatMemoryView.md)|  | 

### Return type

[**UserAllChatMemoryView**](UserAllChatMemoryView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_destroy**
> ai_prompt_orgs_users_all_chats_memory_destroy(org, user_id)



Endpoint for clearing all user chat memories.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_all_chats_memory_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ai_prompt_orgs_users_all_chats_memory_destroy2**
> ai_prompt_orgs_users_all_chats_memory_destroy2(memory_id, org, user_id)



Endpoint for deleting user chat memories..  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
memory_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_all_chats_memory_destroy2(memory_id, org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**|  | 
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

# **ai_prompt_orgs_users_all_chats_memory_retrieve**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_retrieve(org, user_id)



Endpoint for getting user all chats memories.  Accessible to tenant admins and students.  Returns:      200: List of user all chats memories.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/      Response:       [                         {                             \"id\": 1,                             \"username\": \"johndoes\",                             \"platform_key\": \"main\",                             \"content\": \"Loves programming\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_all_chat_memory_view import UserAllChatMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_all_chats_memory_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_all_chats_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserAllChatMemoryView**](UserAllChatMemoryView.md)

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

# **ai_prompt_orgs_users_all_chats_memory_update**
> UserChatMemoryUpdateView ai_prompt_orgs_users_all_chats_memory_update(org, user_id, user_all_chat_memory_view)



Endpoint for updating all user chat memories from previous chat histories.  Accessible to tenant admins and students.  Returns:      20o: task information object.  Example:      PUT: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/      Response:       {                         \"task_id\": \"4194d20c-37d5-4148-882f-f7d2d91f7769\",                          \"message\": \"Your request to create memories from previous chat histories has been queued.\",                      }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_all_chat_memory_view import UserAllChatMemoryView
from iblai.models.user_chat_memory_update_view import UserChatMemoryUpdateView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_all_chat_memory_view = iblai.UserAllChatMemoryView() # UserAllChatMemoryView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_all_chats_memory_update(org, user_id, user_all_chat_memory_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_all_chats_memory_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_all_chat_memory_view** | [**UserAllChatMemoryView**](UserAllChatMemoryView.md)|  | 

### Return type

[**UserChatMemoryUpdateView**](UserChatMemoryUpdateView.md)

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

# **ai_prompt_orgs_users_all_chats_memory_update2**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_update2(memory_id, org, user_id, user_all_chat_memory_view)



Endpoint for updating user chat memories.  Accessible to tenant admins and students.  Returns:      200: user chat memory object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/all-chats-memory/1/      Request:        {                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"content\": \"Loves programming\"                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"content\": \"Loves programming\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_all_chat_memory_view import UserAllChatMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
memory_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_all_chat_memory_view = iblai.UserAllChatMemoryView() # UserAllChatMemoryView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_all_chats_memory_update2(memory_id, org, user_id, user_all_chat_memory_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_all_chats_memory_update2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_all_chats_memory_update2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_all_chat_memory_view** | [**UserAllChatMemoryView**](UserAllChatMemoryView.md)|  | 

### Return type

[**UserAllChatMemoryView**](UserAllChatMemoryView.md)

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

# **ai_prompt_orgs_users_chat_memory_status_retrieve**
> UserChatMemoryStatusView ai_prompt_orgs_users_chat_memory_status_retrieve(org, user_id)



Endpoint for getting user chat memory status.  Accessible to tenant admins and students.  Returns:      200: Obbject of user chat memory status.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/chat-memory-status/      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"enabled\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_chat_memory_status_view import UserChatMemoryStatusView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_chat_memory_status_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_chat_memory_status_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_chat_memory_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserChatMemoryStatusView**](UserChatMemoryStatusView.md)

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

# **ai_prompt_orgs_users_chat_memory_status_update**
> UserChatMemoryStatusView ai_prompt_orgs_users_chat_memory_status_update(org, user_id, user_chat_memory_status_request_view)



Endpoint for updating user chat memory status.  Accessible to tenant admins and students.  Returns:      200: user chat memory status Object.      400: When data is not valid.    Example:      PUT: /api/ai-prompt/orgs/main/users/johndoe/chat-memory-status/      Request:        {                         \"enabled\": false                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"enabled\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_chat_memory_status_request_view import UserChatMemoryStatusRequestView
from iblai.models.user_chat_memory_status_view import UserChatMemoryStatusView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_chat_memory_status_request_view = iblai.UserChatMemoryStatusRequestView() # UserChatMemoryStatusRequestView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_chat_memory_status_update(org, user_id, user_chat_memory_status_request_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_chat_memory_status_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_chat_memory_status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_chat_memory_status_request_view** | [**UserChatMemoryStatusRequestView**](UserChatMemoryStatusRequestView.md)|  | 

### Return type

[**UserChatMemoryStatusView**](UserChatMemoryStatusView.md)

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

# **ai_prompt_orgs_users_languages_create**
> LanguagesView ai_prompt_orgs_users_languages_create(org, user_id, languages_view)



Endpoint for Adding prompt language.  Accessible to tenant admins only.  Returns:      201: Language Object.      400: When data is not valid.    Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/languages/      Request:        Response:       {                         \"name\": \"English\",                         \"code\": \"en\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"English\",                         \"code\": \"en\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.languages_view import LanguagesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
languages_view = iblai.LanguagesView() # LanguagesView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_languages_create(org, user_id, languages_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_languages_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_languages_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **languages_view** | [**LanguagesView**](LanguagesView.md)|  | 

### Return type

[**LanguagesView**](LanguagesView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_languages_destroy**
> ai_prompt_orgs_users_languages_destroy(language_id, org, user_id)



Endpoint for deleting prompt language.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/languages/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
language_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_languages_destroy(language_id, org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_languages_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **int**|  | 
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

# **ai_prompt_orgs_users_languages_retrieve**
> LanguagesView ai_prompt_orgs_users_languages_retrieve(org, user_id)



Endpoint for getting prompt languages.  Accessible to tenant admins and students.  Returns:      200: List of languages.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/languages/      Response:       [                         {                             \"id\": 1,                             \"name\": \"English\",                             \"code\": \"en\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.languages_view import LanguagesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_languages_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_languages_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_languages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**LanguagesView**](LanguagesView.md)

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

# **ai_prompt_orgs_users_languages_update**
> LanguagesView ai_prompt_orgs_users_languages_update(language_id, org, user_id, languages_view)



Endpoint for Adding prompt language.  Accessible to tenant admins only.  Returns:      200: Language Object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/languages/1/      Request:        {                         \"name\": \"English\",                         \"code\": \"en\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"English\",                         \"code\": \"en\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.languages_view import LanguagesView
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
api_instance = iblai.AiPromptApi(api_client)
language_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
languages_view = iblai.LanguagesView() # LanguagesView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_languages_update(language_id, org, user_id, languages_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_languages_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_languages_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **languages_view** | [**LanguagesView**](LanguagesView.md)|  | 

### Return type

[**LanguagesView**](LanguagesView.md)

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

# **ai_prompt_orgs_users_memory_context_retrieve**
> UserMemoryContextResponse ai_prompt_orgs_users_memory_context_retrieve(org, user_id)



Endpoint to get user memory context.  Accessible to tenant admins and students only.  Returns:      200: list of user memory context data.   Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/user-memory-context/       Response:       {                         \"username\": \"johndoe\",                         \"platform_key\": \"main\",                         \"extra_data\": null,                         \"use_reported_skills\": false,                         \"use_desired_skills\": false,                         \"use_credentials\": false,                         \"use_enrolled_courses\": false,                         \"use_time_spent\": false,                         \"use_completed_courses\": false,                         \"use_completed_programs\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_memory_context_response import UserMemoryContextResponse
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_context_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_context_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_context_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserMemoryContextResponse**](UserMemoryContextResponse.md)

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

# **ai_prompt_orgs_users_memory_context_update**
> UserMemoryContextResponse ai_prompt_orgs_users_memory_context_update(org, user_id, user_memory_context_request=user_memory_context_request)



Endpoint to update user memory context.  Accessible to tenant admins and students only.  Returns:      200: list of user memory context data.   Example:      PUT: /api/ai-mentor/orgs/main/users/johndoe/user-memory-context/     Request:       {                         \"extra_data\": \"Keep in mind that i also love football\",                         \"use_reported_skills\": false,                         \"use_desired_skills\": false,                         \"use_credentials\": false,                         \"use_enrolled_courses\": false,                         \"use_time_spent\": false,                         \"use_completed_courses\": false,                         \"use_completed_programs\": false                     }      Response:       {                         \"username\": \"johndoe\",                         \"platform_key\": \"main\",                         \"extra_data\": \"Keep in mind that i also love football\",                         \"use_reported_skills\": false,                         \"use_desired_skills\": false,                         \"use_credentials\": false,                         \"use_enrolled_courses\": false,                         \"use_time_spent\": false,                         \"use_completed_courses\": false,                         \"use_completed_programs\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_memory_context_request import UserMemoryContextRequest
from iblai.models.user_memory_context_response import UserMemoryContextResponse
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_memory_context_request = iblai.UserMemoryContextRequest() # UserMemoryContextRequest |  (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_context_update(org, user_id, user_memory_context_request=user_memory_context_request)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_context_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_context_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_memory_context_request** | [**UserMemoryContextRequest**](UserMemoryContextRequest.md)|  | [optional] 

### Return type

[**UserMemoryContextResponse**](UserMemoryContextResponse.md)

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

# **ai_prompt_orgs_users_memory_create**
> UserCatalogItemMemoryView ai_prompt_orgs_users_memory_create(org, user_id, user_catalog_item_memory_view)



    Endpoint for Adding user catalog item memory.      Accessible to tenant admins and students.      Returns:          201: user catalog item  memory Object.          400: When data is not valid.        Example:          POST: /api/ai-prompt/orgs/main/users/johndoe/memory/          Request:        {                             \"id\": 1,                             \"student\": \"johndoes\",                             \"platform\": \"main\",                             \"catalog_item\": \"Loves programming\",                             \"lessons\": {                                 \"gaming\": \"i learnt how to play chess\"                             },                             \"next_steps\": {                                 \"gaming\": \"I want to learn how to play golf\",                                 \"singing\": \"I want to learn how to sing pop music\"                             }                         }          Response:       {                             \"id\": 1,                             \"student\": \"johndoes\",                             \"platform\": \"main\",                             \"catalog_item\": \"Loves programming\",                             \"lessons\": {     \"gaming\": \"i learnt how to play chess\" }, \"next_steps\": {     \"gaming\": \"I want to learn how to play golf\",     \"singing\": \"I want to learn how to sing pop music\" }                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_catalog_item_memory_view import UserCatalogItemMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_catalog_item_memory_view = iblai.UserCatalogItemMemoryView() # UserCatalogItemMemoryView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_create(org, user_id, user_catalog_item_memory_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_catalog_item_memory_view** | [**UserCatalogItemMemoryView**](UserCatalogItemMemoryView.md)|  | 

### Return type

[**UserCatalogItemMemoryView**](UserCatalogItemMemoryView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_destroy**
> ai_prompt_orgs_users_memory_destroy(org, user_id)



Endpoint for clearing user catalog item memories.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/memory/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_memory_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ai_prompt_orgs_users_memory_destroy2**
> ai_prompt_orgs_users_memory_destroy2(memory_id, org, user_id)



Endpoint for deleting user catalog item memory  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/memory/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
memory_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_memory_destroy2(memory_id, org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**|  | 
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

# **ai_prompt_orgs_users_memory_retrieve**
> UserCatalogItemMemoryView ai_prompt_orgs_users_memory_retrieve(org, user_id)



Endpoint for getting user catalog item memories.  Accessible to tenant admins and students.  Returns:      200: List of user catalog item memories.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/memory/      Response:    [                     {                         \"id\": 1,                         \"student\": \"johndoes\",                         \"platform\": \"main\",                         \"catalog_item\": \"Loves programming\",                         \"lessons\": {                             \"gaming\": \"i learnt how to play chess\"                         },                         \"next_steps\": {                             \"gaming\": \"I want to learn how to play golf\",                             \"singing\": \"I want to learn how to sing pop music\"                         },                      }                  ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_catalog_item_memory_view import UserCatalogItemMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserCatalogItemMemoryView**](UserCatalogItemMemoryView.md)

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

# **ai_prompt_orgs_users_memory_status_retrieve**
> MemoryStatusView ai_prompt_orgs_users_memory_status_retrieve(org, user_id)



Endpoint for getting memory status.  Accessible to tenant admins and students.  Returns:      200: Obbject of memory status.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/memory-status/      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"enabled\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.memory_status_view import MemoryStatusView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_status_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_status_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MemoryStatusView**](MemoryStatusView.md)

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

# **ai_prompt_orgs_users_memory_status_update**
> MemoryStatusView ai_prompt_orgs_users_memory_status_update(org, user_id, memory_status_request_view)



Endpoint for updating user memory status.  Accessible to tenant admins and students.  Returns:      200: user chat memory status Object.      400: When data is not valid.    Example:      PUT: /api/ai-prompt/orgs/main/users/johndoe/memory-status/      Request:        {                         \"enabled\": false                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoes\",                         \"platform_key\": \"main\",                         \"enabled\": false                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.memory_status_request_view import MemoryStatusRequestView
from iblai.models.memory_status_view import MemoryStatusView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
memory_status_request_view = iblai.MemoryStatusRequestView() # MemoryStatusRequestView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_status_update(org, user_id, memory_status_request_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_status_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **memory_status_request_view** | [**MemoryStatusRequestView**](MemoryStatusRequestView.md)|  | 

### Return type

[**MemoryStatusView**](MemoryStatusView.md)

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

# **ai_prompt_orgs_users_memory_update**
> UserCatalogItemMemoryView ai_prompt_orgs_users_memory_update(memory_id, org, user_id, user_catalog_item_memory_view)



Endpoint for updating user catalog item memory.  Accessible to tenant admins and students.  Returns:      200: user catalog item memory object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/memory/1/      Request:        {                         \"id\": 1,                         \"student\": \"johndoes\",                         \"platform\": \"main\",                         \"catalog_item\": \"Loves programming\",                         \"lessons\": \"i learnt about x and y\",                         \"next_steps\": \"learning about z\"                     }      Response:       {                         \"id\": 1,                         \"student\": \"johndoes\",                         \"platform\": \"main\",                         \"catalog_item\": \"Loves programming\",                         \"lessons\": {                             \"gaming\": \"i learnt how to play chess\"                         },                         \"next_steps\": {                             \"gaming\": \"I want to learn how to play golf\",                             \"singing\": \"I want to learn how to sing pop music\"                         }                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_catalog_item_memory_view import UserCatalogItemMemoryView
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
api_instance = iblai.AiPromptApi(api_client)
memory_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_catalog_item_memory_view = iblai.UserCatalogItemMemoryView() # UserCatalogItemMemoryView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_memory_update(memory_id, org, user_id, user_catalog_item_memory_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_memory_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_memory_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_catalog_item_memory_view** | [**UserCatalogItemMemoryView**](UserCatalogItemMemoryView.md)|  | 

### Return type

[**UserCatalogItemMemoryView**](UserCatalogItemMemoryView.md)

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

# **ai_prompt_orgs_users_metadata_retrieve**
> Metadata ai_prompt_orgs_users_metadata_retrieve(org, user_id)



Endpoint for getting prompt metadata.  Accessible to tenant admins and students.  Returns:      200: Metadata Object.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/metadata/      Response:       {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"prompt\": \"testing\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.metadata import Metadata
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_metadata_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_metadata_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Metadata**](Metadata.md)

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

# **ai_prompt_orgs_users_prompt_create**
> Prompt ai_prompt_orgs_users_prompt_create(org, user_id, prompt, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt import Prompt
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
prompt = iblai.Prompt() # Prompt | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompt_create(org, user_id, prompt, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompt_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **prompt** | [**Prompt**](Prompt.md)|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 

### Return type

[**Prompt**](Prompt.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_prompt_destroy**
> ai_prompt_orgs_users_prompt_destroy(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

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
api_instance = iblai.AiPromptApi(api_client)
id = 56 # int | A unique integer value identifying this prompt.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)

try:
    api_instance.ai_prompt_orgs_users_prompt_destroy(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prompt. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 

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

# **ai_prompt_orgs_users_prompt_list**
> List[Prompt] ai_prompt_orgs_users_prompt_list(org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt import Prompt
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompt_list(org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompt_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 

### Return type

[**List[Prompt]**](Prompt.md)

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

# **ai_prompt_orgs_users_prompt_partial_update**
> Prompt ai_prompt_orgs_users_prompt_partial_update(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility, patched_prompt=patched_prompt)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_prompt import PatchedPrompt
from iblai.models.prompt import Prompt
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
api_instance = iblai.AiPromptApi(api_client)
id = 56 # int | A unique integer value identifying this prompt.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)
patched_prompt = iblai.PatchedPrompt() # PatchedPrompt |  (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompt_partial_update(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility, patched_prompt=patched_prompt)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompt_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prompt. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 
 **patched_prompt** | [**PatchedPrompt**](PatchedPrompt.md)|  | [optional] 

### Return type

[**Prompt**](Prompt.md)

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

# **ai_prompt_orgs_users_prompt_retrieve**
> Prompt ai_prompt_orgs_users_prompt_retrieve(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt import Prompt
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
api_instance = iblai.AiPromptApi(api_client)
id = 56 # int | A unique integer value identifying this prompt.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompt_retrieve(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompt_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prompt. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 

### Return type

[**Prompt**](Prompt.md)

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

# **ai_prompt_orgs_users_prompt_update**
> Prompt ai_prompt_orgs_users_prompt_update(id, org, user_id, prompt, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



View to create/retrieve/update a prompt.  Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt import Prompt
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
api_instance = iblai.AiPromptApi(api_client)
id = 56 # int | A unique integer value identifying this prompt.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
prompt = iblai.Prompt() # Prompt | 
category = 56 # int | Category of the prompt (optional)
created_by = 'created_by_example' # str | Option to filter by username of the prompt creators. (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, prompt, default is date (optional)
mentor_unique_id = 'mentor_unique_id_example' # str | Mentor unique id of the prompt (optional)
tag = 56 # int | Tag of the prompt (optional)
visibility = 'visibility_example' # str | Visibility trype the mentor of the prompt (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompt_update(id, org, user_id, prompt, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompt_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompt_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prompt. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **prompt** | [**Prompt**](Prompt.md)|  | 
 **category** | **int**| Category of the prompt | [optional] 
 **created_by** | **str**| Option to filter by username of the prompt creators. | [optional] 
 **filter_by** | **str**| Filter options include, date, prompt, default is date | [optional] 
 **mentor_unique_id** | **str**| Mentor unique id of the prompt | [optional] 
 **tag** | **int**| Tag of the prompt | [optional] 
 **visibility** | **str**| Visibility trype the mentor of the prompt | [optional] 

### Return type

[**Prompt**](Prompt.md)

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

# **ai_prompt_orgs_users_prompts_category_create**
> PromptCategory ai_prompt_orgs_users_prompts_category_create(org, user_id, prompt_category)



This is for adding prompt categories  Accessible to tenant admins only.  Returns:      200 : Prompt category detail.   Example :      POST : /api/ai-prompt/orgs/main/users/johndoe/prompts/category      Request:        {                         \"name\": \"Education\",                         \"description\": \"education testing\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"Education\",                         \"description\": \"education testing\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt_category import PromptCategory
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
prompt_category = iblai.PromptCategory() # PromptCategory | 

try:
    api_response = api_instance.ai_prompt_orgs_users_prompts_category_create(org, user_id, prompt_category)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompts_category_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompts_category_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **prompt_category** | [**PromptCategory**](PromptCategory.md)|  | 

### Return type

[**PromptCategory**](PromptCategory.md)

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

# **ai_prompt_orgs_users_prompts_category_destroy**
> ai_prompt_orgs_users_prompts_category_destroy(org, user_id)



This is for deleting prompt category  Accessible to tenant admins only.  Returns:      204 : No Content.      400 : When data is invalid.      400 : When data is invalid.  Example :      DELETE : /api/ai-prompt/orgs/main/users/johndoe/prompts/category      Request:        {                         \"category\": \"Education\"                     }      Response:       No response body.

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_prompts_category_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompts_category_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ai_prompt_orgs_users_prompts_category_retrieve**
> PromptCategory ai_prompt_orgs_users_prompts_category_retrieve(org, user_id, filter_by=filter_by)



This is for getting prompt categories  Accessible to tenant admins and students.  Returns:      200 : List of prompt categories.  Example :      GET : /api/ai-prompt/orgs/main/users/johndoe/prompts/category      Response:       [                         {                             \"id\": 1,                             \"name\": \"Education\",                             \"description\": \"education testing\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.prompt_category import PromptCategory
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_prompts_category_retrieve(org, user_id, filter_by=filter_by)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompts_category_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompts_category_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 

### Return type

[**PromptCategory**](PromptCategory.md)

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

# **ai_prompt_orgs_users_sessions_guided_prompts_retrieve**
> GuidedPromptsResponse ai_prompt_orgs_users_sessions_guided_prompts_retrieve(org, session_id, user_id)



This is for getting guided prompts for a chat session session.  Accessible to tenant admins and students.  Returns:      200 : Object of list of guided prompts.      500 : When ai response can not be loaded to json.      404: When OpenAI key for tenant is not set.      429: When OpenAI requests have exceeded the rate limit.  Example :      GET : /api/ai-prompt/orgs/main/users/johndoe/sessions/4194d20c-37d5-4148-882f-f7d2d91f7769/guided-prompts/      Response:       {                         \"ai_prompts\": [                             \"What are the benefits of regular exercise?\",                             \"How can I create a healthy meal plan?\",                             \"What are some effective stress management techniques?\"                         ]                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.guided_prompts_response import GuidedPromptsResponse
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_sessions_guided_prompts_retrieve(org, session_id, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_sessions_guided_prompts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_sessions_guided_prompts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GuidedPromptsResponse**](GuidedPromptsResponse.md)

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

# **ai_prompt_orgs_users_styles_create**
> StylesView ai_prompt_orgs_users_styles_create(org, user_id, styles_view)



Endpoint for Adding prompt style.  Accessible to tenant admins only.  Returns:      201: style Object.      400: When data is not valid.    Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/styles/      Request:        Response:       {                         \"description\": \"Sympathetic\"                     }      Response:       {                         \"id\": 1,                         \"description\": \"Sympathetic\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.styles_view import StylesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
styles_view = iblai.StylesView() # StylesView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_styles_create(org, user_id, styles_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_styles_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_styles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **styles_view** | [**StylesView**](StylesView.md)|  | 

### Return type

[**StylesView**](StylesView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_styles_destroy**
> ai_prompt_orgs_users_styles_destroy(org, style_id, user_id)



Endpoint for deleting prompt style.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/styles/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
style_id = 56 # int | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_styles_destroy(org, style_id, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_styles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **style_id** | **int**|  | 
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

# **ai_prompt_orgs_users_styles_retrieve**
> StylesView ai_prompt_orgs_users_styles_retrieve(org, user_id)



Endpoint for getting prompt styles.  Accessible to tenant admins and students.  Returns:      200: List of styles.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/styles/      Response:       [                         {                             \"id\": 1,                             \"description\": \"Sympathetic\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.styles_view import StylesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_styles_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_styles_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_styles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**StylesView**](StylesView.md)

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

# **ai_prompt_orgs_users_styles_update**
> StylesView ai_prompt_orgs_users_styles_update(org, style_id, user_id, styles_view)



Endpoint for Adding prompt style.  Accessible to tenant admins only.  Returns:      200: style Object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/styles/1/      Request:        {                         \"description\": \"Sympathetic\"                     }      Response:       {                         \"id\": 1,                         \"description\": \"Sympathetic\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.styles_view import StylesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
style_id = 56 # int | 
user_id = 'user_id_example' # str | 
styles_view = iblai.StylesView() # StylesView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_styles_update(org, style_id, user_id, styles_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_styles_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_styles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **style_id** | **int**|  | 
 **user_id** | **str**|  | 
 **styles_view** | [**StylesView**](StylesView.md)|  | 

### Return type

[**StylesView**](StylesView.md)

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

# **ai_prompt_orgs_users_tags_create**
> TagsView ai_prompt_orgs_users_tags_create(org, user_id, tags_view)



Endpoint for Adding prompt tag.  Accessible to tenant admins and students.  Returns:      201: tag Object.      400: When data is not valid.    Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tags/      Request:        Response:       {                         \"name\": \"Programming\",                         \"description\": \"tags for programing prompts\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"Programming\",                         \"description\": \"tags for programing prompts\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tags_view import TagsView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
tags_view = iblai.TagsView() # TagsView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_tags_create(org, user_id, tags_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tags_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tags_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **tags_view** | [**TagsView**](TagsView.md)|  | 

### Return type

[**TagsView**](TagsView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_tags_destroy**
> ai_prompt_orgs_users_tags_destroy(org, tag_id, user_id)



Endpoint for deleting prompt tag.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tags/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
tag_id = 56 # int | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_tags_destroy(org, tag_id, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tags_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **tag_id** | **int**|  | 
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

# **ai_prompt_orgs_users_tags_retrieve**
> TagsView ai_prompt_orgs_users_tags_retrieve(org, user_id)



Endpoint for getting prompt tags.  Accessible to tenant admins and students.  Returns:      200: List of tags.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/tags/      Response:       [                         {                             \"id\": 1,                             \"name\": \"Programming\",                             \"description\": \"tags for programing prompts\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tags_view import TagsView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_tags_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tags_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tags_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TagsView**](TagsView.md)

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

# **ai_prompt_orgs_users_tags_update**
> TagsView ai_prompt_orgs_users_tags_update(org, tag_id, user_id, tags_view)



Endpoint for updating prompt tag.  Accessible to tenant admins and students.  Returns:      200: tag Object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tags/1/      Request:        {                         \"name\": \"Programming\",                         \"description\": \"tags for programing prompts\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"Programming\",                         \"description\": \"tags for programing prompts\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tags_view import TagsView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
tag_id = 56 # int | 
user_id = 'user_id_example' # str | 
tags_view = iblai.TagsView() # TagsView | 

try:
    api_response = api_instance.ai_prompt_orgs_users_tags_update(org, tag_id, user_id, tags_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tags_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tags_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **tag_id** | **int**|  | 
 **user_id** | **str**|  | 
 **tags_view** | [**TagsView**](TagsView.md)|  | 

### Return type

[**TagsView**](TagsView.md)

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

# **ai_prompt_orgs_users_tones_create**
> TonesView ai_prompt_orgs_users_tones_create(org, user_id, tones_view=tones_view)



Endpoint for Adding prompt tone.  Accessible to tenant admins only.  Returns:      201: tone Object.      400: When data is not valid.    Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tones/      Request:        Response:       {                         \"description\": \"Sympathetic\"                     }      Response:       {                         \"id\": 1,                         \"description\": \"Sympathetic\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tones_view import TonesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
tones_view = iblai.TonesView() # TonesView |  (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_tones_create(org, user_id, tones_view=tones_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tones_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tones_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **tones_view** | [**TonesView**](TonesView.md)|  | [optional] 

### Return type

[**TonesView**](TonesView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_tones_destroy**
> ai_prompt_orgs_users_tones_destroy(org, tone_id, user_id)



Endpoint for deleting prompt tone.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tone/1/      Response:       No response Data

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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
tone_id = 56 # int | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_prompt_orgs_users_tones_destroy(org, tone_id, user_id)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tones_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **tone_id** | **int**|  | 
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

# **ai_prompt_orgs_users_tones_retrieve**
> TonesView ai_prompt_orgs_users_tones_retrieve(org, user_id)



Endpoint for getting prompt tones.  Accessible to tenant admins and students.  Returns:      200: List of tones.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/tones/      Response:       [                         {                             \"id\": 1,                             \"description\": \"Sympathetic\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tones_view import TonesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_prompt_orgs_users_tones_retrieve(org, user_id)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tones_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tones_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TonesView**](TonesView.md)

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

# **ai_prompt_orgs_users_tones_update**
> TonesView ai_prompt_orgs_users_tones_update(org, tone_id, user_id, tones_view=tones_view)



Endpoint for updating prompt tone.  Accessible to tenant admins only.  Returns:      200: tone Object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/tones/1/      Request:        {                         \"description\": \"Sympathetic\"                     }      Response:       {                         \"id\": 1,                         \"description\": \"Sympathetic\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tones_view import TonesView
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
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
tone_id = 56 # int | 
user_id = 'user_id_example' # str | 
tones_view = iblai.TonesView() # TonesView |  (optional)

try:
    api_response = api_instance.ai_prompt_orgs_users_tones_update(org, tone_id, user_id, tones_view=tones_view)
    print("The response of AiPromptApi->ai_prompt_orgs_users_tones_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_tones_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **tone_id** | **int**|  | 
 **user_id** | **str**|  | 
 **tones_view** | [**TonesView**](TonesView.md)|  | [optional] 

### Return type

[**TonesView**](TonesView.md)

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

