# SCIMGroup

SCIM group serializer for RBAC group management

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | [optional] [default to ["urn:ietf:params:scim:schemas:core:2.0:Group"]]
**id** | **str** | RBAC group unique ID (must match existing RBAC group) | 
**display_name** | **str** | RBAC group display name | 
**description** | **str** | RBAC group description | [optional] 
**members** | **List[Dict[str, object]]** | Users to add/remove from the RBAC group | [optional] 
**meta** | [**SCIMMeta**](SCIMMeta.md) | Resource metadata | [optional] 

## Example

```python
from iblai.models.scim_group import SCIMGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMGroup from a JSON string
scim_group_instance = SCIMGroup.from_json(json)
# print the JSON string representation of the object
print(SCIMGroup.to_json())

# convert the object into a dict
scim_group_dict = scim_group_instance.to_dict()
# create an instance of SCIMGroup from a dict
scim_group_from_dict = SCIMGroup.from_dict(scim_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


