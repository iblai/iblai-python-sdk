# ConversationVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**conversation_count** | **int** |  | 

## Example

```python
from iblai.models.conversation_volume import ConversationVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationVolume from a JSON string
conversation_volume_instance = ConversationVolume.from_json(json)
# print the JSON string representation of the object
print(ConversationVolume.to_json())

# convert the object into a dict
conversation_volume_dict = conversation_volume_instance.to_dict()
# create an instance of ConversationVolume from a dict
conversation_volume_from_dict = ConversationVolume.from_dict(conversation_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


