# PatchedMCPServerConnection

Serializer for managing `MCPServerConnection` records via the API.  The serializer enforces the business rules for combining scope, platform, and authentication configuration while exposing a masked view of any stored credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**server** | **int** |  | [optional] 
**server_name** | **str** |  | [optional] [readonly] 
**scope** | [**MCPServerConnectionScopeEnum**](MCPServerConnectionScopeEnum.md) | Whether this connection is scoped to a user or shared across a platform.  * &#x60;user&#x60; - User * &#x60;mentor&#x60; - Mentor * &#x60;platform&#x60; - Platform | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**platform** | **int** |  | [optional] 
**platform_key** | **str** |  | [optional] [readonly] 
**user** | **str** | edX username | [optional] 
**mentor** | **str** |  | [optional] 
**connected_service** | **int** |  | [optional] 
**connected_service_summary** | **Dict[str, object]** |  | [optional] [readonly] 
**credentials** | **str** | Static credential/token value for token-based authentication. | [optional] 
**authorization_scheme** | **str** | Authorization scheme to prefix tokens with (e.g. &#39;Bearer&#39;). | [optional] 
**extra_headers** | **object** | Additional headers to include when connecting to the MCP server. | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_mcp_server_connection import PatchedMCPServerConnection

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMCPServerConnection from a JSON string
patched_mcp_server_connection_instance = PatchedMCPServerConnection.from_json(json)
# print the JSON string representation of the object
print(PatchedMCPServerConnection.to_json())

# convert the object into a dict
patched_mcp_server_connection_dict = patched_mcp_server_connection_instance.to_dict()
# create an instance of PatchedMCPServerConnection from a dict
patched_mcp_server_connection_from_dict = PatchedMCPServerConnection.from_dict(patched_mcp_server_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


