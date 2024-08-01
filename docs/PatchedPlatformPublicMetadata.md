# PatchedPlatformPublicMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [optional] [readonly] 
**platform_name** | **str** |  | [optional] [readonly] 
**metadata** | **object** | The public metadata | [optional] 
**created_on** | **datetime** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_platform_public_metadata import PatchedPlatformPublicMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlatformPublicMetadata from a JSON string
patched_platform_public_metadata_instance = PatchedPlatformPublicMetadata.from_json(json)
# print the JSON string representation of the object
print(PatchedPlatformPublicMetadata.to_json())

# convert the object into a dict
patched_platform_public_metadata_dict = patched_platform_public_metadata_instance.to_dict()
# create an instance of PatchedPlatformPublicMetadata from a dict
patched_platform_public_metadata_from_dict = PatchedPlatformPublicMetadata.from_dict(patched_platform_public_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


