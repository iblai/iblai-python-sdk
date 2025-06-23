# ProgramGroupSuggestionCreate

Request serializer for ProgramGroupSuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the group suggestion | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**program_key** | **str** | The program key to suggest | 
**group_id** | **int** | The group to suggest the program to | 
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.program_group_suggestion_create import ProgramGroupSuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramGroupSuggestionCreate from a JSON string
program_group_suggestion_create_instance = ProgramGroupSuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramGroupSuggestionCreate.to_json())

# convert the object into a dict
program_group_suggestion_create_dict = program_group_suggestion_create_instance.to_dict()
# create an instance of ProgramGroupSuggestionCreate from a dict
program_group_suggestion_create_from_dict = ProgramGroupSuggestionCreate.from_dict(program_group_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


