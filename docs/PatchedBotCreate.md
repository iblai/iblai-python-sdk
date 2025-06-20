# PatchedBotCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**provider** | [**Provider05cEnum**](Provider05cEnum.md) |  | [optional] 
**is_configured** | **bool** |  | [optional] [readonly] 
**webhook_url** | **str** |  | [optional] [readonly] 
**discord_config** | **int** |  | [optional] [readonly] 
**webex_config** | **int** |  | [optional] [readonly] 
**whatsapp_config** | **int** |  | [optional] [readonly] 
**teams_config** | **int** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_bot_create import PatchedBotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBotCreate from a JSON string
patched_bot_create_instance = PatchedBotCreate.from_json(json)
# print the JSON string representation of the object
print(PatchedBotCreate.to_json())

# convert the object into a dict
patched_bot_create_dict = patched_bot_create_instance.to_dict()
# create an instance of PatchedBotCreate from a dict
patched_bot_create_from_dict = PatchedBotCreate.from_dict(patched_bot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


