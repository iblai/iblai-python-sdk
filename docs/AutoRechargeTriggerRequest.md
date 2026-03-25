# AutoRechargeTriggerRequest

Request schema for POST auto-recharge/trigger/.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The unique key of the platform. Defaults to &#39;main&#39;. | [optional] 
**amount_usd** | **decimal.Decimal** | Optional. When set, perform manual top-up: charge this amount (user USD) and add credits. No threshold, spending limit, or cooldown. Omit to run normal auto-recharge once. | [optional] 

## Example

```python
from iblai.models.auto_recharge_trigger_request import AutoRechargeTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRechargeTriggerRequest from a JSON string
auto_recharge_trigger_request_instance = AutoRechargeTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(AutoRechargeTriggerRequest.to_json())

# convert the object into a dict
auto_recharge_trigger_request_dict = auto_recharge_trigger_request_instance.to_dict()
# create an instance of AutoRechargeTriggerRequest from a dict
auto_recharge_trigger_request_from_dict = AutoRechargeTriggerRequest.from_dict(auto_recharge_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


