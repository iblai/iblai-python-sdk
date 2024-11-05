# TrainDocumentViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathway** | **str** | Pathway for document to be trained in | 
**url** | **str** | Url of the document to be trained | [optional] 
**text** | **str** | Search text for wikipedia | [optional] 
**type** | **str** | Type of document e.g file | 
**file** | **bytearray** | File to be trained | [optional] 
**access** | **str** | Accessibilityto the file | [optional] [default to 'private']
**branch** | **str** | Branch of the repository | [optional] 
**google_drive_auth_data** | **object** | Authentication and scoped details of google drive | [optional] 
**dropbox_auth_data** | **object** | Authentication and scoped details of dropbox | [optional] 

## Example

```python
from iblai.models.train_document_view_request import TrainDocumentViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrainDocumentViewRequest from a JSON string
train_document_view_request_instance = TrainDocumentViewRequest.from_json(json)
# print the JSON string representation of the object
print(TrainDocumentViewRequest.to_json())

# convert the object into a dict
train_document_view_request_dict = train_document_view_request_instance.to_dict()
# create an instance of TrainDocumentViewRequest from a dict
train_document_view_request_from_dict = TrainDocumentViewRequest.from_dict(train_document_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


