# FallbackLLMCreate

Serializer for creating FallbackLLM configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ScopeC1dEnum**](ScopeC1dEnum.md) | Whether this fallback applies to a specific model or entire provider  * &#x60;model&#x60; - Model Specific * &#x60;provider&#x60; - Provider Wide | [optional] 
**tenant_key** | **str** | Tenant key. Leave empty for global configuration. | [optional] 
**source_provider_name** | [**NameEnum**](NameEnum.md) | Source provider name (e.g., &#39;openai&#39;) | 
**source_model_name** | **str** | Source model name (required for model scope) | [optional] 
**fallback_provider_name** | [**NameEnum**](NameEnum.md) | Fallback provider name | 
**fallback_model_name** | **str** | Fallback model name | 
**is_enabled** | **bool** | Whether this fallback configuration is active | [optional] 

## Example

```python
from iblai.models.fallback_llm_create import FallbackLLMCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FallbackLLMCreate from a JSON string
fallback_llm_create_instance = FallbackLLMCreate.from_json(json)
# print the JSON string representation of the object
print(FallbackLLMCreate.to_json())

# convert the object into a dict
fallback_llm_create_dict = fallback_llm_create_instance.to_dict()
# create an instance of FallbackLLMCreate from a dict
fallback_llm_create_from_dict = FallbackLLMCreate.from_dict(fallback_llm_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


