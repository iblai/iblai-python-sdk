# ResourceCreateUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resource ID for updates | [optional] 
**user_id** | **int** | User ID of the resource owner | [optional] 
**username** | **str** | Username of the resource owner | [optional] 
**resource_type** | **str** | Type of resource (e.g., video, document) | 
**url** | **str** | URL of the resource | 
**name** | **str** | Name of the resource | 
**description** | **str** | Description of the resource | [optional] 
**skills** | **List[str]** | List of skill names associated with the resource | [optional] 
**image** | **str** | Image file | [optional] 
**data** | **object** | Additional metadata for the resource | [optional] 

## Example

```python
from iblai.models.resource_create_update import ResourceCreateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreateUpdate from a JSON string
resource_create_update_instance = ResourceCreateUpdate.from_json(json)
# print the JSON string representation of the object
print(ResourceCreateUpdate.to_json())

# convert the object into a dict
resource_create_update_dict = resource_create_update_instance.to_dict()
# create an instance of ResourceCreateUpdate from a dict
resource_create_update_from_dict = ResourceCreateUpdate.from_dict(resource_create_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


