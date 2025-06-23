# CourseSuggestionDetail

Response serializer for course suggestion details

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
**course_id** | **str** | The course ID being suggested | 
**course_name** | **str** | The name of the course being suggested | 

## Example

```python
from iblai.models.course_suggestion_detail import CourseSuggestionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseSuggestionDetail from a JSON string
course_suggestion_detail_instance = CourseSuggestionDetail.from_json(json)
# print the JSON string representation of the object
print(CourseSuggestionDetail.to_json())

# convert the object into a dict
course_suggestion_detail_dict = course_suggestion_detail_instance.to_dict()
# create an instance of CourseSuggestionDetail from a dict
course_suggestion_detail_from_dict = CourseSuggestionDetail.from_dict(course_suggestion_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


