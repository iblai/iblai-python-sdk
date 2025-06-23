# PatchedMCPServer

Serializer for the MCPServer model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**platform** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**url** | **str** | The url of the MCP server. | [optional] 
**transport** | [**TransportEnum**](TransportEnum.md) |  | [optional] 
**headers** | **object** | Headers to send to the MCP server. Useful for authentication, | [optional] 
**platform_key** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mcp_server import PatchedMCPServer

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMCPServer from a JSON string
patched_mcp_server_instance = PatchedMCPServer.from_json(json)
# print the JSON string representation of the object
print(PatchedMCPServer.to_json())

# convert the object into a dict
patched_mcp_server_dict = patched_mcp_server_instance.to_dict()
# create an instance of PatchedMCPServer from a dict
patched_mcp_server_from_dict = PatchedMCPServer.from_dict(patched_mcp_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


