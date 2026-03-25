# PatchedPlatformPublicImageAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**category** | **str** | Category of the asset | [optional] 
**image** | **str** |  | [optional] 
**url** | **str** |  | [optional] [readonly] 
**created_on** | **datetime** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_platform_public_image_asset import PatchedPlatformPublicImageAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlatformPublicImageAsset from a JSON string
patched_platform_public_image_asset_instance = PatchedPlatformPublicImageAsset.from_json(json)
# print the JSON string representation of the object
print(PatchedPlatformPublicImageAsset.to_json())

# convert the object into a dict
patched_platform_public_image_asset_dict = patched_platform_public_image_asset_instance.to_dict()
# create an instance of PatchedPlatformPublicImageAsset from a dict
patched_platform_public_image_asset_from_dict = PatchedPlatformPublicImageAsset.from_dict(patched_platform_public_image_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


