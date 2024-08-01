# IntegrationCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **object** |  | [optional] 
**platform** | **str** | The platform key | 

## Example

```python
from iblai.models.integration_credential import IntegrationCredential

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCredential from a JSON string
integration_credential_instance = IntegrationCredential.from_json(json)
# print the JSON string representation of the object
print(IntegrationCredential.to_json())

# convert the object into a dict
integration_credential_dict = integration_credential_instance.to_dict()
# create an instance of IntegrationCredential from a dict
integration_credential_from_dict = IntegrationCredential.from_dict(integration_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


