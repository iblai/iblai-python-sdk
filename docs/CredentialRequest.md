# CredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the credential provider (e.g., &#39;openai&#39;, &#39;google-drive&#39;) | 
**value** | **object** | Credential data for the provider (API keys, service account details, etc.) | 
**platform** | **str** | Organization key identifier for the tenant | 

## Example

```python
from iblai.models.credential_request import CredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialRequest from a JSON string
credential_request_instance = CredentialRequest.from_json(json)
# print the JSON string representation of the object
print(CredentialRequest.to_json())

# convert the object into a dict
credential_request_dict = credential_request_instance.to_dict()
# create an instance of CredentialRequest from a dict
credential_request_from_dict = CredentialRequest.from_dict(credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


