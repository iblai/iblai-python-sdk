# CourseLicenseAssignmentDetail

Response serializer for course license assignment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment | 
**user_id** | **int** | The ID of the user assigned the license | 
**username** | **str** | The username of the user assigned the license | 
**email** | **str** | The email address of the user assigned the license | 
**active** | **bool** | Whether the assignment is active | 
**fulfilled** | **bool** | Whether the assignment has been fulfilled | [optional] 
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | 
**license_id** | **int** | The ID of the course license | 
**license_name** | **str** | The name of the course license | 
**course_id** | **str** | The course ID associated with the license | 

## Example

```python
from iblai.models.course_license_assignment_detail import CourseLicenseAssignmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLicenseAssignmentDetail from a JSON string
course_license_assignment_detail_instance = CourseLicenseAssignmentDetail.from_json(json)
# print the JSON string representation of the object
print(CourseLicenseAssignmentDetail.to_json())

# convert the object into a dict
course_license_assignment_detail_dict = course_license_assignment_detail_instance.to_dict()
# create an instance of CourseLicenseAssignmentDetail from a dict
course_license_assignment_detail_from_dict = CourseLicenseAssignmentDetail.from_dict(course_license_assignment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


