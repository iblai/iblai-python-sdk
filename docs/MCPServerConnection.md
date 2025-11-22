# MCPServerConnection

Serializer for managing `MCPServerConnection` records via the API.  The serializer enforces the business rules for combining scope, platform, and authentication configuration while exposing a masked view of any stored credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**server** | **int** |  | 
**server_name** | **str** |  | [readonly] 
**scope** | [**MCPServerConnectionScopeEnum**](MCPServerConnectionScopeEnum.md) | Whether this connection is scoped to a user or shared across a platform.  * &#x60;user&#x60; - User * &#x60;mentor&#x60; - Mentor * &#x60;platform&#x60; - Platform | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**platform** | **int** |  | [optional] 
**platform_key** | **str** |  | [readonly] 
**user** | **str** | edX username | [optional] 
**mentor** | **str** |  | [optional] 
**connected_service** | **int** |  | [optional] 
**connected_service_summary** | **Dict[str, object]** |  | [readonly] 
**credentials** | **str** | Static credential/token value for token-based authentication. | [optional] 
**authorization_scheme** | **str** | Authorization scheme to prefix tokens with (e.g. &#39;Bearer&#39;). | [optional] 
**extra_headers** | **object** | Additional headers to include when connecting to the MCP server. | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mcp_server_connection import MCPServerConnection

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerConnection from a JSON string
mcp_server_connection_instance = MCPServerConnection.from_json(json)
# print the JSON string representation of the object
print(MCPServerConnection.to_json())

# convert the object into a dict
mcp_server_connection_dict = mcp_server_connection_instance.to_dict()
# create an instance of MCPServerConnection from a dict
mcp_server_connection_from_dict = MCPServerConnection.from_dict(mcp_server_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


