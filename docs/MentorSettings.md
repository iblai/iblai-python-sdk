# MentorSettings


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
**metadata** | **str** |  | [readonly] 
**mentor_visibility** | [**MentorSettingsMentorVisibility**](MentorSettingsMentorVisibility.md) |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**allow_anonymous** | **str** |  | [readonly] 
**mentor_description** | **str** |  | [readonly] 
**suggested_prompts** | **str** |  | [readonly] 
**proactive_message** | **str** |  | [readonly] 
**mentor_tools** | **str** |  | [readonly] 
**can_use_tools** | **str** |  | [readonly] 
**llm_temperature** | **str** |  | [readonly] 
**llm_provider** | **str** |  | [readonly] 
**llm_name** | **str** |  | [readonly] 
**proactive_prompt** | **str** |  | [readonly] 

## Example

```python
from iblai.models.mentor_settings import MentorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSettings from a JSON string
mentor_settings_instance = MentorSettings.from_json(json)
# print the JSON string representation of the object
print(MentorSettings.to_json())

# convert the object into a dict
mentor_settings_dict = mentor_settings_instance.to_dict()
# create an instance of MentorSettings from a dict
mentor_settings_from_dict = MentorSettings.from_dict(mentor_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

