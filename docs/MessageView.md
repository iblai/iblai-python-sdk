# MessageView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**title** | **str** |  | 
**proactive_prompt** | **str** |  | 
**mentor_unique_id** | **str** |  | 
**platform_key** | **str** |  | 
**previous** | **str** |  | 
**next** | **str** |  | 
**results** | **List[object]** |  | 

## Example

```python
from iblai.models.message_view import MessageView

# TODO update the JSON string below
json = "{}"
# create an instance of MessageView from a JSON string
message_view_instance = MessageView.from_json(json)
# print the JSON string representation of the object
print(MessageView.to_json())

# convert the object into a dict
message_view_dict = message_view_instance.to_dict()
# create an instance of MessageView from a dict
message_view_from_dict = MessageView.from_dict(message_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


