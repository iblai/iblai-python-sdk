# PlatformInfo

Serializer for platform information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_id** | **int** | Platform ID | 
**platform_name** | **str** | Platform name | 
**platform_key** | **str** | Platform key | 

## Example

```python
from iblai.models.platform_info import PlatformInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformInfo from a JSON string
platform_info_instance = PlatformInfo.from_json(json)
# print the JSON string representation of the object
print(PlatformInfo.to_json())

# convert the object into a dict
platform_info_dict = platform_info_instance.to_dict()
# create an instance of PlatformInfo from a dict
platform_info_from_dict = PlatformInfo.from_dict(platform_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


