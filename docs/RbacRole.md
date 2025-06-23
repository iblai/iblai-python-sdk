# RbacRole

Serializer for roles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**platform** | [**RbacPlatform**](RbacPlatform.md) | Platform information (read-only) | [readonly] 
**platform_key** | **str** | Platform key where this role belongs | 
**actions** | **List[str]** | List of actions/permissions this role can perform (e.g., [&#39;Ibl.Mentor/Settings/read&#39;, &#39;Ibl.Mentor/Settings/write&#39;]) | 

## Example

```python
from iblai.models.rbac_role import RbacRole

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRole from a JSON string
rbac_role_instance = RbacRole.from_json(json)
# print the JSON string representation of the object
print(RbacRole.to_json())

# convert the object into a dict
rbac_role_dict = rbac_role_instance.to_dict()
# create an instance of RbacRole from a dict
rbac_role_from_dict = RbacRole.from_dict(rbac_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


