# PatchedSkill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 

## Example

```python
from iblai.models.patched_skill import PatchedSkill

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSkill from a JSON string
patched_skill_instance = PatchedSkill.from_json(json)
# print the JSON string representation of the object
print(PatchedSkill.to_json())

# convert the object into a dict
patched_skill_dict = patched_skill_instance.to_dict()
# create an instance of PatchedSkill from a dict
patched_skill_from_dict = PatchedSkill.from_dict(patched_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


