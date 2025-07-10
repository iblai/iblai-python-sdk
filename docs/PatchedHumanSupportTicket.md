# PatchedHumanSupportTicket

serializer interface intended for students/ non-admin users. This limits students to only update the subject and description of a ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**username** | **str** |  | [optional] [readonly] 
**user** | **int** | edX user ID | [optional] [readonly] 
**session** | **str** |  | [optional] [readonly] 
**subject** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | [**HumanSupportTicketStatusEnum**](HumanSupportTicketStatusEnum.md) |  | [optional] 
**mentor_id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**resolved_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_human_support_ticket import PatchedHumanSupportTicket

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHumanSupportTicket from a JSON string
patched_human_support_ticket_instance = PatchedHumanSupportTicket.from_json(json)
# print the JSON string representation of the object
print(PatchedHumanSupportTicket.to_json())

# convert the object into a dict
patched_human_support_ticket_dict = patched_human_support_ticket_instance.to_dict()
# create an instance of PatchedHumanSupportTicket from a dict
patched_human_support_ticket_from_dict = PatchedHumanSupportTicket.from_dict(patched_human_support_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


