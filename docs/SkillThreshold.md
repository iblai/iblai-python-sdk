# SkillThreshold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the threshold e.g Beginner. | 
**threshold** | **int** | The threshold for the skill. | 
**platform** | **str** | The platform key | 

## Example

```python
from iblai.models.skill_threshold import SkillThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of SkillThreshold from a JSON string
skill_threshold_instance = SkillThreshold.from_json(json)
# print the JSON string representation of the object
print(SkillThreshold.to_json())

# convert the object into a dict
skill_threshold_dict = skill_threshold_instance.to_dict()
# create an instance of SkillThreshold from a dict
skill_threshold_from_dict = SkillThreshold.from_dict(skill_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


