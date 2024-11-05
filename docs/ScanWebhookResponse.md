# ScanWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from iblai.models.scan_webhook_response import ScanWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanWebhookResponse from a JSON string
scan_webhook_response_instance = ScanWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(ScanWebhookResponse.to_json())

# convert the object into a dict
scan_webhook_response_dict = scan_webhook_response_instance.to_dict()
# create an instance of ScanWebhookResponse from a dict
scan_webhook_response_from_dict = ScanWebhookResponse.from_dict(scan_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


