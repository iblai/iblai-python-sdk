# ToolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**display_name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**allow_retriever_mentors** | **bool** |  | [optional] 

## Example

```python
from iblai.models.tool_response import ToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolResponse from a JSON string
tool_response_instance = ToolResponse.from_json(json)
# print the JSON string representation of the object
print(ToolResponse.to_json())

# convert the object into a dict
tool_response_dict = tool_response_instance.to_dict()
# create an instance of ToolResponse from a dict
tool_response_from_dict = ToolResponse.from_dict(tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


