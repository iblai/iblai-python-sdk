# ConversationDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **Dict[str, object]** |  | 
**messages** | **List[Dict[str, object]]** |  | 

## Example

```python
from iblai.models.conversation_detail_response import ConversationDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationDetailResponse from a JSON string
conversation_detail_response_instance = ConversationDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ConversationDetailResponse.to_json())

# convert the object into a dict
conversation_detail_response_dict = conversation_detail_response_instance.to_dict()
# create an instance of ConversationDetailResponse from a dict
conversation_detail_response_from_dict = ConversationDetailResponse.from_dict(conversation_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


