# SkillsDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired** | [**List[Skill]**](Skill.md) |  | 
**reported** | [**List[Skill]**](Skill.md) |  | 

## Example

```python
from iblai.models.skills_detail import SkillsDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SkillsDetail from a JSON string
skills_detail_instance = SkillsDetail.from_json(json)
# print the JSON string representation of the object
print(SkillsDetail.to_json())

# convert the object into a dict
skills_detail_dict = skills_detail_instance.to_dict()
# create an instance of SkillsDetail from a dict
skills_detail_from_dict = SkillsDetail.from_dict(skills_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


