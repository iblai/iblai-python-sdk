# PlatformPublicImageAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**category** | **str** | Category of the asset | 
**image** | **str** |  | 
**url** | **str** |  | [readonly] 
**created_on** | **datetime** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.platform_public_image_asset import PlatformPublicImageAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformPublicImageAsset from a JSON string
platform_public_image_asset_instance = PlatformPublicImageAsset.from_json(json)
# print the JSON string representation of the object
print(PlatformPublicImageAsset.to_json())

# convert the object into a dict
platform_public_image_asset_dict = platform_public_image_asset_instance.to_dict()
# create an instance of PlatformPublicImageAsset from a dict
platform_public_image_asset_from_dict = PlatformPublicImageAsset.from_dict(platform_public_image_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


