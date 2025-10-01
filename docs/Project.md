# Project

Unified serializer for Project model.  Write-only fields: - mentors_to_add: List of mentor unique IDs to add to the project - mentors_to_remove: List of mentor unique IDs to remove from the project  These fields are mutually exclusive and only used during create/update operations. For create: only mentors_to_add is used For update: either can be used, but not both at once

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the project | 
**description** | **str** | Description of the project | [optional] 
**shared** | **bool** | Whether this project is shared with others or personal | [optional] 
**owner** | **int** | User who created this project | [readonly] 
**owner_username** | **str** |  | [readonly] 
**platform** | **int** | Platform this project belongs to | [readonly] 
**platform_key** | **str** |  | [readonly] 
**platform_name** | **str** |  | [readonly] 
**mentor_count** | **int** |  | [readonly] 
**is_personal** | **bool** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**mentors** | [**List[ProjectMentor]**](ProjectMentor.md) |  | [readonly] 
**mentors_to_add** | **List[str]** | List of mentor unique IDs to add to the project | [optional] 
**mentors_to_remove** | **List[str]** | List of mentor unique IDs to remove from the project | [optional] 

## Example

```python
from iblai.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


