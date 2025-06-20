# ProgramMetadataRequest

Request serializer for ProgramMetadataView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | The unique identifier for the program | 
**org** | **str** | The organization associated with the program | [optional] 
**platform_key** | **str** | Platform key identifier (alternative to org) | [optional] 
**program_key** | **str** | Program key (alternative to program_id + org) | [optional] 
**metadata** | **Dict[str, object]** | Metadata to update for the program | 
**update** | **bool** | Whether to update existing metadata | [optional] [default to True]

## Example

```python
from iblai.models.program_metadata_request import ProgramMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramMetadataRequest from a JSON string
program_metadata_request_instance = ProgramMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(ProgramMetadataRequest.to_json())

# convert the object into a dict
program_metadata_request_dict = program_metadata_request_instance.to_dict()
# create an instance of ProgramMetadataRequest from a dict
program_metadata_request_from_dict = ProgramMetadataRequest.from_dict(program_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


