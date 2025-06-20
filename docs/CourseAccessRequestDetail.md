# CourseAccessRequestDetail

Response serializer for access request details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the access request | 
**user_id** | **int** | The ID of the user who made the request | 
**username** | **str** | The username of the user who made the request | 
**name** | **str** | The full name of the user who made the request | 
**approved** | **bool** | Whether the request has been approved (null if not reviewed) | 
**reviewed** | **bool** | Whether the request has been reviewed | 
**created** | **datetime** | When the request was created | 
**modified** | **datetime** | When the request was last modified | 
**metadata** | **Dict[str, object]** | Additional metadata for the request | [optional] 
**platform_key** | **str** | The platform key associated with the request | 
**course_id** | **str** | The course ID associated with the request | 

## Example

```python
from iblai.models.course_access_request_detail import CourseAccessRequestDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAccessRequestDetail from a JSON string
course_access_request_detail_instance = CourseAccessRequestDetail.from_json(json)
# print the JSON string representation of the object
print(CourseAccessRequestDetail.to_json())

# convert the object into a dict
course_access_request_detail_dict = course_access_request_detail_instance.to_dict()
# create an instance of CourseAccessRequestDetail from a dict
course_access_request_detail_from_dict = CourseAccessRequestDetail.from_dict(course_access_request_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


