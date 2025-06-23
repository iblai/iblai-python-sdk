# PatchedRbacPolicy

Serializer for policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**role** | [**RbacBaseRole**](RbacBaseRole.md) | Role information (read-only) | [optional] [readonly] 
**platform** | [**RbacPlatform**](RbacPlatform.md) | Platform information (read-only) | [optional] [readonly] 
**resources** | **List[str]** | List of resource paths this policy grants access to (e.g., [&#39;/platforms/1/mentors&#39;, &#39;/platforms/1/mentors/settings&#39;]) | [optional] 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [optional] [readonly] 
**groups** | [**List[RbacPolicyGroup]**](RbacPolicyGroup.md) |  | [optional] [readonly] 
**role_id** | **int** | ID of the role this policy applies to | [optional] 
**platform_key** | **str** | Platform key where this policy applies | [optional] 
**users_to_add** | **List[int]** | List of user IDs to add to this Policy | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to remove from this Policy | [optional] 
**groups_to_add** | **List[int]** | List of group IDs to add to this Policy | [optional] 
**groups_to_remove** | **List[int]** | List of group IDs to remove from this Policy | [optional] 

## Example

```python
from iblai.models.patched_rbac_policy import PatchedRbacPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRbacPolicy from a JSON string
patched_rbac_policy_instance = PatchedRbacPolicy.from_json(json)
# print the JSON string representation of the object
print(PatchedRbacPolicy.to_json())

# convert the object into a dict
patched_rbac_policy_dict = patched_rbac_policy_instance.to_dict()
# create an instance of PatchedRbacPolicy from a dict
patched_rbac_policy_from_dict = PatchedRbacPolicy.from_dict(patched_rbac_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


