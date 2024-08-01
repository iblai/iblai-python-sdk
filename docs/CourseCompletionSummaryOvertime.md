# CourseCompletionSummaryOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CourseCompletionSummaryDataOvertime**](CourseCompletionSummaryDataOvertime.md) |  | 
**meta** | [**OvertimeMeta**](OvertimeMeta.md) |  | 

## Example

```python
from iblai.models.course_completion_summary_overtime import CourseCompletionSummaryOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionSummaryOvertime from a JSON string
course_completion_summary_overtime_instance = CourseCompletionSummaryOvertime.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionSummaryOvertime.to_json())

# convert the object into a dict
course_completion_summary_overtime_dict = course_completion_summary_overtime_instance.to_dict()
# create an instance of CourseCompletionSummaryOvertime from a dict
course_completion_summary_overtime_from_dict = CourseCompletionSummaryOvertime.from_dict(course_completion_summary_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


