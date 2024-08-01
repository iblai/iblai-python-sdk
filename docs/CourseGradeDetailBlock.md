# CourseGradeDetailBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Block name | 
**id** | **str** | Block Id | 
**attempts** | **str** | Total users who have attempted it | [optional] 
**average** | **str** | Average block value | 

## Example

```python
from iblai.models.course_grade_detail_block import CourseGradeDetailBlock

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradeDetailBlock from a JSON string
course_grade_detail_block_instance = CourseGradeDetailBlock.from_json(json)
# print the JSON string representation of the object
print(CourseGradeDetailBlock.to_json())

# convert the object into a dict
course_grade_detail_block_dict = course_grade_detail_block_instance.to_dict()
# create an instance of CourseGradeDetailBlock from a dict
course_grade_detail_block_from_dict = CourseGradeDetailBlock.from_dict(course_grade_detail_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


