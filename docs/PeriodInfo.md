# PeriodInfo

Information about the analysis period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Start date of analysis period | [optional] 
**end_date** | **str** | End date of analysis period | [optional] 
**period_days** | **int** | Number of days in period | [optional] 
**range_type** | **str** | Type of date range (custom, default, all_time, etc.) | [optional] 

## Example

```python
from iblai.models.period_info import PeriodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodInfo from a JSON string
period_info_instance = PeriodInfo.from_json(json)
# print the JSON string representation of the object
print(PeriodInfo.to_json())

# convert the object into a dict
period_info_dict = period_info_instance.to_dict()
# create an instance of PeriodInfo from a dict
period_info_from_dict = PeriodInfo.from_dict(period_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


