# AgentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | 
**identity** | **str** | Agent persona — name, creature type, visual description, vibe (→ IDENTITY.md). | [optional] 
**soul** | **str** | Behavioral guidelines — personality, communication style, values, boundaries (→ SOUL.md). | [optional] 
**user_context** | **str** | User-specific preferences and environment details — SSH hosts, device names, TTS voices (→ USER.md). | [optional] 
**tools** | **str** | Environment-specific reference notes for tool usage — device names, API aliases (→ TOOLS.md). Does not control which skills load. | [optional] 
**agents** | **str** | Multi-agent routing — agent IDs, workspaces, model assignments, channel bindings (→ AGENTS.md). | [optional] 
**bootstrap** | **str** | One-time first-run ritual — consumed and deleted by instance after use. Stored here for re-push on redeploy (→ BOOTSTRAP.md). | [optional] 
**heartbeat** | **str** | Periodic awareness checklist content. Schedule settings (interval, activeHours) go in config field (→ HEARTBEAT.md). | [optional] 
**memory** | **str** | Seed memory — long-term curated facts. Instance may modify its own copy over time (→ MEMORY.md). | [optional] 
**model** | **str** | LLM model identifier (e.g. anthropic/claude-sonnet-4-5-20250929). | [optional] 
**config** | **object** | Instance config patch sent via config.patch RPC — heartbeat schedule, session isolation, skill toggles, model fallbacks, etc. | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.agent_config import AgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentConfig from a JSON string
agent_config_instance = AgentConfig.from_json(json)
# print the JSON string representation of the object
print(AgentConfig.to_json())

# convert the object into a dict
agent_config_dict = agent_config_instance.to_dict()
# create an instance of AgentConfig from a dict
agent_config_from_dict = AgentConfig.from_dict(agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


