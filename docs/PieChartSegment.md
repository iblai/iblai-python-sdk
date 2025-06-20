# PieChartSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**percentage** | **float** |  | 

## Example

```python
from iblai.models.pie_chart_segment import PieChartSegment

# TODO update the JSON string below
json = "{}"
# create an instance of PieChartSegment from a JSON string
pie_chart_segment_instance = PieChartSegment.from_json(json)
# print the JSON string representation of the object
print(PieChartSegment.to_json())

# convert the object into a dict
pie_chart_segment_dict = pie_chart_segment_instance.to_dict()
# create an instance of PieChartSegment from a dict
pie_chart_segment_from_dict = PieChartSegment.from_dict(pie_chart_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


