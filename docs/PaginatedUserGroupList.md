# PaginatedUserGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserGroup]**](UserGroup.md) |  | 

## Example

```python
from iblai.models.paginated_user_group_list import PaginatedUserGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserGroupList from a JSON string
paginated_user_group_list_instance = PaginatedUserGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserGroupList.to_json())

# convert the object into a dict
paginated_user_group_list_dict = paginated_user_group_list_instance.to_dict()
# create an instance of PaginatedUserGroupList from a dict
paginated_user_group_list_from_dict = PaginatedUserGroupList.from_dict(paginated_user_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


