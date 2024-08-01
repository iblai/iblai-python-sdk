# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product Name | 
**type** | **str** | Product type (Course or Program) | 
**slug** | **str** | Product slug | 
**created_on** | **datetime** | DateTime product was created | 
**price** | **str** | Product cost | 

## Example

```python
from iblai.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


