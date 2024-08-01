# ChatSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 

## Example

```python
from iblai.models.chat_session_response import ChatSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSessionResponse from a JSON string
chat_session_response_instance = ChatSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ChatSessionResponse.to_json())

# convert the object into a dict
chat_session_response_dict = chat_session_response_instance.to_dict()
# create an instance of ChatSessionResponse from a dict
chat_session_response_from_dict = ChatSessionResponse.from_dict(chat_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


