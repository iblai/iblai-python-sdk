# PaginatedTicketMessageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TicketMessage]**](TicketMessage.md) |  | 

## Example

```python
from iblai.models.paginated_ticket_message_list import PaginatedTicketMessageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTicketMessageList from a JSON string
paginated_ticket_message_list_instance = PaginatedTicketMessageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTicketMessageList.to_json())

# convert the object into a dict
paginated_ticket_message_list_dict = paginated_ticket_message_list_instance.to_dict()
# create an instance of PaginatedTicketMessageList from a dict
paginated_ticket_message_list_from_dict = PaginatedTicketMessageList.from_dict(paginated_ticket_message_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


