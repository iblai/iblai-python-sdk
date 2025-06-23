# NoChatMessagesFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] [default to 'No chat messages found.']

## Example

```python
from iblai.models.no_chat_messages_found import NoChatMessagesFound

# TODO update the JSON string below
json = "{}"
# create an instance of NoChatMessagesFound from a JSON string
no_chat_messages_found_instance = NoChatMessagesFound.from_json(json)
# print the JSON string representation of the object
print(NoChatMessagesFound.to_json())

# convert the object into a dict
no_chat_messages_found_dict = no_chat_messages_found_instance.to_dict()
# create an instance of NoChatMessagesFound from a dict
no_chat_messages_found_from_dict = NoChatMessagesFound.from_dict(no_chat_messages_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


