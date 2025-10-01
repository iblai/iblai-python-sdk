# ProjectMentor

Serializer for mentors within a project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**unique_id** | **str** |  | [readonly] 
**slug** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.project_mentor import ProjectMentor

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMentor from a JSON string
project_mentor_instance = ProjectMentor.from_json(json)
# print the JSON string representation of the object
print(ProjectMentor.to_json())

# convert the object into a dict
project_mentor_dict = project_mentor_instance.to_dict()
# create an instance of ProjectMentor from a dict
project_mentor_from_dict = ProjectMentor.from_dict(project_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


