# PathwayDeleteResponse

Serializer for pathway deletion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of pathways deleted | 
**type** | **Dict[str, object]** | Types of objects deleted | 

## Example

```python
from iblai.models.pathway_delete_response import PathwayDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayDeleteResponse from a JSON string
pathway_delete_response_instance = PathwayDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(PathwayDeleteResponse.to_json())

# convert the object into a dict
pathway_delete_response_dict = pathway_delete_response_instance.to_dict()
# create an instance of PathwayDeleteResponse from a dict
pathway_delete_response_from_dict = PathwayDeleteResponse.from_dict(pathway_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


