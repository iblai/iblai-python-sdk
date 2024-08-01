# WebexWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 
**resource** | **str** |  | 

## Example

```python
from iblai.models.webex_webhook import WebexWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of WebexWebhook from a JSON string
webex_webhook_instance = WebexWebhook.from_json(json)
# print the JSON string representation of the object
print(WebexWebhook.to_json())

# convert the object into a dict
webex_webhook_dict = webex_webhook_instance.to_dict()
# create an instance of WebexWebhook from a dict
webex_webhook_from_dict = WebexWebhook.from_dict(webex_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


