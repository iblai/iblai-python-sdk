# LLMModelRegistryMinimal

Minimal serializer for LLMModelRegistry in fallback configs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**llm_name** | **str** | Model identifier (e.g., &#39;gpt-4o&#39;, &#39;gemini-2.5-pro&#39;) | [readonly] 
**display_name** | **str** | Human-readable model name | [readonly] 
**provider_name** | **str** |  | [readonly] 

## Example

```python
from iblai.models.llm_model_registry_minimal import LLMModelRegistryMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of LLMModelRegistryMinimal from a JSON string
llm_model_registry_minimal_instance = LLMModelRegistryMinimal.from_json(json)
# print the JSON string representation of the object
print(LLMModelRegistryMinimal.to_json())

# convert the object into a dict
llm_model_registry_minimal_dict = llm_model_registry_minimal_instance.to_dict()
# create an instance of LLMModelRegistryMinimal from a dict
llm_model_registry_minimal_from_dict = LLMModelRegistryMinimal.from_dict(llm_model_registry_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


