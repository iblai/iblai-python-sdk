# Conversations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**messages** | **str** |  | [readonly] 
**topics** | [**List[TopicModel]**](TopicModel.md) |  | 
**sentiment** | **str** |  | [readonly] 
**mentor** | **str** |  | 
**student** | **str** |  | [readonly] 
**email** | **str** |  | [readonly] 
**model** | **str** |  | 
**rating** | **int** |  | [readonly] 
**platform** | **str** |  | 
**lti_email** | **str** | Email claim from LTI1.3 JWT if an LTI user and available | [readonly] 
**lti_username** | **str** | Username claim from LTI1.3 JWT if an LTI user and available | [readonly] 
**inserted_at** | **datetime** |  | [readonly] 
**has_document** | **bool** |  | [optional] 
**memory_tracked** | **bool** |  | [optional] 
**enable_artifacts** | **bool** |  | [optional] 
**is_shared** | **bool** |  | [optional] 
**is_authenticated** | **bool** | False if session was created by an anonymous user | [optional] 
**llm_name** | **str** |  | [optional] 
**llm_provider** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**title** | **str** | AI-generated title summarizing the conversation | [optional] 
**is_conversation** | **bool** | True if the session has both user and AI messages | [optional] 
**message_count_human** | **int** | Count of human messages in this session | [optional] 
**message_count_ai** | **int** | Count of AI messages in this session | [optional] 
**tools** | **List[int]** |  | [optional] 

## Example

```python
from iblai.models.conversations import Conversations

# TODO update the JSON string below
json = "{}"
# create an instance of Conversations from a JSON string
conversations_instance = Conversations.from_json(json)
# print the JSON string representation of the object
print(Conversations.to_json())

# convert the object into a dict
conversations_dict = conversations_instance.to_dict()
# create an instance of Conversations from a dict
conversations_from_dict = Conversations.from_dict(conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


