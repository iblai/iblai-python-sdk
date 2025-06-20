# ProgramGroupSuggestionDetail

Response serializer for program group suggestion details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the group suggestion | 
**group_id** | **int** | The ID of the group receiving the suggestion | 
**group_name** | **str** | The name of the group receiving the suggestion | 
**platform_key** | **str** | The platform key associated with the suggestion | 
**accepted** | **bool** | Whether the suggestion has been accepted | 
**visible** | **bool** | Whether the suggestion is visible | 
**created** | **datetime** | When the suggestion was created | 
**modified** | **datetime** | When the suggestion was last modified | 
**metadata** | **Dict[str, object]** | Additional metadata for the suggestion | 
**program_key** | **str** | The program key being suggested | 
**program_name** | **str** | The name of the program being suggested | 
**user_count** | **int** | Number of users in the group | 

## Example

```python
from iblai.models.program_group_suggestion_detail import ProgramGroupSuggestionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramGroupSuggestionDetail from a JSON string
program_group_suggestion_detail_instance = ProgramGroupSuggestionDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramGroupSuggestionDetail.to_json())

# convert the object into a dict
program_group_suggestion_detail_dict = program_group_suggestion_detail_instance.to_dict()
# create an instance of ProgramGroupSuggestionDetail from a dict
program_group_suggestion_detail_from_dict = ProgramGroupSuggestionDetail.from_dict(program_group_suggestion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


