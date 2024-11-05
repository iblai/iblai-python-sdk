# Program


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**institution** | [**Institution**](Institution.md) |  | [readonly] 
**institution_id** | **int** |  | 
**name** | **str** |  | 
**program_type** | [**ProgramTypeEnum**](ProgramTypeEnum.md) |  | 
**duration** | **int** | Duration in months | 
**description** | **str** |  | [optional] 
**data** | **object** | Metadata | [optional] 
**metadata** | **object** | Metadata | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.program import Program

# TODO update the JSON string below
json = "{}"
# create an instance of Program from a JSON string
program_instance = Program.from_json(json)
# print the JSON string representation of the object
print(Program.to_json())

# convert the object into a dict
program_dict = program_instance.to_dict()
# create an instance of Program from a dict
program_from_dict = Program.from_dict(program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


