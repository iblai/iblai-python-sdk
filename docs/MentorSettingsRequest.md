# MentorSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**featured** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**mentor_visibility** | **str** |  | [optional] 
**enable_image_generation** | **str** |  | [optional] 
**enable_web_browsing** | **str** |  | [optional] 
**enable_code_interpreter** | **str** |  | [optional] 
**allow_anonymous** | **str** |  | [optional] 
**mentor_description** | **str** |  | [optional] 
**uploaded_profile_image** | **str** |  | [optional] 
**proactive_message** | **str** |  | [optional] 
**tool_slugs** | **List[str]** |  | [optional] 
**llm_temperature** | **float** |  | [optional] 

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

