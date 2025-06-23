# PaginatedUserAppList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserApp]**](UserApp.md) |  | 

## Example

```python
from iblai.models.paginated_user_app_list import PaginatedUserAppList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserAppList from a JSON string
paginated_user_app_list_instance = PaginatedUserAppList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserAppList.to_json())

# convert the object into a dict
paginated_user_app_list_dict = paginated_user_app_list_instance.to_dict()
# create an instance of PaginatedUserAppList from a dict
paginated_user_app_list_from_dict = PaginatedUserAppList.from_dict(paginated_user_app_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


