# UserChatByPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **datetime** |  | 
**user_count** | **int** |  | 

## Example

```python
from iblai.models.user_chat_by_period import UserChatByPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of UserChatByPeriod from a JSON string
user_chat_by_period_instance = UserChatByPeriod.from_json(json)
# print the JSON string representation of the object
print(UserChatByPeriod.to_json())

# convert the object into a dict
user_chat_by_period_dict = user_chat_by_period_instance.to_dict()
# create an instance of UserChatByPeriod from a dict
user_chat_by_period_from_dict = UserChatByPeriod.from_dict(user_chat_by_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


