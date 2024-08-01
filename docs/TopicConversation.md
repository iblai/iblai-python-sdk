# TopicConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** |  | 
**conversation_count** | **int** |  | 

## Example

```python
from iblai.models.topic_conversation import TopicConversation

# TODO update the JSON string below
json = "{}"
# create an instance of TopicConversation from a JSON string
topic_conversation_instance = TopicConversation.from_json(json)
# print the JSON string representation of the object
print(TopicConversation.to_json())

# convert the object into a dict
topic_conversation_dict = topic_conversation_instance.to_dict()
# create an instance of TopicConversation from a dict
topic_conversation_from_dict = TopicConversation.from_dict(topic_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


