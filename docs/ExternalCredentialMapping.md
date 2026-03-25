# ExternalCredentialMapping

Serializer for ExternalCredentialMapping model.  Serializes external credential mappings including credential, platform, provider, external_template_id, and metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**credential_id** | **str** |  | [readonly] 
**credential_name** | **str** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**platform_name** | **str** |  | [readonly] 
**provider** | **int** | The credential provider | [readonly] 
**provider_name** | **str** | The credential provider name (references CredentialProvider.name) | 
**provider_name_display** | **str** | Get display name from provider if available, otherwise use provider_name. | [readonly] 
**external_template_id** | **str** | The template ID in the external system (e.g., Accredible template ID) | [optional] 
**group_id** | **str** | The group ID in the external system (e.g., Accredible group ID). If not set, will fall back to the provider config&#39;s group_id. | [optional] 
**metadata** | **object** | Additional metadata stored as JSON (for general mapping information, not sync status) | [optional] 
**created** | **datetime** |  | [readonly] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.external_credential_mapping import ExternalCredentialMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCredentialMapping from a JSON string
external_credential_mapping_instance = ExternalCredentialMapping.from_json(json)
# print the JSON string representation of the object
print(ExternalCredentialMapping.to_json())

# convert the object into a dict
external_credential_mapping_dict = external_credential_mapping_instance.to_dict()
# create an instance of ExternalCredentialMapping from a dict
external_credential_mapping_from_dict = ExternalCredentialMapping.from_dict(external_credential_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


