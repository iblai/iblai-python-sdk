# PerlearnerGradeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PerlearnerGradeSummaryData]**](PerlearnerGradeSummaryData.md) |  | [optional] 

## Example

```python
from iblai.models.perlearner_grade_summary import PerlearnerGradeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerGradeSummary from a JSON string
perlearner_grade_summary_instance = PerlearnerGradeSummary.from_json(json)
# print the JSON string representation of the object
print(PerlearnerGradeSummary.to_json())

# convert the object into a dict
perlearner_grade_summary_dict = perlearner_grade_summary_instance.to_dict()
# create an instance of PerlearnerGradeSummary from a dict
perlearner_grade_summary_from_dict = PerlearnerGradeSummary.from_dict(perlearner_grade_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


