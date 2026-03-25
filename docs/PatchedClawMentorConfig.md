# PatchedClawMentorConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**mentor** | **str** |  | [optional] 
**server** | **int** |  | [optional] 
**server_name** | **str** |  | [optional] [readonly] 
**agent_config** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**auto_push** | **bool** | When True, saving the mentor&#39;s AgentConfig should trigger an async config push. Signal/hook not yet wired — currently a flag for future use. | [optional] 
**last_config_push** | **datetime** |  | [optional] [readonly] 
**last_config_push_status** | **str** |  | [optional] [readonly] 
**last_push_warnings** | **object** | Security warnings from last config push (baseline verification). | [optional] [readonly] 

## Example

```python
from iblai.models.patched_claw_mentor_config import PatchedClawMentorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClawMentorConfig from a JSON string
patched_claw_mentor_config_instance = PatchedClawMentorConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedClawMentorConfig.to_json())

# convert the object into a dict
patched_claw_mentor_config_dict = patched_claw_mentor_config_instance.to_dict()
# create an instance of PatchedClawMentorConfig from a dict
patched_claw_mentor_config_from_dict = PatchedClawMentorConfig.from_dict(patched_claw_mentor_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


