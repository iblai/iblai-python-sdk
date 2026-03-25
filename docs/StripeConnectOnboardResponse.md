# StripeConnectOnboardResponse

Serializer for Connect onboarding response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**onboarding_url** | **str** |  | 

## Example

```python
from iblai.models.stripe_connect_onboard_response import StripeConnectOnboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StripeConnectOnboardResponse from a JSON string
stripe_connect_onboard_response_instance = StripeConnectOnboardResponse.from_json(json)
# print the JSON string representation of the object
print(StripeConnectOnboardResponse.to_json())

# convert the object into a dict
stripe_connect_onboard_response_dict = stripe_connect_onboard_response_instance.to_dict()
# create an instance of StripeConnectOnboardResponse from a dict
stripe_connect_onboard_response_from_dict = StripeConnectOnboardResponse.from_dict(stripe_connect_onboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


