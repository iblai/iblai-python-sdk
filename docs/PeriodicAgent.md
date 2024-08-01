# PeriodicAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | [**Mentor**](Mentor.md) |  | 
**title** | **str** |  | 
**username** | **str** |  | [readonly] 
**description** | **str** |  | [optional] 
**prompt** | **str** | Prompt for the periodic agent if any. | [optional] 
**task** | [**PeriodicTask**](PeriodicTask.md) |  | 
**created_at** | **datetime** |  | [readonly] 
**modified_at** | **datetime** |  | [readonly] 
**enabled** | **bool** |  | [readonly] 
**one_off** | **str** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**pathway** | **str** |  | [optional] 
**parent_session_id** | **str** |  | [optional] 
**parent_mentor_id** | **int** |  | [optional] 
**previous_agent** | **int** | Agent that needs to run before the current agent runs. | [optional] 
**previous_agent_status** | [**PreviousAgentStatusEnum**](PreviousAgentStatusEnum.md) | The status that the previous agent must be in before this agent gets scheduled.  * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
**previous_agent_output** | **str** | This will be fed into the run of this agent as part of its input prompt. | [readonly] 

## Example

```python
from iblai.models.periodic_agent import PeriodicAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicAgent from a JSON string
periodic_agent_instance = PeriodicAgent.from_json(json)
# print the JSON string representation of the object
print(PeriodicAgent.to_json())

# convert the object into a dict
periodic_agent_dict = periodic_agent_instance.to_dict()
# create an instance of PeriodicAgent from a dict
periodic_agent_from_dict = PeriodicAgent.from_dict(periodic_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


