# MentorSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor_name** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**profile_image** | **str** |  | [optional] 
**initial_message** | **str** |  | [optional] 
**suggested_message** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**user_message_color** | **str** |  | [optional] 
**mentor_bubble_color** | **str** |  | [optional] 
**align_mentor_bubble** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**llm_provider** | **str** |  | [optional] 
**llm_name** | **str** |  | [optional] 
**featured** | **bool** |  | [optional] 
**disable_chathistory** | **bool** |  | [optional] 
**metadata** | **object** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**department_id** | **int** | Department to authorize users by | [optional] 
**mentor_visibility** | **str** |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**allow_anonymous** | **bool** |  | [optional] 
**forkable** | **bool** |  | [optional] 
**forkable_with_training_data** | **bool** |  | [optional] 
**mentor_description** | **str** |  | [optional] 
**uploaded_profile_image** | **str** |  | [optional] 
**proactive_response** | **str** |  | [optional] 
**greeting_method** | [**GreetingMethodEnum**](GreetingMethodEnum.md) |  | [optional] 
**can_use_tools** | **bool** |  | [optional] 
**tool_slugs** | **List[str]** |  | [optional] 
**llm_temperature** | **float** |  | [optional] 
**proactive_prompt** | **str** |  | [optional] 
**moderation_system_prompt** | **str** |  | [optional] 
**post_processing_prompt** | **str** |  | [optional] 
**moderation_response** | **str** |  | [optional] 
**enable_moderation** | **bool** |  | [optional] 
**enable_post_processing_system** | **bool** |  | [optional] 
**enable_openai_assistant** | **bool** |  | [optional] 
**enable_total_grounding** | **bool** |  | [optional] 
**enable_suggested_prompts** | **bool** |  | [optional] 
**enable_guided_prompts** | **bool** |  | [optional] 
**mcp_servers** | **List[int]** |  | [optional] 
**google_voice** | **int** |  | [optional] 
**openai_voice** | **int** |  | [optional] 
**guided_prompt_instructions** | **str** |  | [optional] 
**safety_system_prompt** | **str** |  | [optional] 
**safety_response** | **str** |  | [optional] 
**enable_safety_system** | **bool** |  | [optional] 
**enable_memory_component** | **bool** |  | [optional] [default to False]
**enable_spaced_repetition** | **bool** |  | [optional] [default to False]
**enable_instruction_mode** | **bool** |  | [optional] [default to False]
**enable_socratic_mode** | **bool** |  | [optional] [default to False]
**is_guided_mentor** | **bool** |  | [optional] [default to False]
**enable_email_chat** | **bool** |  | [optional] [default to False]
**categories** | **List[int]** |  | [optional] 

## Example

```python
from iblai.models.mentor_settings_request import MentorSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSettingsRequest from a JSON string
mentor_settings_request_instance = MentorSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(MentorSettingsRequest.to_json())

# convert the object into a dict
mentor_settings_request_dict = mentor_settings_request_instance.to_dict()
# create an instance of MentorSettingsRequest from a dict
mentor_settings_request_from_dict = MentorSettingsRequest.from_dict(mentor_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


