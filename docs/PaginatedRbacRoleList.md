# PaginatedRbacRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RbacRole]**](RbacRole.md) |  | 

## Example

```python
from iblai.models.paginated_rbac_role_list import PaginatedRbacRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRbacRoleList from a JSON string
paginated_rbac_role_list_instance = PaginatedRbacRoleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRbacRoleList.to_json())

# convert the object into a dict
paginated_rbac_role_list_dict = paginated_rbac_role_list_instance.to_dict()
# create an instance of PaginatedRbacRoleList from a dict
paginated_rbac_role_list_from_dict = PaginatedRbacRoleList.from_dict(paginated_rbac_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


