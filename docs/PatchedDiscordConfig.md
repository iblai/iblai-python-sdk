# PatchedDiscordConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**bot** | **int** |  | [optional] [readonly] 
**client_id** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from iblai.models.patched_discord_config import PatchedDiscordConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDiscordConfig from a JSON string
patched_discord_config_instance = PatchedDiscordConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedDiscordConfig.to_json())

# convert the object into a dict
patched_discord_config_dict = patched_discord_config_instance.to_dict()
# create an instance of PatchedDiscordConfig from a dict
patched_discord_config_from_dict = PatchedDiscordConfig.from_dict(patched_discord_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


