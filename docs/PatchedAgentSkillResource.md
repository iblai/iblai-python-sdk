# PatchedAgentSkillResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**skill** | **int** |  | [optional] 
**file_type** | [**FileTypeEnum**](FileTypeEnum.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**content** | **str** | Text content for script/reference resources. | [optional] 
**file** | **str** | Binary file for asset resources. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_agent_skill_resource import PatchedAgentSkillResource

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAgentSkillResource from a JSON string
patched_agent_skill_resource_instance = PatchedAgentSkillResource.from_json(json)
# print the JSON string representation of the object
print(PatchedAgentSkillResource.to_json())

# convert the object into a dict
patched_agent_skill_resource_dict = patched_agent_skill_resource_instance.to_dict()
# create an instance of PatchedAgentSkillResource from a dict
patched_agent_skill_resource_from_dict = PatchedAgentSkillResource.from_dict(patched_agent_skill_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


