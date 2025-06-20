# ProgramLicenseGroupAssignmentCreate

Request serializer for ProgramLicenseGroupAssignmentView POST endpoint.  This serializer validates the request data for creating or updating a program license group assignment. Group assignments will automatically create individual assignments for all users in the group.  Fields:     license_id: The ID of the program license to assign     group_id: The ID of the user group to assign the license to     platform_key: The unique identifier for the platform (for permission validation)     platform_org: The organization identifier for the platform (for permission validation)     active: Whether the group assignment should be active     fulfilled: Whether the group assignment should be marked as fulfilled     redirect_to: URL to redirect to after fulfillment     metadata: Additional metadata for the group assignment  Notes:     - All users in the group will receive individual license assignments     - The license must have enough available seats for all users in the group     - If the license doesn't have enough seats, the operation will fail     - Users who already have a direct assignment to this license will not be affected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the program license to assign | 
**group_id** | **int** | The ID of the user group to assign the license to | 
**platform_key** | **str** | The unique identifier for the platform (for permission validation) | [optional] 
**platform_org** | **str** | The organization identifier for the platform (for permission validation) | [optional] 
**active** | **bool** | Whether the group assignment should be active | [optional] [default to True]
**fulfilled** | **bool** | Whether the group assignment should be marked as fulfilled | [optional] [default to False]
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the group assignment | [optional] 

## Example

```python
from iblai.models.program_license_group_assignment_create import ProgramLicenseGroupAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseGroupAssignmentCreate from a JSON string
program_license_group_assignment_create_instance = ProgramLicenseGroupAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseGroupAssignmentCreate.to_json())

# convert the object into a dict
program_license_group_assignment_create_dict = program_license_group_assignment_create_instance.to_dict()
# create an instance of ProgramLicenseGroupAssignmentCreate from a dict
program_license_group_assignment_create_from_dict = ProgramLicenseGroupAssignmentCreate.from_dict(program_license_group_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


