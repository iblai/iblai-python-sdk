# ChatSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor** | **str** | Name of mentor | 
**tools** | **List[str]** | List of tools slugs to use. Passing &#x60;null&#x60; will use all tools assigned to the mentor. For no tools, pass an empty list. | [optional] 

## Example

```python
from iblai.models.chat_session_request import ChatSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSessionRequest from a JSON string
chat_session_request_instance = ChatSessionRequest.from_json(json)
# print the JSON string representation of the object
print(ChatSessionRequest.to_json())

# convert the object into a dict
chat_session_request_dict = chat_session_request_instance.to_dict()
# create an instance of ChatSessionRequest from a dict
chat_session_request_from_dict = ChatSessionRequest.from_dict(chat_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


