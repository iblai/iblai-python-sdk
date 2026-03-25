# ItemPaywallConfigCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**allow_free_tier** | **bool** |  | [optional] 
**trial_period_days** | **int** |  | [optional] 
**grandfathering_strategy** | [**GrandfatheringStrategyEnum**](GrandfatheringStrategyEnum.md) |  | [optional] 

## Example

```python
from iblai.models.item_paywall_config_create import ItemPaywallConfigCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPaywallConfigCreate from a JSON string
item_paywall_config_create_instance = ItemPaywallConfigCreate.from_json(json)
# print the JSON string representation of the object
print(ItemPaywallConfigCreate.to_json())

# convert the object into a dict
item_paywall_config_create_dict = item_paywall_config_create_instance.to_dict()
# create an instance of ItemPaywallConfigCreate from a dict
item_paywall_config_create_from_dict = ItemPaywallConfigCreate.from_dict(item_paywall_config_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


