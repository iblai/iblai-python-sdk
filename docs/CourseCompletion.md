# CourseCompletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** |  | 
**completion_percentage** | **float** |  | [optional] 
**passed** | **bool** |  | [optional] 
**passed_date** | **datetime** |  | [optional] 

## Example

```python
from iblai.models.course_completion import CourseCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletion from a JSON string
course_completion_instance = CourseCompletion.from_json(json)
# print the JSON string representation of the object
print(CourseCompletion.to_json())

# convert the object into a dict
course_completion_dict = course_completion_instance.to_dict()
# create an instance of CourseCompletion from a dict
course_completion_from_dict = CourseCompletion.from_dict(course_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


