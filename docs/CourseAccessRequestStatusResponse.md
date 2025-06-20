# CourseAccessRequestStatusResponse

Response serializer for CourseLicenseAccessRequestUserView GET endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the access request is active | 
**approved** | **bool** | Whether the access request has been approved (null if not reviewed) | 
**exists** | **bool** | Whether an access request exists for this user and course | 

## Example

```python
from iblai.models.course_access_request_status_response import CourseAccessRequestStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAccessRequestStatusResponse from a JSON string
course_access_request_status_response_instance = CourseAccessRequestStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CourseAccessRequestStatusResponse.to_json())

# convert the object into a dict
course_access_request_status_response_dict = course_access_request_status_response_instance.to_dict()
# create an instance of CourseAccessRequestStatusResponse from a dict
course_access_request_status_response_from_dict = CourseAccessRequestStatusResponse.from_dict(course_access_request_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


