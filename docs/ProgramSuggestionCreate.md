# ProgramSuggestionCreate

Request serializer for ProgramSuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestion | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**program_key** | **str** | The program key to suggest | 
**user_id** | **str** | The user to suggest the program to | 
**username** | **str** | The username of the user to suggest the program to | [optional] 
**email** | **str** | The email of the user to suggest the program to | [optional] 
**suggested_by** | **str** | The user who suggested the program | [optional] 
**direct** | **bool** | Whether the suggestion is direct | [optional] [default to True]
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 

## Example

```python
from iblai.models.program_suggestion_create import ProgramSuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramSuggestionCreate from a JSON string
program_suggestion_create_instance = ProgramSuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramSuggestionCreate.to_json())

# convert the object into a dict
program_suggestion_create_dict = program_suggestion_create_instance.to_dict()
# create an instance of ProgramSuggestionCreate from a dict
program_suggestion_create_from_dict = ProgramSuggestionCreate.from_dict(program_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


