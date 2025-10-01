# SCIMEnterpriseUser

SCIM enterprise user extension serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edx_data** | **object** | edX user data | [optional] 
**user_data** | **object** | User metadata | [optional] 
**departments** | **List[Dict[str, object]]** | List of department memberships | [optional] 
**groups** | **List[Dict[str, object]]** | List of group memberships | [optional] 
**rbac_groups** | **List[Dict[str, object]]** | List of RBAC groups the user belongs to | [optional] 
**platforms** | **List[Dict[str, object]]** | List of platforms the user has access to | [optional] 

## Example

```python
from iblai.models.scim_enterprise_user import SCIMEnterpriseUser

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMEnterpriseUser from a JSON string
scim_enterprise_user_instance = SCIMEnterpriseUser.from_json(json)
# print the JSON string representation of the object
print(SCIMEnterpriseUser.to_json())

# convert the object into a dict
scim_enterprise_user_dict = scim_enterprise_user_instance.to_dict()
# create an instance of SCIMEnterpriseUser from a dict
scim_enterprise_user_from_dict = SCIMEnterpriseUser.from_dict(scim_enterprise_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


