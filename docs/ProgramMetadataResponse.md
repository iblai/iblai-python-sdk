# ProgramMetadataResponse

Response serializer for ProgramMetadataView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Program name | [optional] 
**description** | **str** | Program description | [optional] 
**enabled** | **bool** | Whether the program is enabled | [optional] 
**slug** | **str** | Program slug | [optional] 
**skills** | **List[str]** | List of associated skills | [optional] 
**platform_key** | **str** | Platform key | [optional] 

## Example

```python
from iblai.models.program_metadata_response import ProgramMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramMetadataResponse from a JSON string
program_metadata_response_instance = ProgramMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramMetadataResponse.to_json())

# convert the object into a dict
program_metadata_response_dict = program_metadata_response_instance.to_dict()
# create an instance of ProgramMetadataResponse from a dict
program_metadata_response_from_dict = ProgramMetadataResponse.from_dict(program_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


