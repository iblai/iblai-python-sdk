# UserLicenseGroupAssignmentCreate

Request serializer for UserLicenseGroupAssignmentView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the user license | 
**group_id** | **int** | The ID of the user group to assign the license to | 
**platform_key** | **str** | The unique identifier for the platform | [optional] 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**active** | **bool** | Whether the assignment is active | [optional] [default to True]
**fulfilled** | **bool** | Whether the assignment has been fulfilled | [optional] [default to False]
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | [optional] 

## Example

```python
from iblai.models.user_license_group_assignment_create import UserLicenseGroupAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicenseGroupAssignmentCreate from a JSON string
user_license_group_assignment_create_instance = UserLicenseGroupAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(UserLicenseGroupAssignmentCreate.to_json())

# convert the object into a dict
user_license_group_assignment_create_dict = user_license_group_assignment_create_instance.to_dict()
# create an instance of UserLicenseGroupAssignmentCreate from a dict
user_license_group_assignment_create_from_dict = UserLicenseGroupAssignmentCreate.from_dict(user_license_group_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


