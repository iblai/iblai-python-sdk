# PerlearnerGradeSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **str** | Assignment Type name | 
**weight** | **float** | Assignment weight | 
**weighted_grade** | **float** | Assignment grade | 
**average_section_grade** | **float** | Assignment section grade average in course | 

## Example

```python
from iblai.models.perlearner_grade_summary_data import PerlearnerGradeSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerGradeSummaryData from a JSON string
perlearner_grade_summary_data_instance = PerlearnerGradeSummaryData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerGradeSummaryData.to_json())

# convert the object into a dict
perlearner_grade_summary_data_dict = perlearner_grade_summary_data_instance.to_dict()
# create an instance of PerlearnerGradeSummaryData from a dict
perlearner_grade_summary_data_from_dict = PerlearnerGradeSummaryData.from_dict(perlearner_grade_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


