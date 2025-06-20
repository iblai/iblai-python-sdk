# PaginatedProgramSuggestion

Response serializer for paginated program suggestion list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[ProgramSuggestionDetail]**](ProgramSuggestionDetail.md) | List of program suggestions | 

## Example

```python
from iblai.models.paginated_program_suggestion import PaginatedProgramSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProgramSuggestion from a JSON string
paginated_program_suggestion_instance = PaginatedProgramSuggestion.from_json(json)
# print the JSON string representation of the object
print(PaginatedProgramSuggestion.to_json())

# convert the object into a dict
paginated_program_suggestion_dict = paginated_program_suggestion_instance.to_dict()
# create an instance of PaginatedProgramSuggestion from a dict
paginated_program_suggestion_from_dict = PaginatedProgramSuggestion.from_dict(paginated_program_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


