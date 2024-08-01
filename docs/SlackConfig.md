# SlackConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**slack_team_domain** | **str** | Team Domain in the stated slack workspace. This is also the workspace name. | 
**slack_username** | **str** | Username in the stated slack workspace | 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.slack_config import SlackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfig from a JSON string
slack_config_instance = SlackConfig.from_json(json)
# print the JSON string representation of the object
print(SlackConfig.to_json())

# convert the object into a dict
slack_config_dict = slack_config_instance.to_dict()
# create an instance of SlackConfig from a dict
slack_config_from_dict = SlackConfig.from_dict(slack_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


