# PlatformPublicMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_key** | **str** |  | [readonly] 
**platform_name** | **str** |  | [readonly] 
**metadata** | **object** | The public metadata | [optional] 

## Example

```python
from iblai.models.platform_public_metadata import PlatformPublicMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformPublicMetadata from a JSON string
platform_public_metadata_instance = PlatformPublicMetadata.from_json(json)
# print the JSON string representation of the object
print(PlatformPublicMetadata.to_json())

# convert the object into a dict
platform_public_metadata_dict = platform_public_metadata_instance.to_dict()
# create an instance of PlatformPublicMetadata from a dict
platform_public_metadata_from_dict = PlatformPublicMetadata.from_dict(platform_public_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


