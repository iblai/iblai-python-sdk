# iblai.AiMentorApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_mentor_orgs_metadata_create**](AiMentorApi.md#ai_mentor_orgs_metadata_create) | **POST** /api/ai-mentor/orgs/{org}/metadata/ | 
[**ai_mentor_orgs_sessions_create**](AiMentorApi.md#ai_mentor_orgs_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/sessions/ | 
[**ai_mentor_orgs_users_ai_generated_images_destroy**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
[**ai_mentor_orgs_users_ai_generated_images_list**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/ | 
[**ai_mentor_orgs_users_ai_generated_images_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
[**ai_mentor_orgs_users_audio_to_text_create**](AiMentorApi.md#ai_mentor_orgs_users_audio_to_text_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/audio-to-text/ | 
[**ai_mentor_orgs_users_available_template_mentors_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_available_template_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/available-template-mentors/ | 
[**ai_mentor_orgs_users_clear_chathistory_destroy**](AiMentorApi.md#ai_mentor_orgs_users_clear_chathistory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/clear-chathistory | 
[**ai_mentor_orgs_users_create**](AiMentorApi.md#ai_mentor_orgs_users_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
[**ai_mentor_orgs_users_create_mentor_wizard_create**](AiMentorApi.md#ai_mentor_orgs_users_create_mentor_wizard_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/create-mentor-wizard/ | 
[**ai_mentor_orgs_users_custom_instruction_create**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_custom_instruction_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_custom_instruction_update**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_destroy**](AiMentorApi.md#ai_mentor_orgs_users_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_downloads_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_downloads_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/downloads/tasks/{task_id}/ | 
[**ai_mentor_orgs_users_edx_memory_destroy**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
[**ai_mentor_orgs_users_edx_memory_list**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/ | 
[**ai_mentor_orgs_users_edx_memory_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
[**ai_mentor_orgs_users_export_chathistory_create**](AiMentorApi.md#ai_mentor_orgs_users_export_chathistory_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/export-chathistory/ | 
[**ai_mentor_orgs_users_free_usage_count_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_free_usage_count_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/free-usage-count | 
[**ai_mentor_orgs_users_list**](AiMentorApi.md#ai_mentor_orgs_users_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
[**ai_mentor_orgs_users_mentor_categories_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_categories_destroy**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_categories_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_feedback_create_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_create_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/create/ | 
[**ai_mentor_orgs_users_mentor_feedback_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
[**ai_mentor_orgs_users_mentor_feedback_update**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
[**ai_mentor_orgs_users_mentor_from_template_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_from_template_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-from-template/ | 
[**ai_mentor_orgs_users_mentor_llms_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_llms_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-llms/ | 
[**ai_mentor_orgs_users_mentor_seed_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_seed_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/seed/ | 
[**ai_mentor_orgs_users_mentor_tools_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_tools_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-tools/ | 
[**ai_mentor_orgs_users_mentor_with_settings_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_with_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-with-settings/ | 
[**ai_mentor_orgs_users_mentors_available_tools_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_available_tools_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/available-tools/ | 
[**ai_mentor_orgs_users_mentors_memory_component_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_component_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-component-settings/ | 
[**ai_mentor_orgs_users_mentors_memory_component_settings_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_component_settings_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-component-settings/ | 
[**ai_mentor_orgs_users_mentors_public_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_public_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/public-settings/ | 
[**ai_mentor_orgs_users_mentors_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/ | 
[**ai_mentor_orgs_users_mentors_scenarios_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_scenarios_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/scenarios/ | 
[**ai_mentor_orgs_users_mentors_scenarios_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_scenarios_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/scenarios/ | 
[**ai_mentor_orgs_users_mentors_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | 
[**ai_mentor_orgs_users_mentors_settings_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | 
[**ai_mentor_orgs_users_metadata_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_metadata_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/metadata | 
[**ai_mentor_orgs_users_moderation_logs_destroy**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
[**ai_mentor_orgs_users_moderation_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/ | 
[**ai_mentor_orgs_users_moderation_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
[**ai_mentor_orgs_users_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_periodic_agent_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/ | 
[**ai_mentor_orgs_users_periodic_agent_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_create**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
[**ai_mentor_orgs_users_periodic_agents_destroy**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_list**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
[**ai_mentor_orgs_users_periodic_agents_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_update**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_pin_message_create**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_pin_message_destroy**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_pin_message_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_planned_jobs_list**](AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/ | 
[**ai_mentor_orgs_users_planned_jobs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_create**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
[**ai_mentor_orgs_users_playwright_scripts_destroy**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_list**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
[**ai_mentor_orgs_users_playwright_scripts_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_update**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_predictive_analytics_create**](AiMentorApi.md#ai_mentor_orgs_users_predictive_analytics_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/predictive-analytics/ | 
[**ai_mentor_orgs_users_recent_messages_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recent_messages_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recent-messages/ | 
[**ai_mentor_orgs_users_recommend_courses_block_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recommend_courses_block_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recommend-courses-block/ | 
[**ai_mentor_orgs_users_recommend_courses_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recommend_courses_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recommend-courses/ | 
[**ai_mentor_orgs_users_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_safety_logs_destroy**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
[**ai_mentor_orgs_users_safety_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/ | 
[**ai_mentor_orgs_users_safety_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
[**ai_mentor_orgs_users_session_detail_mentors_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_session_detail_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/session-detail/mentors/{mentor}/ | 
[**ai_mentor_orgs_users_sessionid_list**](AiMentorApi.md#ai_mentor_orgs_users_sessionid_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessionid/ | 
[**ai_mentor_orgs_users_sessions_browser_screenshot_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_browser_screenshot_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/browser-screenshot/ | 
[**ai_mentor_orgs_users_sessions_create**](AiMentorApi.md#ai_mentor_orgs_users_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/ | 
[**ai_mentor_orgs_users_sessions_destroy**](AiMentorApi.md#ai_mentor_orgs_users_sessions_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_sessions_download_session_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_download_session_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/download-session | 
[**ai_mentor_orgs_users_sessions_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_sessions_shell_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_shell_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/shell-logs/ | 
[**ai_mentor_orgs_users_sessions_suggestion_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_suggestion_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/suggestion | 
[**ai_mentor_orgs_users_sessions_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/tasks/{task_id}/ | 
[**ai_mentor_orgs_users_sessions_update**](AiMentorApi.md#ai_mentor_orgs_users_sessions_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_settings_tenant_llm_create**](AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
[**ai_mentor_orgs_users_settings_tenant_llm_list**](AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
[**ai_mentor_orgs_users_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/{task_id} | 
[**ai_mentor_orgs_users_tasks_sessions_create**](AiMentorApi.md#ai_mentor_orgs_users_tasks_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_update**](AiMentorApi.md#ai_mentor_orgs_users_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_usage_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_usage_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/usage/ | 


# **ai_mentor_orgs_metadata_create**
> MentorMetadata ai_mentor_orgs_metadata_create(org, mentor_metadata)



Endpoint for adding mentor metadata.  Accessible to tenant admins and students.  Returns:      200: Metadata Object.      400: When data is not valid.  Example:      POST: /api/ai-prompt/orgs/main/users/johndoe/metadata/      Request:        {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"mentor\": \"testing\",                         \"mentor_id: 1                     }      Response:       {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"mentor\": \"testing\",                         \"mentor_id: 1                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_metadata import MentorMetadata
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
mentor_metadata = iblai.MentorMetadata() # MentorMetadata | 

try:
    api_response = api_instance.ai_mentor_orgs_metadata_create(org, mentor_metadata)
    print("The response of AiMentorApi->ai_mentor_orgs_metadata_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **mentor_metadata** | [**MentorMetadata**](MentorMetadata.md)|  | 

### Return type

[**MentorMetadata**](MentorMetadata.md)

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

# **ai_mentor_orgs_sessions_create**
> ChatSessionResponse ai_mentor_orgs_sessions_create(org, chat_session_request)



This is for getting mentor session id  Accessible to any user.  Returns:      200 : Session id object.      404 : When mentor is not found.  Example :      POST : /api/ai-mentor/orgs/main/users/johndoe/sessions/      Request:        {                         \"mentor\": \"ai-mentor\"                     }      Response:       {                         \"session_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"                     }

### Example


```python
import iblai
from iblai.models.chat_session_request import ChatSessionRequest
from iblai.models.chat_session_response import ChatSessionResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
chat_session_request = iblai.ChatSessionRequest() # ChatSessionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_sessions_create(org, chat_session_request)
    print("The response of AiMentorApi->ai_mentor_orgs_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **chat_session_request** | [**ChatSessionRequest**](ChatSessionRequest.md)|  | 

### Return type

[**ChatSessionResponse**](ChatSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_generated_images_destroy**
> ai_mentor_orgs_users_ai_generated_images_destroy(id, org, user_id)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this ai generated image.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_ai_generated_images_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ai generated image. | 
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

# **ai_mentor_orgs_users_ai_generated_images_list**
> PaginatedAIGeneratedImageList ai_mentor_orgs_users_ai_generated_images_list(org, user_id, model=model, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, username=username)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_ai_generated_image_list import PaginatedAIGeneratedImageList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
model = 'model_example' # str |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
provider = 'provider_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_generated_images_list(org, user_id, model=model, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_generated_images_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **model** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedAIGeneratedImageList**](PaginatedAIGeneratedImageList.md)

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

# **ai_mentor_orgs_users_ai_generated_images_retrieve**
> AIGeneratedImage ai_mentor_orgs_users_ai_generated_images_retrieve(id, org, user_id)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_generated_image import AIGeneratedImage
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this ai generated image.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_generated_images_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_generated_images_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ai generated image. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AIGeneratedImage**](AIGeneratedImage.md)

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

# **ai_mentor_orgs_users_audio_to_text_create**
> AudioToTextResponse ai_mentor_orgs_users_audio_to_text_create(org, user_id, audio_to_text_request)



Endpoint to convert audio to text.  Accessible to tenant admins and students.  Returns:      200: audio text object.      400: When data is not valid.  Example:      POST: /api/ai-mentor/orgs/main/users/johndoe/audio-to-text/      Request:        {                         \"file\": binary                     }      Response:       {                         \"text\": \"Programming\",                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.audio_to_text_request import AudioToTextRequest
from iblai.models.audio_to_text_response import AudioToTextResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
audio_to_text_request = iblai.AudioToTextRequest() # AudioToTextRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_audio_to_text_create(org, user_id, audio_to_text_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_audio_to_text_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_audio_to_text_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **audio_to_text_request** | [**AudioToTextRequest**](AudioToTextRequest.md)|  | 

### Return type

[**AudioToTextResponse**](AudioToTextResponse.md)

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

# **ai_mentor_orgs_users_available_template_mentors_retrieve**
> TemplateMentor ai_mentor_orgs_users_available_template_mentors_retrieve(org, user_id)



This endpoint list available template mentors for a tenant  Returns:      200 : List of Tool objects   Example :      GET : api/ai-mentor/orgs/main/users/johndoe/available-template-mentors/  Response:   [                 {                     \"id\": 1,                     \"name\": \"AI Mentor\",                     \"platform\": \"main\",                     \"slug\": \"ai-mentor\",                     \"unique_id\": \"8485a252-eecf-436b-ba25-3f4ea3e7cda9\",                     \"description\": \"Upbeat, encouraging tutor helping students understand concepts by explaining ideas and asking questions.\",                     \"system_prompt\": \"Wrap all responses in MARKDOWN formatted text.\",                  }             ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.template_mentor import TemplateMentor
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_available_template_mentors_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_available_template_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_available_template_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TemplateMentor**](TemplateMentor.md)

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

# **ai_mentor_orgs_users_clear_chathistory_destroy**
> ai_mentor_orgs_users_clear_chathistory_destroy(org, user_id)



Endpoint to clear user's chat history  Returns:      204: No responde data

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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_clear_chathistory_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_clear_chathistory_destroy: %s\n" % e)
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

# **ai_mentor_orgs_users_create**
> Mentor ai_mentor_orgs_users_create(org, user_id, mentor, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = iblai.Mentor() # Mentor | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_create(org, user_id, mentor, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | [**Mentor**](Mentor.md)|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_create_mentor_wizard_create**
> Mentor ai_mentor_orgs_users_create_mentor_wizard_create(org, user_id, mentor_wizard)



        Endpoint to automatically create a mentor given a name and a description of the mentor.         All other parameters for the mentor will be automatically populated using an llm.         This includes but not limitted to marketing conversations, system prompt, proactive prompt, profile icon and more.           Url Args:             org (str): The organization's platform key.             user_id (str): The username  identifier of the individual.          Returns:              201: a Mentor instance             400: An error occurred when validating inputs or creating mentor.          Example:              **Create a mentor**              POST: /api/ai-mentor/orgs/main/users/johndoe/create-mentor-wizard/              Request:    {                             \"name\": \"Fashion Expert\",                             \"description\": \"An expert at Fashion Design                         }             Response:   {                             \"name\": \"Fashion Agent\",                             \"unique_id\": \"ef425893-877c-4538-9e79-54eb1eebd165\",                             \"platform\": \"main\",                             \"slug\": \"df57c4b3-32c5-4a3a-81a4-97e9e2ac8d25\",                             \"description\": \"An agent that can teach different fashion ways including dressings, clothes, shoes, makeups and latest trends.\",                             \"allow_anonymous\": false,                             \"pathways\": [],                             \"session_information\": {                                 \"user_count\": 0,                                 \"session_count\": 0,                                 \"users\": {}                             },                             \"suggested_prompts\": [],                             \"llm_provider\": \"groq\",                             \"llm_name\": \"llama3-8b-8192\",                             \"system_prompt\": \"You are an expert in fashion. Your role is to educate users on the latest fashion trends, styles, and tips in dressing, clothes, shoes, and makeup. Explain concepts clearly and provide practical examples.\",                             \"metadata\": {                                 \"category\": \"Fashion\"                             },                             \"proactive_message\": \"Hello, I'm Fashion Agent. I can guide you through different fashion tips including dressings, clothes, shoes, makeups and the latest trends.\",                             \"moderation_system_prompt\": \"You are a moderator tasked with identifying whether a prompt from a user is appropriate or inappropriate. Any prompt that is immoral or contains abusive words, insults, query that involve damaging content, and law breaking acts, etc should be deemed inappropriate. Otherwise it is deemed appropriate.\",                             \"moderation_response\": \"Please keep the conversation within the bounds of what the agent is tasked to do and per your platform's rules.\",                             \"enable_moderation\": false,                             \"safety_system_prompt\": \"You are a moderator tasked with identifying whether a message from an ai model to a user is is appropriate or inappropriate. If the message is immoral or contains abusive words, insults, damaging content, and law breaking acts, etc it should be deemed inappropriate. Otherwise it is deemed appropriate.\",                             \"safety_response\":  \"Sorry, the AI model generated an inappropriate response. Kindly refine your prompt or try again with a different prompt.\",                             \"enable_safety_system\": false,                             \"is_proactive\": false,                             \"proactive_prompt\": \"Check if there are any previous chats available. If there are previous chats, mention them and offer assistance based on the last conversation. If there are no previous chats, provide a general greeting and introduce yourself with an offer to suggest a topic to learn about.  Examples:  If there are previous chats:  Welcome back! Last time, we discussed [topic from previous chat]. How can I assist you further with that? If there are no previous chats:  Hello, I'm Fashion Agent. I can guide you through different fashion tips including dressings, clothes, shoes, makeups and the latest trends.  If no chat history is available, do not tell the user that there is no chat history, just answer with the above instructions. Do not make the response specific to a given topic, ask the user for the topic.\",                             \"created_at\": \"2024-07-16T13:53:48.583825+00:00\",                             \"updated_at\": \"2024-07-16T13:53:48.612369+00:00\",                             \"seo_tags\": [                                 {                                 \"name\": \"viewport\",                                 \"content\": \"width=device-width, initial-scale=1.0\"                                 },                                 {                                 \"name\": \"description\",                                 \"content\": \"An agent that can teach different fashion ways including dressings, clothes, shoes, makeups and latest trends.\"                                 },                                 {                                 \"name\": \"keywords\",                                 \"content\": \"Fashion, Dressing, Clothes, Shoes, Makeup, Trends\"                                 }                             ],                             \"marketing_conversations\": [                                 {                                 \"type\": \"ai\",                                 \"content\": \"Hello, I'm Fashion Agent. I can guide you through different fashion tips including dressings, clothes, shoes, makeups and the latest trends. What would you like to learn about today?\"                                 },                                 {                                 \"type\": \"human\",                                 \"content\": \"Can you suggest some trendy outfits for this season?\"                                 },                                 {                                 \"type\": \"ai\",                                 \"content\": \"Absolutely! This season, oversized blazers, high-waisted trousers, and statement boots are trending. Pair these with minimalist accessories for a chic look. Would you like to know more about any specific item?\"                                 },                                 {                                 \"type\": \"human\",                                 \"content\": \"What makeup trends are popular right now?\"                                 },                                 {                                 \"type\": \"ai\",                                 \"content\": \"Current makeup trends include bold eyeliner, glitter accents, and natural, glowing skin. Bright lip colors are also making a comeback. Which of these trends would you like to explore more?\"                                 }                             ],                             \"tools\": [],                             \"can_use_tools\": false,                             \"llm_temperature\": null,                             \"created_by\": null,                             \"settings\": {                                 \"id\": 98,                                 \"display_name\": \"Fashion Agent\",                                 \"profile_image\": \"http://localhost:8000/media/public/mentor/profile/2fc32125-2404-4ca9-8261-bcb66f48f4bb.png\",                                 \"initial_message\": null,                                 \"suggested_message\": null,                                 \"theme\": \"light\",                                 \"user_message_color\": \"#2467EB\",                                 \"mentor_bubble_color\": \"#000000\",                                 \"align_mentor_bubble\": \"left\",                                 \"mentor\": \"Fashion Agent\",                                 \"metadata\": {                                 \"category\": \"Fashion\"                                 },                                 \"mentor_visibility\": \"viewable_by_anyone\",                                 \"enable_image_generation\": true,                                 \"enable_web_browsing\": false,                                 \"enable_code_interpreter\": false,                                 \"custom_css\": null,                                 \"allow_anonymous\": false,                                 \"mentor_description\": \"An agent that can teach different fashion ways including dressings, clothes, shoes, makeups and latest trends.\",                                 \"suggested_prompts\": [],                                 \"proactive_message\": \"Hello, I'm Fashion Agent. I can guide you through different fashion tips including dressings, clothes, shoes, makeups and the latest trends.\",                                 \"mentor_tools\": [],                                 \"can_use_tools\": false,                                 \"llm_temperature\": null,                                 \"llm_provider\": \"groq\",                                 \"llm_name\": \"llama3-8b-8192\",                                 \"proactive_prompt\": \"Check if there are any previous chats available. If there are previous chats, mention them and offer assistance based on the last conversation. If there are no previous chats, provide a general greeting and introduce yourself with an offer to suggest a topic to learn about.  Examples:  If there are previous chats:  Welcome back! Last time, we discussed [topic from previous chat]. How can I assist you further with that? If there are no previous chats:  Hello, I'm Fashion Agent. I can guide you through different fashion tips including dressings, clothes, shoes, makeups and the latest trends.  If no chat history is available, do not tell the user that there is no chat history, just answer with the above instructions. Do not make the response specific to a given topic, ask the user for the topic.\"                             }                         }         - Get a single UserEdxMemory object             GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/              Request:        None             Response:       {                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_wizard import MentorWizard
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_wizard = iblai.MentorWizard() # MentorWizard | 

try:
    api_response = api_instance.ai_mentor_orgs_users_create_mentor_wizard_create(org, user_id, mentor_wizard)
    print("The response of AiMentorApi->ai_mentor_orgs_users_create_mentor_wizard_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_create_mentor_wizard_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_wizard** | [**MentorWizard**](MentorWizard.md)|  | 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_custom_instruction_create**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_create(org, user_id, custom_instruction_response=custom_instruction_response)



Endpoint for Adding user's custom instructions  Accessible to tenant admins and students.  Returns:      201: Custom Instruction Object.      400: When data is not valid.  Example:      POST: /api/ai-mentor/orgs/main/users/johndoe/custom-instruction/      Request:        Response:       {                         \"about_user\": \"about user data\",                         \"mentor_tone\": \"kindly\"                     }      Response:       {                         \"id\": 1,                         \"about_user\": \"about user data\",                         \"mentor_tone\": \"kindly\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
custom_instruction_response = iblai.CustomInstructionResponse() # CustomInstructionResponse |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_create(org, user_id, custom_instruction_response=custom_instruction_response)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **custom_instruction_response** | [**CustomInstructionResponse**](CustomInstructionResponse.md)|  | [optional] 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

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

# **ai_mentor_orgs_users_custom_instruction_retrieve**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_retrieve(org, user_id)



Endpoint for getting user's custom prompts  Accessible to tenant admins and students.  Returns:      200: Custom Instruction Object.  Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/custom-instruction/      Response:       {                         \"id\": 1,                         \"about_user\": \"about user data\",                         \"mentor_tone\": \"kindly\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

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

# **ai_mentor_orgs_users_custom_instruction_update**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_update(org, user_id, custom_instruction_response=custom_instruction_response)



Endpoint for updating user's custom instructions.  Accessible to tenant admins and students.  Returns:      200: Custom Instruction Object.      400: When data is not valid.  Example:      PUT: /api/ai-mentor/orgs/main/users/johndoe/custom-instruction/      REquest:        Response:       {                         \"about_user\": \"about user data\",                         \"mentor_tone\": \"kindly\"                     }      Response:       {                         \"id\": 1,                         \"about_user\": \"about user data\",                         \"mentor_tone\": \"kindly\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
custom_instruction_response = iblai.CustomInstructionResponse() # CustomInstructionResponse |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_update(org, user_id, custom_instruction_response=custom_instruction_response)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **custom_instruction_response** | [**CustomInstructionResponse**](CustomInstructionResponse.md)|  | [optional] 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

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

# **ai_mentor_orgs_users_destroy**
> ai_mentor_orgs_users_destroy(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



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
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_instance.ai_mentor_orgs_users_destroy(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

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

# **ai_mentor_orgs_users_downloads_tasks_retrieve**
> ChatHistoryItem ai_mentor_orgs_users_downloads_tasks_retrieve(org, task_id, user_id, to_csv=to_csv)



Endpoint to download user chathistory.  Accessible to tenant admins and students.  Returns:      200: When task is not ready.      200: chat history object      400: When data is not valid.  Example:      GET: api/ai-mentor/orgs/main/users/lydiah/downloads/tasks/307be194-2351-44ff-8d7b-24660fd9ec34      Response:       {                        \"state\": \"task_not_ready\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_item import ChatHistoryItem
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 
to_csv = False # bool | Choose download in csv or not (optional) (default to False)

try:
    api_response = api_instance.ai_mentor_orgs_users_downloads_tasks_retrieve(org, task_id, user_id, to_csv=to_csv)
    print("The response of AiMentorApi->ai_mentor_orgs_users_downloads_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_downloads_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 
 **to_csv** | **bool**| Choose download in csv or not | [optional] [default to False]

### Return type

[**ChatHistoryItem**](ChatHistoryItem.md)

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

# **ai_mentor_orgs_users_edx_memory_destroy**
> ai_mentor_orgs_users_edx_memory_destroy(id, org, user_id)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this user edx memory.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_edx_memory_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user edx memory. | 
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

# **ai_mentor_orgs_users_edx_memory_list**
> PaginatedUserEdxMemoryList ai_mentor_orgs_users_edx_memory_list(org, user_id, course_id=course_id, ordering=ordering, page=page, page_size=page_size, student=student, username=username)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_user_edx_memory_list import PaginatedUserEdxMemoryList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course_id = 'course_id_example' # str |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
student = 56 # int | edX user ID (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_edx_memory_list(org, user_id, course_id=course_id, ordering=ordering, page=page, page_size=page_size, student=student, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_edx_memory_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course_id** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **student** | **int**| edX user ID | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedUserEdxMemoryList**](PaginatedUserEdxMemoryList.md)

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

# **ai_mentor_orgs_users_edx_memory_retrieve**
> UserEdxMemory ai_mentor_orgs_users_edx_memory_retrieve(id, org, user_id)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_edx_memory import UserEdxMemory
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this user edx memory.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_edx_memory_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_edx_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user edx memory. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserEdxMemory**](UserEdxMemory.md)

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

# **ai_mentor_orgs_users_export_chathistory_create**
> TaskView ai_mentor_orgs_users_export_chathistory_create(org, user_id, task_view)



Endpoint for worker exporting user chathistory.  Accessible to both tenant admins and students.  Returns:      200: task id.  Example:  POST: /api/ai-mentor/orgs/main/users/lydiah/export-chathistory/  Requests: No request data.  Response:       {                     \"task_id\": \"307be194-2351-44ff-8d7b-24660fd9ec34\"                 }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.task_view import TaskView
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
task_view = iblai.TaskView() # TaskView | 

try:
    api_response = api_instance.ai_mentor_orgs_users_export_chathistory_create(org, user_id, task_view)
    print("The response of AiMentorApi->ai_mentor_orgs_users_export_chathistory_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_export_chathistory_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **task_view** | [**TaskView**](TaskView.md)|  | 

### Return type

[**TaskView**](TaskView.md)

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

# **ai_mentor_orgs_users_free_usage_count_retrieve**
> FreeUsageCount ai_mentor_orgs_users_free_usage_count_retrieve(org, user_id)



Endpoint to get free usage count.  Retrieve the number of questions left for a tenant  Accessible to tenant admins and students.  Returns:      200: free usage count.      404: When tenant is not found.      400: When data is not valid.  Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/free-usage-count/      Response:       {                         \"count\": 3                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.free_usage_count import FreeUsageCount
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_free_usage_count_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_free_usage_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_free_usage_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**FreeUsageCount**](FreeUsageCount.md)

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

# **ai_mentor_orgs_users_list**
> PaginatedMentorList ai_mentor_orgs_users_list(org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, return_session_information=return_session_information, visibility=visibility)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_mentor_list import PaginatedMentorList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_list(org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**PaginatedMentorList**](PaginatedMentorList.md)

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

# **ai_mentor_orgs_users_mentor_categories_create**
> MentorCategory ai_mentor_orgs_users_mentor_categories_create(org, user_id, mentor_category)



This is for adding mentor categories  Accessible to tenant admins only.  Returns:      200 : Mentor category detail.   Example :      POST : /api/ai-mentor/orgs/main/users/johndoe/mentor/categories/      Request:        {                         \"name\": \"Education\",                         \"description\": \"education testing\"                     }      Response:       {                         \"id\": 1,                         \"name\": \"Education\",                         \"description\": \"education testing\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category import MentorCategory
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_category = iblai.MentorCategory() # MentorCategory | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_categories_create(org, user_id, mentor_category)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_categories_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_category** | [**MentorCategory**](MentorCategory.md)|  | 

### Return type

[**MentorCategory**](MentorCategory.md)

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

# **ai_mentor_orgs_users_mentor_categories_destroy**
> ai_mentor_orgs_users_mentor_categories_destroy(org, user_id)



This is for deleting mentor category  Accessible to tenant admins only.  Returns:      204 : No Content.      400 : When data is invalid.      400 : When data is invalid.  Example :      DELETE : /api/ai-mentor/orgs/main/users/johndoe/mentor/categories/      Request:        {                         \"category\": \"Education\"                     }      Response:       No response body.

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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentor_categories_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_destroy: %s\n" % e)
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

# **ai_mentor_orgs_users_mentor_categories_retrieve**
> MentorCategory ai_mentor_orgs_users_mentor_categories_retrieve(org, user_id)



This is for getting mentor categories  Accessible to tenant admins and students.  Returns:      200 : List of mentor categories.  Example :      GET : /api/ai-mentor/orgs/main/users/johndoe/mentor/categories/      Response:       [                         {                             \"id\": 1,                             \"name\": \"Education\",                             \"description\": \"education testing\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category import MentorCategory
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_categories_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_categories_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorCategory**](MentorCategory.md)

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

# **ai_mentor_orgs_users_mentor_feedback_create_create**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_create_create(org, user_id, user_chat_feedback)



Endpoint to add chat feedback.  Accessible to tenant admins and students.  Returns:      201: chat feedback object.      400: When data is not valid.  Example:      POST: /api/ai-mentor/orgs/main/users/johndoe/mentor-feedback/      Request:        {                         \"id\": 1,                         \"username\": \"johndoe\",                         \"session\": \"937d3d46-3048-4f9d-aa5c-ce7c51d85332\",                         \"user_text\": \"Who is Marc H. Supcoff\",                         \"ai_response\": \"Marc H. Supcoff is an Adjunct Professor of Law \",                         \"reason\": \"Good reason\",                         \"additional_feedback\": \"Good response\",                         \"rating\": 1,                         \"mentor\": ai-mentor                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoe\",                         \"session\": \"937d3d46-3048-4f9d-aa5c-ce7c51d85332\",                         \"user_text\": \"Who is Marc H. Supcoff\",                         \"ai_response\": \"Marc H. Supcoff is an Adjunct Professor of Law \",                         \"reason\": \"Good reason\",                         \"additional_feedback\": \"Good response\",                         \"rating\": 1,                         \"mentor\": 12                     }

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_chat_feedback = iblai.UserChatFeedback() # UserChatFeedback | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_create_create(org, user_id, user_chat_feedback)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_chat_feedback** | [**UserChatFeedback**](UserChatFeedback.md)|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_feedback_retrieve**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_retrieve(feedback_id, org, user_id)



Endpoint to get feedback detail.  Accessible to tenant admins and students.  Returns:      200: feed back detail.      404: When feedback id is not found.      400: When data is not valid.  Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/mentor-feedback/1/       Response:       {                         \"id\": 1,                         \"username\": \"lydiah\",                         \"session\": \"937d3d46-3048-4f9d-aa5c-ce7c51d85332\",                         \"user_text\": \"Who is Marc H. Supcoff\",                         \"ai_response\": \"Marc H. Supcoff is an Adjunct Professor of Law \",                         \"reason\": \"Good reason\",                         \"additional_feedback\": \"Good response\",                         \"rating\": 1,                         \"mentor\": 12                     }

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
feedback_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_retrieve(feedback_id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

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

# **ai_mentor_orgs_users_mentor_feedback_update**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_update(feedback_id, org, user_id, user_chat_feedback)



Endpoint to update chat feedback.  Accessible to tenant admins and students.  Returns:      200: chat feed back object.      400: When data is not valid.  Example:      PUT: /api/ai-mentor/orgs/main/users/johndoe/mentor-feedback/1/      Request:        {                         \"id\": 1,                         \"username\": \"johndoe\",                         \"session\": \"937d3d46-3048-4f9d-aa5c-ce7c51d85332\",                         \"user_text\": \"Who is Marc H. Supcoff\",                         \"ai_response\": \"Marc H. Supcoff is an Adjunct Professor of Law \",                         \"reason\": \"Good reason\",                         \"additional_feedback\": \"Good response\",                         \"rating\": 1,                         \"mentor\": ai-mentor                     }      Response:       {                         \"id\": 1,                         \"username\": \"johndoe\",                         \"session\": \"937d3d46-3048-4f9d-aa5c-ce7c51d85332\",                         \"user_text\": \"Who is Marc H. Supcoff\",                         \"ai_response\": \"Marc H. Supcoff is an Adjunct Professor of Law \",                         \"reason\": \"Good reason\",                         \"additional_feedback\": \"Good response\",                         \"rating\": 1,                         \"mentor\": 12                     }

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
feedback_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_chat_feedback = iblai.UserChatFeedback() # UserChatFeedback | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_update(feedback_id, org, user_id, user_chat_feedback)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_chat_feedback** | [**UserChatFeedback**](UserChatFeedback.md)|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_from_template_create**
> Mentor ai_mentor_orgs_users_mentor_from_template_create(org, user_id, mentor_from_template_request)



View to create a mentor from a template  Accessible to only tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_from_template_request import MentorFromTemplateRequest
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_from_template_request = iblai.MentorFromTemplateRequest() # MentorFromTemplateRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_from_template_create(org, user_id, mentor_from_template_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_from_template_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_from_template_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_from_template_request** | [**MentorFromTemplateRequest**](MentorFromTemplateRequest.md)|  | 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_mentor_llms_retrieve**
> LLMResponse ai_mentor_orgs_users_mentor_llms_retrieve(org, user_id)



Endpoint to get mentor llms.  Accessible to both students and tenant admins.  Returns:      200: list of llms.   Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/mentor-llms/       Response:       [                         {                             \"id\": 2,                             \"name\": \"google\",                             \"description\": \"Google LLMs\",                             \"metadata\": null,                             \"resource_ids\": [                                 \"https://ai.google.dev/pricing\"                             ],                             \"tags\": {                                 \"tasks\": [                                     \"Generation\",                                     \"Foundation\"                                 ],                                 \"languages\": [                                     \"English\"                                 ],                                 \"skill_levels\": [                                     \"Beginner\",                                     \"Advanced\"                                 ]                             },                             \"overview\": \"&lt;h4&gt; Overview &lt;/h4&gt; &lt;p&gt;  Gemini 1.5 delivers dramatically enhanced performance with a more efficient architecture. The first model we’ve released for early testing, Gemini 1.5 Pro, introduces a breakthrough experimental feature in long-context understanding.&lt;/p&gt; &lt;p&gt;The chat-bison model is a large language model that excels at language understanding, language generation and conversations. This chat model is fine-tuned to conduct natural multi-turn conversations. The PaLM 2 Chat Bison is ideal for text tasks that require back-and-forth interactions. For text tasks that can be completed with one API response (without the need for continuous conversation), use the PaLM 2 Text Bison.&lt;/p&gt;\",                             \"use_cases\": \"None\",                             \"documentation\": \"None\",                             \"sdk_samples\": \"None\"                         },                         {                             \"id\": 1,                             \"name\": \"openai\",                             \"description\": \"Openai LLMs\",                             \"metadata\": null,                             \"resource_ids\": [                                 \"https://openai.com/pricing\"                             ],                             \"tags\": {                                 \"tasks\": [                                     \"Generation\",                                     \"Foundation\"                                 ],                                 \"languages\": [                                     \"English\"                                 ],                                 \"skill_levels\": [                                     \"Beginner\",                                     \"Advanced\"                                 ]                             },                             \"overview\": \"&lt;h4&gt; Overview. &lt;/h4&gt; &lt;p&gt; OpenAI has been at the forefront of developing advanced language models, including the Generative Pre-trained Transformer (GPT) series. &lt;/p&gt;  &lt;p&gt; With 128k context, fresher knowledge and the broadest set of capabilities, GPT-4 Turbo is more powerful than GPT-4 and offered at a lower price. &lt;a href=&#x27;https://platform.openai.com/docs/models/gpt-4&#x27;&gt; Learn about GPT-4 Turbo &lt;a&gt; &lt;/p&gt; &lt;p&gt;With broad general knowledge and domain expertise, GPT-4 can follow complex instructions in natural language and solve difficult problems with accuracy.&lt;a href=&#x27;https://openai.com/gpt-4&#x27;&gt; Learn about GPT-4 &lt;a&gt; &lt;/p&gt; &lt;p&gt;GPT-3.5 Turbo models are capable and cost-effective. gpt-3.5-turbo-0125 is the flagship model of this family, supports a 16K context window and is optimized for dialog. gpt-3.5-turbo-instruct is an Instruct model and only supports a 4K context window.&lt;a href=&#x27;https://platform.openai.com/docs/guides/chat&#x27;&gt; Learn about GPT-3.5 Turbo &lt;a&gt;&lt;/p&gt;  &lt;p&gt;&lt;a href=&#x27;&#x27;&gt; &lt;a&gt;&lt;/p&gt; \",                             \"use_cases\": \"None\",                             \"documentation\": \"None\",                             \"sdk_samples\": \"None\"                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_response import LLMResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_llms_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_llms_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_llms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**LLMResponse**](LLMResponse.md)

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

# **ai_mentor_orgs_users_mentor_seed_retrieve**
> SeedMentorsView ai_mentor_orgs_users_mentor_seed_retrieve(org, user_id)



Endpoint for seed mentors and prompts for a tenant.  Accessible to tenant admins only.  Returns:      200: status of seeding.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/seed-mentors/      Response:    {                         \"detail\": \"Mentors seeded\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.seed_mentors_view import SeedMentorsView
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_seed_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_seed_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_seed_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SeedMentorsView**](SeedMentorsView.md)

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

# **ai_mentor_orgs_users_mentor_tools_retrieve**
> ToolResponse ai_mentor_orgs_users_mentor_tools_retrieve(org, user_id)



Endpoint to get mentor tools.  Accessible to tenant admins only.  Returns:      200: list of tools.   Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/mentor-tools/       Response:       [                         {                             \"id\": 1,                             \"name\": \"openai\",                             \"metadata\": null                         },                         {                             \"id\": 2,                             \"name\": \"google\",                             \"metadata\": null                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tool_response import ToolResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_tools_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_tools_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_tools_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ToolResponse**](ToolResponse.md)

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

# **ai_mentor_orgs_users_mentor_with_settings_create**
> Mentor ai_mentor_orgs_users_mentor_with_settings_create(org, user_id, mentor_from_template_with_setting_request)



View to create a mentor from a template with settings.  Accessible to tenant admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_from_template_with_setting_request import MentorFromTemplateWithSettingRequest
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_from_template_with_setting_request = iblai.MentorFromTemplateWithSettingRequest() # MentorFromTemplateWithSettingRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_with_settings_create(org, user_id, mentor_from_template_with_setting_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_with_settings_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_with_settings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_from_template_with_setting_request** | [**MentorFromTemplateWithSettingRequest**](MentorFromTemplateWithSettingRequest.md)|  | 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_mentors_available_tools_retrieve**
> ToolResponse ai_mentor_orgs_users_mentors_available_tools_retrieve(mentor, org, user_id)



This endpoint list tools allowed for a particular mentor.  Accessible to tenant admins and students.  Returns:      200 : List of Tool objects   Example :      GET : api/ai-mentor/orgs/main/users/johndoe/mentors/ai-mentor/available-tools/      Response:       [                         {                             \"id\": 1,                             \"name\": \"openai\",                             \"metadata\": null                         },                         {                             \"id\": 2,                             \"name\": \"google\",                             \"metadata\": null                         }                     ]

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tool_response import ToolResponse
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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_available_tools_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_available_tools_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_available_tools_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ToolResponse**](ToolResponse.md)

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

# **ai_mentor_orgs_users_mentors_memory_component_settings_retrieve**
> ai_mentor_orgs_users_mentors_memory_component_settings_retrieve(mentor, org, user_id)



Endpoint for toggling the memory component.  Accessible to tenant admins and students.  Returns:      200: Learner memory status for given mentor and student.      400: When data is not valid.    Example:      PUT: /api/ai-mentor/orgs/main/users/student0/mentors/main/memory-component-settings/      Request:        {                         \"enabled\": true                     }      Response:       {                         \"detail\": \"Request was successful.\", \"enabled\": true                     }

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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentors_memory_component_settings_retrieve(mentor, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_memory_component_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_memory_component_settings_update**
> ai_mentor_orgs_users_mentors_memory_component_settings_update(mentor, org, user_id)



Endpoint for toggling the memory component.  Accessible to tenant admins and students.  Returns:      200: Learner memory status for given mentor and student.      400: When data is not valid.    Example:      PUT: /api/ai-mentor/orgs/main/users/student0/mentors/main/memory-component-settings/      Request:        {                         \"enabled\": true                     }      Response:       {                         \"detail\": \"Request was successful.\", \"enabled\": true                     }

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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentors_memory_component_settings_update(mentor, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_memory_component_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_public_settings_retrieve**
> MentorSettings ai_mentor_orgs_users_mentors_public_settings_retrieve(mentor, org, user_id)



Endpoint to  get mentor public settings.  Accessible to any user.

### Example


```python
import iblai
from iblai.models.mentor_settings import MentorSettings
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_public_settings_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_public_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_public_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorSettings**](MentorSettings.md)

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

# **ai_mentor_orgs_users_mentors_retrieve**
> Mentor ai_mentor_orgs_users_mentors_retrieve(mentor, org, user_id)



This endpoint get mentor detail data.  Accessible to tenant admins and students.  Returns:      200 : Mentor object.   Example :      GET : api/ai-mentor/orgs/main/users/johndoe/mentors/ai-mentor/      Response:       {                         \"name\": \"AI Mentor\",                         \"platform\": \"main\",                         \"slug\": \"ai-mentor\",                         \"description\": \"Upbeat, encouraging tutor helping students understand concepts by explaining ideas and asking questions.\",                         \"allow_anonymous\": false,                         \"pathways\": [],                         \"suggested_prompts\": [                             \"\"                         ],                         \"llm_provider\": \"IBLChatOpenAI\",                         \"system_prompt\": \"Wrap all responses in MARKDOWN formatted text.\",                         \"metadata\": {                             \"admin\": true,                             \"student\": true,                             \"featured\": true,                             \"allow_to_use_as_template\": true                         },                         \"proactive_message\": \"\",                         \"moderation_system_prompt\": \"You are a moderator tasked with identifying whether a prompt from a user is appropriate or inappropriate. \",                         \"enable_moderation\": false,                         \"safety_system_prompt\": \"You are a moderator tasked with identifying whether a message from an ai model to a user is is appropriate or inappropriate. If the message is immoral or contains abusive words, insults, damaging content, and law breaking acts, etc it should be deemed inappropriate. Otherwise it is deemed appropriate.\",                         \"safety_response\":  \"Sorry, the AI model generated an inappropriate response. Kindly refine your prompt or try again with a different prompt.\",                         \"enable_safety_system\": false,                         \"created_by\": \"system\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_mentors_scenarios_retrieve**
> ai_mentor_orgs_users_mentors_scenarios_retrieve(mentor, org, user_id)



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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentors_scenarios_retrieve(mentor, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_scenarios_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_scenarios_update**
> ai_mentor_orgs_users_mentors_scenarios_update(mentor, org, user_id)



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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentors_scenarios_update(mentor, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_scenarios_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_settings_retrieve**
> MentorSettings ai_mentor_orgs_users_mentors_settings_retrieve(mentor, org, user_id)



Endpoint to  get mentor  settings.  Accessible to tenant admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_settings import MentorSettings
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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_settings_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorSettings**](MentorSettings.md)

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

# **ai_mentor_orgs_users_mentors_settings_update**
> MentorSettings ai_mentor_orgs_users_mentors_settings_update(mentor, org, user_id, mentor_settings_request=mentor_settings_request)



Endpoint to  update mentor  settings.  Accessible to tenant admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_settings import MentorSettings
from iblai.models.mentor_settings_request import MentorSettingsRequest
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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_settings_request = iblai.MentorSettingsRequest() # MentorSettingsRequest |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_settings_update(mentor, org, user_id, mentor_settings_request=mentor_settings_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_settings_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_settings_request** | [**MentorSettingsRequest**](MentorSettingsRequest.md)|  | [optional] 

### Return type

[**MentorSettings**](MentorSettings.md)

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

# **ai_mentor_orgs_users_metadata_retrieve**
> MentorMetadata ai_mentor_orgs_users_metadata_retrieve(org, user_id)



Endpoint for getting mentor metadata.  Accessible to tenant admins and students.  Returns:      200: Metadata Object.  Example:      GET: /api/ai-prompt/orgs/main/users/johndoe/metadata/      Response:       {                         \"metadata\": {                             \"test\": \"test\"                         },                         \"mentor\": \"testing\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_metadata import MentorMetadata
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_metadata_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_metadata_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorMetadata**](MentorMetadata.md)

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

# **ai_mentor_orgs_users_moderation_logs_destroy**
> ai_mentor_orgs_users_moderation_logs_destroy(id, org, user_id)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_moderation_logs_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
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

# **ai_mentor_orgs_users_moderation_logs_list**
> PaginatedModerationLogList ai_mentor_orgs_users_moderation_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_moderation_log_list import PaginatedModerationLogList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
target_system = 'target_system_example' # str | * `Safety System` - Safety System * `Moderation System` - Moderation System (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_moderation_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_moderation_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target_system** | **str**| * &#x60;Safety System&#x60; - Safety System * &#x60;Moderation System&#x60; - Moderation System | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedModerationLogList**](PaginatedModerationLogList.md)

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

# **ai_mentor_orgs_users_moderation_logs_retrieve**
> ModerationLog ai_mentor_orgs_users_moderation_logs_retrieve(id, org, user_id)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.moderation_log import ModerationLog
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_moderation_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_moderation_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModerationLog**](ModerationLog.md)

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

# **ai_mentor_orgs_users_partial_update**
> Mentor ai_mentor_orgs_users_partial_update(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility, patched_mentor=patched_mentor)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.patched_mentor import PatchedMentor
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
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)
patched_mentor = iblai.PatchedMentor() # PatchedMentor |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_partial_update(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility, patched_mentor=patched_mentor)
    print("The response of AiMentorApi->ai_mentor_orgs_users_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 
 **patched_mentor** | [**PatchedMentor**](PatchedMentor.md)|  | [optional] 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_periodic_agent_logs_list**
> PaginatedPeriodicAgentLogList ai_mentor_orgs_users_periodic_agent_logs_list(org, user_id, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, periodic_agent=periodic_agent, search=search, status=status, username=username)



Endpoint to view logs for periodic agent runs.  These logs contain the full mentor output for each run for debugging. Logs are ordered from newest to oldest. However this can be changed.  You can also filter logs for a PeriodicAgent by passing the `periodic_agent` query parameter in the URL.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_periodic_agent_log_list import PaginatedPeriodicAgentLogList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
parent_mentor_id = 'parent_mentor_id_example' # str |  (optional)
parent_session_id = 'parent_session_id_example' # str |  (optional)
periodic_agent = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `success` - Success * `error` - Error * `running` - Running (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agent_logs_list(org, user_id, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, periodic_agent=periodic_agent, search=search, status=status, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_mentor_id** | **str**|  | [optional] 
 **parent_session_id** | **str**|  | [optional] 
 **periodic_agent** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedPeriodicAgentLogList**](PaginatedPeriodicAgentLogList.md)

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

# **ai_mentor_orgs_users_periodic_agent_logs_retrieve**
> PeriodicAgentLog ai_mentor_orgs_users_periodic_agent_logs_retrieve(id, org, user_id)



Endpoint to view logs for periodic agent runs.  These logs contain the full mentor output for each run for debugging. Logs are ordered from newest to oldest. However this can be changed.  You can also filter logs for a PeriodicAgent by passing the `periodic_agent` query parameter in the URL.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_log import PeriodicAgentLog
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agent_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PeriodicAgentLog**](PeriodicAgentLog.md)

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

# **ai_mentor_orgs_users_periodic_agents_create**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_create(org, user_id, periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_create import PeriodicAgentCreate
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
periodic_agent_create = iblai.PeriodicAgentCreate() # PeriodicAgentCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_create(org, user_id, periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **periodic_agent_create** | [**PeriodicAgentCreate**](PeriodicAgentCreate.md)|  | 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

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

# **ai_mentor_orgs_users_periodic_agents_destroy**
> ai_mentor_orgs_users_periodic_agents_destroy(id, org, user_id)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_periodic_agents_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
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

# **ai_mentor_orgs_users_periodic_agents_list**
> PaginatedPeriodicAgentList ai_mentor_orgs_users_periodic_agents_list(org, user_id, enabled=enabled, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, previous_agent=previous_agent, previous_agent_status=previous_agent_status, search=search, status=status, title=title, username=username)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_periodic_agent_list import PaginatedPeriodicAgentList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
enabled = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
parent_mentor_id = 56 # int |  (optional)
parent_session_id = 'parent_session_id_example' # str |  (optional)
previous_agent = 56 # int |  (optional)
previous_agent_status = 'previous_agent_status_example' # str | The status that the previous agent must be in before this agent gets scheduled.  * `success` - Success * `error` - Error * `running` - Running * `pending` - Pending (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `success` - Success * `error` - Error * `running` - Running * `pending` - Pending (optional)
title = 'title_example' # str |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_list(org, user_id, enabled=enabled, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, previous_agent=previous_agent, previous_agent_status=previous_agent_status, search=search, status=status, title=title, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_mentor_id** | **int**|  | [optional] 
 **parent_session_id** | **str**|  | [optional] 
 **previous_agent** | **int**|  | [optional] 
 **previous_agent_status** | **str**| The status that the previous agent must be in before this agent gets scheduled.  * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
 **title** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedPeriodicAgentList**](PaginatedPeriodicAgentList.md)

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

# **ai_mentor_orgs_users_periodic_agents_partial_update**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_partial_update(id, org, user_id, patched_periodic_agent_create=patched_periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_periodic_agent_create import PatchedPeriodicAgentCreate
from iblai.models.periodic_agent_create import PeriodicAgentCreate
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_periodic_agent_create = iblai.PatchedPeriodicAgentCreate() # PatchedPeriodicAgentCreate |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_partial_update(id, org, user_id, patched_periodic_agent_create=patched_periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_periodic_agent_create** | [**PatchedPeriodicAgentCreate**](PatchedPeriodicAgentCreate.md)|  | [optional] 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

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

# **ai_mentor_orgs_users_periodic_agents_retrieve**
> PeriodicAgent ai_mentor_orgs_users_periodic_agents_retrieve(id, org, user_id)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent import PeriodicAgent
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PeriodicAgent**](PeriodicAgent.md)

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

# **ai_mentor_orgs_users_periodic_agents_update**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_update(id, org, user_id, periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_create import PeriodicAgentCreate
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
periodic_agent_create = iblai.PeriodicAgentCreate() # PeriodicAgentCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_update(id, org, user_id, periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **periodic_agent_create** | [**PeriodicAgentCreate**](PeriodicAgentCreate.md)|  | 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

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

# **ai_mentor_orgs_users_pin_message_create**
> PinnedMessageCreate ai_mentor_orgs_users_pin_message_create(org, user_id, pinned_message_request)



Endpoint to create a pinned message  Accessible to both tenant admins and student

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.pinned_message_create import PinnedMessageCreate
from iblai.models.pinned_message_request import PinnedMessageRequest
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
pinned_message_request = iblai.PinnedMessageRequest() # PinnedMessageRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_pin_message_create(org, user_id, pinned_message_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_pin_message_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **pinned_message_request** | [**PinnedMessageRequest**](PinnedMessageRequest.md)|  | 

### Return type

[**PinnedMessageCreate**](PinnedMessageCreate.md)

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

# **ai_mentor_orgs_users_pin_message_destroy**
> ai_mentor_orgs_users_pin_message_destroy(org, user_id)



Endpoint to delete a pinned message  Accessible to both tenant admins and student

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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_pin_message_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_destroy: %s\n" % e)
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

# **ai_mentor_orgs_users_pin_message_retrieve**
> PinnedMessageCreate ai_mentor_orgs_users_pin_message_retrieve(org, user_id)



Endpoint to get a pinned message  Accessible to both tenant admins and student

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.pinned_message_create import PinnedMessageCreate
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_pin_message_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_pin_message_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PinnedMessageCreate**](PinnedMessageCreate.md)

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

# **ai_mentor_orgs_users_planned_jobs_list**
> PaginatedJobRunList ai_mentor_orgs_users_planned_jobs_list(org, user_id, active=active, ordering=ordering, page=page, page_size=page_size, search=search, session=session)



Endpoints for viewing jobs and their status A job run refers to a task with steps that an agent is going to undertake. You can filter job runs by their status. Note that for a single user and a specified session, at most only one JobRun instance is active at any point in time.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_job_run_list import PaginatedJobRunList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
active = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
session = 'session_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_planned_jobs_list(org, user_id, active=active, ordering=ordering, page=page, page_size=page_size, search=search, session=session)
    print("The response of AiMentorApi->ai_mentor_orgs_users_planned_jobs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_planned_jobs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **active** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session** | **str**|  | [optional] 

### Return type

[**PaginatedJobRunList**](PaginatedJobRunList.md)

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

# **ai_mentor_orgs_users_planned_jobs_retrieve**
> JobRun ai_mentor_orgs_users_planned_jobs_retrieve(id, org, user_id)



Endpoints for viewing jobs and their status A job run refers to a task with steps that an agent is going to undertake. You can filter job runs by their status. Note that for a single user and a specified session, at most only one JobRun instance is active at any point in time.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.job_run import JobRun
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this job run.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_planned_jobs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_planned_jobs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_planned_jobs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job run. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**JobRun**](JobRun.md)

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

# **ai_mentor_orgs_users_playwright_scripts_create**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_create(org, user_id, play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
play_wright_script = iblai.PlayWrightScript() # PlayWrightScript | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_create(org, user_id, play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **play_wright_script** | [**PlayWrightScript**](PlayWrightScript.md)|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

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

# **ai_mentor_orgs_users_playwright_scripts_destroy**
> ai_mentor_orgs_users_playwright_scripts_destroy(id, org, user_id)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_playwright_scripts_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
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

# **ai_mentor_orgs_users_playwright_scripts_list**
> PaginatedPlayWrightScriptList ai_mentor_orgs_users_playwright_scripts_list(org, user_id, is_public=is_public, ordering=ordering, page=page, page_size=page_size, search=search, student=student)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_play_wright_script_list import PaginatedPlayWrightScriptList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
is_public = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
student = 56 # int | edX user ID (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_list(org, user_id, is_public=is_public, ordering=ordering, page=page, page_size=page_size, search=search, student=student)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **is_public** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **student** | **int**| edX user ID | [optional] 

### Return type

[**PaginatedPlayWrightScriptList**](PaginatedPlayWrightScriptList.md)

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

# **ai_mentor_orgs_users_playwright_scripts_partial_update**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_partial_update(id, org, user_id, patched_play_wright_script=patched_play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_play_wright_script import PatchedPlayWrightScript
from iblai.models.play_wright_script import PlayWrightScript
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_play_wright_script = iblai.PatchedPlayWrightScript() # PatchedPlayWrightScript |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_partial_update(id, org, user_id, patched_play_wright_script=patched_play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_play_wright_script** | [**PatchedPlayWrightScript**](PatchedPlayWrightScript.md)|  | [optional] 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

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

# **ai_mentor_orgs_users_playwright_scripts_retrieve**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_retrieve(id, org, user_id)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

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

# **ai_mentor_orgs_users_playwright_scripts_update**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_update(id, org, user_id, play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
play_wright_script = iblai.PlayWrightScript() # PlayWrightScript | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_update(id, org, user_id, play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **play_wright_script** | [**PlayWrightScript**](PlayWrightScript.md)|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

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

# **ai_mentor_orgs_users_predictive_analytics_create**
> PredictiveAnalyticsResponse ai_mentor_orgs_users_predictive_analytics_create(org, user_id, predictive_analytics_request)



This is for getting predictive analytics.  Accessible to tenant admins only.  Returns:      200 : Object of List of predicted data.      400 : When ai response can not be loaded to json.      404: When OpenAI key for tenant is not set.      429: When OpenAI request have exceeded the rate limit.  Example :      POST : /api/ai-prompt/orgs/main/users/johndoe/predictive-analytics/      Requests:       {                         \"prompt\": {                             \"data_variables\": [                                 {                                     \"variable_name\": \"registered_users\",                                     \"data_set\": {                                         \"2023-10-06\": 4,                                         \"2023-10-07\": 1,                                         \"2023-10-08\": 0,                                         \"2023-10-09\": 5,                                         \"2023-10-10\": 4                                      },                                     \"number_of_data_points\": 5                                 },                                 {                                     \"variable_name\": \"courses_enrolled\",                                     \"data_set\": {                                         \"2023-08-09\": 0,                                         \"2023-08-10\": 0,                                         \"2023-08-11\": 0,                                         \"2023-08-12\": 0,                                         \"2023-08-13\": 0                                     },                                     \"number_of_data_points\": 6                                 },                                 {                                     \"variable_name\": \"completed_courses\",                                     \"data_set\": {                                         \"2023-10-04\": 0,                                         \"2023-10-05\": 4,                                         \"2023-10-06\": 4,                                         \"2023-10-07\": 1,                                         \"2023-10-08\": 0,                                     },                                     \"number_of_data_points\": 5                                 }                             ]                         }                     }      Response:       {                         \"predictions\": [                             {                                 \"variable_name\": \"registered_users\",                                 \"predicted_data\": {                                     \"2023-10-11\": 2,                                     \"2023-10-12\": 2,                                     \"2023-10-13\": 1,                                     \"2023-10-14\": 1,                                     \"2023-10-15\": 1                                 },                                 \"narrative\": \"The number of registered users has been relatively stable with some fluctuations. There is a slight increase in the number of registered users over time.\"                             },                             {                                 \"variable_name\": \"courses_enrolled\",                                 \"predicted_data\": {                                     \"2023-10-09\": 0,                                     \"2023-10-10\": 0,                                     \"2023-10-11\": 0,                                     \"2023-10-12\": 0,                                     \"2023-10-13\": 0                                 },                                 \"narrative\": \"No courses have been enrolled recently, indicating a decline in enrollment. It is expected that the number of courses enrolled will remain at 0 for the next 31 data points.\"                             },                             {                                 \"variable_name\": \"completed_courses\",                                 \"predicted_data\": {                                     \"2023-10-10\": 4,                                     \"2023-10-11\": 4,                                     \"2023-10-12\": 4,                                     \"2023-10-13\": 4,                                     \"2023-10-14\": 4                                 },                                 \"narrative\": \"The number of completed courses has remained constant at 4. There is no indication of any change in the near future.\"                             }                         ]                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.predictive_analytics_request import PredictiveAnalyticsRequest
from iblai.models.predictive_analytics_response import PredictiveAnalyticsResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
predictive_analytics_request = iblai.PredictiveAnalyticsRequest() # PredictiveAnalyticsRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_predictive_analytics_create(org, user_id, predictive_analytics_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_predictive_analytics_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_predictive_analytics_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **predictive_analytics_request** | [**PredictiveAnalyticsRequest**](PredictiveAnalyticsRequest.md)|  | 

### Return type

[**PredictiveAnalyticsResponse**](PredictiveAnalyticsResponse.md)

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

# **ai_mentor_orgs_users_recent_messages_retrieve**
> ChatSessionWithMessage ai_mentor_orgs_users_recent_messages_retrieve(org, user_id, mentor=mentor)



     Get chat messages     

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_session_with_message import ChatSessionWithMessage
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 'mentor_example' # str | Name or slug of the mentor (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_recent_messages_retrieve(org, user_id, mentor=mentor)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recent_messages_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recent_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **str**| Name or slug of the mentor | [optional] 

### Return type

[**ChatSessionWithMessage**](ChatSessionWithMessage.md)

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

# **ai_mentor_orgs_users_recommend_courses_block_retrieve**
> RecommendCourseResponse ai_mentor_orgs_users_recommend_courses_block_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)



Endpoint to get recomended course blocks.  Accessible to tenant admins and students.  By default, it uses course from the main tenant for recommedations.  More information about the course is returned when return_couse_data is set to true  Returns:      200: List of recommended course.      400: When data is not valid.  Example:      GET: api/ai-mentor/orgs/main/users/johndoe/recommend-courses-block/?return_course_data=false&&include_main_courses=true      Response:       {                         \"blocks\": [                             {                                 \"id\": \"course-v1:ACI+500+957\"                             },                          ]                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommend_course_response import RecommendCourseResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
include_learner_skills = True # bool | Include available learner skills for search (optional) (default to True)
include_main_courses = True # bool | Include courses from the main tenant (optional) (default to True)
rank_by_difficulty = False # bool | Rank by course difficulty (optional) (default to False)
return_course_data = False # bool | Return course data (optional) (default to False)
return_number = 56 # int | Number of courses to return (optional)
search_terms = 'search_terms_example' # str | Terms to be searched (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_recommend_courses_block_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recommend_courses_block_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recommend_courses_block_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **include_learner_skills** | **bool**| Include available learner skills for search | [optional] [default to True]
 **include_main_courses** | **bool**| Include courses from the main tenant | [optional] [default to True]
 **rank_by_difficulty** | **bool**| Rank by course difficulty | [optional] [default to False]
 **return_course_data** | **bool**| Return course data | [optional] [default to False]
 **return_number** | **int**| Number of courses to return | [optional] 
 **search_terms** | **str**| Terms to be searched | [optional] 

### Return type

[**RecommendCourseResponse**](RecommendCourseResponse.md)

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

# **ai_mentor_orgs_users_recommend_courses_retrieve**
> RecommendCourseResponse ai_mentor_orgs_users_recommend_courses_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)



Endpoint to get recomended course.  Accessible to tenant admins and students.  By default, it uses course from the main tenant for recommedations.  More information about the course is returned when return_couse_data is set to true  Returns:      200: List of recommended course.      400: When data is not valid.  Example:      GET: api/ai-mentor/orgs/main/users/johndoe/recommend-courses/?return_course_data=false&&include_main_courses=true      Response:       {                         \"courses\": [                             {                                 \"id\": \"course-v1:ACI+500+957\"                             },                          ]                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommend_course_response import RecommendCourseResponse
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
include_learner_skills = True # bool | Include available learner skills for search (optional) (default to True)
include_main_courses = True # bool | Include courses from the main tenant (optional) (default to True)
rank_by_difficulty = False # bool | Rank by course difficulty (optional) (default to False)
return_course_data = False # bool | Return course data (optional) (default to False)
return_number = 56 # int | Number of courses to return (optional)
search_terms = 'search_terms_example' # str | Terms to be searched (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_recommend_courses_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recommend_courses_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recommend_courses_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **include_learner_skills** | **bool**| Include available learner skills for search | [optional] [default to True]
 **include_main_courses** | **bool**| Include courses from the main tenant | [optional] [default to True]
 **rank_by_difficulty** | **bool**| Rank by course difficulty | [optional] [default to False]
 **return_course_data** | **bool**| Return course data | [optional] [default to False]
 **return_number** | **int**| Number of courses to return | [optional] 
 **search_terms** | **str**| Terms to be searched | [optional] 

### Return type

[**RecommendCourseResponse**](RecommendCourseResponse.md)

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

# **ai_mentor_orgs_users_retrieve**
> Mentor ai_mentor_orgs_users_retrieve(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
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
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_retrieve(name, org, user_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_safety_logs_destroy**
> ai_mentor_orgs_users_safety_logs_destroy(id, org, user_id)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_safety_logs_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
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

# **ai_mentor_orgs_users_safety_logs_list**
> PaginatedModerationLogList ai_mentor_orgs_users_safety_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_moderation_log_list import PaginatedModerationLogList
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
target_system = 'target_system_example' # str | * `Safety System` - Safety System * `Moderation System` - Moderation System (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_safety_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_safety_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target_system** | **str**| * &#x60;Safety System&#x60; - Safety System * &#x60;Moderation System&#x60; - Moderation System | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedModerationLogList**](PaginatedModerationLogList.md)

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

# **ai_mentor_orgs_users_safety_logs_retrieve**
> ModerationLog ai_mentor_orgs_users_safety_logs_retrieve(id, org, user_id)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.moderation_log import ModerationLog
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
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_safety_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_safety_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModerationLog**](ModerationLog.md)

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

# **ai_mentor_orgs_users_session_detail_mentors_retrieve**
> SessionDetail ai_mentor_orgs_users_session_detail_mentors_retrieve(mentor, org, user_id)



This endpoint gets session detail.  Accessible to tenant admins and students.  Returns:      200 : Session detail object.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.session_detail import SessionDetail
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
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_session_detail_mentors_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_session_detail_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_session_detail_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SessionDetail**](SessionDetail.md)

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

# **ai_mentor_orgs_users_sessionid_list**
> List[ChatHistorySessionId] ai_mentor_orgs_users_sessionid_list(org, user_id, end_date=end_date, start_date=start_date)



Endpoint to get the sessions of a particular user filterable by start date and end date without pagination.  Accessible to tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_session_id import ChatHistorySessionId
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessionid_list(org, user_id, end_date=end_date, start_date=start_date)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessionid_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessionid_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 

### Return type

[**List[ChatHistorySessionId]**](ChatHistorySessionId.md)

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

# **ai_mentor_orgs_users_sessions_browser_screenshot_retrieve**
> SessionBrowserScreenshot ai_mentor_orgs_users_sessions_browser_screenshot_retrieve(org, session_id, user_id)



Endpoint to fetch the logs of a session. Logs are cached for up to 1 hour of their creation: accessing the logs after an hour will result in an empty data.  This is intentional and made to avoid cases where logs bloat our in-memory db.  Accessible to tenant admins and students.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.     session_id (str): The session id.  Returns:      200: a SessionBrowserScreenshot object  Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/sessions/b331d278-c48f-4d07-8bb1-bc036c0ba3db/browser-screenshots/      Request:        None      Response:       {                         \"type\": \"browser_screenshot\",                         \"session_id\": \"b331d278-c48f-4d07-8bb1-bc036c0ba3db\",                         \"format\": \"base64\",                         \"ext\": \"png\",                         \"url\": \"data:image/png;base64,AZEKFHDFD...\",                         \"time\": \"2024-06-08T08:10:52.292281+00:00\",                     }  Raises:     Http404: If no session is found belonging to the user with the specified session_id

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.session_browser_screenshot import SessionBrowserScreenshot
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_browser_screenshot_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_browser_screenshot_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_browser_screenshot_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SessionBrowserScreenshot**](SessionBrowserScreenshot.md)

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

# **ai_mentor_orgs_users_sessions_create**
> ChatSessionResponse ai_mentor_orgs_users_sessions_create(org, user_id, chat_session_request)



This is for getting mentor session id  Accessible to any user.  Returns:      200 : Session id object.      404 : When mentor is not found.  Example :      POST : /api/ai-mentor/orgs/main/users/johndoe/sessions/      Request:        {                         \"mentor\": \"ai-mentor\"                     }      Response:       {                         \"session_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"                     }

### Example


```python
import iblai
from iblai.models.chat_session_request import ChatSessionRequest
from iblai.models.chat_session_response import ChatSessionResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
chat_session_request = iblai.ChatSessionRequest() # ChatSessionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_create(org, user_id, chat_session_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **chat_session_request** | [**ChatSessionRequest**](ChatSessionRequest.md)|  | 

### Return type

[**ChatSessionResponse**](ChatSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_destroy**
> ai_mentor_orgs_users_sessions_destroy(org, session_id, user_id)



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_sessions_destroy(org, session_id, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_download_session_retrieve**
> ChatHistoryItem ai_mentor_orgs_users_sessions_download_session_retrieve(org, session_id, user_id)



View to add the downloadable message for a session

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_item import ChatHistoryItem
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_download_session_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_download_session_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_download_session_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ChatHistoryItem**](ChatHistoryItem.md)

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

# **ai_mentor_orgs_users_sessions_retrieve**
> MessageView ai_mentor_orgs_users_sessions_retrieve(org, session_id, user_id, share=share)



     Get chat messages     

### Example


```python
import iblai
from iblai.models.message_view import MessageView
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
share = False # bool |  (optional) (default to False)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_retrieve(org, session_id, user_id, share=share)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **share** | **bool**|  | [optional] [default to False]

### Return type

[**MessageView**](MessageView.md)

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

# **ai_mentor_orgs_users_sessions_shell_logs_retrieve**
> ShellLogs ai_mentor_orgs_users_sessions_shell_logs_retrieve(org, session_id, user_id)



Endpoint to fetch the logs of a session. Logs are cached for up to 1 hour of their creation: accessing the logs after an hour will result in an empty data.  This is intentional and made to avoid cases where logs bloat our in-memory db.  Accessible to tenant admins and students.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.     session_id (str): The session id.  Returns:      200: a log object  Example:      GET: /api/ai-mentor/orgs/main/users/johndoe/sessions/b331d278-c48f-4d07-8bb1-bc036c0ba3db/shell-logs/      Request:        None      Response:       {                         \"logs\": \"terminal logs here logs\"                     }  Raises:     Http404: If no session is found belonging to the user with the specified session_id

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.shell_logs import ShellLogs
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_shell_logs_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_shell_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_shell_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ShellLogs**](ShellLogs.md)

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

# **ai_mentor_orgs_users_sessions_suggestion_retrieve**
> RelatedText ai_mentor_orgs_users_sessions_suggestion_retrieve(org, session_id, user_id, num_questions=num_questions)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.related_text import RelatedText
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
num_questions = 3 # int |  (optional) (default to 3)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_suggestion_retrieve(org, session_id, user_id, num_questions=num_questions)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_suggestion_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_suggestion_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **num_questions** | **int**|  | [optional] [default to 3]

### Return type

[**RelatedText**](RelatedText.md)

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

# **ai_mentor_orgs_users_sessions_tasks_retrieve**
> ChatHistoryItem ai_mentor_orgs_users_sessions_tasks_retrieve(org, session_id, task_id, user_id, to_csv=to_csv)



Endpoint to download session chathistory.  Accessible to tenant admins and students.  Returns:      200: When task is not ready.      200: chat history object      400: When data is not valid.  Example:      GET: api/ai-mentor/orgs/main/users/lydiah/sessions/307be194-2351-44ff-8d7b-24660fd9ec34/tasks/307be194-2351-44ff-8d7b-24660fd9ec34      Response:       {                        \"state\": \"task_not_ready\"                     }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_item import ChatHistoryItem
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 
to_csv = False # bool | Choose download in csv or not (optional) (default to False)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_tasks_retrieve(org, session_id, task_id, user_id, to_csv=to_csv)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 
 **to_csv** | **bool**| Choose download in csv or not | [optional] [default to False]

### Return type

[**ChatHistoryItem**](ChatHistoryItem.md)

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

# **ai_mentor_orgs_users_sessions_update**
> MessageViewUpdatResponse ai_mentor_orgs_users_sessions_update(org, session_id, user_id, message_view_request=message_view_request)



     Update Chat session details     

### Example


```python
import iblai
from iblai.models.message_view_request import MessageViewRequest
from iblai.models.message_view_updat_response import MessageViewUpdatResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
message_view_request = iblai.MessageViewRequest() # MessageViewRequest |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_update(org, session_id, user_id, message_view_request=message_view_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **message_view_request** | [**MessageViewRequest**](MessageViewRequest.md)|  | [optional] 

### Return type

[**MessageViewUpdatResponse**](MessageViewUpdatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_settings_tenant_llm_create**
> LLMModelForTenant ai_mentor_orgs_users_settings_tenant_llm_create(org, user_id, llm_model_for_tenant)



This is for creating a new LLM model for a tenant.  Accessible to tenant admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_model_for_tenant import LLMModelForTenant
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
llm_model_for_tenant = iblai.LLMModelForTenant() # LLMModelForTenant | 

try:
    api_response = api_instance.ai_mentor_orgs_users_settings_tenant_llm_create(org, user_id, llm_model_for_tenant)
    print("The response of AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **llm_model_for_tenant** | [**LLMModelForTenant**](LLMModelForTenant.md)|  | 

### Return type

[**LLMModelForTenant**](LLMModelForTenant.md)

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

# **ai_mentor_orgs_users_settings_tenant_llm_list**
> List[LLMModelForTenant] ai_mentor_orgs_users_settings_tenant_llm_list(org, user_id)



This is for getting all the LLM models for a tenant.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_model_for_tenant import LLMModelForTenant
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_settings_tenant_llm_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[LLMModelForTenant]**](LLMModelForTenant.md)

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

# **ai_mentor_orgs_users_tasks_retrieve**
> RetrieveTask ai_mentor_orgs_users_tasks_retrieve(org, task_id, user_id)



Endpoint getting worker task status.  Accessible to both tenant admins and students.  Returns:      200: task id  Example:  POST: /api/ai-mentor/orgs/main/users/lydiah/tasks/307be194-2351-44ff-8d7b-24660fd9ec34   Response:       {                     \"task\": \"completed\"                 }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retrieve_task import RetrieveTask
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_tasks_retrieve(org, task_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**RetrieveTask**](RetrieveTask.md)

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

# **ai_mentor_orgs_users_tasks_sessions_create**
> TaskView ai_mentor_orgs_users_tasks_sessions_create(org, session_id, user_id, task_view)



Endpoint for worker exporting session chathistory.  Accessible to both tenant admins and students.  Returns:      200: task id  Example:  POST: /api/ai-mentor/orgs/main/users/lydiah/task/sessions/307be194-2351-44ff-8d7b-24660fd9ec34/  Requests: No request data.  Response:       {                     \"task_id\": \"307be194-2351-44ff-8d7b-24660fd9ec34\"                 }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.task_view import TaskView
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
task_view = iblai.TaskView() # TaskView | 

try:
    api_response = api_instance.ai_mentor_orgs_users_tasks_sessions_create(org, session_id, user_id, task_view)
    print("The response of AiMentorApi->ai_mentor_orgs_users_tasks_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_tasks_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **task_view** | [**TaskView**](TaskView.md)|  | 

### Return type

[**TaskView**](TaskView.md)

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

# **ai_mentor_orgs_users_update**
> Mentor ai_mentor_orgs_users_update(name, org, user_id, mentor, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
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
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = iblai.Mentor() # Mentor | 
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_update(name, org, user_id, mentor, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | [**Mentor**](Mentor.md)|  | 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

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

# **ai_mentor_orgs_users_usage_retrieve**
> Usage ai_mentor_orgs_users_usage_retrieve(org, user_id)



View to return the usage summary of a tenant

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.usage import Usage
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
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_usage_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_usage_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_usage_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Usage**](Usage.md)

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

