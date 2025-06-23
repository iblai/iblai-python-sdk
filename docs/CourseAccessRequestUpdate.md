# CourseAccessRequestUpdate

Request serializer for CourseLicenseAccessRequestManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **int** | The ID of the access request to update | 
**platform_key** | **str** | The unique identifier for the platform | [optional] 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**approved** | **bool** | Whether to approve the request | [optional] 
**active** | **bool** | Whether the request should remain active | [optional] 

## Example

```python
from iblai.models.course_access_request_update import CourseAccessRequestUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAccessRequestUpdate from a JSON string
course_access_request_update_instance = CourseAccessRequestUpdate.from_json(json)
# print the JSON string representation of the object
print(CourseAccessRequestUpdate.to_json())

# convert the object into a dict
course_access_request_update_dict = course_access_request_update_instance.to_dict()
# create an instance of CourseAccessRequestUpdate from a dict
course_access_request_update_from_dict = CourseAccessRequestUpdate.from_dict(course_access_request_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


