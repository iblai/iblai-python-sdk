# UserCatalogItemMemoryView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**student** | **str** | edX username | [optional] 
**platform** | **str** | The platform key | [optional] 
**catalog_item** | **str** |  | [optional] 
**lessons** | **object** |  | [optional] 
**next_steps** | **object** |  | [optional] 

## Example

```python
from iblai.models.user_catalog_item_memory_view import UserCatalogItemMemoryView

# TODO update the JSON string below
json = "{}"
# create an instance of UserCatalogItemMemoryView from a JSON string
user_catalog_item_memory_view_instance = UserCatalogItemMemoryView.from_json(json)
# print the JSON string representation of the object
print(UserCatalogItemMemoryView.to_json())

# convert the object into a dict
user_catalog_item_memory_view_dict = user_catalog_item_memory_view_instance.to_dict()
# create an instance of UserCatalogItemMemoryView from a dict
user_catalog_item_memory_view_from_dict = UserCatalogItemMemoryView.from_dict(user_catalog_item_memory_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


