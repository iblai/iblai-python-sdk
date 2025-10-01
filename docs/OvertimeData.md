# OvertimeData

Individual overtime data point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**value** | **float** | Cost value for this time period | 

## Example

```python
from iblai.models.overtime_data import OvertimeData

# TODO update the JSON string below
json = "{}"
# create an instance of OvertimeData from a JSON string
overtime_data_instance = OvertimeData.from_json(json)
# print the JSON string representation of the object
print(OvertimeData.to_json())

# convert the object into a dict
overtime_data_dict = overtime_data_instance.to_dict()
# create an instance of OvertimeData from a dict
overtime_data_from_dict = OvertimeData.from_dict(overtime_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


