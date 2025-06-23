# PatchedConversations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**messages** | **str** |  | [optional] [readonly] 
**topics** | [**List[TopicModel]**](TopicModel.md) |  | [optional] 
**sentiment** | **str** |  | [optional] [readonly] 
**mentor** | **str** |  | [optional] 
**student** | **str** |  | [optional] [readonly] 
**email** | **str** |  | [optional] [readonly] 
**model** | **str** |  | [optional] 
**rating** | **int** |  | [optional] [readonly] 
**platform** | **str** |  | [optional] 
**lti_email** | **str** | Email claim from LTI1.3 JWT if an LTI user and available | [optional] [readonly] 
**lti_username** | **str** | Username claim from LTI1.3 JWT if an LTI user and available | [optional] [readonly] 
**inserted_at** | **datetime** |  | [optional] [readonly] 
**has_document** | **bool** |  | [optional] 
**memory_tracked** | **bool** |  | [optional] 
**llm_name** | **str** |  | [optional] 
**llm_provider** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**tools** | **List[int]** |  | [optional] 

## Example

```python
from iblai.models.patched_conversations import PatchedConversations

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedConversations from a JSON string
patched_conversations_instance = PatchedConversations.from_json(json)
# print the JSON string representation of the object
print(PatchedConversations.to_json())

# convert the object into a dict
patched_conversations_dict = patched_conversations_instance.to_dict()
# create an instance of PatchedConversations from a dict
patched_conversations_from_dict = PatchedConversations.from_dict(patched_conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


