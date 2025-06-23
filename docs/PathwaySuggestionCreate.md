# PathwaySuggestionCreate

Request serializer for PathwaySuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestion | 
**pathway_id** | **str** | The pathway ID to suggest | 
**pathway_uuid** | **str** | The pathway UUID to suggest | 
**user_id** | **str** | The user to suggest the pathway to | 
**username** | **str** | The username of the user to suggest the pathway to | [optional] 
**email** | **str** | The email of the user to suggest the pathway to | [optional] 
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 
**suggested_by** | **str** | The user who suggested the pathway | [optional] 
**direct** | **bool** | Whether the suggestion is direct | [optional] [default to True]
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.pathway_suggestion_create import PathwaySuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaySuggestionCreate from a JSON string
pathway_suggestion_create_instance = PathwaySuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(PathwaySuggestionCreate.to_json())

# convert the object into a dict
pathway_suggestion_create_dict = pathway_suggestion_create_instance.to_dict()
# create an instance of PathwaySuggestionCreate from a dict
pathway_suggestion_create_from_dict = PathwaySuggestionCreate.from_dict(pathway_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


