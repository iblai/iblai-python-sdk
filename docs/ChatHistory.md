# ChatHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**message** | **object** |  | [optional] 
**inserted_at** | **datetime** |  | [readonly] 
**title** | **str** |  | [optional] 
**feedback** | **str** |  | [readonly] 
**document_sources** | **object** |  | [optional] 

## Example

```python
from iblai.models.chat_history import ChatHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistory from a JSON string
chat_history_instance = ChatHistory.from_json(json)
# print the JSON string representation of the object
print(ChatHistory.to_json())

# convert the object into a dict
chat_history_dict = chat_history_instance.to_dict()
# create an instance of ChatHistory from a dict
chat_history_from_dict = ChatHistory.from_dict(chat_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


