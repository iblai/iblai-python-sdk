# PaginatedUserEdxMemoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserEdxMemory]**](UserEdxMemory.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_user_edx_memory_list import PaginatedUserEdxMemoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserEdxMemoryList from a JSON string
paginated_user_edx_memory_list_instance = PaginatedUserEdxMemoryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserEdxMemoryList.to_json())

# convert the object into a dict
paginated_user_edx_memory_list_dict = paginated_user_edx_memory_list_instance.to_dict()
# create an instance of PaginatedUserEdxMemoryList from a dict
paginated_user_edx_memory_list_from_dict = PaginatedUserEdxMemoryList.from_dict(paginated_user_edx_memory_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


