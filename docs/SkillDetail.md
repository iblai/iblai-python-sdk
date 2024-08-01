# SkillDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name | [optional] 
**courses** | [**List[CourseSkill]**](CourseSkill.md) |  | 
**related_skills** | **int** |  | [readonly] 

## Example

```python
from iblai.models.skill_detail import SkillDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SkillDetail from a JSON string
skill_detail_instance = SkillDetail.from_json(json)
# print the JSON string representation of the object
print(SkillDetail.to_json())

# convert the object into a dict
skill_detail_dict = skill_detail_instance.to_dict()
# create an instance of SkillDetail from a dict
skill_detail_from_dict = SkillDetail.from_dict(skill_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


