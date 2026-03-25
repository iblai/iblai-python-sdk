# SessionsChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**points** | [**List[SessionChartPoint]**](SessionChartPoint.md) |  | 

## Example

```python
from iblai.models.sessions_chart import SessionsChart

# TODO update the JSON string below
json = "{}"
# create an instance of SessionsChart from a JSON string
sessions_chart_instance = SessionsChart.from_json(json)
# print the JSON string representation of the object
print(SessionsChart.to_json())

# convert the object into a dict
sessions_chart_dict = sessions_chart_instance.to_dict()
# create an instance of SessionsChart from a dict
sessions_chart_from_dict = SessionsChart.from_dict(sessions_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


