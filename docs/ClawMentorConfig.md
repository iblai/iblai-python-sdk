# ClawMentorConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | 
**server** | **int** |  | 
**server_name** | **str** |  | [readonly] 
**agent_config** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**auto_push** | **bool** | When True, saving the mentor&#39;s AgentConfig should trigger an async config push. Signal/hook not yet wired — currently a flag for future use. | [optional] 
**last_config_push** | **datetime** |  | [readonly] 
**last_config_push_status** | **str** |  | [readonly] 
**last_push_warnings** | **object** | Security warnings from last config push (baseline verification). | [readonly] 

## Example

```python
from iblai.models.claw_mentor_config import ClawMentorConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClawMentorConfig from a JSON string
claw_mentor_config_instance = ClawMentorConfig.from_json(json)
# print the JSON string representation of the object
print(ClawMentorConfig.to_json())

# convert the object into a dict
claw_mentor_config_dict = claw_mentor_config_instance.to_dict()
# create an instance of ClawMentorConfig from a dict
claw_mentor_config_from_dict = ClawMentorConfig.from_dict(claw_mentor_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


