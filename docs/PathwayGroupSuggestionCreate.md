# PathwayGroupSuggestionCreate

Request serializer for PathwayGroupSuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the group suggestion | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**pathway_uuid** | **str** | The pathway UUID to suggest | 
**group_id** | **int** | The group to suggest the pathway to | 
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 
**suggested_by** | **str** | The user who suggested the group | [optional] 
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.pathway_group_suggestion_create import PathwayGroupSuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PathwayGroupSuggestionCreate from a JSON string
pathway_group_suggestion_create_instance = PathwayGroupSuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(PathwayGroupSuggestionCreate.to_json())

# convert the object into a dict
pathway_group_suggestion_create_dict = pathway_group_suggestion_create_instance.to_dict()
# create an instance of PathwayGroupSuggestionCreate from a dict
pathway_group_suggestion_create_from_dict = PathwayGroupSuggestionCreate.from_dict(pathway_group_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


