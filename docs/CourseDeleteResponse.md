# CourseDeleteResponse

Serializer for course deletion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of courses deleted | 
**type** | **Dict[str, object]** | Types of objects deleted | 

## Example

```python
from iblai.models.course_delete_response import CourseDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseDeleteResponse from a JSON string
course_delete_response_instance = CourseDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(CourseDeleteResponse.to_json())

# convert the object into a dict
course_delete_response_dict = course_delete_response_instance.to_dict()
# create an instance of CourseDeleteResponse from a dict
course_delete_response_from_dict = CourseDeleteResponse.from_dict(course_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


