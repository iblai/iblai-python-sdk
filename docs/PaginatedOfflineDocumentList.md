# PaginatedOfflineDocumentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[OfflineDocument]**](OfflineDocument.md) |  | 

## Example

```python
from iblai.models.paginated_offline_document_list import PaginatedOfflineDocumentList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOfflineDocumentList from a JSON string
paginated_offline_document_list_instance = PaginatedOfflineDocumentList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOfflineDocumentList.to_json())

# convert the object into a dict
paginated_offline_document_list_dict = paginated_offline_document_list_instance.to_dict()
# create an instance of PaginatedOfflineDocumentList from a dict
paginated_offline_document_list_from_dict = PaginatedOfflineDocumentList.from_dict(paginated_offline_document_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


