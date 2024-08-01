# PatchedSkillThreshold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the threshold e.g Beginner. | [optional] 
**threshold** | **int** | The threshold for the skill. | [optional] 
**platform** | **str** | The platform key | [optional] 

## Example

```python
from iblai.models.patched_skill_threshold import PatchedSkillThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSkillThreshold from a JSON string
patched_skill_threshold_instance = PatchedSkillThreshold.from_json(json)
# print the JSON string representation of the object
print(PatchedSkillThreshold.to_json())

# convert the object into a dict
patched_skill_threshold_dict = patched_skill_threshold_instance.to_dict()
# create an instance of PatchedSkillThreshold from a dict
patched_skill_threshold_from_dict = PatchedSkillThreshold.from_dict(patched_skill_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


