# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**id** | **int** |  | [readonly] 
**name** | **str** | The display name of the resource. | [readonly] 
**url** | **str** | Resource URL. | [readonly] 
**resource_type** | **str** | Resource type. | [readonly] 
**data** | **object** | Metadata | [readonly] 
**image** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


