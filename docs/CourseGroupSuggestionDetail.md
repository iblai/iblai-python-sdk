# CourseGroupSuggestionDetail

Response serializer for course group suggestion details

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
**course_id** | **str** | The course ID being suggested | 
**course_name** | **str** | The name of the course being suggested | 
**user_count** | **int** | Number of users in the group | [optional] 

## Example

```python
from iblai.models.course_group_suggestion_detail import CourseGroupSuggestionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseGroupSuggestionDetail from a JSON string
course_group_suggestion_detail_instance = CourseGroupSuggestionDetail.from_json(json)
# print the JSON string representation of the object
print(CourseGroupSuggestionDetail.to_json())

# convert the object into a dict
course_group_suggestion_detail_dict = course_group_suggestion_detail_instance.to_dict()
# create an instance of CourseGroupSuggestionDetail from a dict
course_group_suggestion_detail_from_dict = CourseGroupSuggestionDetail.from_dict(course_group_suggestion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


