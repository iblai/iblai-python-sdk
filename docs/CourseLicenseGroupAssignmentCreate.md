# CourseLicenseGroupAssignmentCreate

Request serializer for CourseLicenseGroupAssignmentView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **int** | The ID of the course license | 
**group_id** | **int** | The group ID to assign the license to | 
**platform_key** | **str** | The unique identifier for the platform | [optional] 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**active** | **bool** | Whether the assignment is active | [optional] [default to True]
**fulfilled** | **bool** | Whether the assignment has been fulfilled | [optional] [default to False]
**metadata** | **Dict[str, object]** | Additional metadata for the assignment | [optional] 

## Example

```python
from iblai.models.course_license_group_assignment_create import CourseLicenseGroupAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLicenseGroupAssignmentCreate from a JSON string
course_license_group_assignment_create_instance = CourseLicenseGroupAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(CourseLicenseGroupAssignmentCreate.to_json())

# convert the object into a dict
course_license_group_assignment_create_dict = course_license_group_assignment_create_instance.to_dict()
# create an instance of CourseLicenseGroupAssignmentCreate from a dict
course_license_group_assignment_create_from_dict = CourseLicenseGroupAssignmentCreate.from_dict(course_license_group_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


