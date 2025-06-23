# UserSearchResponse

Response serializer for UsersSearchView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[Dict[str, object]]** | List of search results (can include user_resume, education, institution, etc.) | 
**count** | **int** | Total number of results | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from iblai.models.user_search_response import UserSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchResponse from a JSON string
user_search_response_instance = UserSearchResponse.from_json(json)
# print the JSON string representation of the object
print(UserSearchResponse.to_json())

# convert the object into a dict
user_search_response_dict = user_search_response_instance.to_dict()
# create an instance of UserSearchResponse from a dict
user_search_response_from_dict = UserSearchResponse.from_dict(user_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


