# CourseGradeSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **str** | Assignment Type name | 
**weight** | **float** | Assignment weight | 
**average_weighted_grade** | **float** | Assignment weighted grade average in course | 
**average_section_grade** | **float** | Assignment section grade average in course | 

## Example

```python
from iblai.models.course_grade_summary_data import CourseGradeSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradeSummaryData from a JSON string
course_grade_summary_data_instance = CourseGradeSummaryData.from_json(json)
# print the JSON string representation of the object
print(CourseGradeSummaryData.to_json())

# convert the object into a dict
course_grade_summary_data_dict = course_grade_summary_data_instance.to_dict()
# create an instance of CourseGradeSummaryData from a dict
course_grade_summary_data_from_dict = CourseGradeSummaryData.from_dict(course_grade_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


