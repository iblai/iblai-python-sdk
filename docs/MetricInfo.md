# MetricInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**unit** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from iblai.models.metric_info import MetricInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetricInfo from a JSON string
metric_info_instance = MetricInfo.from_json(json)
# print the JSON string representation of the object
print(MetricInfo.to_json())

# convert the object into a dict
metric_info_dict = metric_info_instance.to_dict()
# create an instance of MetricInfo from a dict
metric_info_from_dict = MetricInfo.from_dict(metric_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


