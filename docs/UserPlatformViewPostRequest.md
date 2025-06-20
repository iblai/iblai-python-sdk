# UserPlatformViewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**platform_key** | **str** |  | 
**added_on** | **datetime** |  | [optional] 
**expired_on** | **datetime** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_platform_view_post_request import UserPlatformViewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlatformViewPostRequest from a JSON string
user_platform_view_post_request_instance = UserPlatformViewPostRequest.from_json(json)
# print the JSON string representation of the object
print(UserPlatformViewPostRequest.to_json())

# convert the object into a dict
user_platform_view_post_request_dict = user_platform_view_post_request_instance.to_dict()
# create an instance of UserPlatformViewPostRequest from a dict
user_platform_view_post_request_from_dict = UserPlatformViewPostRequest.from_dict(user_platform_view_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


