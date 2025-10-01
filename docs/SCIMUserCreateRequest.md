# SCIMUserCreateRequest

SCIM user creation request serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | [optional] [default to ["urn:ietf:params:scim:schemas:core:2.0:User"]]
**user_name** | **str** | Unique username/email for the user | 
**name** | [**SCIMName**](SCIMName.md) | User&#39;s name information | 
**emails** | [**List[SCIMEmail]**](SCIMEmail.md) | User&#39;s email addresses | 
**active** | **bool** | Whether the user is active | [optional] [default to True]
**display_name** | **str** | Display name | [optional] 
**locale** | **str** | User locale | [optional] 
**timezone** | **str** | User timezone | [optional] 
**title** | **str** | Job title | [optional] 
**organization** | **str** | Organization | [optional] 
**phone_numbers** | [**List[SCIMPhoneNumber]**](SCIMPhoneNumber.md) | Phone numbers | [optional] 
**addresses** | [**List[SCIMAddress]**](SCIMAddress.md) | Addresses | [optional] 
**entitlements** | **List[str]** | User entitlements | [optional] 
**roles** | **List[str]** | User roles | [optional] 
**x509_certificates** | **List[str]** | X.509 certificates | [optional] 
**password** | **str** | User password | [optional] 
**provider** | **str** | Authentication provider | [optional] 
**tpa_uid** | **str** | Third-party authentication UID | [optional] 
**is_staff** | **bool** | Whether the user is a staff member | [optional] [default to False]
**update** | **bool** | Whether to update existing user | [optional] [default to False]
**platform_orgs** | **List[str]** | List of platform organizations to link the user to | [optional] 
**department_ids** | **List[int]** | List of department IDs to make the user a member of | [optional] 
**group_ids** | **List[int]** | List of group IDs to add the user to | [optional] 
**rbac_group_unique_ids** | **List[str]** | List of RBAC group unique IDs to add the user to | [optional] 
**meta** | [**SCIMMeta**](SCIMMeta.md) | Resource metadata | [optional] 

## Example

```python
from iblai.models.scim_user_create_request import SCIMUserCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMUserCreateRequest from a JSON string
scim_user_create_request_instance = SCIMUserCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMUserCreateRequest.to_json())

# convert the object into a dict
scim_user_create_request_dict = scim_user_create_request_instance.to_dict()
# create an instance of SCIMUserCreateRequest from a dict
scim_user_create_request_from_dict = SCIMUserCreateRequest.from_dict(scim_user_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


