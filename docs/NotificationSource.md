# NotificationSource

Request serializer for source validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationSourceTypeEnum**](NotificationSourceTypeEnum.md) |  | 
**data** | **object** |  | 

## Example

```python
from iblai.models.notification_source import NotificationSource

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSource from a JSON string
notification_source_instance = NotificationSource.from_json(json)
# print the JSON string representation of the object
print(NotificationSource.to_json())

# convert the object into a dict
notification_source_dict = notification_source_instance.to_dict()
# create an instance of NotificationSource from a dict
notification_source_from_dict = NotificationSource.from_dict(notification_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


