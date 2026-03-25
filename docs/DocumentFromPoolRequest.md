# DocumentFromPoolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_pathway** | **str** | Pathway for document to be trained in. | 
**document_id** | **int** | The document id from pool. | 

## Example

```python
from iblai.models.document_from_pool_request import DocumentFromPoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFromPoolRequest from a JSON string
document_from_pool_request_instance = DocumentFromPoolRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentFromPoolRequest.to_json())

# convert the object into a dict
document_from_pool_request_dict = document_from_pool_request_instance.to_dict()
# create an instance of DocumentFromPoolRequest from a dict
document_from_pool_request_from_dict = DocumentFromPoolRequest.from_dict(document_from_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


