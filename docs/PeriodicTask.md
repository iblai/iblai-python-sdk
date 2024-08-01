# PeriodicTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Short Description For This Task | [readonly] 
**crontab** | [**CrontabSchedule**](CrontabSchedule.md) |  | 
**one_off** | **bool** | If True, the schedule will only run the task a single time | [optional] 
**start_time** | **datetime** | Datetime when the schedule should begin triggering the task to run | [optional] 
**enabled** | **bool** | Set to False to disable the schedule | [optional] 

## Example

```python
from iblai.models.periodic_task import PeriodicTask

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicTask from a JSON string
periodic_task_instance = PeriodicTask.from_json(json)
# print the JSON string representation of the object
print(PeriodicTask.to_json())

# convert the object into a dict
periodic_task_dict = periodic_task_instance.to_dict()
# create an instance of PeriodicTask from a dict
periodic_task_from_dict = PeriodicTask.from_dict(periodic_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


