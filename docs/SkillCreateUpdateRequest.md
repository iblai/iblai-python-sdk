# SkillCreateUpdateRequest

Serializer for skill creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Skill ID (for updates) | [optional] 
**name** | **str** | Skill name | 
**slug** | **str** | Skill slug | [optional] 
**platform_key** | **str** | Platform key | [optional] 
**data** | **object** | Additional skill data | [optional] 

## Example

```python
from iblai.models.skill_create_update_request import SkillCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SkillCreateUpdateRequest from a JSON string
skill_create_update_request_instance = SkillCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SkillCreateUpdateRequest.to_json())

# convert the object into a dict
skill_create_update_request_dict = skill_create_update_request_instance.to_dict()
# create an instance of SkillCreateUpdateRequest from a dict
skill_create_update_request_from_dict = SkillCreateUpdateRequest.from_dict(skill_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


