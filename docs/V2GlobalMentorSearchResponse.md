# V2GlobalMentorSearchResponse

Response serializer for V2 Global Mentor Search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** | List of mentor search results | 
**count** | **int** | Total number of results | 
**next** | **str** | URL for next page of results | [optional] 
**previous** | **str** | URL for previous page of results | [optional] 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from iblai.models.v2_global_mentor_search_response import V2GlobalMentorSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2GlobalMentorSearchResponse from a JSON string
v2_global_mentor_search_response_instance = V2GlobalMentorSearchResponse.from_json(json)
# print the JSON string representation of the object
print(V2GlobalMentorSearchResponse.to_json())

# convert the object into a dict
v2_global_mentor_search_response_dict = v2_global_mentor_search_response_instance.to_dict()
# create an instance of V2GlobalMentorSearchResponse from a dict
v2_global_mentor_search_response_from_dict = V2GlobalMentorSearchResponse.from_dict(v2_global_mentor_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


