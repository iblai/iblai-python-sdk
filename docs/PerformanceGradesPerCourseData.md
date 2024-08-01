# PerformanceGradesPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Course name | 
**course_id** | **str** | Course id | 
**num_enrollments** | **int** | Course enrollments | 
**num_passed** | **int** | Total users who have passed the course | 
**avg_grade** | **float** | Course Average grade | 

## Example

```python
from iblai.models.performance_grades_per_course_data import PerformanceGradesPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceGradesPerCourseData from a JSON string
performance_grades_per_course_data_instance = PerformanceGradesPerCourseData.from_json(json)
# print the JSON string representation of the object
print(PerformanceGradesPerCourseData.to_json())

# convert the object into a dict
performance_grades_per_course_data_dict = performance_grades_per_course_data_instance.to_dict()
# create an instance of PerformanceGradesPerCourseData from a dict
performance_grades_per_course_data_from_dict = PerformanceGradesPerCourseData.from_dict(performance_grades_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


