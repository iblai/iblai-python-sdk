# PaginatedUserMemoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserMemory]**](UserMemory.md) |  | 

## Example

```python
from iblai.models.paginated_user_memory_list import PaginatedUserMemoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserMemoryList from a JSON string
paginated_user_memory_list_instance = PaginatedUserMemoryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserMemoryList.to_json())

# convert the object into a dict
paginated_user_memory_list_dict = paginated_user_memory_list_instance.to_dict()
# create an instance of PaginatedUserMemoryList from a dict
paginated_user_memory_list_from_dict = PaginatedUserMemoryList.from_dict(paginated_user_memory_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


