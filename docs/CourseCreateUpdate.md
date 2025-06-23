# CourseCreateUpdate

Serializer for course creation/update request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The unique identifier for the course | 
**org** | **str** | The organization associated with the course | 
**name** | **str** | The name of the course | [optional] 
**slug** | **str** | The slug for the course | [optional] 
**data** | **object** | Additional course data | [optional] 

## Example

```python
from iblai.models.course_create_update import CourseCreateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCreateUpdate from a JSON string
course_create_update_instance = CourseCreateUpdate.from_json(json)
# print the JSON string representation of the object
print(CourseCreateUpdate.to_json())

# convert the object into a dict
course_create_update_dict = course_create_update_instance.to_dict()
# create an instance of CourseCreateUpdate from a dict
course_create_update_from_dict = CourseCreateUpdate.from_dict(course_create_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


