# ReportedRoleCreateUpdateRequest

Serializer for reported role creation/update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**username** | **str** | Username | [optional] 
**roles** | **List[Dict[str, object]]** | List of roles (can be role IDs or objects with name, platform_key, etc.) | 
**data** | **object** | Additional data | [optional] 

## Example

```python
from iblai.models.reported_role_create_update_request import ReportedRoleCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportedRoleCreateUpdateRequest from a JSON string
reported_role_create_update_request_instance = ReportedRoleCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReportedRoleCreateUpdateRequest.to_json())

# convert the object into a dict
reported_role_create_update_request_dict = reported_role_create_update_request_instance.to_dict()
# create an instance of ReportedRoleCreateUpdateRequest from a dict
reported_role_create_update_request_from_dict = ReportedRoleCreateUpdateRequest.from_dict(reported_role_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


