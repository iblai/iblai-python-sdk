# StripeCheckoutSessionRequest

Serializer for Stripe checkout session creation requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Product SKU | [optional] 
**product** | **str** | Alternative to SKU | [optional] 
**success_url** | **str** | URL to redirect after successful payment | 
**cancel_url** | **str** | URL to redirect if checkout cancelled | 
**mode** | [**StripeCheckoutSessionRequestModeEnum**](StripeCheckoutSessionRequestModeEnum.md) | Checkout mode  * &#x60;subscription&#x60; - subscription * &#x60;payment&#x60; - payment * &#x60;setup&#x60; - setup | [optional] 
**metered** | **bool** | Whether to use metered billing | [optional] [default to False]
**quantity** | **int** | Subscription quantity | [optional] [default to 1]
**coupon** | **str** | Coupon code to apply | [optional] 
**is_free_trial** | **bool** | Enable free trial | [optional] [default to False]
**trial_days** | **int** | Trial period in days | [optional] 
**skip_card** | **bool** | Skip card collection for trial | [optional] [default to False]

## Example

```python
from iblai.models.stripe_checkout_session_request import StripeCheckoutSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCheckoutSessionRequest from a JSON string
stripe_checkout_session_request_instance = StripeCheckoutSessionRequest.from_json(json)
# print the JSON string representation of the object
print(StripeCheckoutSessionRequest.to_json())

# convert the object into a dict
stripe_checkout_session_request_dict = stripe_checkout_session_request_instance.to_dict()
# create an instance of StripeCheckoutSessionRequest from a dict
stripe_checkout_session_request_from_dict = StripeCheckoutSessionRequest.from_dict(stripe_checkout_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


