# PinnedMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session id of the message to pin | 

## Example

```python
from iblai.models.pinned_message_request import PinnedMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedMessageRequest from a JSON string
pinned_message_request_instance = PinnedMessageRequest.from_json(json)
# print the JSON string representation of the object
print(PinnedMessageRequest.to_json())

# convert the object into a dict
pinned_message_request_dict = pinned_message_request_instance.to_dict()
# create an instance of PinnedMessageRequest from a dict
pinned_message_request_from_dict = PinnedMessageRequest.from_dict(pinned_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


