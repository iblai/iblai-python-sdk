# ScanWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 
**filename** | **str** |  | 
**status** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from iblai.models.scan_webhook_request import ScanWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScanWebhookRequest from a JSON string
scan_webhook_request_instance = ScanWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ScanWebhookRequest.to_json())

# convert the object into a dict
scan_webhook_request_dict = scan_webhook_request_instance.to_dict()
# create an instance of ScanWebhookRequest from a dict
scan_webhook_request_from_dict = ScanWebhookRequest.from_dict(scan_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


