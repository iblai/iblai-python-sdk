# MetricChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**change** | **float** |  | 

## Example

```python
from iblai.models.metric_change import MetricChange

# TODO update the JSON string below
json = "{}"
# create an instance of MetricChange from a JSON string
metric_change_instance = MetricChange.from_json(json)
# print the JSON string representation of the object
print(MetricChange.to_json())

# convert the object into a dict
metric_change_dict = metric_change_instance.to_dict()
# create an instance of MetricChange from a dict
metric_change_from_dict = MetricChange.from_dict(metric_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


