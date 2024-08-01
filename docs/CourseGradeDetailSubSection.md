# CourseGradeDetailSubSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Block name | 
**id** | **str** | Block Id | 
**attempts** | **str** | Total users who have attempted it | [optional] 
**average** | **str** | Average block value | 
**problems** | [**List[CourseGradeDetailBlock]**](CourseGradeDetailBlock.md) | Problems in section | [optional] 

## Example

```python
from iblai.models.course_grade_detail_sub_section import CourseGradeDetailSubSection

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGradeDetailSubSection from a JSON string
course_grade_detail_sub_section_instance = CourseGradeDetailSubSection.from_json(json)
# print the JSON string representation of the object
print(CourseGradeDetailSubSection.to_json())

# convert the object into a dict
course_grade_detail_sub_section_dict = course_grade_detail_sub_section_instance.to_dict()
# create an instance of CourseGradeDetailSubSection from a dict
course_grade_detail_sub_section_from_dict = CourseGradeDetailSubSection.from_dict(course_grade_detail_sub_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


