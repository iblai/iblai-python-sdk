# UserChatMemoryUpdateView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Id of the schedled task | 
**message** | **str** | Message about the scheduled task | 

## Example

```python
from iblai.models.user_chat_memory_update_view import UserChatMemoryUpdateView

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatMemoryUpdateView from a JSON string
user_chat_memory_update_view_instance = UserChatMemoryUpdateView.from_json(json)
# print the JSON string representation of the object
print(UserChatMemoryUpdateView.to_json())

# convert the object into a dict
user_chat_memory_update_view_dict = user_chat_memory_update_view_instance.to_dict()
# create an instance of UserChatMemoryUpdateView from a dict
user_chat_memory_update_view_from_dict = UserChatMemoryUpdateView.from_dict(user_chat_memory_update_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


