# SkillsMetric

Serializer for skills metrics with breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reported** | **int** |  | 
**desired** | **int** |  | 
**assigned** | **int** |  | 
**total** | **int** |  | 
**details** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from iblai.models.skills_metric import SkillsMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SkillsMetric from a JSON string
skills_metric_instance = SkillsMetric.from_json(json)
# print the JSON string representation of the object
print(SkillsMetric.to_json())

# convert the object into a dict
skills_metric_dict = skills_metric_instance.to_dict()
# create an instance of SkillsMetric from a dict
skills_metric_from_dict = SkillsMetric.from_dict(skills_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


