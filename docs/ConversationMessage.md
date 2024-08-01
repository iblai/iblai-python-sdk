# ConversationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_message** | **str** |  | [readonly] 
**topics** | [**List[TopicModel]**](TopicModel.md) |  | 
**id** | **str** |  | 
**user_id** | **str** |  | 
**message_count** | **str** |  | [readonly] 
**model** | **str** |  | 
**inserted_at** | **datetime** |  | 
**user_sentiment** | **str** |  | [readonly] 

## Example

```python
from iblai.models.conversation_message import ConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessage from a JSON string
conversation_message_instance = ConversationMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationMessage.to_json())

# convert the object into a dict
conversation_message_dict = conversation_message_instance.to_dict()
# create an instance of ConversationMessage from a dict
conversation_message_from_dict = ConversationMessage.from_dict(conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


