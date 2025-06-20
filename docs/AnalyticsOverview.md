# AnalyticsOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_volume** | [**MetricChange**](MetricChange.md) |  | 
**users** | [**MetricChange**](MetricChange.md) |  | 
**topics** | [**MetricChange**](MetricChange.md) |  | 
**user_rating** | [**MetricChange**](MetricChange.md) |  | 

## Example

```python
from iblai.models.analytics_overview import AnalyticsOverview

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsOverview from a JSON string
analytics_overview_instance = AnalyticsOverview.from_json(json)
# print the JSON string representation of the object
print(AnalyticsOverview.to_json())

# convert the object into a dict
analytics_overview_dict = analytics_overview_instance.to_dict()
# create an instance of AnalyticsOverview from a dict
analytics_overview_from_dict = AnalyticsOverview.from_dict(analytics_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


