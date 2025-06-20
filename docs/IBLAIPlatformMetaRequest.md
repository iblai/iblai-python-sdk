# IBLAIPlatformMetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | Platform metadata including LLM configurations and active services | 

## Example

```python
from iblai.models.iblai_platform_meta_request import IBLAIPlatformMetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBLAIPlatformMetaRequest from a JSON string
iblai_platform_meta_request_instance = IBLAIPlatformMetaRequest.from_json(json)
# print the JSON string representation of the object
print(IBLAIPlatformMetaRequest.to_json())

# convert the object into a dict
iblai_platform_meta_request_dict = iblai_platform_meta_request_instance.to_dict()
# create an instance of IBLAIPlatformMetaRequest from a dict
iblai_platform_meta_request_from_dict = IBLAIPlatformMetaRequest.from_dict(iblai_platform_meta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


