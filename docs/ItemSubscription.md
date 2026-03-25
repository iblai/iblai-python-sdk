# ItemSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [readonly] 
**user_id** | **int** |  | [readonly] 
**username** | **str** |  | [readonly] 
**email** | **str** |  | [readonly] 
**item_type** | [**ItemType40fEnum**](ItemType40fEnum.md) | Type of item being subscribed to  * &#x60;mentor&#x60; - Mentor * &#x60;course&#x60; - Course * &#x60;program&#x60; - Program * &#x60;pathway&#x60; - Pathway | 
**item_id** | **str** | Identifier for the item | 
**item_name** | **str** |  | [readonly] 
**status** | [**Status0e3Enum**](Status0e3Enum.md) | Current subscription status  * &#x60;active&#x60; - Active * &#x60;free&#x60; - Free Tier * &#x60;grandfathered&#x60; - Grandfathered * &#x60;trialing&#x60; - Trialing * &#x60;past_due&#x60; - Past Due * &#x60;canceled&#x60; - Canceled * &#x60;incomplete&#x60; - Incomplete | [optional] 
**price** | [**ItemPrice**](ItemPrice.md) |  | [readonly] 
**current_period_start** | **datetime** | Start of current billing period | [optional] 
**current_period_end** | **datetime** | End of current billing period | [optional] 
**trial_end** | **datetime** | When the trial ends (if applicable) | [optional] 
**cancel_at_period_end** | **bool** | Whether subscription will cancel at period end | [optional] 
**canceled_at** | **datetime** | When the subscription was canceled | [optional] 
**is_grandfathered** | **bool** | Whether this is a grandfathered pre-paywall user | [optional] 
**grandfathered_at** | **datetime** | When the user was grandfathered | [optional] 
**billing_portal_url** | **str** |  | [readonly] 
**metadata** | **object** | Additional subscription metadata | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.item_subscription import ItemSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSubscription from a JSON string
item_subscription_instance = ItemSubscription.from_json(json)
# print the JSON string representation of the object
print(ItemSubscription.to_json())

# convert the object into a dict
item_subscription_dict = item_subscription_instance.to_dict()
# create an instance of ItemSubscription from a dict
item_subscription_from_dict = ItemSubscription.from_dict(item_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


