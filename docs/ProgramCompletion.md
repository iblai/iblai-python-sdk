# ProgramCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** |  | 
**completion_percentage** | **float** |  | [optional] 
**passed** | **bool** |  | [optional] 
**passed_date** | **datetime** |  | [optional] 

## Example

```python
from iblai.models.program_completion import ProgramCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCompletion from a JSON string
program_completion_instance = ProgramCompletion.from_json(json)
# print the JSON string representation of the object
print(ProgramCompletion.to_json())

# convert the object into a dict
program_completion_dict = program_completion_instance.to_dict()
# create an instance of ProgramCompletion from a dict
program_completion_from_dict = ProgramCompletion.from_dict(program_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


