# ContentDetailsTimeSeries

Serializer describing the time series block.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | Metric represented in the time series | 
**interval** | **str** | Aggregation interval (e.g., month) | 
**data** | [**List[ContentDetailsTimeSeriesPoint]**](ContentDetailsTimeSeriesPoint.md) |  | 

## Example

```python
from iblai.models.content_details_time_series import ContentDetailsTimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsTimeSeries from a JSON string
content_details_time_series_instance = ContentDetailsTimeSeries.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsTimeSeries.to_json())

# convert the object into a dict
content_details_time_series_dict = content_details_time_series_instance.to_dict()
# create an instance of ContentDetailsTimeSeries from a dict
content_details_time_series_from_dict = ContentDetailsTimeSeries.from_dict(content_details_time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


