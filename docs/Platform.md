# Platform

Note: Create and update operations deprecated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The platform key | 
**name** | **str** | The name of the platform | [optional] 
**org** | **str** | The associated edX org code | [optional] 
**lms_url** | **str** | The LMS URL for the platform | [optional] 
**cms_url** | **str** | The CMS URL for the platform | [optional] 
**portal_url** | **str** | The portal URL for the platform | [optional] 

## Example

```python
from iblai.models.platform import Platform

# TODO update the JSON string below
json = "{}"
# create an instance of Platform from a JSON string
platform_instance = Platform.from_json(json)
# print the JSON string representation of the object
print(Platform.to_json())

# convert the object into a dict
platform_dict = platform_instance.to_dict()
# create an instance of Platform from a dict
platform_from_dict = Platform.from_dict(platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


