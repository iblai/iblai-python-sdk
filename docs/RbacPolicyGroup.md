# RbacPolicyGroup

Serializer for RBAC groups when returned in a policy.  We are limiting the returne data since we don't need everything there

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Optional name of the group | [optional] 
**unique_id** | **str** | The unique identifier for the group | 
**description** | **str** | Optional group description | [optional] 

## Example

```python
from iblai.models.rbac_policy_group import RbacPolicyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RbacPolicyGroup from a JSON string
rbac_policy_group_instance = RbacPolicyGroup.from_json(json)
# print the JSON string representation of the object
print(RbacPolicyGroup.to_json())

# convert the object into a dict
rbac_policy_group_dict = rbac_policy_group_instance.to_dict()
# create an instance of RbacPolicyGroup from a dict
rbac_policy_group_from_dict = RbacPolicyGroup.from_dict(rbac_policy_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


