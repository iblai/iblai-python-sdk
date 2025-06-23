# PlatformList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The platform key | 
**name** | **str** | The name of the platform | [optional] 
**org** | **str** | The associated edX org code | [optional] 
**lms_url** | **str** | The LMS URL for the platform | [optional] 
**cms_url** | **str** | The CMS URL for the platform | [optional] 
**portal_url** | **str** | The portal URL for the platform | [optional] 
**status** | [**PlatformListStatusEnum**](PlatformListStatusEnum.md) |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from iblai.models.platform_list import PlatformList

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformList from a JSON string
platform_list_instance = PlatformList.from_json(json)
# print the JSON string representation of the object
print(PlatformList.to_json())

# convert the object into a dict
platform_list_dict = platform_list_instance.to_dict()
# create an instance of PlatformList from a dict
platform_list_from_dict = PlatformList.from_dict(platform_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


