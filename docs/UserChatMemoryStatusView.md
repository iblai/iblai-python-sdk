# UserChatMemoryStatusView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | 
**platform_key** | **str** |  | 
**enabled** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_chat_memory_status_view import UserChatMemoryStatusView

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatMemoryStatusView from a JSON string
user_chat_memory_status_view_instance = UserChatMemoryStatusView.from_json(json)
# print the JSON string representation of the object
print(UserChatMemoryStatusView.to_json())

# convert the object into a dict
user_chat_memory_status_view_dict = user_chat_memory_status_view_instance.to_dict()
# create an instance of UserChatMemoryStatusView from a dict
user_chat_memory_status_view_from_dict = UserChatMemoryStatusView.from_dict(user_chat_memory_status_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


