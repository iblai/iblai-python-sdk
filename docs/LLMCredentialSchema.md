# LLMCredentialSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**var_schema** | **object** |  | [optional] 
**service_info** | [**ExternalServiceInfo**](ExternalServiceInfo.md) |  | [readonly] 

## Example

```python
from iblai.models.llm_credential_schema import LLMCredentialSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LLMCredentialSchema from a JSON string
llm_credential_schema_instance = LLMCredentialSchema.from_json(json)
# print the JSON string representation of the object
print(LLMCredentialSchema.to_json())

# convert the object into a dict
llm_credential_schema_dict = llm_credential_schema_instance.to_dict()
# create an instance of LLMCredentialSchema from a dict
llm_credential_schema_from_dict = LLMCredentialSchema.from_dict(llm_credential_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


