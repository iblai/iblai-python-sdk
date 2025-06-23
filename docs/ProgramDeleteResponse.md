# ProgramDeleteResponse

Serializer for program deletion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of programs deleted | 
**type** | **Dict[str, object]** | Types of objects deleted | 

## Example

```python
from iblai.models.program_delete_response import ProgramDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramDeleteResponse from a JSON string
program_delete_response_instance = ProgramDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramDeleteResponse.to_json())

# convert the object into a dict
program_delete_response_dict = program_delete_response_instance.to_dict()
# create an instance of ProgramDeleteResponse from a dict
program_delete_response_from_dict = ProgramDeleteResponse.from_dict(program_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


