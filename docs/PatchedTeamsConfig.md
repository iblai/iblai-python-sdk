# PatchedTeamsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**bot** | **int** |  | [optional] [readonly] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**verification_token** | **str** |  | [optional] 

## Example

```python
from iblai.models.patched_teams_config import PatchedTeamsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTeamsConfig from a JSON string
patched_teams_config_instance = PatchedTeamsConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedTeamsConfig.to_json())

# convert the object into a dict
patched_teams_config_dict = patched_teams_config_instance.to_dict()
# create an instance of PatchedTeamsConfig from a dict
patched_teams_config_from_dict = PatchedTeamsConfig.from_dict(patched_teams_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


