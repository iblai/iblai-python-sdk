# PatchedBotCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**app_token** | **str** |  | [optional] 
**verification_token** | **str** |  | [optional] 
**provider** | [**ProviderBd1Enum**](ProviderBd1Enum.md) |  | [optional] 
**config** | **object** |  | [optional] 
**webhook_url** | **str** |  | [optional] [readonly] 

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


