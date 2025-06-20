# DiscordConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**bot** | **int** |  | [readonly] 
**client_id** | **str** |  | 
**token** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from iblai.models.discord_config import DiscordConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordConfig from a JSON string
discord_config_instance = DiscordConfig.from_json(json)
# print the JSON string representation of the object
print(DiscordConfig.to_json())

# convert the object into a dict
discord_config_dict = discord_config_instance.to_dict()
# create an instance of DiscordConfig from a dict
discord_config_from_dict = DiscordConfig.from_dict(discord_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


