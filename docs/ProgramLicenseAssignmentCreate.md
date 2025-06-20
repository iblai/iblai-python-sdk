# ProgramLicenseAssignmentCreate

Request serializer for ProgramLicenseAssignmentView POST endpoint.  This serializer validates the request data for creating or updating a program license assignment. Either user_id or email must be provided to identify the user to assign the license to.  Fields:     license_id: The ID of the program license to assign     user_id: The user ID to assign the license to (required if email not provided)     username: The username to assign the license to (alternative to user_id)     email: The email to assign the license to (required if user_id not provided)     platform_key: The unique identifier for the platform (for permission validation)     platform_org: The organization identifier for the platform (for permission validation)     active: Whether the assignment should be active     fulfilled: Whether the assignment should be marked as fulfilled     direct: Whether the assignment is being directly assigned to the user     redirect_to: URL to redirect to after fulfillment     metadata: Additional metadata for the assignment  Notes:     - If both user_id and email are provided, user_id takes precedence     - If the user doesn't exist but email is provided, an email-only assignment will be created     - The license must have available seats for the assignment to succeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the program license to assign | 
**user_id** | **int** | The user ID to assign the license to (required if email not provided) | [optional] 
**username** | **str** | The username to assign the license to (alternative to user_id) | [optional] 
**email** | **str** | The email to assign the license to (required if user_id not provided) | [optional] 
**platform_key** | **str** | The unique identifier for the platform (for permission validation) | [optional] 
**platform_org** | **str** | The organization identifier for the platform (for permission validation) | [optional] 
**active** | **bool** | Whether the assignment should be active | [optional] [default to True]
**fulfilled** | **bool** | Whether the assignment should be marked as fulfilled | [optional] [default to False]
**direct** | **bool** | Whether the assignment is being directly assigned to the user | [optional] [default to True]
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | [optional] 

## Example

```python
from iblai.models.program_license_assignment_create import ProgramLicenseAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramLicenseAssignmentCreate from a JSON string
program_license_assignment_create_instance = ProgramLicenseAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(ProgramLicenseAssignmentCreate.to_json())

# convert the object into a dict
program_license_assignment_create_dict = program_license_assignment_create_instance.to_dict()
# create an instance of ProgramLicenseAssignmentCreate from a dict
program_license_assignment_create_from_dict = ProgramLicenseAssignmentCreate.from_dict(program_license_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


