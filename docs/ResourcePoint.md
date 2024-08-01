# ResourcePoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the resource. | [optional] 
**points** | **int** |  | [readonly] 

## Example

```python
from iblai.models.resource_point import ResourcePoint

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoint from a JSON string
resource_point_instance = ResourcePoint.from_json(json)
# print the JSON string representation of the object
print(ResourcePoint.to_json())

# convert the object into a dict
resource_point_dict = resource_point_instance.to_dict()
# create an instance of ResourcePoint from a dict
resource_point_from_dict = ResourcePoint.from_dict(resource_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


