# PaginatedRbacGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RbacGroup]**](RbacGroup.md) |  | 

## Example

```python
from iblai.models.paginated_rbac_group_list import PaginatedRbacGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRbacGroupList from a JSON string
paginated_rbac_group_list_instance = PaginatedRbacGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRbacGroupList.to_json())

# convert the object into a dict
paginated_rbac_group_list_dict = paginated_rbac_group_list_instance.to_dict()
# create an instance of PaginatedRbacGroupList from a dict
paginated_rbac_group_list_from_dict = PaginatedRbacGroupList.from_dict(paginated_rbac_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


