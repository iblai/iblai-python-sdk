# ConversationListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_name** | **str** |  | 
**platform_key** | **str** |  | 
**mentor** | **str** |  | 
**mentor_unique_id** | **str** |  | 
**model** | **str** |  | 
**cost** | **str** |  | [readonly] 
**username** | **str** |  | [optional] 
**name** | **str** |  | 
**first_user_message** | **str** |  | [optional] 
**topics** | **object** |  | 
**message_count** | **int** |  | 
**user_queries** | **int** |  | [optional] 
**assistant_responses** | **int** |  | [optional] 
**average_sentiment** | **float** |  | [optional] 
**sentiment** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**platform** | **int** |  | 
**session** | **str** |  | 
**user** | **int** | edX user ID | [optional] 

## Example

```python
from iblai.models.conversation_list_item import ConversationListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationListItem from a JSON string
conversation_list_item_instance = ConversationListItem.from_json(json)
# print the JSON string representation of the object
print(ConversationListItem.to_json())

# convert the object into a dict
conversation_list_item_dict = conversation_list_item_instance.to_dict()
# create an instance of ConversationListItem from a dict
conversation_list_item_from_dict = ConversationListItem.from_dict(conversation_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


