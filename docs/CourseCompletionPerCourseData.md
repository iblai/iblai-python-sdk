# CourseCompletionPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | 
**name** | **str** | Course Name | 
**enrollments** | **int** | Number of enrollments | 
**completions** | **int** | Number of completions | 
**average** | **float** | Average Completions. | 

## Example

```python
from iblai.models.course_completion_per_course_data import CourseCompletionPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionPerCourseData from a JSON string
course_completion_per_course_data_instance = CourseCompletionPerCourseData.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionPerCourseData.to_json())

# convert the object into a dict
course_completion_per_course_data_dict = course_completion_per_course_data_instance.to_dict()
# create an instance of CourseCompletionPerCourseData from a dict
course_completion_per_course_data_from_dict = CourseCompletionPerCourseData.from_dict(course_completion_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


