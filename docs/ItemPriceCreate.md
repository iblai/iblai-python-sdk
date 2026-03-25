# ItemPriceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for this pricing tier (e.g., &#39;Basic&#39;, &#39;Premium&#39;) | 
**description** | **str** | Description of what&#39;s included in this tier | [optional] 
**amount** | **decimal.Decimal** |  | 
**currency** | **str** | Currency code (e.g., &#39;usd&#39;, &#39;eur&#39;) | [optional] 
**interval** | [**IntervalEnum**](IntervalEnum.md) | Billing interval  * &#x60;month&#x60; - Monthly * &#x60;year&#x60; - Yearly * &#x60;one_time&#x60; - One Time | [optional] 
**is_active** | **bool** | Whether this price is currently available for purchase | [optional] 
**features** | **object** | List of features included in this tier | [optional] 
**sort_order** | **int** | Display order for this price tier | [optional] 

## Example

```python
from iblai.models.item_price_create import ItemPriceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPriceCreate from a JSON string
item_price_create_instance = ItemPriceCreate.from_json(json)
# print the JSON string representation of the object
print(ItemPriceCreate.to_json())

# convert the object into a dict
item_price_create_dict = item_price_create_instance.to_dict()
# create an instance of ItemPriceCreate from a dict
item_price_create_from_dict = ItemPriceCreate.from_dict(item_price_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


