# CourseGradingDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Chapter name | 
**id** | **str** | Chapter Id | 
**subsections** | [**List[CourseGradeDetailSubSection]**](CourseGradeDetailSubSection.md) |  | [optional] 

## Example

```python
from iblai.models.course_grading_detail_data import CourseGradingDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingDetailData from a JSON string
course_grading_detail_data_instance = CourseGradingDetailData.from_json(json)
# print the JSON string representation of the object
print(CourseGradingDetailData.to_json())

# convert the object into a dict
course_grading_detail_data_dict = course_grading_detail_data_instance.to_dict()
# create an instance of CourseGradingDetailData from a dict
course_grading_detail_data_from_dict = CourseGradingDetailData.from_dict(course_grading_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


