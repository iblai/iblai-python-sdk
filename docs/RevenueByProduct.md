# RevenueByProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_table** | [**List[ProductTable]**](ProductTable.md) |  | [optional] 
**summary** | [**Summary**](Summary.md) |  | [optional] 

## Example

```python
from iblai.models.revenue_by_product import RevenueByProduct

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueByProduct from a JSON string
revenue_by_product_instance = RevenueByProduct.from_json(json)
# print the JSON string representation of the object
print(RevenueByProduct.to_json())

# convert the object into a dict
revenue_by_product_dict = revenue_by_product_instance.to_dict()
# create an instance of RevenueByProduct from a dict
revenue_by_product_from_dict = RevenueByProduct.from_dict(revenue_by_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


