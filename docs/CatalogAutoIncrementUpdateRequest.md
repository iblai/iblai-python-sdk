# CatalogAutoIncrementUpdateRequest

Serializer for auto increment update request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Platform key identifier | [optional] 
**org** | **str** | Platform organization identifier | [optional] 
**number_type** | **str** | Type of number requested (e.g., course, program, pathway) | 

## Example

```python
from iblai.models.catalog_auto_increment_update_request import CatalogAutoIncrementUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAutoIncrementUpdateRequest from a JSON string
catalog_auto_increment_update_request_instance = CatalogAutoIncrementUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CatalogAutoIncrementUpdateRequest.to_json())

# convert the object into a dict
catalog_auto_increment_update_request_dict = catalog_auto_increment_update_request_instance.to_dict()
# create an instance of CatalogAutoIncrementUpdateRequest from a dict
catalog_auto_increment_update_request_from_dict = CatalogAutoIncrementUpdateRequest.from_dict(catalog_auto_increment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


