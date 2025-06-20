# UserSearchViewGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 
**results** | **List[Dict[str, object]]** |  | 

## Example

```python
from iblai.models.user_search_view_get_response import UserSearchViewGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchViewGetResponse from a JSON string
user_search_view_get_response_instance = UserSearchViewGetResponse.from_json(json)
# print the JSON string representation of the object
print(UserSearchViewGetResponse.to_json())

# convert the object into a dict
user_search_view_get_response_dict = user_search_view_get_response_instance.to_dict()
# create an instance of UserSearchViewGetResponse from a dict
user_search_view_get_response_from_dict = UserSearchViewGetResponse.from_dict(user_search_view_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


