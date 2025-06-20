# RecommendedCoursesResponse

Response serializer for RecommendedCoursesView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[Dict[str, object]]** | List of content items matching the search criteria | 
**count** | **int** | Total number of items matching the search criteria | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 
**facets** | **Dict[str, object]** | Facet information for filtering | [optional] 

## Example

```python
from iblai.models.recommended_courses_response import RecommendedCoursesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendedCoursesResponse from a JSON string
recommended_courses_response_instance = RecommendedCoursesResponse.from_json(json)
# print the JSON string representation of the object
print(RecommendedCoursesResponse.to_json())

# convert the object into a dict
recommended_courses_response_dict = recommended_courses_response_instance.to_dict()
# create an instance of RecommendedCoursesResponse from a dict
recommended_courses_response_from_dict = RecommendedCoursesResponse.from_dict(recommended_courses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


