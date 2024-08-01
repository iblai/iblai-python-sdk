# Prompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | [optional] 
**tone** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**is_system** | **bool** |  | [optional] [default to True]
**metadata** | **object** |  | [optional] 
**category** | **str** |  | [optional] 
**prompt** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**prompt_visibility** | [**PatchedPromptPromptVisibility**](PatchedPromptPromptVisibility.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**created_by** | **str** |  | [optional] 
**platform** | **int** |  | 

## Example

```python
from iblai.models.prompt import Prompt

# TODO update the JSON string below
json = "{}"
# create an instance of Prompt from a JSON string
prompt_instance = Prompt.from_json(json)
# print the JSON string representation of the object
print(Prompt.to_json())

# convert the object into a dict
prompt_dict = prompt_instance.to_dict()
# create an instance of Prompt from a dict
prompt_from_dict = Prompt.from_dict(prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


