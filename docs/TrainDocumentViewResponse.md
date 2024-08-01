# TrainDocumentViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Task ID of the training | 
**message** | **str** | Message of the training | 

## Example

```python
from iblai.models.train_document_view_response import TrainDocumentViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrainDocumentViewResponse from a JSON string
train_document_view_response_instance = TrainDocumentViewResponse.from_json(json)
# print the JSON string representation of the object
print(TrainDocumentViewResponse.to_json())

# convert the object into a dict
train_document_view_response_dict = train_document_view_response_instance.to_dict()
# create an instance of TrainDocumentViewResponse from a dict
train_document_view_response_from_dict = TrainDocumentViewResponse.from_dict(train_document_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


