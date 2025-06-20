# PathwayCreateUpdateRequest

Serializer for pathway creation/update request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathway_id** | **str** | Pathway ID | [optional] 
**pathway_uuid** | **str** | Pathway UUID | [optional] 
**user_id** | **int** | User ID of the pathway owner | 
**username** | **str** | Username of the pathway owner | [optional] 
**name** | **str** | Pathway name | 
**slug** | **str** | Pathway slug | [optional] 
**visible** | **bool** | Whether the pathway is visible | [optional] [default to True]
**platform_key** | **str** | Platform key | [optional] 
**path** | **List[Dict[str, object]]** | List of items in the pathway with item_id and optional position | 
**data** | **object** | Additional pathway data | [optional] 

## Example

```python
from iblai.models.pathway_create_update_request import PathwayCreateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayCreateUpdateRequest from a JSON string
pathway_create_update_request_instance = PathwayCreateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PathwayCreateUpdateRequest.to_json())

# convert the object into a dict
pathway_create_update_request_dict = pathway_create_update_request_instance.to_dict()
# create an instance of PathwayCreateUpdateRequest from a dict
pathway_create_update_request_from_dict = PathwayCreateUpdateRequest.from_dict(pathway_create_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


