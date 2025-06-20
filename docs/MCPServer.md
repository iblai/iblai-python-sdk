# MCPServer

Serializer for the MCPServer model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**platform** | **int** |  | [readonly] 
**name** | **str** |  | 
**url** | **str** | The url of the MCP server. | 
**transport** | [**TransportEnum**](TransportEnum.md) |  | [optional] 
**headers** | **object** | Headers to send to the MCP server. Useful for authentication, | [optional] 
**platform_key** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mcp_server import MCPServer

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServer from a JSON string
mcp_server_instance = MCPServer.from_json(json)
# print the JSON string representation of the object
print(MCPServer.to_json())

# convert the object into a dict
mcp_server_dict = mcp_server_instance.to_dict()
# create an instance of MCPServer from a dict
mcp_server_from_dict = MCPServer.from_dict(mcp_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


