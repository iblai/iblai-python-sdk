# IBLAIPlatformMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 

## Example

```python
from iblai.models.iblai_platform_meta import IBLAIPlatformMeta

# TODO update the JSON string below
json = "{}"
# create an instance of IBLAIPlatformMeta from a JSON string
iblai_platform_meta_instance = IBLAIPlatformMeta.from_json(json)
# print the JSON string representation of the object
print(IBLAIPlatformMeta.to_json())

# convert the object into a dict
iblai_platform_meta_dict = iblai_platform_meta_instance.to_dict()
# create an instance of IBLAIPlatformMeta from a dict
iblai_platform_meta_from_dict = IBLAIPlatformMeta.from_dict(iblai_platform_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


