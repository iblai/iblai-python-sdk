# LLMCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **object** |  | [optional] 
**platform** | **str** | The platform key | 

## Example

```python
from iblai.models.llm_credential_response import LLMCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LLMCredentialResponse from a JSON string
llm_credential_response_instance = LLMCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(LLMCredentialResponse.to_json())

# convert the object into a dict
llm_credential_response_dict = llm_credential_response_instance.to_dict()
# create an instance of LLMCredentialResponse from a dict
llm_credential_response_from_dict = LLMCredentialResponse.from_dict(llm_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


