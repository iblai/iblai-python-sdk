# RoleCreateUpdateRequest

Serializer for role creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Role ID (for updates) | [optional] 
**name** | **str** | Role name | 
**slug** | **str** | Role slug | [optional] 
**platform_key** | **str** | Platform key | [optional] 
**data** | **object** | Additional role data | [optional] 

## Example

```python
from iblai.models.role_create_update_request import RoleCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCreateUpdateRequest from a JSON string
role_create_update_request_instance = RoleCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RoleCreateUpdateRequest.to_json())

# convert the object into a dict
role_create_update_request_dict = role_create_update_request_instance.to_dict()
# create an instance of RoleCreateUpdateRequest from a dict
role_create_update_request_from_dict = RoleCreateUpdateRequest.from_dict(role_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


