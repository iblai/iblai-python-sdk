# ChatHistoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**content** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from iblai.models.chat_history_item import ChatHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistoryItem from a JSON string
chat_history_item_instance = ChatHistoryItem.from_json(json)
# print the JSON string representation of the object
print(ChatHistoryItem.to_json())

# convert the object into a dict
chat_history_item_dict = chat_history_item_instance.to_dict()
# create an instance of ChatHistoryItem from a dict
chat_history_item_from_dict = ChatHistoryItem.from_dict(chat_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


