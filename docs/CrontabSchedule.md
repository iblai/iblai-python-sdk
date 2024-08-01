# CrontabSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | **str** | Cron Minutes to Run. Use \&quot;*\&quot; for \&quot;all\&quot;. (Example: \&quot;0,30\&quot;) | [optional] 
**hour** | **str** | Cron Hours to Run. Use \&quot;*\&quot; for \&quot;all\&quot;. (Example: \&quot;8,20\&quot;) | [optional] 
**day_of_week** | **str** | Cron Days Of The Week to Run. Use \&quot;*\&quot; for \&quot;all\&quot;, Sunday is 0 or 7, Monday is 1. (Example: \&quot;0,5\&quot;) | [optional] 
**day_of_month** | **str** | Cron Days Of The Month to Run. Use \&quot;*\&quot; for \&quot;all\&quot;. (Example: \&quot;1,15\&quot;) | [optional] 
**month_of_year** | **str** | Cron Months (1-12) Of The Year to Run. Use \&quot;*\&quot; for \&quot;all\&quot;. (Example: \&quot;1,12\&quot;) | [optional] 

## Example

```python
from iblai.models.crontab_schedule import CrontabSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CrontabSchedule from a JSON string
crontab_schedule_instance = CrontabSchedule.from_json(json)
# print the JSON string representation of the object
print(CrontabSchedule.to_json())

# convert the object into a dict
crontab_schedule_dict = crontab_schedule_instance.to_dict()
# create an instance of CrontabSchedule from a dict
crontab_schedule_from_dict = CrontabSchedule.from_dict(crontab_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


