# MemoryComponentMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MemoryComponentData]**](MemoryComponentData.md) |  | [readonly] 

## Example

```python
from iblai.models.memory_component_memory import MemoryComponentMemory

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryComponentMemory from a JSON string
memory_component_memory_instance = MemoryComponentMemory.from_json(json)
# print the JSON string representation of the object
print(MemoryComponentMemory.to_json())

# convert the object into a dict
memory_component_memory_dict = memory_component_memory_instance.to_dict()
# create an instance of MemoryComponentMemory from a dict
memory_component_memory_from_dict = MemoryComponentMemory.from_dict(memory_component_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


