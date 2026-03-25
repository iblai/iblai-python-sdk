# PatchedAgentSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**instruction** | **str** | SKILL.md body — the agent runbook for this skill. | [optional] 
**metadata** | **object** | SKILL.md frontmatter (requires, primaryEnv, emoji, etc.). | [optional] 
**enabled** | **bool** |  | [optional] 
**platform_key** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_agent_skill import PatchedAgentSkill

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentSkill from a JSON string
patched_agent_skill_instance = PatchedAgentSkill.from_json(json)
# print the JSON string representation of the object
print(PatchedAgentSkill.to_json())

# convert the object into a dict
patched_agent_skill_dict = patched_agent_skill_instance.to_dict()
# create an instance of PatchedAgentSkill from a dict
patched_agent_skill_from_dict = PatchedAgentSkill.from_dict(patched_agent_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


