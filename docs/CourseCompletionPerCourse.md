# CourseCompletionPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CourseCompletionPerCourseData]**](CourseCompletionPerCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.course_completion_per_course import CourseCompletionPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionPerCourse from a JSON string
course_completion_per_course_instance = CourseCompletionPerCourse.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionPerCourse.to_json())

# convert the object into a dict
course_completion_per_course_dict = course_completion_per_course_instance.to_dict()
# create an instance of CourseCompletionPerCourse from a dict
course_completion_per_course_from_dict = CourseCompletionPerCourse.from_dict(course_completion_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


