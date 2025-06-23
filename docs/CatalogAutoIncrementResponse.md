# CatalogAutoIncrementResponse

Response serializer for CatalogAutoIncrementView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_number** | **int** | Current course auto-increment number | 
**item_number** | **int** | Current item auto-increment number | [optional] 
**program_number** | **int** | Current program auto-increment number | [optional] 
**org** | **str** | Platform organization | 
**key** | **str** | Platform key | 

## Example

```python
from iblai.models.catalog_auto_increment_response import CatalogAutoIncrementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAutoIncrementResponse from a JSON string
catalog_auto_increment_response_instance = CatalogAutoIncrementResponse.from_json(json)
# print the JSON string representation of the object
print(CatalogAutoIncrementResponse.to_json())

# convert the object into a dict
catalog_auto_increment_response_dict = catalog_auto_increment_response_instance.to_dict()
# create an instance of CatalogAutoIncrementResponse from a dict
catalog_auto_increment_response_from_dict = CatalogAutoIncrementResponse.from_dict(catalog_auto_increment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


