# UserGroupPolicy

Serializer for usergroup-specific RBAC policies using ModelSerializer pattern. Accepts usergroup_id and role, generates resources and role internally.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Policy name. If not supplied, defaults to a UUID4 | [readonly] 
**platform_key** | **str** | Platform key where the usergroup belongs | 
**usergroup_id** | **int** | ID of the usergroup to manage access for | 
**role** | **str** | Role for accessing this usergroup (read, edit, view analytics, send notifications) | 
**resources** | **object** | List of resources this policy applies to | [readonly] 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [readonly] 
**groups** | [**List[RbacPolicyGroup]**](RbacPolicyGroup.md) |  | [readonly] 
**groups_to_add** | **List[int]** | List of RbacGroup IDs to grant access to this usergroup | [optional] 
**groups_to_remove** | **List[int]** | List of RbacGroup IDs to revoke access from this usergroup | [optional] 
**users_to_add** | **List[int]** | List of user IDs to grant access to this usergroup | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to revoke access from this usergroup | [optional] 

## Example

```python
from iblai.models.user_group_policy import UserGroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupPolicy from a JSON string
user_group_policy_instance = UserGroupPolicy.from_json(json)
# print the JSON string representation of the object
print(UserGroupPolicy.to_json())

# convert the object into a dict
user_group_policy_dict = user_group_policy_instance.to_dict()
# create an instance of UserGroupPolicy from a dict
user_group_policy_from_dict = UserGroupPolicy.from_dict(user_group_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


