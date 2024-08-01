# AvgCourseGradeWithCutoffData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_cutoffs** | **Dict[str, object]** | Dictionary showing grade cutoffs | 
**average_grade** | **float** | Course Average grade | 

## Example

```python
from iblai.models.avg_course_grade_with_cutoff_data import AvgCourseGradeWithCutoffData

# TODO update the JSON string below
json = "{}"
# create an instance of AvgCourseGradeWithCutoffData from a JSON string
avg_course_grade_with_cutoff_data_instance = AvgCourseGradeWithCutoffData.from_json(json)
# print the JSON string representation of the object
print(AvgCourseGradeWithCutoffData.to_json())

# convert the object into a dict
avg_course_grade_with_cutoff_data_dict = avg_course_grade_with_cutoff_data_instance.to_dict()
# create an instance of AvgCourseGradeWithCutoffData from a dict
avg_course_grade_with_cutoff_data_from_dict = AvgCourseGradeWithCutoffData.from_dict(avg_course_grade_with_cutoff_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


