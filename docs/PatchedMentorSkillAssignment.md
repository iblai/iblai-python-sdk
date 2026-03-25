# PatchedMentorSkillAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**mentor** | **str** |  | [optional] 
**skill** | **int** |  | [optional] 
**skill_name** | **str** |  | [optional] [readonly] 
**enabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mentor_skill_assignment import PatchedMentorSkillAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentorSkillAssignment from a JSON string
patched_mentor_skill_assignment_instance = PatchedMentorSkillAssignment.from_json(json)
# print the JSON string representation of the object
print(PatchedMentorSkillAssignment.to_json())

# convert the object into a dict
patched_mentor_skill_assignment_dict = patched_mentor_skill_assignment_instance.to_dict()
# create an instance of PatchedMentorSkillAssignment from a dict
patched_mentor_skill_assignment_from_dict = PatchedMentorSkillAssignment.from_dict(patched_mentor_skill_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


