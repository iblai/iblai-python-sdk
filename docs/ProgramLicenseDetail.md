# ProgramLicenseDetail

Response serializer for program license details.  This serializer represents a program license with all its attributes, including basic license information, program details, and usage statistics.  Fields:     id: The unique identifier for the license     created: When the license was created     started: When the license becomes active     expired: When the license expires (null if no expiration)     name: The display name of the license     count: The number of seats purchased     active: Whether the license is active     metadata: Additional license metadata     source: The source identifier for the license     external_id: External identifier for the license (null if none)     platform_key: The platform key associated with the license     program_id: The program ID associated with the license     program_name: The name of the program associated with the license     usage_count: Number of assignments using this license     assignments: Assignment counts (if verbose mode is enabled)  Notes:     - The assignments field is only included when verbose=true in the request     - The expired field may be null if the license doesn't expire     - The external_id field may be null if not provided

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the license | 
**created** | **datetime** | When the license was created | 
**started** | **datetime** | When the license becomes active | 
**expired** | **datetime** | When the license expires (null if no expiration) | 
**name** | **str** | The display name of the license | 
**count** | **int** | The number of seats purchased | 
**active** | **bool** | Whether the license is active | 
**metadata** | **Dict[str, object]** | Additional license metadata | 
**source** | **str** | The source identifier for the license | 
**external_id** | **str** | External identifier for the license (null if none) | 
**platform_key** | **str** | The platform key associated with the license | 
**program_id** | **str** | The program ID associated with the license | [optional] 
**program_key** | **str** | The program key associated with the license | [optional] 
**program_name** | **str** | The name of the program associated with the license | [optional] 
**usage_count** | **int** | Number of assignments using this license | 
**assignments** | **Dict[str, int]** | Assignment counts by status (only included in verbose mode) | [optional] 

## Example

```python
from iblai.models.program_license_detail import ProgramLicenseDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseDetail from a JSON string
program_license_detail_instance = ProgramLicenseDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseDetail.to_json())

# convert the object into a dict
program_license_detail_dict = program_license_detail_instance.to_dict()
# create an instance of ProgramLicenseDetail from a dict
program_license_detail_from_dict = ProgramLicenseDetail.from_dict(program_license_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


