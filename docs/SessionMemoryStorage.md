# SessionMemoryStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | [**MemoryComponentMemory**](MemoryComponentMemory.md) |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**session_id** | **str** |  | [readonly] 

## Example

```python
from iblai.models.session_memory_storage import SessionMemoryStorage

# TODO update the JSON string below
json = "{}"
# create an instance of SessionMemoryStorage from a JSON string
session_memory_storage_instance = SessionMemoryStorage.from_json(json)
# print the JSON string representation of the object
print(SessionMemoryStorage.to_json())

# convert the object into a dict
session_memory_storage_dict = session_memory_storage_instance.to_dict()
# create an instance of SessionMemoryStorage from a dict
session_memory_storage_from_dict = SessionMemoryStorage.from_dict(session_memory_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


