# CourseGradeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CourseGradeSummaryData]**](CourseGradeSummaryData.md) |  | [optional] 

## Example

```python
from iblai.models.course_grade_summary import CourseGradeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradeSummary from a JSON string
course_grade_summary_instance = CourseGradeSummary.from_json(json)
# print the JSON string representation of the object
print(CourseGradeSummary.to_json())

# convert the object into a dict
course_grade_summary_dict = course_grade_summary_instance.to_dict()
# create an instance of CourseGradeSummary from a dict
course_grade_summary_from_dict = CourseGradeSummary.from_dict(course_grade_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


