# UserAllChatMemoryView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | 
**platform_key** | **str** |  | 
**content** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from iblai.models.user_all_chat_memory_view import UserAllChatMemoryView

# TODO update the JSON string below
json = "{}"
# create an instance of UserAllChatMemoryView from a JSON string
user_all_chat_memory_view_instance = UserAllChatMemoryView.from_json(json)
# print the JSON string representation of the object
print(UserAllChatMemoryView.to_json())

# convert the object into a dict
user_all_chat_memory_view_dict = user_all_chat_memory_view_instance.to_dict()
# create an instance of UserAllChatMemoryView from a dict
user_all_chat_memory_view_from_dict = UserAllChatMemoryView.from_dict(user_all_chat_memory_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


