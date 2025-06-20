# MemoryComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_gaps** | **List[str]** |  | [readonly] 
**lessons_learned** | **List[str]** |  | [readonly] 
**help_requests** | **List[str]** |  | [readonly] 

## Example

```python
from iblai.models.memory_component_response import MemoryComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryComponentResponse from a JSON string
memory_component_response_instance = MemoryComponentResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryComponentResponse.to_json())

# convert the object into a dict
memory_component_response_dict = memory_component_response_instance.to_dict()
# create an instance of MemoryComponentResponse from a dict
memory_component_response_from_dict = MemoryComponentResponse.from_dict(memory_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


