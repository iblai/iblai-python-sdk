# PatchedProject

Unified serializer for Project model.  Write-only fields: - mentors_to_add: List of mentor unique IDs to add to the project - mentors_to_remove: List of mentor unique IDs to remove from the project  These fields are mutually exclusive and only used during create/update operations. For create: only mentors_to_add is used For update: either can be used, but not both at once

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Name of the project | [optional] 
**description** | **str** | Description of the project | [optional] 
**shared** | **bool** | Whether this project is shared with others or personal | [optional] 
**owner** | **int** | User who created this project | [optional] [readonly] 
**owner_username** | **str** |  | [optional] [readonly] 
**platform** | **int** | Platform this project belongs to | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**platform_name** | **str** |  | [optional] [readonly] 
**mentor_count** | **int** |  | [optional] [readonly] 
**is_personal** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**mentors** | [**List[ProjectMentor]**](ProjectMentor.md) |  | [optional] [readonly] 
**mentors_to_add** | **List[str]** | List of mentor unique IDs to add to the project | [optional] 
**mentors_to_remove** | **List[str]** | List of mentor unique IDs to remove from the project | [optional] 

## Example

```python
from iblai.models.patched_project import PatchedProject

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProject from a JSON string
patched_project_instance = PatchedProject.from_json(json)
# print the JSON string representation of the object
print(PatchedProject.to_json())

# convert the object into a dict
patched_project_dict = patched_project_instance.to_dict()
# create an instance of PatchedProject from a dict
patched_project_from_dict = PatchedProject.from_dict(patched_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


