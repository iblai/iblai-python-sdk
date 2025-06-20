# PathwaySuggestionBulkCreate

Request serializer for PathwaySuggestionBulkManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestions | 
**platform_org** | **str** | The organization identifier for the platform | [optional] 
**suggestion_data** | **List[Dict[str, object]]** | List of suggestion data objects, each containing pathway_id, user_id, etc. | 
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.pathway_suggestion_bulk_create import PathwaySuggestionBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaySuggestionBulkCreate from a JSON string
pathway_suggestion_bulk_create_instance = PathwaySuggestionBulkCreate.from_json(json)
# print the JSON string representation of the object
print(PathwaySuggestionBulkCreate.to_json())

# convert the object into a dict
pathway_suggestion_bulk_create_dict = pathway_suggestion_bulk_create_instance.to_dict()
# create an instance of PathwaySuggestionBulkCreate from a dict
pathway_suggestion_bulk_create_from_dict = PathwaySuggestionBulkCreate.from_dict(pathway_suggestion_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


