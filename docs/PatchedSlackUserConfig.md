# PatchedSlackUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**user** | **int** | edX user ID | [optional] [readonly] 
**slack_team_domain** | **str** | Team Domain in the stated slack workspace. This is also the workspace name. | [optional] 
**slack_username** | **str** | Username in the stated slack workspace | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_slack_user_config import PatchedSlackUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSlackUserConfig from a JSON string
patched_slack_user_config_instance = PatchedSlackUserConfig.from_json(json)
# print the JSON string representation of the object
print(PatchedSlackUserConfig.to_json())

# convert the object into a dict
patched_slack_user_config_dict = patched_slack_user_config_instance.to_dict()
# create an instance of PatchedSlackUserConfig from a dict
patched_slack_user_config_from_dict = PatchedSlackUserConfig.from_dict(patched_slack_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


