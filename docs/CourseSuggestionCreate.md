# CourseSuggestionCreate

Request serializer for CourseSuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the suggestion | 
**course_id** | **str** | The course ID to suggest | 
**user_id** | **str** | The user to suggest the course to | 
**username** | **str** | The username of the user to suggest the course to | [optional] 
**email** | **str** | The email of the user to suggest the course to | [optional] 
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 
**suggested_by** | **str** | The user who suggested the course | [optional] 
**direct** | **bool** | Whether the suggestion is direct | [optional] [default to True]
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.course_suggestion_create import CourseSuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSuggestionCreate from a JSON string
course_suggestion_create_instance = CourseSuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(CourseSuggestionCreate.to_json())

# convert the object into a dict
course_suggestion_create_dict = course_suggestion_create_instance.to_dict()
# create an instance of CourseSuggestionCreate from a dict
course_suggestion_create_from_dict = CourseSuggestionCreate.from_dict(course_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


