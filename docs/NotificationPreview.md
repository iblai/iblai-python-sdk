# NotificationPreview

Request serializer for notification preview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | Use a predefined template in the system | [optional] 
**template_data** | [**NotificationTemplateData**](NotificationTemplateData.md) | Specify this to send a new custom message without using a predefined template | [optional] 
**channels** | **List[int]** | Specify the channel ids to send notifications to. | 
**sources** | [**List[NotificationSource]**](NotificationSource.md) | Specify the sources to send notifications to | 
**context** | **Dict[str, object]** | Specify the context that would be available in the message text | [optional] 
**process_on** | **datetime** | (ISO datetime) Specify the date and time of processing this notification. Note, notifications are sent hourly and only scheduled messages prior to the beginning of the hour would be sent | [optional] 

## Example

```python
from iblai.models.notification_preview import NotificationPreview

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreview from a JSON string
notification_preview_instance = NotificationPreview.from_json(json)
# print the JSON string representation of the object
print(NotificationPreview.to_json())

# convert the object into a dict
notification_preview_dict = notification_preview_instance.to_dict()
# create an instance of NotificationPreview from a dict
notification_preview_from_dict = NotificationPreview.from_dict(notification_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


