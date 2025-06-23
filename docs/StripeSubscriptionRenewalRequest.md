# StripeSubscriptionRenewalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_session_uuid** | **str** |  | 
**return_url** | **str** |  | 

## Example

```python
from iblai.models.stripe_subscription_renewal_request import StripeSubscriptionRenewalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeSubscriptionRenewalRequest from a JSON string
stripe_subscription_renewal_request_instance = StripeSubscriptionRenewalRequest.from_json(json)
# print the JSON string representation of the object
print(StripeSubscriptionRenewalRequest.to_json())

# convert the object into a dict
stripe_subscription_renewal_request_dict = stripe_subscription_renewal_request_instance.to_dict()
# create an instance of StripeSubscriptionRenewalRequest from a dict
stripe_subscription_renewal_request_from_dict = StripeSubscriptionRenewalRequest.from_dict(stripe_subscription_renewal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


