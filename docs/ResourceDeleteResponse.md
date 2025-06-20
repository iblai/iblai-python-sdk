# ResourceDeleteResponse

Serializer for resource deletion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of resources deleted | 
**type** | **Dict[str, object]** | Types of objects deleted | 

## Example

```python
from iblai.models.resource_delete_response import ResourceDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDeleteResponse from a JSON string
resource_delete_response_instance = ResourceDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceDeleteResponse.to_json())

# convert the object into a dict
resource_delete_response_dict = resource_delete_response_instance.to_dict()
# create an instance of ResourceDeleteResponse from a dict
resource_delete_response_from_dict = ResourceDeleteResponse.from_dict(resource_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


