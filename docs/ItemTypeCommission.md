# ItemTypeCommission

Commission percentages keyed by item type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor** | **float** | Commission percentage for mentor sales | 
**course** | **float** | Commission percentage for course sales | 
**program** | **float** | Commission percentage for program sales | 

## Example

```python
from iblai.models.item_type_commission import ItemTypeCommission

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTypeCommission from a JSON string
item_type_commission_instance = ItemTypeCommission.from_json(json)
# print the JSON string representation of the object
print(ItemTypeCommission.to_json())

# convert the object into a dict
item_type_commission_dict = item_type_commission_instance.to_dict()
# create an instance of ItemTypeCommission from a dict
item_type_commission_from_dict = ItemTypeCommission.from_dict(item_type_commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


