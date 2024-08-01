# PromptCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.prompt_category import PromptCategory

# TODO update the JSON string below
json = "{}"
# create an instance of PromptCategory from a JSON string
prompt_category_instance = PromptCategory.from_json(json)
# print the JSON string representation of the object
print(PromptCategory.to_json())

# convert the object into a dict
prompt_category_dict = prompt_category_instance.to_dict()
# create an instance of PromptCategory from a dict
prompt_category_from_dict = PromptCategory.from_dict(prompt_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


