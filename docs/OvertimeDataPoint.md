# OvertimeDataPoint

Serializer for individual overtime data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**value** | **int** | Time spent in seconds for this date | 

## Example

```python
from iblai.models.overtime_data_point import OvertimeDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of OvertimeDataPoint from a JSON string
overtime_data_point_instance = OvertimeDataPoint.from_json(json)
# print the JSON string representation of the object
print(OvertimeDataPoint.to_json())

# convert the object into a dict
overtime_data_point_dict = overtime_data_point_instance.to_dict()
# create an instance of OvertimeDataPoint from a dict
overtime_data_point_from_dict = OvertimeDataPoint.from_dict(overtime_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


