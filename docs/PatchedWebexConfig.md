# PatchedWebexConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**bot** | **int** |  | [optional] [readonly] 
**webex_bot_id** | **str** | Bot id from webex | [optional] 
**bot_access_token** | **str** |  | [optional] 
**bot_username** | **str** |  | [optional] 

## Example

```python
from iblai.models.patched_webex_config import PatchedWebexConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWebexConfig from a JSON string
patched_webex_config_instance = PatchedWebexConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedWebexConfig.to_json())

# convert the object into a dict
patched_webex_config_dict = patched_webex_config_instance.to_dict()
# create an instance of PatchedWebexConfig from a dict
patched_webex_config_from_dict = PatchedWebexConfig.from_dict(patched_webex_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


