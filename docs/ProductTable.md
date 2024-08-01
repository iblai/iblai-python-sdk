# ProductTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name | 
**type** | **str** | Product Type (Course or Program) | 
**total_sales** | **float** | Gross sales for product | 
**coupons** | **float** | Total of all coupons for product | 
**net_sales** | **float** | Net sales for product | 
**orders** | **int** | Quantity of product purchased | 

## Example

```python
from iblai.models.product_table import ProductTable

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTable from a JSON string
product_table_instance = ProductTable.from_json(json)
# print the JSON string representation of the object
print(ProductTable.to_json())

# convert the object into a dict
product_table_dict = product_table_instance.to_dict()
# create an instance of ProductTable from a dict
product_table_from_dict = ProductTable.from_dict(product_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


