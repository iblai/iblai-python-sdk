# MemoryComponentMemoryDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MemoryComponentData]**](MemoryComponentData.md) |  | 
**catalog_item** | **str** |  | [readonly] 
**mentor_unique_id** | **str** |  | [readonly] 
**student** | **str** |  | [readonly] 
**inserted_at** | **str** |  | [readonly] 

## Example

```python
from iblai.models.memory_component_memory_detail import MemoryComponentMemoryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryComponentMemoryDetail from a JSON string
memory_component_memory_detail_instance = MemoryComponentMemoryDetail.from_json(json)
# print the JSON string representation of the object
print(MemoryComponentMemoryDetail.to_json())

# convert the object into a dict
memory_component_memory_detail_dict = memory_component_memory_detail_instance.to_dict()
# create an instance of MemoryComponentMemoryDetail from a dict
memory_component_memory_detail_from_dict = MemoryComponentMemoryDetail.from_dict(memory_component_memory_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


