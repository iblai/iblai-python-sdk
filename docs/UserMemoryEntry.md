# UserMemoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [optional] 
**key** | **str** |  | 
**value** | **str** |  | [optional] 
**inserted_at** | **str** |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**expires_at** | **str** |  | [readonly] 
**category** | **str** |  | [readonly] 

## Example

```python
from iblai.models.user_memory_entry import UserMemoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemoryEntry from a JSON string
user_memory_entry_instance = UserMemoryEntry.from_json(json)
# print the JSON string representation of the object
print(UserMemoryEntry.to_json())

# convert the object into a dict
user_memory_entry_dict = user_memory_entry_instance.to_dict()
# create an instance of UserMemoryEntry from a dict
user_memory_entry_from_dict = UserMemoryEntry.from_dict(user_memory_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


