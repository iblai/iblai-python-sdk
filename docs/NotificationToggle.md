# NotificationToggle

Serializer for toggling notification preference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_notification** | **bool** |  | 

## Example

```python
from iblai.models.notification_toggle import NotificationToggle

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationToggle from a JSON string
notification_toggle_instance = NotificationToggle.from_json(json)
# print the JSON string representation of the object
print(NotificationToggle.to_json())

# convert the object into a dict
notification_toggle_dict = notification_toggle_instance.to_dict()
# create an instance of NotificationToggle from a dict
notification_toggle_from_dict = NotificationToggle.from_dict(notification_toggle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


