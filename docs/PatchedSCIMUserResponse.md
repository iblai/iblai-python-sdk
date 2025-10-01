# PatchedSCIMUserResponse

SCIM user response serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | [optional] 
**id** | **str** | User ID | [optional] 
**user_name** | **str** | Username | [optional] 
**name** | [**SCIMName**](SCIMName.md) | User&#39;s name information | [optional] 
**emails** | [**List[SCIMEmail]**](SCIMEmail.md) | User&#39;s email addresses | [optional] 
**active** | **bool** | Whether the user is active | [optional] 
**urn_ietf_params_scim_schemas_extension_enterprise_2_0_user** | [**SCIMEnterpriseUser**](SCIMEnterpriseUser.md) | Enterprise user extension data | [optional] 
**meta** | [**SCIMMeta**](SCIMMeta.md) | Resource metadata | [optional] 

## Example

```python
from iblai.models.patched_scim_user_response import PatchedSCIMUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMUserResponse from a JSON string
patched_scim_user_response_instance = PatchedSCIMUserResponse.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMUserResponse.to_json())

# convert the object into a dict
patched_scim_user_response_dict = patched_scim_user_response_instance.to_dict()
# create an instance of PatchedSCIMUserResponse from a dict
patched_scim_user_response_from_dict = PatchedSCIMUserResponse.from_dict(patched_scim_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


