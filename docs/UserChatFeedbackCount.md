# UserChatFeedbackCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**week** | **datetime** |  | 
**feedback_count** | **int** |  | 

## Example

```python
from iblai.models.user_chat_feedback_count import UserChatFeedbackCount

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatFeedbackCount from a JSON string
user_chat_feedback_count_instance = UserChatFeedbackCount.from_json(json)
# print the JSON string representation of the object
print(UserChatFeedbackCount.to_json())

# convert the object into a dict
user_chat_feedback_count_dict = user_chat_feedback_count_instance.to_dict()
# create an instance of UserChatFeedbackCount from a dict
user_chat_feedback_count_from_dict = UserChatFeedbackCount.from_dict(user_chat_feedback_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


