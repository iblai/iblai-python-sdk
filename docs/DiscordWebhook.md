# DiscordWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**type** | **str** |  | 
**token** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from iblai.models.discord_webhook import DiscordWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordWebhook from a JSON string
discord_webhook_instance = DiscordWebhook.from_json(json)
# print the JSON string representation of the object
print(DiscordWebhook.to_json())

# convert the object into a dict
discord_webhook_dict = discord_webhook_instance.to_dict()
# create an instance of DiscordWebhook from a dict
discord_webhook_from_dict = DiscordWebhook.from_dict(discord_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


