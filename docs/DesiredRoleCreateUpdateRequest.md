# DesiredRoleCreateUpdateRequest

Serializer for desired role creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**username** | **str** | Username | [optional] 
**roles** | **List[Dict[str, object]]** | List of roles (can be role IDs or objects with name, platform_key, etc.) | 
**data** | **object** | Additional data | [optional] 

## Example

```python
from iblai.models.desired_role_create_update_request import DesiredRoleCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredRoleCreateUpdateRequest from a JSON string
desired_role_create_update_request_instance = DesiredRoleCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DesiredRoleCreateUpdateRequest.to_json())

# convert the object into a dict
desired_role_create_update_request_dict = desired_role_create_update_request_instance.to_dict()
# create an instance of DesiredRoleCreateUpdateRequest from a dict
desired_role_create_update_request_from_dict = DesiredRoleCreateUpdateRequest.from_dict(desired_role_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


