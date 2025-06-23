# CourseGroupSuggestionCreate

Request serializer for CourseGroupSuggestionManagementView POST endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** | The platform for the group suggestion | 
**course_id** | **str** | The course ID to suggest | 
**group_id** | **int** | The group to suggest the course to | 
**accepted** | **bool** | Whether the suggestion is accepted | [optional] [default to False]
**visible** | **bool** | Whether the suggestion is visible | [optional] [default to True]
**metadata** | **Dict[str, object]** | Additional suggestion metadata | [optional] 
**suggested_by** | **str** | The user who suggested the group | [optional] 
**direct** | **bool** | Whether the suggestion is direct | [optional] [default to True]
**department_mode** | **bool** | Flag to ensure department admins can call the API | [optional] [default to False]

## Example

```python
from iblai.models.course_group_suggestion_create import CourseGroupSuggestionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGroupSuggestionCreate from a JSON string
course_group_suggestion_create_instance = CourseGroupSuggestionCreate.from_json(json)
# print the JSON string representation of the object
print(CourseGroupSuggestionCreate.to_json())

# convert the object into a dict
course_group_suggestion_create_dict = course_group_suggestion_create_instance.to_dict()
# create an instance of CourseGroupSuggestionCreate from a dict
course_group_suggestion_create_from_dict = CourseGroupSuggestionCreate.from_dict(course_group_suggestion_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


