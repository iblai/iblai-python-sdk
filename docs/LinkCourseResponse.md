# LinkCourseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor_unique_id** | **str** |  | 
**course_id** | **str** |  | [optional] 
**is_linked** | **bool** |  | 

## Example

```python
from iblai.models.link_course_response import LinkCourseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkCourseResponse from a JSON string
link_course_response_instance = LinkCourseResponse.from_json(json)
# print the JSON string representation of the object
print(LinkCourseResponse.to_json())

# convert the object into a dict
link_course_response_dict = link_course_response_instance.to_dict()
# create an instance of LinkCourseResponse from a dict
link_course_response_from_dict = LinkCourseResponse.from_dict(link_course_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


