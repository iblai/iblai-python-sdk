# AgentSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**instruction** | **str** | SKILL.md body — the agent runbook for this skill. | [optional] 
**metadata** | **object** | SKILL.md frontmatter (requires, primaryEnv, emoji, etc.). | [optional] 
**enabled** | **bool** |  | [optional] 
**platform_key** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.agent_skill import AgentSkill

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkill from a JSON string
agent_skill_instance = AgentSkill.from_json(json)
# print the JSON string representation of the object
print(AgentSkill.to_json())

# convert the object into a dict
agent_skill_dict = agent_skill_instance.to_dict()
# create an instance of AgentSkill from a dict
agent_skill_from_dict = AgentSkill.from_dict(agent_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


