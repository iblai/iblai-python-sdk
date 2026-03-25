# PaginatedItemPaywallConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ItemPaywallConfig]**](ItemPaywallConfig.md) |  | 

## Example

```python
from iblai.models.paginated_item_paywall_config_list import PaginatedItemPaywallConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedItemPaywallConfigList from a JSON string
paginated_item_paywall_config_list_instance = PaginatedItemPaywallConfigList.from_json(json)
# print the JSON string representation of the object
print(PaginatedItemPaywallConfigList.to_json())

# convert the object into a dict
paginated_item_paywall_config_list_dict = paginated_item_paywall_config_list_instance.to_dict()
# create an instance of PaginatedItemPaywallConfigList from a dict
paginated_item_paywall_config_list_from_dict = PaginatedItemPaywallConfigList.from_dict(paginated_item_paywall_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


