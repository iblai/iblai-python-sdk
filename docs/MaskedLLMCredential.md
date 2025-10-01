# MaskedLLMCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **object** |  | [optional] 
**platform** | **str** | The platform key | 
**service_info** | [**ExternalServiceInfo**](ExternalServiceInfo.md) |  | [readonly] 

## Example

```python
from iblai.models.masked_llm_credential import MaskedLLMCredential

# TODO update the JSON string below
json = "{}"
# create an instance of MaskedLLMCredential from a JSON string
masked_llm_credential_instance = MaskedLLMCredential.from_json(json)
# print the JSON string representation of the object
print(MaskedLLMCredential.to_json())

# convert the object into a dict
masked_llm_credential_dict = masked_llm_credential_instance.to_dict()
# create an instance of MaskedLLMCredential from a dict
masked_llm_credential_from_dict = MaskedLLMCredential.from_dict(masked_llm_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


