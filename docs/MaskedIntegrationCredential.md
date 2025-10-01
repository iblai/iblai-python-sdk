# MaskedIntegrationCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **object** |  | [optional] 
**platform** | **str** | The platform key | 
**service_info** | [**ExternalServiceInfo**](ExternalServiceInfo.md) |  | [readonly] 

## Example

```python
from iblai.models.masked_integration_credential import MaskedIntegrationCredential

# TODO update the JSON string below
json = "{}"
# create an instance of MaskedIntegrationCredential from a JSON string
masked_integration_credential_instance = MaskedIntegrationCredential.from_json(json)
# print the JSON string representation of the object
print(MaskedIntegrationCredential.to_json())

# convert the object into a dict
masked_integration_credential_dict = masked_integration_credential_instance.to_dict()
# create an instance of MaskedIntegrationCredential from a dict
masked_integration_credential_from_dict = MaskedIntegrationCredential.from_dict(masked_integration_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


