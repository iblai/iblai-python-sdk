# TenantLaunchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | 
**firstname** | **str** |  | [optional] [default to '']
**lastname** | **str** |  | [optional] [default to '']
**password** | **str** |  | [optional] 
**name** | **str** | Organization name | 
**key** | **str** | Unique key for the organization | 
**ignore_user_exists** | **bool** |  | [optional] [default to False]

## Example

```python
from iblai.models.tenant_launch_request import TenantLaunchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantLaunchRequest from a JSON string
tenant_launch_request_instance = TenantLaunchRequest.from_json(json)
# print the JSON string representation of the object
print(TenantLaunchRequest.to_json())

# convert the object into a dict
tenant_launch_request_dict = tenant_launch_request_instance.to_dict()
# create an instance of TenantLaunchRequest from a dict
tenant_launch_request_from_dict = TenantLaunchRequest.from_dict(tenant_launch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


