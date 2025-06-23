# UserPlatformManagementListViewGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 
**results** | **List[Dict[str, object]]** |  | 

## Example

```python
from iblai.models.user_platform_management_list_view_get_response import UserPlatformManagementListViewGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlatformManagementListViewGetResponse from a JSON string
user_platform_management_list_view_get_response_instance = UserPlatformManagementListViewGetResponse.from_json(json)
# print the JSON string representation of the object
print(UserPlatformManagementListViewGetResponse.to_json())

# convert the object into a dict
user_platform_management_list_view_get_response_dict = user_platform_management_list_view_get_response_instance.to_dict()
# create an instance of UserPlatformManagementListViewGetResponse from a dict
user_platform_management_list_view_get_response_from_dict = UserPlatformManagementListViewGetResponse.from_dict(user_platform_management_list_view_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


