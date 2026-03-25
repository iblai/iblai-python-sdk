# LLMProviderMinimal

Minimal serializer for LLMProvider in fallback configs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | [**NameEnum**](NameEnum.md) | Provider identifier (e.g., &#39;openai&#39;, &#39;google&#39;)  * &#x60;openai&#x60; - OpenAI * &#x60;google&#x60; - Google * &#x60;anthropic&#x60; - Anthropic * &#x60;azure_openai&#x60; - Azure OpenAI * &#x60;groq&#x60; - Groq * &#x60;bedrock&#x60; - AWS Bedrock * &#x60;perplexity&#x60; - Perplexity * &#x60;nvidia&#x60; - NVIDIA * &#x60;sagemaker&#x60; - AWS SageMaker * &#x60;xai&#x60; - xAI * &#x60;deepseek&#x60; - DeepSeek * &#x60;fake&#x60; - Fake (Testing) | [readonly] 
**display_name** | **str** | Human-readable provider name | [readonly] 

## Example

```python
from iblai.models.llm_provider_minimal import LLMProviderMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of LLMProviderMinimal from a JSON string
llm_provider_minimal_instance = LLMProviderMinimal.from_json(json)
# print the JSON string representation of the object
print(LLMProviderMinimal.to_json())

# convert the object into a dict
llm_provider_minimal_dict = llm_provider_minimal_instance.to_dict()
# create an instance of LLMProviderMinimal from a dict
llm_provider_minimal_from_dict = LLMProviderMinimal.from_dict(llm_provider_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


