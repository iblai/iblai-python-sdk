# PatchedUserGroup

Serializer for UserGroups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Group display name | [optional] 
**platform** | [**RbacPlatform**](RbacPlatform.md) |  | [optional] [readonly] 
**platform_key** | **str** | The platform key | [optional] 
**description** | **str** | Group description | [optional] 
**owner** | [**RbacUser**](RbacUser.md) |  | [optional] [readonly] 
**users_to_set** | **List[int]** | List of user IDs to set in this group (replaces all existing users) | [optional] 

## Example

```python
from iblai.models.patched_user_group import PatchedUserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserGroup from a JSON string
patched_user_group_instance = PatchedUserGroup.from_json(json)
# print the JSON string representation of the object
print(PatchedUserGroup.to_json())

# convert the object into a dict
patched_user_group_dict = patched_user_group_instance.to_dict()
# create an instance of PatchedUserGroup from a dict
patched_user_group_from_dict = PatchedUserGroup.from_dict(patched_user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


