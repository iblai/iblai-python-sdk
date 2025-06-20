# MarkAllReadRequest

Serializer for the request to mark notifications as read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_ids** | **List[str]** | Optional list of notification IDs to mark as read. If not provided, all unread notifications will be marked as read. | [optional] 

## Example

```python
from iblai.models.mark_all_read_request import MarkAllReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAllReadRequest from a JSON string
mark_all_read_request_instance = MarkAllReadRequest.from_json(json)
# print the JSON string representation of the object
print(MarkAllReadRequest.to_json())

# convert the object into a dict
mark_all_read_request_dict = mark_all_read_request_instance.to_dict()
# create an instance of MarkAllReadRequest from a dict
mark_all_read_request_from_dict = MarkAllReadRequest.from_dict(mark_all_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


