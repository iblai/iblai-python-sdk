# PublicItemPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | [**ItemType3e2Enum**](ItemType3e2Enum.md) |  | 
**item_id** | **str** |  | 
**item_name** | **str** |  | 
**is_paywalled** | **bool** |  | 
**allow_free_tier** | **bool** |  | 
**trial_period_days** | **int** |  | 
**prices** | [**List[ItemPrice]**](ItemPrice.md) |  | 

## Example

```python
from iblai.models.public_item_pricing import PublicItemPricing

# TODO update the JSON string below
json = "{}"
# create an instance of PublicItemPricing from a JSON string
public_item_pricing_instance = PublicItemPricing.from_json(json)
# print the JSON string representation of the object
print(PublicItemPricing.to_json())

# convert the object into a dict
public_item_pricing_dict = public_item_pricing_instance.to_dict()
# create an instance of PublicItemPricing from a dict
public_item_pricing_from_dict = PublicItemPricing.from_dict(public_item_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


