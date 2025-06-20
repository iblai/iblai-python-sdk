# SendNotification

Request serializer for sending notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **str** |  | 

## Example

```python
from iblai.models.send_notification import SendNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SendNotification from a JSON string
send_notification_instance = SendNotification.from_json(json)
# print the JSON string representation of the object
print(SendNotification.to_json())

# convert the object into a dict
send_notification_dict = send_notification_instance.to_dict()
# create an instance of SendNotification from a dict
send_notification_from_dict = SendNotification.from_dict(send_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


