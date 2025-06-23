# TenantLaunchFailed

Launch process started but could not complete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to False]
**message** | **object** |  | 
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**org** | **str** |  | 
**lms_url** | **str** |  | 
**cms_url** | **str** |  | 
**portal_url** | **str** |  | 
**edx_role** | **str** |  | 

## Example

```python
from iblai.models.tenant_launch_failed import TenantLaunchFailed

# TODO update the JSON string below
json = "{}"
# create an instance of TenantLaunchFailed from a JSON string
tenant_launch_failed_instance = TenantLaunchFailed.from_json(json)
# print the JSON string representation of the object
print(TenantLaunchFailed.to_json())

# convert the object into a dict
tenant_launch_failed_dict = tenant_launch_failed_instance.to_dict()
# create an instance of TenantLaunchFailed from a dict
tenant_launch_failed_from_dict = TenantLaunchFailed.from_dict(tenant_launch_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


