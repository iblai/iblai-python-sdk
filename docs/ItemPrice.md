# ItemPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** | Display name for this pricing tier (e.g., &#39;Basic&#39;, &#39;Premium&#39;) | 
**description** | **str** | Description of what&#39;s included in this tier | [optional] 
**amount** | **decimal.Decimal** | Price amount in USD (e.g., 9.99 for $9.99, 0 for free) | 
**currency** | **str** | Currency code (e.g., &#39;usd&#39;, &#39;eur&#39;) | [optional] 
**interval** | [**IntervalEnum**](IntervalEnum.md) | Billing interval  * &#x60;month&#x60; - Monthly * &#x60;year&#x60; - Yearly * &#x60;one_time&#x60; - One Time | [optional] 
**stripe_price_id** | **str** | Stripe Price ID (on the connected account) | [readonly] 
**is_active** | **bool** | Whether this price is currently available for purchase | [optional] 
**features** | **object** | List of features included in this tier | [optional] 
**sort_order** | **int** | Display order for this price tier | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.item_price import ItemPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPrice from a JSON string
item_price_instance = ItemPrice.from_json(json)
# print the JSON string representation of the object
print(ItemPrice.to_json())

# convert the object into a dict
item_price_dict = item_price_instance.to_dict()
# create an instance of ItemPrice from a dict
item_price_from_dict = ItemPrice.from_dict(item_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


