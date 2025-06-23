# ProgramLicenseGroupAssignmentDetail

Response serializer for program license group assignment details.  This serializer represents a program license group assignment with all its attributes, including group information, license details, and assignment status.  Fields:     id: The unique identifier for the group assignment     group_id: The ID of the group assigned the license     group_name: The name of the group assigned the license     active: Whether the group assignment is active and valid     fulfilled: Whether the group assignment has been processed/fulfilled     redirect_to: URL to redirect to after fulfillment     metadata: Additional metadata for the group assignment     created: When the group assignment was created     modified: When the group assignment was last modified     license_id: The ID of the program license     license_name: The name of the program license     program_key: The program key associated with the license     program_name: The name of the program associated with the license     user_count: Number of users in the group     assigned_count: Number of users in the group who have been assigned the license

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment | 
**group_id** | **int** | The ID of the group assigned the license | 
**group_name** | **str** | The name of the group assigned the license | 
**active** | **bool** | Whether the assignment is active and valid | 
**fulfilled** | **bool** | Whether the assignment has been processed/fulfilled | 
**redirect_to** | **str** | URL to redirect to after fulfillment | 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | 
**created** | **datetime** | When the assignment was created | 
**modified** | **datetime** | When the assignment was last modified | 
**license_id** | **int** | The ID of the program license | 
**license_name** | **str** | The name of the program license | 
**program_key** | **str** | The program key associated with the license | 
**program_name** | **str** | The name of the program associated with the license | 
**user_count** | **int** | Number of users in the group | 
**assigned_count** | **int** | Number of users in the group who have been assigned the license | 

## Example

```python
from iblai.models.program_license_group_assignment_detail import ProgramLicenseGroupAssignmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseGroupAssignmentDetail from a JSON string
program_license_group_assignment_detail_instance = ProgramLicenseGroupAssignmentDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseGroupAssignmentDetail.to_json())

# convert the object into a dict
program_license_group_assignment_detail_dict = program_license_group_assignment_detail_instance.to_dict()
# create an instance of ProgramLicenseGroupAssignmentDetail from a dict
program_license_group_assignment_detail_from_dict = ProgramLicenseGroupAssignmentDetail.from_dict(program_license_group_assignment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


