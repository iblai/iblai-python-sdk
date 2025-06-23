# LinkCourseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** |  | 

## Example

```python
from iblai.models.link_course_request import LinkCourseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkCourseRequest from a JSON string
link_course_request_instance = LinkCourseRequest.from_json(json)
# print the JSON string representation of the object
print(LinkCourseRequest.to_json())

# convert the object into a dict
link_course_request_dict = link_course_request_instance.to_dict()
# create an instance of LinkCourseRequest from a dict
link_course_request_from_dict = LinkCourseRequest.from_dict(link_course_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


