# CourseCompletionSummaryDataOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overtime** | **Dict[str, object]** | Dates are keys and values are the value for the date in the key. e,g &#x60;{\&quot;2020-01-01\&quot;: 30. ...}&#x60; | [optional] 
**total_user_count** | **int** | Total unique active users in this period | 
**completed_count** | **int** | Total course completions | 
**completed_percent** | **float** | Completion percent for the time range | 

## Example

```python
from iblai.models.course_completion_summary_data_overtime import CourseCompletionSummaryDataOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletionSummaryDataOvertime from a JSON string
course_completion_summary_data_overtime_instance = CourseCompletionSummaryDataOvertime.from_json(json)
# print the JSON string representation of the object
print(CourseCompletionSummaryDataOvertime.to_json())

# convert the object into a dict
course_completion_summary_data_overtime_dict = course_completion_summary_data_overtime_instance.to_dict()
# create an instance of CourseCompletionSummaryDataOvertime from a dict
course_completion_summary_data_overtime_from_dict = CourseCompletionSummaryDataOvertime.from_dict(course_completion_summary_data_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


