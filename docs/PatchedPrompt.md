# PatchedPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**mentor** | **str** |  | [optional] 
**tone** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**is_system** | **bool** |  | [optional] [default to True]
**metadata** | **object** |  | [optional] 
**category** | **str** |  | [optional] 
**prompt** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**prompt_visibility** | [**PatchedPromptPromptVisibility**](PatchedPromptPromptVisibility.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] 
**platform** | **int** |  | [optional] 

## Example

```python
from iblai.models.patched_prompt import PatchedPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPrompt from a JSON string
patched_prompt_instance = PatchedPrompt.from_json(json)
# print the JSON string representation of the object
print(PatchedPrompt.to_json())

# convert the object into a dict
patched_prompt_dict = patched_prompt_instance.to_dict()
# create an instance of PatchedPrompt from a dict
patched_prompt_from_dict = PatchedPrompt.from_dict(patched_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


