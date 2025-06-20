# PaginatedProgramGroupSuggestion

Response serializer for paginated program group suggestion list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[ProgramGroupSuggestionDetail]**](ProgramGroupSuggestionDetail.md) | List of program group suggestions | 

## Example

```python
from iblai.models.paginated_program_group_suggestion import PaginatedProgramGroupSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProgramGroupSuggestion from a JSON string
paginated_program_group_suggestion_instance = PaginatedProgramGroupSuggestion.from_json(json)
# print the JSON string representation of the object
print(PaginatedProgramGroupSuggestion.to_json())

# convert the object into a dict
paginated_program_group_suggestion_dict = paginated_program_group_suggestion_instance.to_dict()
# create an instance of PaginatedProgramGroupSuggestion from a dict
paginated_program_group_suggestion_from_dict = PaginatedProgramGroupSuggestion.from_dict(paginated_program_group_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


