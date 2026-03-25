# PeriodicAgentStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_tasks** | **int** |  | 
**succeeded_tasks** | **int** |  | 
**failed_tasks** | **int** |  | 
**running_tasks** | **int** |  | 
**pending_tasks** | **int** |  | 

## Example

```python
from iblai.models.periodic_agent_statistics import PeriodicAgentStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicAgentStatistics from a JSON string
periodic_agent_statistics_instance = PeriodicAgentStatistics.from_json(json)
# print the JSON string representation of the object
print(PeriodicAgentStatistics.to_json())

# convert the object into a dict
periodic_agent_statistics_dict = periodic_agent_statistics_instance.to_dict()
# create an instance of PeriodicAgentStatistics from a dict
periodic_agent_statistics_from_dict = PeriodicAgentStatistics.from_dict(periodic_agent_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


