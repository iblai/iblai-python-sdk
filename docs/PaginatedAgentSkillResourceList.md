# PaginatedAgentSkillResourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[AgentSkillResource]**](AgentSkillResource.md) |  | 

## Example

```python
from iblai.models.paginated_agent_skill_resource_list import PaginatedAgentSkillResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAgentSkillResourceList from a JSON string
paginated_agent_skill_resource_list_instance = PaginatedAgentSkillResourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAgentSkillResourceList.to_json())

# convert the object into a dict
paginated_agent_skill_resource_list_dict = paginated_agent_skill_resource_list_instance.to_dict()
# create an instance of PaginatedAgentSkillResourceList from a dict
paginated_agent_skill_resource_list_from_dict = PaginatedAgentSkillResourceList.from_dict(paginated_agent_skill_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


