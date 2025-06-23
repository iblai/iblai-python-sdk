# MessageViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**tools** | **List[str]** | List of tools slugs to use | [optional] [default to []]

## Example

```python
from iblai.models.message_view_request import MessageViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageViewRequest from a JSON string
message_view_request_instance = MessageViewRequest.from_json(json)
# print the JSON string representation of the object
print(MessageViewRequest.to_json())

# convert the object into a dict
message_view_request_dict = message_view_request_instance.to_dict()
# create an instance of MessageViewRequest from a dict
message_view_request_from_dict = MessageViewRequest.from_dict(message_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


