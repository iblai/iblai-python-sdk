# PathwayCompletionResponse

Response serializer for PathwayCompletionQueryView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of items in the pathway | 
**completion_percentage** | **float** | Overall completion percentage for the pathway (0.0 to 1.0) | 

## Example

```python
from iblai.models.pathway_completion_response import PathwayCompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayCompletionResponse from a JSON string
pathway_completion_response_instance = PathwayCompletionResponse.from_json(json)
# print the JSON string representation of the object
print(PathwayCompletionResponse.to_json())

# convert the object into a dict
pathway_completion_response_dict = pathway_completion_response_instance.to_dict()
# create an instance of PathwayCompletionResponse from a dict
pathway_completion_response_from_dict = PathwayCompletionResponse.from_dict(pathway_completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


