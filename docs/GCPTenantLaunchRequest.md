# GCPTenantLaunchRequest


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
**x_gcp_marketplace_token** | **str** | GCP Marketplace token | 
**product_id** | **str** | GCP product to subscribe to | [optional] [default to '']

## Example

```python
from iblai.models.gcp_tenant_launch_request import GCPTenantLaunchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTenantLaunchRequest from a JSON string
gcp_tenant_launch_request_instance = GCPTenantLaunchRequest.from_json(json)
# print the JSON string representation of the object
print(GCPTenantLaunchRequest.to_json())

# convert the object into a dict
gcp_tenant_launch_request_dict = gcp_tenant_launch_request_instance.to_dict()
# create an instance of GCPTenantLaunchRequest from a dict
gcp_tenant_launch_request_from_dict = GCPTenantLaunchRequest.from_dict(gcp_tenant_launch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


