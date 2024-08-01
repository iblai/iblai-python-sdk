# ActiveUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActiveUsersData]**](ActiveUsersData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.active_users_list import ActiveUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveUsersList from a JSON string
active_users_list_instance = ActiveUsersList.from_json(json)
# print the JSON string representation of the object
print(ActiveUsersList.to_json())

# convert the object into a dict
active_users_list_dict = active_users_list_instance.to_dict()
# create an instance of ActiveUsersList from a dict
active_users_list_from_dict = ActiveUsersList.from_dict(active_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


