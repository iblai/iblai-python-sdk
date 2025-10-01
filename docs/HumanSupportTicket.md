# HumanSupportTicket

serializer interface intended for students/ non-admin users. This limits students to only update the subject and description of a ticket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**session** | **str** |  | [readonly] 
**subject** | **str** |  | 
**description** | **str** |  | 
**status** | [**HumanSupportTicketStatusEnum**](HumanSupportTicketStatusEnum.md) |  | [optional] 
**mentor_id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**resolved_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.human_support_ticket import HumanSupportTicket

# TODO update the JSON string below
json = "{}"
# create an instance of HumanSupportTicket from a JSON string
human_support_ticket_instance = HumanSupportTicket.from_json(json)
# print the JSON string representation of the object
print(HumanSupportTicket.to_json())

# convert the object into a dict
human_support_ticket_dict = human_support_ticket_instance.to_dict()
# create an instance of HumanSupportTicket from a dict
human_support_ticket_from_dict = HumanSupportTicket.from_dict(human_support_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


