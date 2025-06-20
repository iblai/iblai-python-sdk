# UserLicenseAssignmentDetail

Response serializer for user license assignment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment | 
**user_id** | **int** | The ID of the user assigned the license | 
**username** | **str** | The username of the user assigned the license | 
**email** | **str** | The email address of the user assigned the license | 
**active** | **bool** | Whether the assignment is active | 
**fulfilled** | **bool** | Whether the assignment has been fulfilled | 
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | 
**license_id** | **int** | The ID of the user license | 
**license_name** | **str** | The name of the user license | 
**platform_key** | **str** | The platform key associated with the license | 

## Example

```python
from iblai.models.user_license_assignment_detail import UserLicenseAssignmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicenseAssignmentDetail from a JSON string
user_license_assignment_detail_instance = UserLicenseAssignmentDetail.from_json(json)
# print the JSON string representation of the object
print(UserLicenseAssignmentDetail.to_json())

# convert the object into a dict
user_license_assignment_detail_dict = user_license_assignment_detail_instance.to_dict()
# create an instance of UserLicenseAssignmentDetail from a dict
user_license_assignment_detail_from_dict = UserLicenseAssignmentDetail.from_dict(user_license_assignment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


