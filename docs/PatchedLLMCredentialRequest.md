# PatchedLLMCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential provider | [optional] 
**value** | **object** | Value of the credential provider | [optional] 
**platform** | **str** | Key of the tenant | [optional] 

## Example

```python
from iblai.models.patched_llm_credential_request import PatchedLLMCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLLMCredentialRequest from a JSON string
patched_llm_credential_request_instance = PatchedLLMCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLLMCredentialRequest.to_json())

# convert the object into a dict
patched_llm_credential_request_dict = patched_llm_credential_request_instance.to_dict()
# create an instance of PatchedLLMCredentialRequest from a dict
patched_llm_credential_request_from_dict = PatchedLLMCredentialRequest.from_dict(patched_llm_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


