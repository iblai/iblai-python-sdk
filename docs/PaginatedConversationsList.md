# PaginatedConversationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Conversations]**](Conversations.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_conversations_list import PaginatedConversationsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConversationsList from a JSON string
paginated_conversations_list_instance = PaginatedConversationsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConversationsList.to_json())

# convert the object into a dict
paginated_conversations_list_dict = paginated_conversations_list_instance.to_dict()
# create an instance of PaginatedConversationsList from a dict
paginated_conversations_list_from_dict = PaginatedConversationsList.from_dict(paginated_conversations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


