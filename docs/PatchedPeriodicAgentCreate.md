# PatchedPeriodicAgentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**mentor** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**username** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**prompt** | **str** | Prompt for the periodic agent if any. | [optional] 
**task** | [**PeriodicTask**](PeriodicTask.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**modified_at** | **datetime** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] [readonly] 
**one_off** | **str** |  | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**pathway** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 
**callback_secret** | **str** |  | [optional] 
**parent_session_id** | **str** |  | [optional] 
**parent_mentor_id** | **int** |  | [optional] 
**previous_agent** | **int** | Agent that needs to run before the current agent runs. | [optional] 
**previous_agent_status** | [**PreviousAgentStatusEnum**](PreviousAgentStatusEnum.md) | The status that the previous agent must be in before this agent gets scheduled.  * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
**previous_agent_output** | **str** | This will be fed into the run of this agent as part of its input prompt. | [optional] [readonly] 

## Example

```python
from iblai.models.patched_periodic_agent_create import PatchedPeriodicAgentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPeriodicAgentCreate from a JSON string
patched_periodic_agent_create_instance = PatchedPeriodicAgentCreate.from_json(json)
# print the JSON string representation of the object
print(PatchedPeriodicAgentCreate.to_json())

# convert the object into a dict
patched_periodic_agent_create_dict = patched_periodic_agent_create_instance.to_dict()
# create an instance of PatchedPeriodicAgentCreate from a dict
patched_periodic_agent_create_from_dict = PatchedPeriodicAgentCreate.from_dict(patched_periodic_agent_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


