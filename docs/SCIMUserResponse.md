# SCIMUserResponse

SCIM user response serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | 
**id** | **str** | User ID | 
**user_name** | **str** | Username | 
**name** | [**SCIMName**](SCIMName.md) | User&#39;s name information | 
**emails** | [**List[SCIMEmail]**](SCIMEmail.md) | User&#39;s email addresses | 
**active** | **bool** | Whether the user is active | 
**urn_ietf_params_scim_schemas_extension_enterprise_2_0_user** | [**SCIMEnterpriseUser**](SCIMEnterpriseUser.md) | Enterprise user extension data | 
**meta** | [**SCIMMeta**](SCIMMeta.md) | Resource metadata | [optional] 

## Example

```python
from iblai.models.scim_user_response import SCIMUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMUserResponse from a JSON string
scim_user_response_instance = SCIMUserResponse.from_json(json)
# print the JSON string representation of the object
print(SCIMUserResponse.to_json())

# convert the object into a dict
scim_user_response_dict = scim_user_response_instance.to_dict()
# create an instance of SCIMUserResponse from a dict
scim_user_response_from_dict = SCIMUserResponse.from_dict(scim_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


