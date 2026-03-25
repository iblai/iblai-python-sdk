# PaginatedAgentSkillList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AgentSkill]**](AgentSkill.md) |  | 

## Example

```python
from iblai.models.paginated_agent_skill_list import PaginatedAgentSkillList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentSkillList from a JSON string
paginated_agent_skill_list_instance = PaginatedAgentSkillList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAgentSkillList.to_json())

# convert the object into a dict
paginated_agent_skill_list_dict = paginated_agent_skill_list_instance.to_dict()
# create an instance of PaginatedAgentSkillList from a dict
paginated_agent_skill_list_from_dict = PaginatedAgentSkillList.from_dict(paginated_agent_skill_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


