# PeriodicAgentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**content** | **str** |  | [optional] 
**status** | [**PeriodicAgentLogStatusEnum**](PeriodicAgentLogStatusEnum.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**modified_at** | **datetime** |  | [readonly] 
**periodic_agent** | **int** |  | 

## Example

```python
from iblai.models.periodic_agent_log import PeriodicAgentLog

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicAgentLog from a JSON string
periodic_agent_log_instance = PeriodicAgentLog.from_json(json)
# print the JSON string representation of the object
print(PeriodicAgentLog.to_json())

# convert the object into a dict
periodic_agent_log_dict = periodic_agent_log_instance.to_dict()
# create an instance of PeriodicAgentLog from a dict
periodic_agent_log_from_dict = PeriodicAgentLog.from_dict(periodic_agent_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


