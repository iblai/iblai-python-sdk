# ContentSummary

Serializer for content summary data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | [**ContentTotals**](ContentTotals.md) |  | 
**averages** | [**ContentAverages**](ContentAverages.md) |  | 
**overtime** | [**List[OvertimeDataPoint]**](OvertimeDataPoint.md) | Time spent over time data (courses only, when include_overtime&#x3D;true) | [optional] 

## Example

```python
from iblai.models.content_summary import ContentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ContentSummary from a JSON string
content_summary_instance = ContentSummary.from_json(json)
# print the JSON string representation of the object
print(ContentSummary.to_json())

# convert the object into a dict
content_summary_dict = content_summary_instance.to_dict()
# create an instance of ContentSummary from a dict
content_summary_from_dict = ContentSummary.from_dict(content_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


