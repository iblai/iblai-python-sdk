# ContentDetailsTimeSeriesPoint

Serializer for individual time series points in content details response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | ISO8601 timestamp representing the aggregated period | 
**value** | **float** | Value for the requested metric during the period | 
**average** | **float** | Average value for the period (used for ratings) | [optional] 

## Example

```python
from iblai.models.content_details_time_series_point import ContentDetailsTimeSeriesPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsTimeSeriesPoint from a JSON string
content_details_time_series_point_instance = ContentDetailsTimeSeriesPoint.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsTimeSeriesPoint.to_json())

# convert the object into a dict
content_details_time_series_point_dict = content_details_time_series_point_instance.to_dict()
# create an instance of ContentDetailsTimeSeriesPoint from a dict
content_details_time_series_point_from_dict = ContentDetailsTimeSeriesPoint.from_dict(content_details_time_series_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


