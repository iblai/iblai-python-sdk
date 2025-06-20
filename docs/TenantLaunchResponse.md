# TenantLaunchResponse

Launch process completed successfully

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
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
from iblai.models.tenant_launch_response import TenantLaunchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantLaunchResponse from a JSON string
tenant_launch_response_instance = TenantLaunchResponse.from_json(json)
# print the JSON string representation of the object
print(TenantLaunchResponse.to_json())

# convert the object into a dict
tenant_launch_response_dict = tenant_launch_response_instance.to_dict()
# create an instance of TenantLaunchResponse from a dict
tenant_launch_response_from_dict = TenantLaunchResponse.from_dict(tenant_launch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


