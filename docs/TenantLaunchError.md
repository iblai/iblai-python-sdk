# TenantLaunchError

An unexpected error occurred during launch process

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to False]
**message** | **object** |  | 
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from iblai.models.tenant_launch_error import TenantLaunchError

# TODO update the JSON string below
json = "{}"
# create an instance of TenantLaunchError from a JSON string
tenant_launch_error_instance = TenantLaunchError.from_json(json)
# print the JSON string representation of the object
print(TenantLaunchError.to_json())

# convert the object into a dict
tenant_launch_error_dict = tenant_launch_error_instance.to_dict()
# create an instance of TenantLaunchError from a dict
tenant_launch_error_from_dict = TenantLaunchError.from_dict(tenant_launch_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


