# PointsMetric

Serializer for points metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**details** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from iblai.models.points_metric import PointsMetric

# TODO update the JSON string below
json = "{}"
# create an instance of PointsMetric from a JSON string
points_metric_instance = PointsMetric.from_json(json)
# print the JSON string representation of the object
print(PointsMetric.to_json())

# convert the object into a dict
points_metric_dict = points_metric_instance.to_dict()
# create an instance of PointsMetric from a dict
points_metric_from_dict = PointsMetric.from_dict(points_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


