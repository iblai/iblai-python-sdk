# PatchedMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**flow** | **object** | The langflow json for the mentor | [optional] 
**slug** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**allow_anonymous** | **bool** |  | [optional] 
**metadata** | **object** |  | [optional] 
**enable_moderation** | **bool** |  | [optional] 
**is_proactive** | **bool** | If true, the mentor will be prompted to start a conversation with a user. | [optional] 
**proactive_prompt** | **str** | Prompt to start a conversation with a user. This prompt will be fed to the mentor as soon as the user enters the chatroom. This is used if is_proactive is true. | [optional] 
**moderation_system_prompt** | **str** | The prompt for the moderation system. This prompt must clearly distinguish between &#39;Approapriate&#39; and &#39;Not Appropriate&#39; queries. | [optional] 
**moderation_response** | **str** | Desired feedback to return to the user when their prompt is deemed inappropriate. | [optional] 
**proactive_message** | **str** | Prompt to start a conversation with a user. | [optional] 
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mentor import PatchedMentor

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentor from a JSON string
patched_mentor_instance = PatchedMentor.from_json(json)
# print the JSON string representation of the object
print(PatchedMentor.to_json())

# convert the object into a dict
patched_mentor_dict = patched_mentor_instance.to_dict()
# create an instance of PatchedMentor from a dict
patched_mentor_from_dict = PatchedMentor.from_dict(patched_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


