# ClawInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**claw_type** | [**ClawTypeEnum**](ClawTypeEnum.md) |  | [optional] 
**provision_mode** | [**ProvisionModeEnum**](ProvisionModeEnum.md) | Managed &#x3D; provisioned by us. Self-hosted &#x3D; tenant provides the server.  * &#x60;managed&#x60; - Managed * &#x60;self_hosted&#x60; - Self-hosted | [readonly] 
**server_url** | **str** | HTTPS URL of the Claw worker instance. | 
**gateway_token** | **str** |  | 
**deployment_backend** | **int** | Backend that deployed this server. Null &#x3D; manually configured. | [optional] 
**auth_headers** | **object** | Per-server auth headers (overrides backend defaults). | [optional] 
**connection_params** | **object** | Variant-specific connection parameters (write-only in API). OpenClaw: device_identity.private_key_pem, timeouts. IronClaw: typically empty (bearer token covered by gateway_token). | [optional] 
**status** | [**ClawInstanceStatusEnum**](ClawInstanceStatusEnum.md) |  | [readonly] 
**deploy_state** | [**DeployStateEnum**](DeployStateEnum.md) |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**last_health_check** | **datetime** |  | [readonly] 
**last_health_status** | **str** |  | [readonly] 
**claw_version** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.claw_instance import ClawInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ClawInstance from a JSON string
claw_instance_instance = ClawInstance.from_json(json)
# print the JSON string representation of the object
print(ClawInstance.to_json())

# convert the object into a dict
claw_instance_dict = claw_instance_instance.to_dict()
# create an instance of ClawInstance from a dict
claw_instance_from_dict = ClawInstance.from_dict(claw_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


