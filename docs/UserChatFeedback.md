# UserChatFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** |  | 
**session** | **str** |  | 
**user_text** | **str** |  | 
**ai_response** | **str** |  | 
**reason** | **str** |  | 
**additional_feedback** | **str** |  | 
**rating** | [**RatingEnum**](RatingEnum.md) |  | [optional] 
**inserted_at** | **datetime** |  | [optional] 
**mentor** | **int** |  | 

## Example

```python
from iblai.models.user_chat_feedback import UserChatFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatFeedback from a JSON string
user_chat_feedback_instance = UserChatFeedback.from_json(json)
# print the JSON string representation of the object
print(UserChatFeedback.to_json())

# convert the object into a dict
user_chat_feedback_dict = user_chat_feedback_instance.to_dict()
# create an instance of UserChatFeedback from a dict
user_chat_feedback_from_dict = UserChatFeedback.from_dict(user_chat_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


