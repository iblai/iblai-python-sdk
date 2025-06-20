# ConversationRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**full_conversation_text** | **str** |  | 
**rating_text** | **str** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from iblai.models.conversation_rating import ConversationRating

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationRating from a JSON string
conversation_rating_instance = ConversationRating.from_json(json)
# print the JSON string representation of the object
print(ConversationRating.to_json())

# convert the object into a dict
conversation_rating_dict = conversation_rating_instance.to_dict()
# create an instance of ConversationRating from a dict
conversation_rating_from_dict = ConversationRating.from_dict(conversation_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


