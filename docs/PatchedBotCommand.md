# PatchedBotCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**command** | **str** |  | [optional] 
**mentor** | **int** |  | [optional] 
**bot** | **int** |  | [optional] 

## Example

```python
from iblai.models.patched_bot_command import PatchedBotCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBotCommand from a JSON string
patched_bot_command_instance = PatchedBotCommand.from_json(json)
# print the JSON string representation of the object
print(PatchedBotCommand.to_json())

# convert the object into a dict
patched_bot_command_dict = patched_bot_command_instance.to_dict()
# create an instance of PatchedBotCommand from a dict
patched_bot_command_from_dict = PatchedBotCommand.from_dict(patched_bot_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


