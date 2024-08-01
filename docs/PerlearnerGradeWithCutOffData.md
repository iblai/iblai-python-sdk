# PerlearnerGradeWithCutOffData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_cutoffs** | **Dict[str, object]** | Dictionary showing grade cutoffs | 
**grade** | **float** | Grade | 

## Example

```python
from iblai.models.perlearner_grade_with_cut_off_data import PerlearnerGradeWithCutOffData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerGradeWithCutOffData from a JSON string
perlearner_grade_with_cut_off_data_instance = PerlearnerGradeWithCutOffData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerGradeWithCutOffData.to_json())

# convert the object into a dict
perlearner_grade_with_cut_off_data_dict = perlearner_grade_with_cut_off_data_instance.to_dict()
# create an instance of PerlearnerGradeWithCutOffData from a dict
perlearner_grade_with_cut_off_data_from_dict = PerlearnerGradeWithCutOffData.from_dict(perlearner_grade_with_cut_off_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


