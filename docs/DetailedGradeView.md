# DetailedGradeView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DetailedGradeViewData]**](DetailedGradeViewData.md) |  | [optional] 

## Example

```python
from iblai.models.detailed_grade_view import DetailedGradeView

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedGradeView from a JSON string
detailed_grade_view_instance = DetailedGradeView.from_json(json)
# print the JSON string representation of the object
print(DetailedGradeView.to_json())

# convert the object into a dict
detailed_grade_view_dict = detailed_grade_view_instance.to_dict()
# create an instance of DetailedGradeView from a dict
detailed_grade_view_from_dict = DetailedGradeView.from_dict(detailed_grade_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


