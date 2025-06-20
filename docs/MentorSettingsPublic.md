# MentorSettingsPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**display_name** | **str** |  | [optional] 
**profile_image** | **str** |  | [optional] 
**initial_message** | **str** |  | [optional] 
**suggested_message** | **str** |  | [optional] 
**theme** | [**ThemeEnum**](ThemeEnum.md) |  | [optional] 
**user_message_color** | **str** |  | [optional] 
**mentor_bubble_color** | **str** |  | [optional] 
**align_mentor_bubble** | [**AlignMentorBubbleEnum**](AlignMentorBubbleEnum.md) |  | [optional] 
**mentor** | **str** |  | [readonly] 
**mentor_slug** | **str** |  | [readonly] 
**mentor_unique_id** | **str** |  | [readonly] 
**metadata** | **object** |  | [readonly] 
**mentor_visibility** | [**MentorSettingsMentorVisibility**](MentorSettingsMentorVisibility.md) |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**allow_anonymous** | **bool** |  | [readonly] 
**mentor_description** | **str** |  | [readonly] 
**suggested_prompts** | **object** |  | [readonly] 
**proactive_response** | **str** |  | [readonly] 
**greeting_method** | **str** |  | [readonly] 
**mentor_tools** | **object** |  | [readonly] 
**can_use_tools** | **bool** |  | [readonly] 
**llm_name** | **str** |  | [readonly] 
**proactive_prompt** | **str** |  | [readonly] 
**enable_memory_component** | **bool** |  | [readonly] 
**enable_email_chat** | **bool** |  | [readonly] 
**enable_spaced_repetition** | **bool** |  | [readonly] 
**enable_instruction_mode** | **bool** |  | [readonly] 
**enable_socratic_mode** | **bool** |  | [readonly] 
**is_guided_mentor** | **bool** |  | [readonly] 
**enable_guided_prompts** | **bool** |  | [readonly] 
**enable_moderation** | **bool** |  | [readonly] 
**enable_post_processing_system** | **bool** |  | [readonly] 
**enable_safety_system** | **bool** |  | [readonly] 
**forkable** | **bool** |  | [readonly] 
**forkable_with_training_data** | **bool** |  | [readonly] 

## Example

```python
from iblai.models.mentor_settings_public import MentorSettingsPublic

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSettingsPublic from a JSON string
mentor_settings_public_instance = MentorSettingsPublic.from_json(json)
# print the JSON string representation of the object
print(MentorSettingsPublic.to_json())

# convert the object into a dict
mentor_settings_public_dict = mentor_settings_public_instance.to_dict()
# create an instance of MentorSettingsPublic from a dict
mentor_settings_public_from_dict = MentorSettingsPublic.from_dict(mentor_settings_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


