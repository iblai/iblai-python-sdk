# MentorSearchResponse

Response serializer for MentorSearchView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Mentor]**](Mentor.md) | List of mentors matching the search criteria | 
**count** | **int** | Total number of mentors matching the search criteria | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 
**facets** | [**Dict[str, MentorFacet]**](MentorFacet.md) | Facet information for filtering | [optional] 

## Example

```python
from iblai.models.mentor_search_response import MentorSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSearchResponse from a JSON string
mentor_search_response_instance = MentorSearchResponse.from_json(json)
# print the JSON string representation of the object
print(MentorSearchResponse.to_json())

# convert the object into a dict
mentor_search_response_dict = mentor_search_response_instance.to_dict()
# create an instance of MentorSearchResponse from a dict
mentor_search_response_from_dict = MentorSearchResponse.from_dict(mentor_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


