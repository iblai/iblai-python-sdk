# PathwaySuggestionDetail

Response serializer for pathway suggestion details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the suggestion | 
**user_id** | **int** | The ID of the user receiving the suggestion | 
**username** | **str** | The username of the user receiving the suggestion | 
**name** | **str** | The full name of the user receiving the suggestion | 
**platform_key** | **str** | The platform key associated with the suggestion | 
**accepted** | **bool** | Whether the suggestion has been accepted by the user | 
**visible** | **bool** | Whether the suggestion is visible to the user | 
**created** | **datetime** | When the suggestion was created | 
**modified** | **datetime** | When the suggestion was last modified | 
**metadata** | **Dict[str, object]** | Additional metadata for the suggestion | 
**pathway_id** | **str** | The pathway ID being suggested | 
**pathway_uuid** | **str** | The UUID of the pathway being suggested | 
**pathway_name** | **str** | The name of the pathway being suggested | 
**pathway_platform_key** | **str** | The platform key associated with the pathway | 

## Example

```python
from iblai.models.pathway_suggestion_detail import PathwaySuggestionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaySuggestionDetail from a JSON string
pathway_suggestion_detail_instance = PathwaySuggestionDetail.from_json(json)
# print the JSON string representation of the object
print(PathwaySuggestionDetail.to_json())

# convert the object into a dict
pathway_suggestion_detail_dict = pathway_suggestion_detail_instance.to_dict()
# create an instance of PathwaySuggestionDetail from a dict
pathway_suggestion_detail_from_dict = PathwaySuggestionDetail.from_dict(pathway_suggestion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


