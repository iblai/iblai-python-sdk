# CourseGradingDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CourseGradingDetailData]**](CourseGradingDetailData.md) |  | [optional] 

## Example

```python
from iblai.models.course_grading_detail import CourseGradingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradingDetail from a JSON string
course_grading_detail_instance = CourseGradingDetail.from_json(json)
# print the JSON string representation of the object
print(CourseGradingDetail.to_json())

# convert the object into a dict
course_grading_detail_dict = course_grading_detail_instance.to_dict()
# create an instance of CourseGradingDetail from a dict
course_grading_detail_from_dict = CourseGradingDetail.from_dict(course_grading_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


