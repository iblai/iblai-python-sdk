# ResourceScrappedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**status** | [**ResourceScrappedDataStatus**](ResourceScrappedDataStatus.md) |  | [optional] 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 
**resource** | **int** |  | 
**content** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**extra_data** | **object** |  | [optional] 

## Example

```python
from iblai.models.resource_scrapped_data import ResourceScrappedData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceScrappedData from a JSON string
resource_scrapped_data_instance = ResourceScrappedData.from_json(json)
# print the JSON string representation of the object
print(ResourceScrappedData.to_json())

# convert the object into a dict
resource_scrapped_data_dict = resource_scrapped_data_instance.to_dict()
# create an instance of ResourceScrappedData from a dict
resource_scrapped_data_from_dict = ResourceScrappedData.from_dict(resource_scrapped_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


