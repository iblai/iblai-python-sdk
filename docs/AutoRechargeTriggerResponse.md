# AutoRechargeTriggerResponse

Response schema for POST auto-recharge/trigger/ (200).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AutoRechargeTriggerResponseStatusEnum**](AutoRechargeTriggerResponseStatusEnum.md) | &#39;triggered&#39; if a charge was attempted, &#39;skipped&#39; otherwise.  * &#x60;triggered&#x60; - triggered * &#x60;skipped&#x60; - skipped | 

## Example

```python
from iblai.models.auto_recharge_trigger_response import AutoRechargeTriggerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRechargeTriggerResponse from a JSON string
auto_recharge_trigger_response_instance = AutoRechargeTriggerResponse.from_json(json)
# print the JSON string representation of the object
print(AutoRechargeTriggerResponse.to_json())

# convert the object into a dict
auto_recharge_trigger_response_dict = auto_recharge_trigger_response_instance.to_dict()
# create an instance of AutoRechargeTriggerResponse from a dict
auto_recharge_trigger_response_from_dict = AutoRechargeTriggerResponse.from_dict(auto_recharge_trigger_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


