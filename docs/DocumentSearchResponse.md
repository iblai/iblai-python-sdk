# DocumentSearchResponse

Response serializer for DocumentSearchView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Document]**](Document.md) | List of documents matching the search criteria | 
**count** | **int** | Total number of documents matching the search criteria | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 
**facets** | [**Dict[str, DocumentFacet]**](DocumentFacet.md) | Facet information for filtering | 

## Example

```python
from iblai.models.document_search_response import DocumentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSearchResponse from a JSON string
document_search_response_instance = DocumentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentSearchResponse.to_json())

# convert the object into a dict
document_search_response_dict = document_search_response_instance.to_dict()
# create an instance of DocumentSearchResponse from a dict
document_search_response_from_dict = DocumentSearchResponse.from_dict(document_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


