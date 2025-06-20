# StripeLocalProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**price** | **str** |  | [readonly] 
**stripe_product_id** | **str** |  | [optional] 
**sku** | **str** |  | 
**platform** | **str** |  | [readonly] 

## Example

```python
from iblai.models.stripe_local_product import StripeLocalProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StripeLocalProduct from a JSON string
stripe_local_product_instance = StripeLocalProduct.from_json(json)
# print the JSON string representation of the object
print(StripeLocalProduct.to_json())

# convert the object into a dict
stripe_local_product_dict = stripe_local_product_instance.to_dict()
# create an instance of StripeLocalProduct from a dict
stripe_local_product_from_dict = StripeLocalProduct.from_dict(stripe_local_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


