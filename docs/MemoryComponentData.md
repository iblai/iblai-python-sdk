# MemoryComponentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**KindEnum**](KindEnum.md) |  | [optional] 
**content** | **str** |  | 

## Example

```python
from iblai.models.memory_component_data import MemoryComponentData

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryComponentData from a JSON string
memory_component_data_instance = MemoryComponentData.from_json(json)
# print the JSON string representation of the object
print(MemoryComponentData.to_json())

# convert the object into a dict
memory_component_data_dict = memory_component_data_instance.to_dict()
# create an instance of MemoryComponentData from a dict
memory_component_data_from_dict = MemoryComponentData.from_dict(memory_component_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


