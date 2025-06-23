# StripeNewUserTenantLaunchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] [default to '']
**lastname** | **str** |  | [optional] [default to '']
**password** | **str** |  | [optional] 
**name** | **str** | Organization name | 
**key** | **str** | Unique key for the organization | 
**ignore_user_exists** | **bool** |  | [optional] [default to False]
**stripe_checkout_id_alt** | **str** | Stripe Checkout Id to launch the tenant | 

## Example

```python
from iblai.models.stripe_new_user_tenant_launch_request import StripeNewUserTenantLaunchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeNewUserTenantLaunchRequest from a JSON string
stripe_new_user_tenant_launch_request_instance = StripeNewUserTenantLaunchRequest.from_json(json)
# print the JSON string representation of the object
print(StripeNewUserTenantLaunchRequest.to_json())

# convert the object into a dict
stripe_new_user_tenant_launch_request_dict = stripe_new_user_tenant_launch_request_instance.to_dict()
# create an instance of StripeNewUserTenantLaunchRequest from a dict
stripe_new_user_tenant_launch_request_from_dict = StripeNewUserTenantLaunchRequest.from_dict(stripe_new_user_tenant_launch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


