# OfflineDocument

Serializes documents for offline use.  Returns documents with S3 URLs that can be downloaded for offline use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tokens** | **int** |  | [optional] 
**is_trained** | **bool** |  | [optional] 
**access** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**last_trained_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.offline_document import OfflineDocument

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineDocument from a JSON string
offline_document_instance = OfflineDocument.from_json(json)
# print the JSON string representation of the object
print(OfflineDocument.to_json())

# convert the object into a dict
offline_document_dict = offline_document_instance.to_dict()
# create an instance of OfflineDocument from a dict
offline_document_from_dict = OfflineDocument.from_dict(offline_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


