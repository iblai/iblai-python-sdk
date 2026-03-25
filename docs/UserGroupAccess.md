# UserGroupAccess

ModelSerializer for user group access policies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | Platform key where the groups exist | 
**user_id** | **int** | ID of the user to manage group access for | 
**groups_to_add** | **List[int]** | List of group IDs to grant access to | [optional] 
**groups_to_remove** | **List[int]** | List of group IDs to revoke access from | [optional] 
**policy_id** | **int** | Policy ID | [readonly] 
**policy_name** | **str** | Policy name | [readonly] 
**groups_with_access** | [**List[UserGroupAccessInfo]**](UserGroupAccessInfo.md) | Groups with access | [readonly] 

## Example

```python
from iblai.models.user_group_access import UserGroupAccess

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupAccess from a JSON string
user_group_access_instance = UserGroupAccess.from_json(json)
# print the JSON string representation of the object
print(UserGroupAccess.to_json())

# convert the object into a dict
user_group_access_dict = user_group_access_instance.to_dict()
# create an instance of UserGroupAccess from a dict
user_group_access_from_dict = UserGroupAccess.from_dict(user_group_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


