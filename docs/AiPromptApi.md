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
[**ai_prompt_orgs_users_prompts_public_list**](AiPromptApi.md#ai_prompt_orgs_users_prompts_public_list) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/public/ | 
[**ai_prompt_orgs_users_prompts_public_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_prompts_public_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/public/{id}/ | 
[**ai_prompt_orgs_users_sessions_guided_prompts_retrieve**](AiPromptApi.md#ai_prompt_orgs_users_sessions_guided_prompts_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/sessions/{session_id}/guided-prompts/ | Retrieve guided prompts for a chat session
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



Create or update metadata for a prompt.  Args:     request: The HTTP request containing the metadata.     org: The organization/tenant identifier.  Returns:     Response: The created or updated prompt metadata.  Raises:     BadRequest: If the provided data is invalid.

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
metadata = {"metadata":{"category":"technical","difficulty":"intermediate","tags":["python","programming"]},"prompt_id":123} # Metadata | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_create**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_create(org, user_id, user_all_chat_memory_view)



Create a new chat memory entry for a user.  Args:     request: The HTTP request containing the chat memory data.     org: The organization/tenant identifier.     user_id: The ID of the user to create chat memory for.  Returns:     Response: The created chat memory entry.  Raises:     BadRequest: If the provided data is invalid.

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
user_all_chat_memory_view = {"username":"johndoe","platform_key":"main","content":"Previous conversation context about machine learning concepts.","session_id":"937d3d46-3048-4f9d-aa5c-ce7c51d85332"} # UserAllChatMemoryView | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_destroy**
> ai_prompt_orgs_users_all_chats_memory_destroy(org, user_id)



Delete all chat memory for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to delete chat memory for.  Returns:     Response: A success message if the memory was deleted.  Raises:     NotFound: If no chat memory exists for the user.

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
**204** | Memory successfully deleted |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_destroy2**
> ai_prompt_orgs_users_all_chats_memory_destroy2(memory_id, org, user_id)



Delete a specific chat memory entry.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the memory.     memory_id: The ID of the specific memory entry to delete.  Returns:     Response: A success message if the memory was deleted.  Raises:     NotFound: If the specified memory entry does not exist.

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
**204** | Memory successfully deleted |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_retrieve**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_retrieve(org, user_id)



Retrieve chat memory for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve chat memory for.  Returns:     Response: The user's chat memory entries.  Raises:     NotFound: If no chat memory exists for the user.

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
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_update**
> UserChatMemoryUpdateView ai_prompt_orgs_users_all_chats_memory_update(org, user_id, user_all_chat_memory_view)



Update chat memory for a specific user.  Args:     request: The HTTP request containing the updated chat memory data.     org: The organization/tenant identifier.     user_id: The ID of the user to update chat memory for.  Returns:     Response: A confirmation of the scheduled update task.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If no chat memory exists for the user.

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
**400** | Invalid data |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_all_chats_memory_update2**
> UserAllChatMemoryView ai_prompt_orgs_users_all_chats_memory_update2(memory_id, org, user_id, user_all_chat_memory_view)



Update a specific chat memory entry.  Args:     request: The HTTP request containing the updated chat memory data.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the memory.     memory_id: The ID of the specific memory entry to update.  Returns:     Response: The updated chat memory entry.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the specified memory entry does not exist.

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
user_all_chat_memory_view = {"username":"johndoe","platform_key":"main","content":"Updated conversation context about machine learning concepts.","session_id":"937d3d46-3048-4f9d-aa5c-ce7c51d85332"} # UserAllChatMemoryView | 

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
**400** | Invalid data |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_chat_memory_status_retrieve**
> UserChatMemoryStatusView ai_prompt_orgs_users_chat_memory_status_retrieve(org, user_id)



Retrieve the chat memory status for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve memory status for.  Returns:     Response: The user's chat memory status.  Raises:     NotFound: If no memory status exists for the user.

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
**404** | Memory status not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_chat_memory_status_update**
> UserChatMemoryStatusView ai_prompt_orgs_users_chat_memory_status_update(org, user_id, user_chat_memory_status_request_view)



Update the chat memory status for a specific user.  Args:     request: The HTTP request containing the updated status.     org: The organization/tenant identifier.     user_id: The ID of the user to update memory status for.  Returns:     Response: The updated chat memory status.  Raises:     BadRequest: If the provided data is invalid.

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
user_chat_memory_status_request_view = {"enabled":false} # UserChatMemoryStatusRequestView | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_languages_create**
> LanguagesView ai_prompt_orgs_users_languages_create(org, user_id, languages_view)



Create a new prompt language.  Args:     request: The HTTP request containing the language data.     org: The organization/tenant identifier.     user_id: The ID of the user creating the language.  Returns:     Response: The created prompt language.  Raises:     BadRequest: If the provided data is invalid.

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
languages_view = {"name":"French","code":"fr"} # LanguagesView | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_languages_destroy**
> ai_prompt_orgs_users_languages_destroy(language_id, org, user_id)



Delete a specific prompt language.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     language_id: The ID of the language to delete.  Returns:     Response: A success message if the language was deleted.  Raises:     NotFound: If the specified language does not exist.

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
**204** | Language successfully deleted |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_languages_retrieve**
> LanguagesView ai_prompt_orgs_users_languages_retrieve(org, user_id)



Retrieve all available prompt languages.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.  Returns:     Response: A list of available prompt languages.

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



Update a specific prompt language.  Args:     request: The HTTP request containing the updated language data.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     language_id: The ID of the language to update.  Returns:     Response: The updated prompt language.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the specified language does not exist.

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
languages_view = {"name":"French (Updated)","code":"fr"} # LanguagesView | 

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
**400** | Invalid data |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_context_retrieve**
> UserMemoryContextResponse ai_prompt_orgs_users_memory_context_retrieve(org, user_id)



Retrieve a user's memory context settings.

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



Updates the user's memory context settings.  Returns:      200: list of user memory context data.

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
user_memory_context_request = {"extra_data":"Keep in mind that i also love football","use_reported_skills":false,"use_desired_skills":false,"use_credentials":false,"use_enrolled_courses":false,"use_time_spent":false,"use_completed_courses":false,"use_completed_programs":false} # UserMemoryContextRequest |  (optional)

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



Create a new catalog item memory entry for a user.  Args:     request: The HTTP request containing the catalog item memory data.     org: The organization/tenant identifier.     user_id: The ID of the user to create catalog item memory for.  Returns:     Response: The created catalog item memory entry.  Raises:     BadRequest: If the provided data is invalid.

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
user_catalog_item_memory_view = {"student":"johndoe","platform":"main","catalog_item":"course-v1:edX+DemoX+Demo_Course","lessons":{"completed":["lesson1","lesson2"],"in_progress":["lesson3"]},"next_steps":{"recommended":["lesson4","lesson5"]}} # UserCatalogItemMemoryView | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_destroy**
> ai_prompt_orgs_users_memory_destroy(org, user_id)



Delete all catalog item memory for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to delete catalog item memory for.  Returns:     Response: A success message if the memory was deleted.  Raises:     NotFound: If no catalog item memory exists for the user.

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
**204** | Memory successfully deleted |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_destroy2**
> ai_prompt_orgs_users_memory_destroy2(memory_id, org, user_id)



Delete a specific catalog item memory entry.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the memory.     memory_id: The ID of the specific memory entry to delete.  Returns:     Response: A success message if the memory was deleted.  Raises:     NotFound: If the specified memory entry does not exist.

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
**204** | Memory successfully deleted |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_retrieve**
> UserCatalogItemMemoryView ai_prompt_orgs_users_memory_retrieve(org, user_id)



Retrieve catalog item memory for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve catalog item memory for.  Returns:     Response: The user's catalog item memory entries.  Raises:     NotFound: If no catalog item memory exists for the user.

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
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_status_retrieve**
> MemoryStatusView ai_prompt_orgs_users_memory_status_retrieve(org, user_id)



Retrieve the memory status for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve memory status for.  Returns:     Response: The user's memory status.  Raises:     NotFound: If no memory status exists for the user.

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
**404** | Memory status not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_status_update**
> MemoryStatusView ai_prompt_orgs_users_memory_status_update(org, user_id, memory_status_request_view)



Update the memory status for a specific user.  Args:     request: The HTTP request containing the updated status.     org: The organization/tenant identifier.     user_id: The ID of the user to update memory status for.  Returns:     Response: The updated memory status.  Raises:     BadRequest: If the provided data is invalid.

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
memory_status_request_view = {"enabled":false} # MemoryStatusRequestView | 

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
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_memory_update**
> UserCatalogItemMemoryView ai_prompt_orgs_users_memory_update(memory_id, org, user_id, user_catalog_item_memory_view)



Update a specific catalog item memory entry.  Args:     request: The HTTP request containing the updated catalog item memory data.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the memory.     memory_id: The ID of the specific memory entry to update.  Returns:     Response: The updated catalog item memory entry.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the specified memory entry does not exist.

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
user_catalog_item_memory_view = {"student":"johndoe","platform":"main","catalog_item":"course-v1:edX+DemoX+Demo_Course","lessons":{"completed":["lesson1","lesson2","lesson3"],"in_progress":["lesson4"]},"next_steps":{"recommended":["lesson5","lesson6"]}} # UserCatalogItemMemoryView | 

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
**400** | Invalid data |  -  |
**404** | Memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_metadata_retrieve**
> Metadata ai_prompt_orgs_users_metadata_retrieve(org, user_id)



Retrieve metadata for a prompt.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.  Returns:     Response: The prompt metadata.  Raises:     NotFound: If no metadata exists for the specific prompt

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
**404** | Metadata not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_prompt_create**
> Prompt ai_prompt_orgs_users_prompt_create(org, user_id, prompt, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



Create a new prompt.  Args:     request: HTTP request containing prompt data.  Returns:     Response with created prompt details.  Raises:     ValidationError: If the input data is invalid.

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
prompt = {"text":"What are the benefits of exercise?","category":"health","tags":[1,2],"mentor":3,"prompt_visibility":"viewable_by_anyone"} # Prompt | 
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



API viewset for managing prompts.  This view allows tenant admins and students to create, retrieve, update, and filter prompts based on various parameters.  Permissions:     - Accessible to both tenant administrators and students

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



API viewset for managing prompts.  This view allows tenant admins and students to create, retrieve, update, and filter prompts based on various parameters.  Permissions:     - Accessible to both tenant administrators and students

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



API viewset for managing prompts.  This view allows tenant admins and students to create, retrieve, update, and filter prompts based on various parameters.  Permissions:     - Accessible to both tenant administrators and students

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



API viewset for managing prompts.  This view allows tenant admins and students to create, retrieve, update, and filter prompts based on various parameters.  Permissions:     - Accessible to both tenant administrators and students

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



Update an existing prompt.  Args:     request: HTTP request containing updated prompt data.  Returns:     Response with updated prompt details.  Raises:     ValidationError: If the input data is invalid.     PermissionDenied: If the prompt is system-generated and cannot be edited.

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
prompt = {"text":"Updated prompt text","category":"updated_category","tags":[3,4],"mentor":1,"prompt_visibility":"viewable_by_admins"} # Prompt | 
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



Create a new prompt category.  Args:     request: The HTTP request containing category information.     org: Organization key identifier.     user_id: User performing the request.  Returns:     - 201: Created prompt category.     - 401: If the user is not a tenant admin.     - 400: If request data is invalid.

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
**201** | Created prompt category |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_prompts_category_destroy**
> ai_prompt_orgs_users_prompts_category_destroy(org, user_id)



Delete a prompt category.  Args:     request: The HTTP request containing the category to delete.     org: Organization key identifier.     user_id: User performing the request.  Returns:     - 204: No Content (successful deletion).     - 401: If the user is not a tenant admin.     - 400: If request data is invalid.     - 404: If the category does not exist.

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
**204** | Prompt category deleted successfully. |  -  |
**400** | Invalid request data. |  -  |
**404** | Prompt category not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_prompts_category_retrieve**
> PromptCategory ai_prompt_orgs_users_prompts_category_retrieve(org, user_id, filter_by=filter_by)



Retrieve a list of prompt categories.  Query Parameters:     - filter_by (optional): Sorts categories by name if set to \"name\".  Args:     request: The HTTP request.     org: Organization key identifier.  Returns:     - 200: List of prompt categories.     - 400: If query parameters are invalid.

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

# **ai_prompt_orgs_users_prompts_public_list**
> List[Prompt] ai_prompt_orgs_users_prompts_public_list(org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



API viewset for managing prompts.  This view allows anyone to retrieve, and filter prompts based on various parameters.  Permissions:     - Accessible to anyone

### Example


```python
import iblai
from iblai.models.prompt import Prompt
from iblai.rest import ApiException
from pprint import pprint


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
    api_response = api_instance.ai_prompt_orgs_users_prompts_public_list(org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompts_public_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompts_public_list: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_prompts_public_retrieve**
> Prompt ai_prompt_orgs_users_prompts_public_retrieve(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)



API viewset for managing prompts.  This view allows anyone to retrieve, and filter prompts based on various parameters.  Permissions:     - Accessible to anyone

### Example


```python
import iblai
from iblai.models.prompt import Prompt
from iblai.rest import ApiException
from pprint import pprint


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
    api_response = api_instance.ai_prompt_orgs_users_prompts_public_retrieve(id, org, user_id, category=category, created_by=created_by, filter_by=filter_by, mentor_unique_id=mentor_unique_id, tag=tag, visibility=visibility)
    print("The response of AiPromptApi->ai_prompt_orgs_users_prompts_public_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiPromptApi->ai_prompt_orgs_users_prompts_public_retrieve: %s\n" % e)
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

No authorization required

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

Retrieve guided prompts for a chat session

Fetches AI-generated guided prompts for a given session and organization.

### Example


```python
import iblai
from iblai.models.guided_prompts_response import GuidedPromptsResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiPromptApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Retrieve guided prompts for a chat session
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompt_orgs_users_styles_create**
> StylesView ai_prompt_orgs_users_styles_create(org, user_id, styles_view)



Endpoint for Adding prompt style.  Accessible to tenant admins only.  Returns:      201: style Object.      400: When data is not valid.

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
styles_view = {"description":"Sympathetic"} # StylesView | 

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



Endpoint for deleting prompt style.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.

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



Endpoint for getting prompt styles.  Accessible to tenant admins and students.  Returns:      200: List of styles.

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



Endpoint for Adding prompt style.  Accessible to tenant admins only.  Returns:      200: style Object.      400: When data is not valid.

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
styles_view = {"description":"Sympathetic"} # StylesView | 

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
tags_view = {"name":"Programming","description":"tags for programing prompts"} # TagsView | 

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



Endpoint for deleting prompt tag.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.

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



Endpoint for getting prompt tags.  Accessible to tenant admins and students.  Returns:      200: List of tags.

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



Endpoint for updating prompt tag.  Accessible to tenant admins and students.  Returns:      200: tag Object.      400: When data is not valid.

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
tags_view = {"name":"Programming","description":"tags for programing prompts"} # TagsView | 

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



Endpoint for Adding prompt tone.  Accessible to tenant admins only.  Returns:      201: tone Object.      400: When data is not valid.

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
tones_view = {"description":"Sympathetic"} # TonesView |  (optional)

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



Endpoint for deleting prompt tone.  Accessible to tenant admins and students.  Returns:      204: No response data.      400: When data is not valid.

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



Endpoint for getting prompt tones.  Accessible to tenant admins and students.  Returns:      200: List of tones.

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



Endpoint for updating prompt tone.  Accessible to tenant admins only.  Returns:      200: tone Object.      400: When data is not valid.

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
tones_view = {"description":"Sympathetic"} # TonesView |  (optional)

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

