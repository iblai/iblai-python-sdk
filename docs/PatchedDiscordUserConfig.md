# PatchedDiscordUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**user** | **int** | edX user ID | [optional] [readonly] 
**discord_user_id** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_discord_user_config import PatchedDiscordUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDiscordUserConfig from a JSON string
patched_discord_user_config_instance = PatchedDiscordUserConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedDiscordUserConfig.to_json())

# convert the object into a dict
patched_discord_user_config_dict = patched_discord_user_config_instance.to_dict()
# create an instance of PatchedDiscordUserConfig from a dict
patched_discord_user_config_from_dict = PatchedDiscordUserConfig.from_dict(patched_discord_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


