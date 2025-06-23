# Bot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**platform** | **int** |  | [readonly] 
**tenant** | **str** |  | [readonly] 
**name** | **str** |  | 
**provider** | [**Provider05cEnum**](Provider05cEnum.md) |  | 
**is_configured** | **bool** |  | [readonly] 
**slack_config** | **int** |  | 
**discord_config** | **int** |  | [readonly] 
**webex_config** | **int** |  | [readonly] 
**whatsapp_config** | **int** |  | [readonly] 
**teams_config** | **int** |  | [readonly] 
**webhook_url** | **str** |  | [readonly] 

## Example

```python
from iblai.models.bot import Bot

# TODO update the JSON string below
json = "{}"
# create an instance of Bot from a JSON string
bot_instance = Bot.from_json(json)
# print the JSON string representation of the object
print(Bot.to_json())

# convert the object into a dict
bot_dict = bot_instance.to_dict()
# create an instance of Bot from a dict
bot_from_dict = Bot.from_dict(bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


