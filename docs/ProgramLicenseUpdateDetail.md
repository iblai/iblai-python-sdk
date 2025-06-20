# ProgramLicenseUpdateDetail

Request serializer for ProgramLicenseUpdateView POST endpoint.  This serializer validates the request data for updating an existing program license. Either license_id or external_id must be provided to identify the license to update.  Fields:     license_id: The ID of the license to update (required if external_id not provided)     external_id: External identifier of the license to update (required if license_id not provided)     name: Updated display name for the license     count: Updated number of seats purchased     started: Updated date when license should begin     expired: Updated date when license should expire     active: Updated active status     metadata: Updated additional license metadata     enrollment_config: Updated enrollment configuration     source: Updated source identifier     transaction_id: Transaction identifier for tracking     change_type: Type of change being made (default: \"update\")  Notes:     - Cannot update the platform or program associated with a license     - A license history record is automatically created for each update     - If count is reduced, it must not be less than the number of active assignments     - Setting active=false will not deactivate existing assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the license to update (required if external_id not provided) | [optional] 
**external_id** | **str** | External identifier of the license to update (required if license_id not provided) | [optional] 
**name** | **str** | Updated display name for the license | [optional] 
**count** | **int** | Updated number of seats purchased | [optional] 
**started** | **datetime** | Updated date when license should begin | [optional] 
**expired** | **datetime** | Updated date when license should expire | [optional] 
**active** | **bool** | Updated active status | [optional] 
**metadata** | **Dict[str, object]** | Updated additional license metadata | [optional] 
**enrollment_config** | **Dict[str, object]** | Updated enrollment configuration | [optional] 
**source** | **str** | Updated source identifier | [optional] 
**transaction_id** | **str** | Transaction identifier for tracking | [optional] 
**change_type** | **str** | Type of change being made | [optional] [default to 'update']

## Example

```python
from iblai.models.program_license_update_detail import ProgramLicenseUpdateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseUpdateDetail from a JSON string
program_license_update_detail_instance = ProgramLicenseUpdateDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseUpdateDetail.to_json())

# convert the object into a dict
program_license_update_detail_dict = program_license_update_detail_instance.to_dict()
# create an instance of ProgramLicenseUpdateDetail from a dict
program_license_update_detail_from_dict = ProgramLicenseUpdateDetail.from_dict(program_license_update_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


