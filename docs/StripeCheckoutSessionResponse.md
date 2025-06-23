# StripeCheckoutSessionResponse

Stripe checkout session serialized response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_to** | **str** |  | 

## Example

```python
from iblai.models.stripe_checkout_session_response import StripeCheckoutSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCheckoutSessionResponse from a JSON string
stripe_checkout_session_response_instance = StripeCheckoutSessionResponse.from_json(json)
# print the JSON string representation of the object
print(StripeCheckoutSessionResponse.to_json())

# convert the object into a dict
stripe_checkout_session_response_dict = stripe_checkout_session_response_instance.to_dict()
# create an instance of StripeCheckoutSessionResponse from a dict
stripe_checkout_session_response_from_dict = StripeCheckoutSessionResponse.from_dict(stripe_checkout_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


