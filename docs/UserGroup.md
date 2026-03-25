# UserGroup

Serializer for UserGroups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Group display name | 
**platform** | [**RbacPlatform**](RbacPlatform.md) |  | [readonly] 
**platform_key** | **str** | The platform key | 
**description** | **str** | Group description | [optional] 
**owner** | [**RbacUser**](RbacUser.md) |  | [readonly] 
**users_to_set** | **List[int]** | List of user IDs to set in this group (replaces all existing users) | [optional] 

## Example

```python
from iblai.models.user_group import UserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroup from a JSON string
user_group_instance = UserGroup.from_json(json)
# print the JSON string representation of the object
print(UserGroup.to_json())

# convert the object into a dict
user_group_dict = user_group_instance.to_dict()
# create an instance of UserGroup from a dict
user_group_from_dict = UserGroup.from_dict(user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


