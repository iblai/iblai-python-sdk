# CourseSuggestionBulkCreate

Request serializer for CourseSuggestionBulkManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestions | 
**suggestion_data** | **List[Dict[str, object]]** | List of suggestion data objects, each containing course_id, user_id, etc. | 
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.course_suggestion_bulk_create import CourseSuggestionBulkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSuggestionBulkCreate from a JSON string
course_suggestion_bulk_create_instance = CourseSuggestionBulkCreate.from_json(json)
# print the JSON string representation of the object
print(CourseSuggestionBulkCreate.to_json())

# convert the object into a dict
course_suggestion_bulk_create_dict = course_suggestion_bulk_create_instance.to_dict()
# create an instance of CourseSuggestionBulkCreate from a dict
course_suggestion_bulk_create_from_dict = CourseSuggestionBulkCreate.from_dict(course_suggestion_bulk_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


