# ProgramCompletionResponse

Response serializer for ProgramCompletionQueryView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of courses in the program | 
**completion_percentage** | **float** | Overall completion percentage for the program (0.0 to 1.0) | 

## Example

```python
from iblai.models.program_completion_response import ProgramCompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCompletionResponse from a JSON string
program_completion_response_instance = ProgramCompletionResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramCompletionResponse.to_json())

# convert the object into a dict
program_completion_response_dict = program_completion_response_instance.to_dict()
# create an instance of ProgramCompletionResponse from a dict
program_completion_response_from_dict = ProgramCompletionResponse.from_dict(program_completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


