# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**username** | **str** |  | 
**title** | **str** |  | [readonly] 
**body** | **str** |  | [readonly] 
**status** | [**MessageStatus**](MessageStatus.md) |  | [optional] 
**channel** | **int** |  | [optional] 
**context** | **object** |  | [optional] 
**short_message** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from iblai.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


