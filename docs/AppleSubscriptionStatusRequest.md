# AppleSubscriptionStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | **str** |  | [optional] [default to 'com.ibleducation.community']

## Example

```python
from iblai.models.apple_subscription_status_request import AppleSubscriptionStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppleSubscriptionStatusRequest from a JSON string
apple_subscription_status_request_instance = AppleSubscriptionStatusRequest.from_json(json)
# print the JSON string representation of the object
print(AppleSubscriptionStatusRequest.to_json())

# convert the object into a dict
apple_subscription_status_request_dict = apple_subscription_status_request_instance.to_dict()
# create an instance of AppleSubscriptionStatusRequest from a dict
apple_subscription_status_request_from_dict = AppleSubscriptionStatusRequest.from_dict(apple_subscription_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


