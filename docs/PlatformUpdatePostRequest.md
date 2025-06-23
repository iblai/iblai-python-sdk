# PlatformUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**key** | **str** |  | 
**new_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**lms_url** | **str** |  | [optional] 
**cms_url** | **str** |  | [optional] 
**portal_url** | **str** |  | [optional] 

## Example

```python
from iblai.models.platform_update_post_request import PlatformUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformUpdatePostRequest from a JSON string
platform_update_post_request_instance = PlatformUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(PlatformUpdatePostRequest.to_json())

# convert the object into a dict
platform_update_post_request_dict = platform_update_post_request_instance.to_dict()
# create an instance of PlatformUpdatePostRequest from a dict
platform_update_post_request_from_dict = PlatformUpdatePostRequest.from_dict(platform_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


