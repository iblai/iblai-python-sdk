# TeamsWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**channel_data** | **Dict[str, object]** |  | [optional] 
**entities** | **List[object]** |  | [optional] 
**text** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**text_format** | **str** |  | [optional] 
**recipient** | **Dict[str, object]** |  | [optional] 
**conversation** | **Dict[str, object]** |  | [optional] 
**from_** | **Dict[str, object]** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**service_url** | **str** |  | [optional] 
**local_timezone** | **str** |  | [optional] 
**local_timestamp** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from iblai.models.teams_webhook import TeamsWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsWebhook from a JSON string
teams_webhook_instance = TeamsWebhook.from_json(json)
# print the JSON string representation of the object
print(TeamsWebhook.to_json())

# convert the object into a dict
teams_webhook_dict = teams_webhook_instance.to_dict()
# create an instance of TeamsWebhook from a dict
teams_webhook_from_dict = TeamsWebhook.from_dict(teams_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


