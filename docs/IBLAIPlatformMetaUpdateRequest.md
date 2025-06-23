# IBLAIPlatformMetaUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_llm** | **str** | The LLM provider to set as active (e.g., &#39;openai&#39;, &#39;google&#39;) | [optional] 
**llms** | **List[str]** | List of LLM providers to add to available providers | [optional] 

## Example

```python
from iblai.models.iblai_platform_meta_update_request import IBLAIPlatformMetaUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBLAIPlatformMetaUpdateRequest from a JSON string
iblai_platform_meta_update_request_instance = IBLAIPlatformMetaUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(IBLAIPlatformMetaUpdateRequest.to_json())

# convert the object into a dict
iblai_platform_meta_update_request_dict = iblai_platform_meta_update_request_instance.to_dict()
# create an instance of IBLAIPlatformMetaUpdateRequest from a dict
iblai_platform_meta_update_request_from_dict = IBLAIPlatformMetaUpdateRequest.from_dict(iblai_platform_meta_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


