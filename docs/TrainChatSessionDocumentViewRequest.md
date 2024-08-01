# TrainChatSessionDocumentViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | File to be trained | 

## Example

```python
from iblai.models.train_chat_session_document_view_request import TrainChatSessionDocumentViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrainChatSessionDocumentViewRequest from a JSON string
train_chat_session_document_view_request_instance = TrainChatSessionDocumentViewRequest.from_json(json)
# print the JSON string representation of the object
print(TrainChatSessionDocumentViewRequest.to_json())

# convert the object into a dict
train_chat_session_document_view_request_dict = train_chat_session_document_view_request_instance.to_dict()
# create an instance of TrainChatSessionDocumentViewRequest from a dict
train_chat_session_document_view_request_from_dict = TrainChatSessionDocumentViewRequest.from_dict(train_chat_session_document_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


