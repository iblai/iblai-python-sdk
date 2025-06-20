# Document

Serializer for document objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Document ID | 
**document_name** | **str** | Name of the document | 
**document_type** | **str** | Type of document (e.g., &#39;pdf&#39;, &#39;text&#39;) | 
**access** | **str** | Access level of the document | 
**training_status** | **str** | Training status of the document | 
**date_created** | **datetime** | Date when the document was created | 
**last_modified** | **datetime** | Date when the document was last modified | 
**url** | **str** | URL to access the document | 
**metadata** | **object** | Additional metadata for the document | 

## Example

```python
from iblai.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


