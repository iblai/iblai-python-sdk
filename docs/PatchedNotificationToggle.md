# PatchedNotificationToggle

Serializer for toggling notification preference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_notification** | **bool** | True to enable, False to disable this notification type for the platform | [optional] 

## Example

```python
from iblai.models.patched_notification_toggle import PatchedNotificationToggle

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationToggle from a JSON string
patched_notification_toggle_instance = PatchedNotificationToggle.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationToggle.to_json())

# convert the object into a dict
patched_notification_toggle_dict = patched_notification_toggle_instance.to_dict()
# create an instance of PatchedNotificationToggle from a dict
patched_notification_toggle_from_dict = PatchedNotificationToggle.from_dict(patched_notification_toggle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


