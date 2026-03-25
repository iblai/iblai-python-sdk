# MentorPolicy

Serializer for mentor-specific RBAC policies using ModelSerializer pattern. Accepts mentor_id and role, generates resources and role internally.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Policy name. If not supplied, defaults to a UUID4 | [readonly] 
**platform_key** | **str** | Platform key where the mentor belongs | 
**mentor_id** | **int** | ID of the mentor to manage access for | 
**role** | **str** | Role for accessing this mentor (viewer or editor) | 
**resources** | **object** | List of resources this policy applies to | [readonly] 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [readonly] 
**groups** | [**List[RbacPolicyGroup]**](RbacPolicyGroup.md) |  | [readonly] 
**groups_to_add** | **List[int]** | List of group IDs to grant access to this mentor | [optional] 
**groups_to_remove** | **List[int]** | List of group IDs to revoke access from this mentor | [optional] 
**users_to_add** | **List[int]** | List of user IDs to grant access to this mentor | [optional] 
**usernames_to_add** | **List[str]** | List of usernames to grant access to this mentor | [optional] 
**emails_to_add** | **List[str]** | List of user emails to grant access to this mentor | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to revoke access from this mentor | [optional] 

## Example

```python
from iblai.models.mentor_policy import MentorPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of MentorPolicy from a JSON string
mentor_policy_instance = MentorPolicy.from_json(json)
# print the JSON string representation of the object
print(MentorPolicy.to_json())

# convert the object into a dict
mentor_policy_dict = mentor_policy_instance.to_dict()
# create an instance of MentorPolicy from a dict
mentor_policy_from_dict = MentorPolicy.from_dict(mentor_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


