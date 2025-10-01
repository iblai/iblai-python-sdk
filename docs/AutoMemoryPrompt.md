# AutoMemoryPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_memory_prompt** | **str** |  | [optional] 
**reset** | **bool** |  | [optional] 

## Example

```python
from iblai.models.auto_memory_prompt import AutoMemoryPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of AutoMemoryPrompt from a JSON string
auto_memory_prompt_instance = AutoMemoryPrompt.from_json(json)
# print the JSON string representation of the object
print(AutoMemoryPrompt.to_json())

# convert the object into a dict
auto_memory_prompt_dict = auto_memory_prompt_instance.to_dict()
# create an instance of AutoMemoryPrompt from a dict
auto_memory_prompt_from_dict = AutoMemoryPrompt.from_dict(auto_memory_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


