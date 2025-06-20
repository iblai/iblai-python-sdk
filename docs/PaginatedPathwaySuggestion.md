# PaginatedPathwaySuggestion

Response serializer for paginated pathway suggestion list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[PathwaySuggestionDetail]**](PathwaySuggestionDetail.md) | List of pathway suggestions | 

## Example

```python
from iblai.models.paginated_pathway_suggestion import PaginatedPathwaySuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPathwaySuggestion from a JSON string
paginated_pathway_suggestion_instance = PaginatedPathwaySuggestion.from_json(json)
# print the JSON string representation of the object
print(PaginatedPathwaySuggestion.to_json())

# convert the object into a dict
paginated_pathway_suggestion_dict = paginated_pathway_suggestion_instance.to_dict()
# create an instance of PaginatedPathwaySuggestion from a dict
paginated_pathway_suggestion_from_dict = PaginatedPathwaySuggestion.from_dict(paginated_pathway_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


