# CredentialProviderConfig

Serializer for CredentialProviderConfig model.  Serializes provider configuration including platform, provider name, config JSON, enabled status, and timestamps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**platform_name** | **str** |  | [readonly] 
**provider_name** | **str** | The credential provider name (references CredentialProvider.name) | 
**provider_name_display** | **str** | Get display name from provider if available, otherwise use provider_name. | [readonly] 
**config** | **object** | Provider-specific configuration in JSON format | [optional] 
**enabled** | **bool** | Whether this provider integration is enabled for the platform | [optional] 
**created** | **datetime** |  | [readonly] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.credential_provider_config import CredentialProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialProviderConfig from a JSON string
credential_provider_config_instance = CredentialProviderConfig.from_json(json)
# print the JSON string representation of the object
print(CredentialProviderConfig.to_json())

# convert the object into a dict
credential_provider_config_dict = credential_provider_config_instance.to_dict()
# create an instance of CredentialProviderConfig from a dict
credential_provider_config_from_dict = CredentialProviderConfig.from_dict(credential_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


