# SkillInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Display name | [optional] 
**course_count** | **int** | Number of courses with skill | [readonly] 
**user_count** | **int** | Number of users with skill | [readonly] 
**total_points** | **int** | Total points for skill | [readonly] 
**average_points** | **float** | Average points for skill | [readonly] 

## Example

```python
from iblai.models.skill_info import SkillInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SkillInfo from a JSON string
skill_info_instance = SkillInfo.from_json(json)
# print the JSON string representation of the object
print(SkillInfo.to_json())

# convert the object into a dict
skill_info_dict = skill_info_instance.to_dict()
# create an instance of SkillInfo from a dict
skill_info_from_dict = SkillInfo.from_dict(skill_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


