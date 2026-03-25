# CallConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | 
**mode** | [**CallConfigurationModeEnum**](CallConfigurationModeEnum.md) |  | [optional] 
**tts_provider** | [**TtsProviderEnum**](TtsProviderEnum.md) |  | [optional] 
**stt_provider** | [**SttProviderEnum**](SttProviderEnum.md) |  | [optional] 
**llm_provider** | [**LlmProviderEnum**](LlmProviderEnum.md) |  | [optional] 
**language** | **str** | Language code for TTS, STT, and LLM (e.g., &#39;en&#39;, &#39;en-US&#39;, &#39;es&#39;, &#39;fr&#39;). Defaults to &#39;en&#39; (English). | [optional] 
**use_function_calling_for_rag** | **bool** | Whether to use function calls in the agent or force RAG calls before LLM generation | [optional] 
**google_voice** | [**Voice**](Voice.md) |  | [optional] 
**openai_voice** | [**Voice**](Voice.md) |  | [optional] 
**openai_voice_id** | **int** |  | [optional] 
**google_voice_id** | **int** |  | [optional] 
**enable_video** | **bool** | Whether to enable video for the call. (applicable only for realtime mode) | [optional] 
**screensharing_system_prompt** | **str** | System prompt to use for screensharing guidance. Defaults to VIDEO_GUIDANCE_PROMPT from constants. | [optional] 
**screensharing_proactive_prompt** | **str** | Proactive prompt used during screensharing calls to guide the conversation. | [optional] 
**platform_key** | **str** |  | [readonly] 

## Example

```python
from iblai.models.call_configuration import CallConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CallConfiguration from a JSON string
call_configuration_instance = CallConfiguration.from_json(json)
# print the JSON string representation of the object
print(CallConfiguration.to_json())

# convert the object into a dict
call_configuration_dict = call_configuration_instance.to_dict()
# create an instance of CallConfiguration from a dict
call_configuration_from_dict = CallConfiguration.from_dict(call_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


