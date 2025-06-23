# ProgramCreateUpdateRequest

Serializer for program creation/update request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Program ID | 
**program_key** | **str** | Program key | [optional] 
**name** | **str** | Program name | 
**slug** | **str** | Program slug | [optional] 
**org** | **str** | Organization | [optional] 
**platform_key** | **str** | Platform key | [optional] 
**enabled** | **bool** | Whether the program is enabled | [optional] [default to True]
**course_list** | **List[Dict[str, object]]** | List of courses in the program with course_id and optional position | 
**program_type** | **str** | Program type | [optional] 
**data** | **object** | Additional program data | [optional] 

## Example

```python
from iblai.models.program_create_update_request import ProgramCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCreateUpdateRequest from a JSON string
program_create_update_request_instance = ProgramCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProgramCreateUpdateRequest.to_json())

# convert the object into a dict
program_create_update_request_dict = program_create_update_request_instance.to_dict()
# create an instance of ProgramCreateUpdateRequest from a dict
program_create_update_request_from_dict = ProgramCreateUpdateRequest.from_dict(program_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


