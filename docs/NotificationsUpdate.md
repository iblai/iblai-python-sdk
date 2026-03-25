# NotificationsUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | Comma-separated list of notification UUIDs to update | [optional] [default to '']
**status** | [**Status3daEnum**](Status3daEnum.md) | New status to set (e.g. read, unread)  * &#x60;READ&#x60; - Read * &#x60;UNREAD&#x60; - Unread * &#x60;CANCELLED&#x60; - Cancelled | 

## Example

```python
from iblai.models.notifications_update import NotificationsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsUpdate from a JSON string
notifications_update_instance = NotificationsUpdate.from_json(json)
# print the JSON string representation of the object
print(NotificationsUpdate.to_json())

# convert the object into a dict
notifications_update_dict = notifications_update_instance.to_dict()
# create an instance of NotificationsUpdate from a dict
notifications_update_from_dict = NotificationsUpdate.from_dict(notifications_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


