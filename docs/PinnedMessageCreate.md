# PinnedMessageCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**platform** | **str** | The platform key | 
**username** | **str** |  | 
**session_id** | **str** |  | 

## Example

```python
from iblai.models.pinned_message_create import PinnedMessageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PinnedMessageCreate from a JSON string
pinned_message_create_instance = PinnedMessageCreate.from_json(json)
# print the JSON string representation of the object
print(PinnedMessageCreate.to_json())

# convert the object into a dict
pinned_message_create_dict = pinned_message_create_instance.to_dict()
# create an instance of PinnedMessageCreate from a dict
pinned_message_create_from_dict = PinnedMessageCreate.from_dict(pinned_message_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


