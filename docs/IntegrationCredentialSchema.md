# IntegrationCredentialSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**var_schema** | **object** |  | [optional] 
**service_info** | [**ExternalServiceInfo**](ExternalServiceInfo.md) |  | [readonly] 

## Example

```python
from iblai.models.integration_credential_schema import IntegrationCredentialSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCredentialSchema from a JSON string
integration_credential_schema_instance = IntegrationCredentialSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationCredentialSchema.to_json())

# convert the object into a dict
integration_credential_schema_dict = integration_credential_schema_instance.to_dict()
# create an instance of IntegrationCredentialSchema from a dict
integration_credential_schema_from_dict = IntegrationCredentialSchema.from_dict(integration_credential_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


