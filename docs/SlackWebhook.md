# SlackWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**event** | **Dict[str, object]** |  | 
**command** | **str** |  | 
**response_url** | **str** |  | 

## Example

```python
from iblai.models.slack_webhook import SlackWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SlackWebhook from a JSON string
slack_webhook_instance = SlackWebhook.from_json(json)
# print the JSON string representation of the object
print(SlackWebhook.to_json())

# convert the object into a dict
slack_webhook_dict = slack_webhook_instance.to_dict()
# create an instance of SlackWebhook from a dict
slack_webhook_from_dict = SlackWebhook.from_dict(slack_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


