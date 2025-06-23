# ProgramLicenseAssignmentDetail

Response serializer for program license assignment details.  This serializer represents a program license assignment with all its attributes, including user information, license details, and assignment status.  Fields:     id: The unique identifier for the assignment     user_id: The ID of the user assigned the license (may be null for email-only assignments)     username: The username of the user assigned the license (may be null for email-only assignments)     name: The full name of the user assigned the license (may be null for email-only assignments)     email: The email address of the user assigned the license (may be null for user-only assignments)     active: Whether the assignment is active and valid     fulfilled: Whether the assignment has been processed/fulfilled     direct: Whether the assignment was directly assigned to the user (vs. via a group)     redirect_to: URL to redirect to after fulfillment     metadata: Additional metadata for the assignment     created: When the assignment was created     modified: When the assignment was last modified     license_id: The ID of the program license     license_name: The name of the program license     program_key: The program key associated with the license

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment | 
**user_id** | **int** | The ID of the user assigned the license | 
**username** | **str** | The username of the user assigned the license | 
**name** | **str** | The full name of the user assigned the license | 
**email** | **str** | The email address of the user assigned the license | 
**active** | **bool** | Whether the assignment is active and valid | 
**fulfilled** | **bool** | Whether the assignment has been processed/fulfilled | 
**direct** | **bool** | Whether the assignment was directly assigned to the user (vs. via a group) | [optional] 
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | 
**created** | **datetime** | When the assignment was created | [optional] 
**modified** | **datetime** | When the assignment was last modified | [optional] 
**license_id** | **int** | The ID of the program license | 
**license_name** | **str** | The name of the program license | 
**program_key** | **str** | The program key associated with the license | 

## Example

```python
from iblai.models.program_license_assignment_detail import ProgramLicenseAssignmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseAssignmentDetail from a JSON string
program_license_assignment_detail_instance = ProgramLicenseAssignmentDetail.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseAssignmentDetail.to_json())

# convert the object into a dict
program_license_assignment_detail_dict = program_license_assignment_detail_instance.to_dict()
# create an instance of ProgramLicenseAssignmentDetail from a dict
program_license_assignment_detail_from_dict = ProgramLicenseAssignmentDetail.from_dict(program_license_assignment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


