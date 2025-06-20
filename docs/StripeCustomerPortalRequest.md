# StripeCustomerPortalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** |  | 

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


