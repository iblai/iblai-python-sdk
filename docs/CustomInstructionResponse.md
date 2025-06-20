# CustomInstructionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**about_user** | **str** |  | [optional] 
**mentor_tone** | **str** |  | [optional] 
**profession** | **str** | Position or work. eg: Engineer, student etc. | [optional] 
**desired_mentor_traits** | **str** | Comma separated list of expected traits for mentor. | [optional] 

## Example

```python
from iblai.models.custom_instruction_response import CustomInstructionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInstructionResponse from a JSON string
custom_instruction_response_instance = CustomInstructionResponse.from_json(json)
# print the JSON string representation of the object
print(CustomInstructionResponse.to_json())

# convert the object into a dict
custom_instruction_response_dict = custom_instruction_response_instance.to_dict()
# create an instance of CustomInstructionResponse from a dict
custom_instruction_response_from_dict = CustomInstructionResponse.from_dict(custom_instruction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


