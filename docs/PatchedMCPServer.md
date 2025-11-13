# PatchedMCPServer

Serializer for the MCPServer model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**platform** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** | A description of the MCP server. | [optional] 
**url** | **str** | The url of the MCP server. | [optional] 
**image** | **str** |  | [optional] 
**transport** | [**TransportEnum**](TransportEnum.md) |  | [optional] 
**credentials** | **str** | Authorization credentials to uauthenticate to the mcp server. if provided takes priority over connected service and headers. Token here must be the full authorization value. For example: &#x60;&lt;scheme&gt; &lt;credentials&gt;&#x60; | [optional] 
**extra_headers** | **object** | Headers to send to the MCP server. Useful for authentication, | [optional] 
**platform_key** | **str** |  | [optional] [readonly] 
**is_featured** | **bool** | Featured mcp servers will be accessible to all other tenants. | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) | The type of authentication to use for the MCP server.  * &#x60;none&#x60; - None * &#x60;token&#x60; - Token * &#x60;oauth2&#x60; - Oauth2 | [optional] 
**is_enabled** | **bool** | Whether the MCP server is enabled or not. | [optional] 
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


