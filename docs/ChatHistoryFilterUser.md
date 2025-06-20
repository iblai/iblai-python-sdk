# ChatHistoryFilterUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | 
**lti_email** | **str** |  | [readonly] 

## Example

```python
from iblai.models.chat_history_filter_user import ChatHistoryFilterUser

# TODO update the JSON string below
json = "{}"
# create an instance of ChatHistoryFilterUser from a JSON string
chat_history_filter_user_instance = ChatHistoryFilterUser.from_json(json)
# print the JSON string representation of the object
print(ChatHistoryFilterUser.to_json())

# convert the object into a dict
chat_history_filter_user_dict = chat_history_filter_user_instance.to_dict()
# create an instance of ChatHistoryFilterUser from a dict
chat_history_filter_user_from_dict = ChatHistoryFilterUser.from_dict(chat_history_filter_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


