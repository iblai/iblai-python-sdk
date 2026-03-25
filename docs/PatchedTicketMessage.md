# PatchedTicketMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**ticket** | **int** |  | [optional] 
**sender** | **int** | edX user ID | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_ticket_message import PatchedTicketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTicketMessage from a JSON string
patched_ticket_message_instance = PatchedTicketMessage.from_json(json)
# print the JSON string representation of the object
print(PatchedTicketMessage.to_json())

# convert the object into a dict
patched_ticket_message_dict = patched_ticket_message_instance.to_dict()
# create an instance of PatchedTicketMessage from a dict
patched_ticket_message_from_dict = PatchedTicketMessage.from_dict(patched_ticket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


