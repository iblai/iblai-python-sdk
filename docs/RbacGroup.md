# RbacGroup

Serializer for RBAC groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**unique_id** | **str** | The unique identifier for the group | 
**platform** | [**RbacPlatform**](RbacPlatform.md) |  | [readonly] 
**platform_key** | **str** | The platform key | 
**name** | **str** | Optional name of the group | [optional] 
**description** | **str** | Optional group description | [optional] 
**users** | [**List[RbacUser]**](RbacUser.md) |  | [readonly] 
**users_to_add** | **List[int]** | List of user IDs to add to this group | [optional] 
**users_to_remove** | **List[int]** | List of user IDs to remove from this group | [optional] 

## Example

```python
from iblai.models.rbac_group import RbacGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RbacGroup from a JSON string
rbac_group_instance = RbacGroup.from_json(json)
# print the JSON string representation of the object
print(RbacGroup.to_json())

# convert the object into a dict
rbac_group_dict = rbac_group_instance.to_dict()
# create an instance of RbacGroup from a dict
rbac_group_from_dict = RbacGroup.from_dict(rbac_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


