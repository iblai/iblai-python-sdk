# ItemPaywallConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**ItemType40fEnum**](ItemType40fEnum.md) | Type of item being paywalled (e.g. mentor, course, program)  * &#x60;mentor&#x60; - Mentor * &#x60;course&#x60; - Course * &#x60;program&#x60; - Program * &#x60;pathway&#x60; - Pathway | 
**item_id** | **str** | Identifier for the item (UUID for mentors, slug/key for others) | 
**item_name** | **str** |  | [readonly] 
**is_enabled** | **bool** | Whether the paywall is enabled for this item | [optional] 
**description** | **str** | Marketing description shown to customers at checkout. If blank, a default is generated from the item name. | [optional] 
**allow_free_tier** | **bool** | Whether to allow a free tier (bypasses checkout) | [optional] 
**stripe_product_id** | **str** | Stripe Product ID for this item (on the connected account) | [readonly] 
**trial_period_days** | **int** | Number of days for free trial (0 &#x3D; no trial) | [optional] 
**grandfathering_strategy** | [**GrandfatheringStrategyEnum**](GrandfatheringStrategyEnum.md) | How to handle existing users when enabling the paywall  * &#x60;free_forever&#x60; - Free Forever - Existing users get unlimited free access * &#x60;require_subscription&#x60; - Require Subscription - All users must subscribe (no grandfathering) | [optional] 
**paywall_enabled_at** | **datetime** | When the paywall was first enabled (for grandfathering cutoff) | [readonly] 
**prices** | [**List[ItemPrice]**](ItemPrice.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.item_paywall_config import ItemPaywallConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPaywallConfig from a JSON string
item_paywall_config_instance = ItemPaywallConfig.from_json(json)
# print the JSON string representation of the object
print(ItemPaywallConfig.to_json())

# convert the object into a dict
item_paywall_config_dict = item_paywall_config_instance.to_dict()
# create an instance of ItemPaywallConfig from a dict
item_paywall_config_from_dict = ItemPaywallConfig.from_dict(item_paywall_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


