# PatchedRbacGroup

Serializer for RBAC groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**unique_id** | **str** | The unique identifier for the group | [optional] 
**platform** | [**RbacPlatform**](RbacPlatform.md) |  | [optional] [readonly] 
**platform_key** | **str** | The platform key | [optional] 
**name** | **str** | Optional name of the group | [optional] 
**description** | **str** | Optional group description | [optional] 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [optional] [readonly] 
**users_to_add** | **List[int]** | List of user IDs to add to this group | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to remove from this group | [optional] 

## Example

```python
from iblai.models.patched_rbac_group import PatchedRbacGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRbacGroup from a JSON string
patched_rbac_group_instance = PatchedRbacGroup.from_json(json)
# print the JSON string representation of the object
print(PatchedRbacGroup.to_json())

# convert the object into a dict
patched_rbac_group_dict = patched_rbac_group_instance.to_dict()
# create an instance of PatchedRbacGroup from a dict
patched_rbac_group_from_dict = PatchedRbacGroup.from_dict(patched_rbac_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


