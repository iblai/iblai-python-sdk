# AWSTenantLaunchRequest


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
**aws_transaction_id** | **str** | AWS Marketplace Customer Id and Product Code Identifier | 

## Example

```python
from iblai.models.aws_tenant_launch_request import AWSTenantLaunchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AWSTenantLaunchRequest from a JSON string
aws_tenant_launch_request_instance = AWSTenantLaunchRequest.from_json(json)
# print the JSON string representation of the object
print(AWSTenantLaunchRequest.to_json())

# convert the object into a dict
aws_tenant_launch_request_dict = aws_tenant_launch_request_instance.to_dict()
# create an instance of AWSTenantLaunchRequest from a dict
aws_tenant_launch_request_from_dict = AWSTenantLaunchRequest.from_dict(aws_tenant_launch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


