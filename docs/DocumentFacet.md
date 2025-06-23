# DocumentFacet

Serializer for document facets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of documents in this facet | 
**terms** | **Dict[str, object]** | Terms and their counts in this facet | 
**other** | **int** | Count of documents not in any term | 

## Example

```python
from iblai.models.document_facet import DocumentFacet

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentFacet from a JSON string
document_facet_instance = DocumentFacet.from_json(json)
# print the JSON string representation of the object
print(DocumentFacet.to_json())

# convert the object into a dict
document_facet_dict = document_facet_instance.to_dict()
# create an instance of DocumentFacet from a dict
document_facet_from_dict = DocumentFacet.from_dict(document_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


