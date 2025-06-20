# PaginatedCourseGroupSuggestion

Response serializer for paginated course group suggestion list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseGroupSuggestionDetail]**](CourseGroupSuggestionDetail.md) | List of course group suggestions | 

## Example

```python
from iblai.models.paginated_course_group_suggestion import PaginatedCourseGroupSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseGroupSuggestion from a JSON string
paginated_course_group_suggestion_instance = PaginatedCourseGroupSuggestion.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseGroupSuggestion.to_json())

# convert the object into a dict
paginated_course_group_suggestion_dict = paginated_course_group_suggestion_instance.to_dict()
# create an instance of PaginatedCourseGroupSuggestion from a dict
paginated_course_group_suggestion_from_dict = PaginatedCourseGroupSuggestion.from_dict(paginated_course_group_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


