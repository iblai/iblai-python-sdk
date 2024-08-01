# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** | WP Customer ID | 
**status** | **str** | WooCommerce order status | 
**order_date** | **datetime** | WooCommerce order date | 
**coupons** | **str** | Total discount by coupons | 
**value** | **str** | Net order value | 

## Example

```python
from iblai.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


