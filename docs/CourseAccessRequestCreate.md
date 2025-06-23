# CourseAccessRequestCreate

Request serializer for CourseLicenseAccessRequestUserView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The unique identifier for the platform | [optional] 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**course_id** | **str** | The unique identifier for the course | 

## Example

```python
from iblai.models.course_access_request_create import CourseAccessRequestCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAccessRequestCreate from a JSON string
course_access_request_create_instance = CourseAccessRequestCreate.from_json(json)
# print the JSON string representation of the object
print(CourseAccessRequestCreate.to_json())

# convert the object into a dict
course_access_request_create_dict = course_access_request_create_instance.to_dict()
# create an instance of CourseAccessRequestCreate from a dict
course_access_request_create_from_dict = CourseAccessRequestCreate.from_dict(course_access_request_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


