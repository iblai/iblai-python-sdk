# MetricDetail

Base serializer for detailed metric data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**details** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from iblai.models.metric_detail import MetricDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDetail from a JSON string
metric_detail_instance = MetricDetail.from_json(json)
# print the JSON string representation of the object
print(MetricDetail.to_json())

# convert the object into a dict
metric_detail_dict = metric_detail_instance.to_dict()
# create an instance of MetricDetail from a dict
metric_detail_from_dict = MetricDetail.from_dict(metric_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


