# CourseLicenseGroupAssignmentDetail

Response serializer for course license group assignment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment | 
**group_id** | **int** | The ID of the group assigned the license | 
**group_name** | **str** | The name of the group assigned the license | 
**active** | **bool** | Whether the assignment is active | 
**fulfilled** | **bool** | Whether the assignment has been fulfilled | [optional] 
**redirect_to** | **str** | URL to redirect to after fulfillment | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | 
**license_id** | **int** | The ID of the course license | 
**license_name** | **str** | The name of the course license | 
**course_id** | **str** | The course ID associated with the license | 

## Example

```python
from iblai.models.course_license_group_assignment_detail import CourseLicenseGroupAssignmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLicenseGroupAssignmentDetail from a JSON string
course_license_group_assignment_detail_instance = CourseLicenseGroupAssignmentDetail.from_json(json)
# print the JSON string representation of the object
print(CourseLicenseGroupAssignmentDetail.to_json())

# convert the object into a dict
course_license_group_assignment_detail_dict = course_license_group_assignment_detail_instance.to_dict()
# create an instance of CourseLicenseGroupAssignmentDetail from a dict
course_license_group_assignment_detail_from_dict = CourseLicenseGroupAssignmentDetail.from_dict(course_license_group_assignment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


