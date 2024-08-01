# UserChatMemoryStatusRequestView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable memory use | 

## Example

```python
from iblai.models.user_chat_memory_status_request_view import UserChatMemoryStatusRequestView

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatMemoryStatusRequestView from a JSON string
user_chat_memory_status_request_view_instance = UserChatMemoryStatusRequestView.from_json(json)
# print the JSON string representation of the object
print(UserChatMemoryStatusRequestView.to_json())

# convert the object into a dict
user_chat_memory_status_request_view_dict = user_chat_memory_status_request_view_instance.to_dict()
# create an instance of UserChatMemoryStatusRequestView from a dict
user_chat_memory_status_request_view_from_dict = UserChatMemoryStatusRequestView.from_dict(user_chat_memory_status_request_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


