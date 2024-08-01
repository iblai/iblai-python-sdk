# DetailedGradeSubsection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Subsection name | 
**id** | **str** | Subsection Id | 
**graded_earned** | **str** | Subsection earned mark | 
**graded_possible** | **str** | Subsection Possible Mark | 
**graded_percent** | **str** | Subsection Grade | 

## Example

```python
from iblai.models.detailed_grade_subsection import DetailedGradeSubsection

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedGradeSubsection from a JSON string
detailed_grade_subsection_instance = DetailedGradeSubsection.from_json(json)
# print the JSON string representation of the object
print(DetailedGradeSubsection.to_json())

# convert the object into a dict
detailed_grade_subsection_dict = detailed_grade_subsection_instance.to_dict()
# create an instance of DetailedGradeSubsection from a dict
detailed_grade_subsection_from_dict = DetailedGradeSubsection.from_dict(detailed_grade_subsection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


