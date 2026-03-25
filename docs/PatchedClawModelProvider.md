# PatchedClawModelProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**server** | **int** |  | [optional] 
**server_name** | **str** |  | [optional] [readonly] 
**name** | **str** | Provider identifier in the Claw config (e.g. &#39;minimax&#39;) | [optional] 
**base_url** | **str** | Provider API endpoint (e.g. https://api.minimax.io/anthropic) | [optional] 
**api_type** | **str** | Claw provider API type (e.g. &#39;openai-completions&#39;, &#39;anthropic-messages&#39;). | [optional] 
**credential_name** | **str** | Name of the LLMCredential to resolve the API key from | [optional] 
**credential_key** | **str** | Key within the LLMCredential value JSON to extract the API key | [optional] 
**model_catalog** | **object** | List of {\&quot;id\&quot;: \&quot;...\&quot;, \&quot;name\&quot;: \&quot;...\&quot;} entries for the provider model catalog | [optional] 
**enabled** | **bool** |  | [optional] 
**models_mode** | **str** | &#39;merge&#39; adds to built-in models, &#39;replace&#39; uses only configured providers. | [optional] 
**last_provider_push** | **datetime** |  | [optional] [readonly] 
**last_provider_push_status** | **str** |  | [optional] [readonly] 
**credential_resolved** | **bool** | Check if the referenced LLMCredential exists for this platform. | [optional] [readonly] 

## Example

```python
from iblai.models.patched_claw_model_provider import PatchedClawModelProvider

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClawModelProvider from a JSON string
patched_claw_model_provider_instance = PatchedClawModelProvider.from_json(json)
# print the JSON string representation of the object
print(PatchedClawModelProvider.to_json())

# convert the object into a dict
patched_claw_model_provider_dict = patched_claw_model_provider_instance.to_dict()
# create an instance of PatchedClawModelProvider from a dict
patched_claw_model_provider_from_dict = PatchedClawModelProvider.from_dict(patched_claw_model_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


