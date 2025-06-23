# PathwayGroupSuggestionDetail

Response serializer for pathway group suggestion details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the group suggestion | 
**group_id** | **int** | The ID of the group receiving the suggestion | 
**group_name** | **str** | The name of the group receiving the suggestion | 
**platform_key** | **str** | The platform key associated with the suggestion | 
**accepted** | **bool** | Whether the suggestion has been accepted | [optional] 
**visible** | **bool** | Whether the suggestion is visible | 
**created** | **datetime** | When the suggestion was created | 
**modified** | **datetime** | When the suggestion was last modified | 
**metadata** | **Dict[str, object]** | Additional metadata for the suggestion | 
**pathway_id** | **str** | The pathway ID being suggested | 
**pathway_uuid** | **str** | The UUID of the pathway being suggested | 
**pathway_name** | **str** | The name of the pathway being suggested | 
**pathway_platform_key** | **str** | The platform key associated with the pathway | 
**user_count** | **int** | Number of users in the group | [optional] 

## Example

```python
from iblai.models.pathway_group_suggestion_detail import PathwayGroupSuggestionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayGroupSuggestionDetail from a JSON string
pathway_group_suggestion_detail_instance = PathwayGroupSuggestionDetail.from_json(json)
# print the JSON string representation of the object
print(PathwayGroupSuggestionDetail.to_json())

# convert the object into a dict
pathway_group_suggestion_detail_dict = pathway_group_suggestion_detail_instance.to_dict()
# create an instance of PathwayGroupSuggestionDetail from a dict
pathway_group_suggestion_detail_from_dict = PathwayGroupSuggestionDetail.from_dict(pathway_group_suggestion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


