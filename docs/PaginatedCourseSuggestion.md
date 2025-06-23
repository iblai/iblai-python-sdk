# PaginatedCourseSuggestion

Response serializer for paginated course suggestion list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseSuggestionDetail]**](CourseSuggestionDetail.md) | List of course suggestions | 

## Example

```python
from iblai.models.paginated_course_suggestion import PaginatedCourseSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseSuggestion from a JSON string
paginated_course_suggestion_instance = PaginatedCourseSuggestion.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseSuggestion.to_json())

# convert the object into a dict
paginated_course_suggestion_dict = paginated_course_suggestion_instance.to_dict()
# create an instance of PaginatedCourseSuggestion from a dict
paginated_course_suggestion_from_dict = PaginatedCourseSuggestion.from_dict(paginated_course_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


