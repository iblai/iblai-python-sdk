# AgentSkillResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**skill** | **int** |  | 
**file_type** | [**FileTypeEnum**](FileTypeEnum.md) |  | 
**filename** | **str** |  | 
**content** | **str** | Text content for script/reference resources. | [optional] 
**file** | **str** | Binary file for asset resources. | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.agent_skill_resource import AgentSkillResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkillResource from a JSON string
agent_skill_resource_instance = AgentSkillResource.from_json(json)
# print the JSON string representation of the object
print(AgentSkillResource.to_json())

# convert the object into a dict
agent_skill_resource_dict = agent_skill_resource_instance.to_dict()
# create an instance of AgentSkillResource from a dict
agent_skill_resource_from_dict = AgentSkillResource.from_dict(agent_skill_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


