# OvertimeMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total records | 
**change_range** | **int** | Change in range | [optional] [default to 0]
**change_last_seven_days** | **int** | Change in last 7 days | [optional] [default to 0]
**change_last_thirty_days** | **int** | Change in last 30 days | [optional] [default to 0]
**change_last_seven_days_percent** | **float** | Change in last 7 days in percentage | [optional] [default to 0.0]
**change_last_thirty_days_percent** | **float** | Change in last 30 days in percentage | [optional] [default to 0.0]
**change_range_percent** | **float** | Change in range in percentage | [optional] 

## Example

```python
from iblai.models.overtime_meta import OvertimeMeta

# TODO update the JSON string below
json = "{}"
# create an instance of OvertimeMeta from a JSON string
overtime_meta_instance = OvertimeMeta.from_json(json)
# print the JSON string representation of the object
print(OvertimeMeta.to_json())

# convert the object into a dict
overtime_meta_dict = overtime_meta_instance.to_dict()
# create an instance of OvertimeMeta from a dict
overtime_meta_from_dict = OvertimeMeta.from_dict(overtime_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


