# DiscordUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**discord_user_id** | **str** |  | 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.discord_user_config import DiscordUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordUserConfig from a JSON string
discord_user_config_instance = DiscordUserConfig.from_json(json)
# print the JSON string representation of the object
print(DiscordUserConfig.to_json())

# convert the object into a dict
discord_user_config_dict = discord_user_config_instance.to_dict()
# create an instance of DiscordUserConfig from a dict
discord_user_config_from_dict = DiscordUserConfig.from_dict(discord_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


