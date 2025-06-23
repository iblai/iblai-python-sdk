# GlobalCatalogSearchResponse

Response serializer for GlobalCatalogSearchView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[Dict[str, object]]** | List of content items matching the search criteria | 
**count** | **int** | Total number of items matching the search criteria | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 
**facets** | **Dict[str, object]** | Facet information for filtering | [optional] 

## Example

```python
from iblai.models.global_catalog_search_response import GlobalCatalogSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalCatalogSearchResponse from a JSON string
global_catalog_search_response_instance = GlobalCatalogSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GlobalCatalogSearchResponse.to_json())

# convert the object into a dict
global_catalog_search_response_dict = global_catalog_search_response_instance.to_dict()
# create an instance of GlobalCatalogSearchResponse from a dict
global_catalog_search_response_from_dict = GlobalCatalogSearchResponse.from_dict(global_catalog_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


