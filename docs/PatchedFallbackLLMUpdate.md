# PatchedFallbackLLMUpdate

Serializer for updating FallbackLLM configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ScopeC1dEnum**](ScopeC1dEnum.md) | Whether this fallback applies to a specific model or entire provider  * &#x60;model&#x60; - Model Specific * &#x60;provider&#x60; - Provider Wide | [optional] 
**source_provider** | **int** | The provider whose models this fallback applies to | [optional] 
**source_model** | **int** | Specific model this fallback applies to (only for model scope) | [optional] 
**fallback_provider** | **int** | The provider to use as fallback | [optional] 
**fallback_model** | **int** | The model to use as fallback | [optional] 
**is_enabled** | **bool** | Whether this fallback configuration is active | [optional] 

## Example

```python
from iblai.models.patched_fallback_llm_update import PatchedFallbackLLMUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFallbackLLMUpdate from a JSON string
patched_fallback_llm_update_instance = PatchedFallbackLLMUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedFallbackLLMUpdate.to_json())

# convert the object into a dict
patched_fallback_llm_update_dict = patched_fallback_llm_update_instance.to_dict()
# create an instance of PatchedFallbackLLMUpdate from a dict
patched_fallback_llm_update_from_dict = PatchedFallbackLLMUpdate.from_dict(patched_fallback_llm_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


