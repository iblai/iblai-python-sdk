# ContextResponse

Response serializer for context endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from iblai.models.context_response import ContextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContextResponse from a JSON string
context_response_instance = ContextResponse.from_json(json)
# print the JSON string representation of the object
print(ContextResponse.to_json())

# convert the object into a dict
context_response_dict = context_response_instance.to_dict()
# create an instance of ContextResponse from a dict
context_response_from_dict = ContextResponse.from_dict(context_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


