# MentorFromTemplateWithSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**profile_image** | **str** |  | [optional] 
**initial_message** | **str** |  | [optional] 
**suggested_message** | **str** |  | [optional] 
**new_mentor_name** | **str** |  | 
**theme** | **str** |  | [optional] 
**user_message_color** | **str** |  | [optional] 
**mentor_bubble_color** | **str** |  | [optional] 
**align_mentor_bubble** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**llm_provider** | **str** |  | [optional] 
**llm_name** | **str** |  | [optional] 
**mentor_visibility** | **str** |  | [optional] 
**enable_image_generation** | **bool** |  | [optional] 
**enable_web_browsing** | **bool** |  | [optional] 
**enable_code_interpreter** | **bool** |  | [optional] 
**metadata** | **object** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**uploaded_profile_image** | **str** |  | [optional] 
**proactive_message** | **str** |  | [optional] 
**tool_slugs** | **List[str]** |  | [optional] 
**llm_temperature** | **float** |  | [optional] 
**seo_tags** | **object** |  | [optional] 
**marketing_conversations** | **object** |  | [optional] 
**proactive_prompt** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_from_template_with_setting_request import MentorFromTemplateWithSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorFromTemplateWithSettingRequest from a JSON string
mentor_from_template_with_setting_request_instance = MentorFromTemplateWithSettingRequest.from_json(json)
# print the JSON string representation of the object
print(MentorFromTemplateWithSettingRequest.to_json())

# convert the object into a dict
mentor_from_template_with_setting_request_dict = mentor_from_template_with_setting_request_instance.to_dict()
# create an instance of MentorFromTemplateWithSettingRequest from a dict
mentor_from_template_with_setting_request_from_dict = MentorFromTemplateWithSettingRequest.from_dict(mentor_from_template_with_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


