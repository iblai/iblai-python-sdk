# PatchedNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**username** | **str** |  | [optional] 
**title** | **str** |  | [optional] [readonly] 
**body** | **str** |  | [optional] [readonly] 
**status** | [**MessageStatus**](MessageStatus.md) |  | [optional] 
**channel** | **str** |  | [optional] [readonly] 
**context** | **object** |  | [optional] 
**short_message** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_notification import PatchedNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotification from a JSON string
patched_notification_instance = PatchedNotification.from_json(json)
# print the JSON string representation of the object
print(PatchedNotification.to_json())

# convert the object into a dict
patched_notification_dict = patched_notification_instance.to_dict()
# create an instance of PatchedNotification from a dict
patched_notification_from_dict = PatchedNotification.from_dict(patched_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


