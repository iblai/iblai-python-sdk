# RbacPolicy

Serializer for policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**role** | [**RbacBaseRole**](RbacBaseRole.md) | Role information (read-only) | [readonly] 
**platform** | [**RbacPlatform**](RbacPlatform.md) | Platform information (read-only) | [readonly] 
**resources** | **List[str]** | List of resource paths this policy grants access to (e.g., [&#39;/platforms/1/mentors&#39;, &#39;/platforms/1/mentors/settings&#39;]) | 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [readonly] 
**groups** | [**List[RbacPolicyGroup]**](RbacPolicyGroup.md) |  | [readonly] 
**role_id** | **int** | ID of the role this policy applies to | 
**platform_key** | **str** | Platform key where this policy applies | 
**users_to_add** | **List[int]** | List of user IDs to add to this Policy | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to remove from this Policy | [optional] 
**groups_to_add** | **List[int]** | List of group IDs to add to this Policy | [optional] 
**groups_to_remove** | **List[int]** | List of group IDs to remove from this Policy | [optional] 

## Example

```python
from iblai.models.rbac_policy import RbacPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of RbacPolicy from a JSON string
rbac_policy_instance = RbacPolicy.from_json(json)
# print the JSON string representation of the object
print(RbacPolicy.to_json())

# convert the object into a dict
rbac_policy_dict = rbac_policy_instance.to_dict()
# create an instance of RbacPolicy from a dict
rbac_policy_from_dict = RbacPolicy.from_dict(rbac_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


