# BotCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**provider** | [**Provider05cEnum**](Provider05cEnum.md) |  | 
**is_configured** | **bool** |  | [readonly] 
**webhook_url** | **str** |  | [readonly] 
**discord_config** | **int** |  | [readonly] 
**webex_config** | **int** |  | [readonly] 
**whatsapp_config** | **int** |  | [readonly] 
**teams_config** | **int** |  | [readonly] 

## Example

```python
from iblai.models.bot_create import BotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BotCreate from a JSON string
bot_create_instance = BotCreate.from_json(json)
# print the JSON string representation of the object
print(BotCreate.to_json())

# convert the object into a dict
bot_create_dict = bot_create_instance.to_dict()
# create an instance of BotCreate from a dict
bot_create_from_dict = BotCreate.from_dict(bot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


