# WebexConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**bot** | **int** |  | [readonly] 
**webex_bot_id** | **str** | Bot id from webex | 
**bot_access_token** | **str** |  | 
**bot_username** | **str** |  | 

## Example

```python
from iblai.models.webex_config import WebexConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebexConfig from a JSON string
webex_config_instance = WebexConfig.from_json(json)
# print the JSON string representation of the object
print(WebexConfig.to_json())

# convert the object into a dict
webex_config_dict = webex_config_instance.to_dict()
# create an instance of WebexConfig from a dict
webex_config_from_dict = WebexConfig.from_dict(webex_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


