# ProgramSuggestionBulkCreate

Request serializer for ProgramSuggestionBulkManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestions | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**suggestion_data** | **List[Dict[str, object]]** | List of suggestion data objects, each containing program_key, user_id, etc. | 
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.program_suggestion_bulk_create import ProgramSuggestionBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramSuggestionBulkCreate from a JSON string
program_suggestion_bulk_create_instance = ProgramSuggestionBulkCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramSuggestionBulkCreate.to_json())

# convert the object into a dict
program_suggestion_bulk_create_dict = program_suggestion_bulk_create_instance.to_dict()
# create an instance of ProgramSuggestionBulkCreate from a dict
program_suggestion_bulk_create_from_dict = ProgramSuggestionBulkCreate.from_dict(program_suggestion_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


