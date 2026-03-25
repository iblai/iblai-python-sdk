# PaginatedMCPServerConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MCPServerConnection]**](MCPServerConnection.md) |  | 

## Example

```python
from iblai.models.paginated_mcp_server_connection_list import PaginatedMCPServerConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMCPServerConnectionList from a JSON string
paginated_mcp_server_connection_list_instance = PaginatedMCPServerConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMCPServerConnectionList.to_json())

# convert the object into a dict
paginated_mcp_server_connection_list_dict = paginated_mcp_server_connection_list_instance.to_dict()
# create an instance of PaginatedMCPServerConnectionList from a dict
paginated_mcp_server_connection_list_from_dict = PaginatedMCPServerConnectionList.from_dict(paginated_mcp_server_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


