# StripeCustomerPortalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | URL to redirect to when the customer exits the portal (back button) | 
**subscription_id** | **str** | Subscription ID required for subscription_update or subscription_cancel flows | [optional] 
**flow_type** | **str** | Type of flow to present: &#39;payment_method_update&#39; for adding/updating payment method, &#39;subscription_update&#39; for updating subscription, &#39;subscription_cancel&#39; for cancellation. If not provided, shows the default portal homepage.  * &#x60;payment_method_update&#x60; - Payment Method Update * &#x60;subscription_update&#x60; - Subscription Update * &#x60;subscription_cancel&#x60; - Subscription Cancel | [optional] 
**after_completion_url** | **str** | URL to redirect after the flow is completed successfully. Only used when flow_type is set. Defaults to return_url if not provided. | [optional] 

## Example

```python
from iblai.models.stripe_customer_portal_request import StripeCustomerPortalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerPortalRequest from a JSON string
stripe_customer_portal_request_instance = StripeCustomerPortalRequest.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerPortalRequest.to_json())

# convert the object into a dict
stripe_customer_portal_request_dict = stripe_customer_portal_request_instance.to_dict()
# create an instance of StripeCustomerPortalRequest from a dict
stripe_customer_portal_request_from_dict = StripeCustomerPortalRequest.from_dict(stripe_customer_portal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


