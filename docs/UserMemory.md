# UserMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [readonly] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [readonly] 
**unique_id** | **str** |  | [optional] 
**username** | **str** |  | [readonly] 
**platform** | **str** |  | [readonly] 
**mentor** | **str** |  | [readonly] 
**session_id** | **str** |  | [readonly] 
**catalog_item_type** | **str** |  | [readonly] 
**catalog_item_id** | **str** |  | [readonly] 
**entries** | [**List[UserMemoryEntry]**](UserMemoryEntry.md) |  | 
**inserted_at** | **str** |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**is_auto_generated** | **bool** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from iblai.models.user_memory import UserMemory

# TODO update the JSON string below
json = "{}"
# create an instance of UserMemory from a JSON string
user_memory_instance = UserMemory.from_json(json)
# print the JSON string representation of the object
print(UserMemory.to_json())

# convert the object into a dict
user_memory_dict = user_memory_instance.to_dict()
# create an instance of UserMemory from a dict
user_memory_from_dict = UserMemory.from_dict(user_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


