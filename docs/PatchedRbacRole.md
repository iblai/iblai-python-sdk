# PatchedRbacRole

Serializer for roles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**platform** | [**RbacPlatform**](RbacPlatform.md) | Platform information (read-only) | [optional] [readonly] 
**platform_key** | **str** | Platform key where this role belongs | [optional] 
**actions** | **List[str]** | List of actions/permissions this role can perform (e.g., [&#39;Ibl.Mentor/Settings/read&#39;, &#39;Ibl.Mentor/Settings/write&#39;]) | [optional] 

## Example

```python
from iblai.models.patched_rbac_role import PatchedRbacRole

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRbacRole from a JSON string
patched_rbac_role_instance = PatchedRbacRole.from_json(json)
# print the JSON string representation of the object
print(PatchedRbacRole.to_json())

# convert the object into a dict
patched_rbac_role_dict = patched_rbac_role_instance.to_dict()
# create an instance of PatchedRbacRole from a dict
patched_rbac_role_from_dict = PatchedRbacRole.from_dict(patched_rbac_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


