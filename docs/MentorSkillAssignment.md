# MentorSkillAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | 
**skill** | **int** |  | 
**skill_name** | **str** |  | [readonly] 
**enabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mentor_skill_assignment import MentorSkillAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSkillAssignment from a JSON string
mentor_skill_assignment_instance = MentorSkillAssignment.from_json(json)
# print the JSON string representation of the object
print(MentorSkillAssignment.to_json())

# convert the object into a dict
mentor_skill_assignment_dict = mentor_skill_assignment_instance.to_dict()
# create an instance of MentorSkillAssignment from a dict
mentor_skill_assignment_from_dict = MentorSkillAssignment.from_dict(mentor_skill_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


