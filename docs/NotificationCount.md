# NotificationCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status3daEnum**](Status3daEnum.md) | Filter count by notification status  * &#x60;READ&#x60; - Read * &#x60;UNREAD&#x60; - Unread * &#x60;CANCELLED&#x60; - Cancelled | [optional] 
**channel** | **str** | Filter count by delivery channel | [optional] 

## Example

```python
from iblai.models.notification_count import NotificationCount

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCount from a JSON string
notification_count_instance = NotificationCount.from_json(json)
# print the JSON string representation of the object
print(NotificationCount.to_json())

# convert the object into a dict
notification_count_dict = notification_count_instance.to_dict()
# create an instance of NotificationCount from a dict
notification_count_from_dict = NotificationCount.from_dict(notification_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


