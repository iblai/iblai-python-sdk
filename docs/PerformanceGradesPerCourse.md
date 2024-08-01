# PerformanceGradesPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PerformanceGradesPerCourseData]**](PerformanceGradesPerCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.performance_grades_per_course import PerformanceGradesPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceGradesPerCourse from a JSON string
performance_grades_per_course_instance = PerformanceGradesPerCourse.from_json(json)
# print the JSON string representation of the object
print(PerformanceGradesPerCourse.to_json())

# convert the object into a dict
performance_grades_per_course_dict = performance_grades_per_course_instance.to_dict()
# create an instance of PerformanceGradesPerCourse from a dict
performance_grades_per_course_from_dict = PerformanceGradesPerCourse.from_dict(performance_grades_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


