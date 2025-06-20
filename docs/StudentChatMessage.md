# StudentChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**chat_message_count** | **int** |  | 

## Example

```python
from iblai.models.student_chat_message import StudentChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StudentChatMessage from a JSON string
student_chat_message_instance = StudentChatMessage.from_json(json)
# print the JSON string representation of the object
print(StudentChatMessage.to_json())

# convert the object into a dict
student_chat_message_dict = student_chat_message_instance.to_dict()
# create an instance of StudentChatMessage from a dict
student_chat_message_from_dict = StudentChatMessage.from_dict(student_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


