# LauncherViewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**key** | **str** |  | 
**name** | **str** |  | [optional] 
**org** | **str** |  | [optional] 
**lms_url** | **str** |  | [optional] 
**cms_url** | **str** |  | [optional] 
**portal_url** | **str** |  | [optional] 

## Example

```python
from iblai.models.launcher_view_post_request import LauncherViewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherViewPostRequest from a JSON string
launcher_view_post_request_instance = LauncherViewPostRequest.from_json(json)
# print the JSON string representation of the object
print(LauncherViewPostRequest.to_json())

# convert the object into a dict
launcher_view_post_request_dict = launcher_view_post_request_instance.to_dict()
# create an instance of LauncherViewPostRequest from a dict
launcher_view_post_request_from_dict = LauncherViewPostRequest.from_dict(launcher_view_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


