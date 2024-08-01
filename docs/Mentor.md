# Mentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**unique_id** | **str** |  | [optional] 
**flow** | **object** | The langflow json for the mentor | 
**slug** | **str** |  | 
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
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mentor import Mentor

# TODO update the JSON string below
json = "{}"
# create an instance of Mentor from a JSON string
mentor_instance = Mentor.from_json(json)
# print the JSON string representation of the object
print(Mentor.to_json())

# convert the object into a dict
mentor_dict = mentor_instance.to_dict()
# create an instance of Mentor from a dict
mentor_from_dict = Mentor.from_dict(mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


