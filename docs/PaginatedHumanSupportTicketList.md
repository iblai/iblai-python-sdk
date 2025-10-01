# PaginatedHumanSupportTicketList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[HumanSupportTicket]**](HumanSupportTicket.md) |  | 

## Example

```python
from iblai.models.paginated_human_support_ticket_list import PaginatedHumanSupportTicketList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedHumanSupportTicketList from a JSON string
paginated_human_support_ticket_list_instance = PaginatedHumanSupportTicketList.from_json(json)
# print the JSON string representation of the object
print(PaginatedHumanSupportTicketList.to_json())

# convert the object into a dict
paginated_human_support_ticket_list_dict = paginated_human_support_ticket_list_instance.to_dict()
# create an instance of PaginatedHumanSupportTicketList from a dict
paginated_human_support_ticket_list_from_dict = PaginatedHumanSupportTicketList.from_dict(paginated_human_support_ticket_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


