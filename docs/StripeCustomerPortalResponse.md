# StripeCustomerPortalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from iblai.models.stripe_customer_portal_response import StripeCustomerPortalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerPortalResponse from a JSON string
stripe_customer_portal_response_instance = StripeCustomerPortalResponse.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerPortalResponse.to_json())

# convert the object into a dict
stripe_customer_portal_response_dict = stripe_customer_portal_response_instance.to_dict()
# create an instance of StripeCustomerPortalResponse from a dict
stripe_customer_portal_response_from_dict = StripeCustomerPortalResponse.from_dict(stripe_customer_portal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


