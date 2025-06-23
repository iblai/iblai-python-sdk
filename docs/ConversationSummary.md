# ConversationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_conversations** | **int** |  | 
**total_human_messages** | **int** |  | 
**total_ai_messages** | **int** |  | 

## Example

```python
from iblai.models.conversation_summary import ConversationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationSummary from a JSON string
conversation_summary_instance = ConversationSummary.from_json(json)
# print the JSON string representation of the object
print(ConversationSummary.to_json())

# convert the object into a dict
conversation_summary_dict = conversation_summary_instance.to_dict()
# create an instance of ConversationSummary from a dict
conversation_summary_from_dict = ConversationSummary.from_dict(conversation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


