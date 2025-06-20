# PieChartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_users** | [**PieChartSegment**](PieChartSegment.md) |  | 
**returning_users** | [**PieChartSegment**](PieChartSegment.md) |  | 

## Example

```python
from iblai.models.pie_chart_data import PieChartData

# TODO update the JSON string below
json = "{}"
# create an instance of PieChartData from a JSON string
pie_chart_data_instance = PieChartData.from_json(json)
# print the JSON string representation of the object
print(PieChartData.to_json())

# convert the object into a dict
pie_chart_data_dict = pie_chart_data_instance.to_dict()
# create an instance of PieChartData from a dict
pie_chart_data_from_dict = PieChartData.from_dict(pie_chart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


