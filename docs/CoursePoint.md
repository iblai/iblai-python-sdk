# CoursePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The edX course ID string for the course. | 
**points** | **int** |  | 

## Example

```python
from iblai.models.course_point import CoursePoint

# TODO update the JSON string below
json = "{}"
# create an instance of CoursePoint from a JSON string
course_point_instance = CoursePoint.from_json(json)
# print the JSON string representation of the object
print(CoursePoint.to_json())

# convert the object into a dict
course_point_dict = course_point_instance.to_dict()
# create an instance of CoursePoint from a dict
course_point_from_dict = CoursePoint.from_dict(course_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


