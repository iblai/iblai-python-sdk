# PlatformMetrics

Serializer for detailed platform metrics (platform-specific view).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollments** | [**MetricDetail**](MetricDetail.md) |  | 
**programs** | [**MetricDetail**](MetricDetail.md) |  | 
**pathways** | [**MetricDetail**](MetricDetail.md) |  | 
**resources** | [**MetricDetail**](MetricDetail.md) |  | 
**skills** | [**SkillsMetric**](SkillsMetric.md) |  | 
**credentials** | [**MetricDetail**](MetricDetail.md) |  | 
**points** | [**PointsMetric**](PointsMetric.md) |  | 

## Example

```python
from iblai.models.platform_metrics import PlatformMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformMetrics from a JSON string
platform_metrics_instance = PlatformMetrics.from_json(json)
# print the JSON string representation of the object
print(PlatformMetrics.to_json())

# convert the object into a dict
platform_metrics_dict = platform_metrics_instance.to_dict()
# create an instance of PlatformMetrics from a dict
platform_metrics_from_dict = PlatformMetrics.from_dict(platform_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


