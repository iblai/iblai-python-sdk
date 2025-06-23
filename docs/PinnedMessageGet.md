# PinnedMessageGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**mentor** | [**Mentor**](Mentor.md) |  | 
**messages** | [**List[ChatHistory]**](ChatHistory.md) |  | 

## Example

```python
from iblai.models.pinned_message_get import PinnedMessageGet

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedMessageGet from a JSON string
pinned_message_get_instance = PinnedMessageGet.from_json(json)
# print the JSON string representation of the object
print(PinnedMessageGet.to_json())

# convert the object into a dict
pinned_message_get_dict = pinned_message_get_instance.to_dict()
# create an instance of PinnedMessageGet from a dict
pinned_message_get_from_dict = PinnedMessageGet.from_dict(pinned_message_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


