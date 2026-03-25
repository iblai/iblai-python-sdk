# SessionChartPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**value** | **int** |  | 

## Example

```python
from iblai.models.session_chart_point import SessionChartPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SessionChartPoint from a JSON string
session_chart_point_instance = SessionChartPoint.from_json(json)
# print the JSON string representation of the object
print(SessionChartPoint.to_json())

# convert the object into a dict
session_chart_point_dict = session_chart_point_instance.to_dict()
# create an instance of SessionChartPoint from a dict
session_chart_point_from_dict = SessionChartPoint.from_dict(session_chart_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


