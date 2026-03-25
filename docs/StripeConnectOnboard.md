# StripeConnectOnboard

Serializer for Connect onboarding request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | URL to redirect after onboarding completes | 
**refresh_url** | **str** | URL to redirect if onboarding link expires | 
**business_type** | [**BusinessTypeEnum**](BusinessTypeEnum.md) | Type of business  * &#x60;individual&#x60; - individual * &#x60;company&#x60; - company | [optional] 

## Example

```python
from iblai.models.stripe_connect_onboard import StripeConnectOnboard

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectOnboard from a JSON string
stripe_connect_onboard_instance = StripeConnectOnboard.from_json(json)
# print the JSON string representation of the object
print(StripeConnectOnboard.to_json())

# convert the object into a dict
stripe_connect_onboard_dict = stripe_connect_onboard_instance.to_dict()
# create an instance of StripeConnectOnboard from a dict
stripe_connect_onboard_from_dict = StripeConnectOnboard.from_dict(stripe_connect_onboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


