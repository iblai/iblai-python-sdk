# DetailedGradeViewData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Chapter name | 
**id** | **str** | Chapter Id | 
**children** | [**List[DetailedGradeSubsection]**](DetailedGradeSubsection.md) |  | [optional] 

## Example

```python
from iblai.models.detailed_grade_view_data import DetailedGradeViewData

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedGradeViewData from a JSON string
detailed_grade_view_data_instance = DetailedGradeViewData.from_json(json)
# print the JSON string representation of the object
print(DetailedGradeViewData.to_json())

# convert the object into a dict
detailed_grade_view_data_dict = detailed_grade_view_data_instance.to_dict()
# create an instance of DetailedGradeViewData from a dict
detailed_grade_view_data_from_dict = DetailedGradeViewData.from_dict(detailed_grade_view_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


