# ChatSessionWithMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**mentor** | [**ChartsessionMentor**](ChartsessionMentor.md) |  | 
**messages_count** | **int** |  | 
**messages** | [**List[ChatHistory]**](ChatHistory.md) |  | 

## Example

```python
from iblai.models.chat_session_with_message import ChatSessionWithMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSessionWithMessage from a JSON string
chat_session_with_message_instance = ChatSessionWithMessage.from_json(json)
# print the JSON string representation of the object
print(ChatSessionWithMessage.to_json())

# convert the object into a dict
chat_session_with_message_dict = chat_session_with_message_instance.to_dict()
# create an instance of ChatSessionWithMessage from a dict
chat_session_with_message_from_dict = ChatSessionWithMessage.from_dict(chat_session_with_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


