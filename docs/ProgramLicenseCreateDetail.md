# ProgramLicenseCreateDetail

Request serializer for ProgramLicenseCreateView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The unique identifier for the platform (required if platform_id not provided) | [optional] 
**platform_org** | **str** | The organization identifier for the platform (required if platform_id not provided) | [optional] 
**platform_id** | **int** | The ID of the platform (required if platform_key/org not provided) | [optional] 
**program_key** | **str** | The unique identifier for the program to license | 
**name** | **str** | Display name for the license | 
**count** | **int** | Number of seats purchased | 
**started** | **datetime** | Date when license should begin | 
**expired** | **datetime** | Date when license should expire | [optional] 
**external_id** | **str** | External identifier for the license | [optional] 
**active** | **bool** | Whether the license should be active | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional license metadata | [optional] 
**enrollment_config** | **Dict[str, object]** | Enrollment configuration | [optional] 
**source** | **str** | Source identifier | [optional] [default to 'api']
**transaction_id** | **str** | Transaction identifier for tracking | [optional] 

## Example

```python
from iblai.models.program_license_create_detail import ProgramLicenseCreateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseCreateDetail from a JSON string
program_license_create_detail_instance = ProgramLicenseCreateDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseCreateDetail.to_json())

# convert the object into a dict
program_license_create_detail_dict = program_license_create_detail_instance.to_dict()
# create an instance of ProgramLicenseCreateDetail from a dict
program_license_create_detail_from_dict = ProgramLicenseCreateDetail.from_dict(program_license_create_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


