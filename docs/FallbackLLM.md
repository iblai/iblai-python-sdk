# FallbackLLM

Serializer for FallbackLLM configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**scope** | [**ScopeC1dEnum**](ScopeC1dEnum.md) | Whether this fallback applies to a specific model or entire provider  * &#x60;model&#x60; - Model Specific * &#x60;provider&#x60; - Provider Wide | [optional] 
**source_provider** | **int** | The provider whose models this fallback applies to | 
**source_provider_detail** | [**LLMProviderMinimal**](LLMProviderMinimal.md) |  | [readonly] 
**source_model** | **int** | Specific model this fallback applies to (only for model scope) | 
**source_model_detail** | [**LLMModelRegistryMinimal**](LLMModelRegistryMinimal.md) |  | [readonly] 
**fallback_provider** | **int** | The provider to use as fallback | 
**fallback_provider_detail** | [**LLMProviderMinimal**](LLMProviderMinimal.md) |  | [readonly] 
**fallback_model** | **int** | The model to use as fallback | 
**fallback_model_detail** | [**LLMModelRegistryMinimal**](LLMModelRegistryMinimal.md) |  | [readonly] 
**tenant** | **int** | Tenant this config applies to. Null means global. | 
**tenant_key** | **str** |  | [readonly] 
**is_enabled** | **bool** | Whether this fallback configuration is active | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.fallback_llm import FallbackLLM

# TODO update the JSON string below
json = "{}"
# create an instance of FallbackLLM from a JSON string
fallback_llm_instance = FallbackLLM.from_json(json)
# print the JSON string representation of the object
print(FallbackLLM.to_json())

# convert the object into a dict
fallback_llm_dict = fallback_llm_instance.to_dict()
# create an instance of FallbackLLM from a dict
fallback_llm_from_dict = FallbackLLM.from_dict(fallback_llm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


