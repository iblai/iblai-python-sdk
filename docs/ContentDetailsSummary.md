# ContentDetailsSummary

Serializer for summary data in the content details endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | **Dict[str, float]** | Total counts related to the content item | 
**averages** | **Dict[str, Optional[float]]** | Average values related to the content item | 
**time_series** | [**ContentDetailsTimeSeries**](ContentDetailsTimeSeries.md) | Optional time series data for the requested metric | [optional] 

## Example

```python
from iblai.models.content_details_summary import ContentDetailsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsSummary from a JSON string
content_details_summary_instance = ContentDetailsSummary.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsSummary.to_json())

# convert the object into a dict
content_details_summary_dict = content_details_summary_instance.to_dict()
# create an instance of ContentDetailsSummary from a dict
content_details_summary_from_dict = ContentDetailsSummary.from_dict(content_details_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


