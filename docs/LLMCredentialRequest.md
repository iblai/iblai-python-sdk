# LLMCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential provider | 
**value** | **object** | Value of the credential provider | 
**platform** | **str** | Key of the tenant | 

## Example

```python
from iblai.models.llm_credential_request import LLMCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LLMCredentialRequest from a JSON string
llm_credential_request_instance = LLMCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(LLMCredentialRequest.to_json())

# convert the object into a dict
llm_credential_request_dict = llm_credential_request_instance.to_dict()
# create an instance of LLMCredentialRequest from a dict
llm_credential_request_from_dict = LLMCredentialRequest.from_dict(llm_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


