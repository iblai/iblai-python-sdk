# PatchedClawInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**claw_type** | [**ClawTypeEnum**](ClawTypeEnum.md) |  | [optional] 
**provision_mode** | [**ProvisionModeEnum**](ProvisionModeEnum.md) | Managed &#x3D; provisioned by us. Self-hosted &#x3D; tenant provides the server.  * &#x60;managed&#x60; - Managed * &#x60;self_hosted&#x60; - Self-hosted | [optional] [readonly] 
**server_url** | **str** | HTTPS URL of the Claw worker instance. | [optional] 
**gateway_token** | **str** |  | [optional] 
**deployment_backend** | **int** | Backend that deployed this server. Null &#x3D; manually configured. | [optional] 
**auth_headers** | **object** | Per-server auth headers (overrides backend defaults). | [optional] 
**connection_params** | **object** | Variant-specific connection parameters (write-only in API). OpenClaw: device_identity.private_key_pem, timeouts. IronClaw: typically empty (bearer token covered by gateway_token). | [optional] 
**status** | [**ClawInstanceStatusEnum**](ClawInstanceStatusEnum.md) |  | [optional] [readonly] 
**deploy_state** | [**DeployStateEnum**](DeployStateEnum.md) |  | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**last_health_check** | **datetime** |  | [optional] [readonly] 
**last_health_status** | **str** |  | [optional] [readonly] 
**claw_version** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_claw_instance import PatchedClawInstance

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClawInstance from a JSON string
patched_claw_instance_instance = PatchedClawInstance.from_json(json)
# print the JSON string representation of the object
print(PatchedClawInstance.to_json())

# convert the object into a dict
patched_claw_instance_dict = patched_claw_instance_instance.to_dict()
# create an instance of PatchedClawInstance from a dict
patched_claw_instance_from_dict = PatchedClawInstance.from_dict(patched_claw_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


