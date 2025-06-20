# TeamsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**bot** | **int** |  | [readonly] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**verification_token** | **str** |  | [optional] 

## Example

```python
from iblai.models.teams_config import TeamsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsConfig from a JSON string
teams_config_instance = TeamsConfig.from_json(json)
# print the JSON string representation of the object
print(TeamsConfig.to_json())

# convert the object into a dict
teams_config_dict = teams_config_instance.to_dict()
# create an instance of TeamsConfig from a dict
teams_config_from_dict = TeamsConfig.from_dict(teams_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


