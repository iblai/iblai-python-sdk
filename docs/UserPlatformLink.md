# UserPlatformLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**username** | **str** |  | 
**email** | **str** |  | 
**user_active** | **bool** |  | 
**key** | **str** |  | 
**org** | **str** |  | 
**lms_url** | **str** |  | 
**cms_url** | **str** |  | 
**portal_url** | **str** |  | 
**is_admin** | **bool** |  | [optional] 
**is_staff** | **bool** |  | [optional] 
**added_on** | **datetime** |  | [optional] 
**expired_on** | **datetime** |  | [optional] 
**public** | **str** |  | [readonly] 
**active** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_platform_link import UserPlatformLink

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlatformLink from a JSON string
user_platform_link_instance = UserPlatformLink.from_json(json)
# print the JSON string representation of the object
print(UserPlatformLink.to_json())

# convert the object into a dict
user_platform_link_dict = user_platform_link_instance.to_dict()
# create an instance of UserPlatformLink from a dict
user_platform_link_from_dict = UserPlatformLink.from_dict(user_platform_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


