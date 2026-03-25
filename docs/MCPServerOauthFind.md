# MCPServerOauthFind


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**callback_url** | **str** |  | [optional] [default to '']
**name** | **str** |  | [optional] [default to '']

## Example

```python
from iblai.models.mcp_server_oauth_find import MCPServerOauthFind

# TODO update the JSON string below
json = "{}"
# create an instance of MCPServerOauthFind from a JSON string
mcp_server_oauth_find_instance = MCPServerOauthFind.from_json(json)
# print the JSON string representation of the object
print(MCPServerOauthFind.to_json())

# convert the object into a dict
mcp_server_oauth_find_dict = mcp_server_oauth_find_instance.to_dict()
# create an instance of MCPServerOauthFind from a dict
mcp_server_oauth_find_from_dict = MCPServerOauthFind.from_dict(mcp_server_oauth_find_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


