# LtiTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | The title of the tool | 
**issuer** | **str** | This value will look someting like https://example.com. Value provided by Lti 1.3 Platform. | 
**client_id** | **str** | The client id provided by Lti 1.3 Platform | 
**auth_login_url** | **str** | The Platforms OIDC Login endpoint. Value provided by LTI 1.3 Platform. | 
**auth_token_url** | **str** | The Platforms OIDC Token endpoint. Value provided by LTI 1.3 Platform. | 
**auth_audience** | **str** | The platforms Oauth2 Audience (aud). Usually can be skipped. | [optional] 
**key_set_url** | **str** | The platforms JWKS endpoint. Value provided by LTI 1.3 Platform. | [optional] 
**key_set** | **object** | In case Platform&#39;s JWKS endpoint is not available, you can provide the JWKS here. Value provided by LTI 1.3 Platform. | [optional] 
**tool_key** | **int** | Reference to Lti Tool | 
**deployment_ids** | **List[str]** | List of deployment ids. Example: [\&quot;1\&quot;, \&quot;deployment-2\&quot;]. Value(s) provided by LTI 1.3 Platform. | 
**platform_key** | **str** |  | 
**launch_gate** | [**LtiLaunchGate**](LtiLaunchGate.md) |  | 

## Example

```python
from iblai.models.lti_tool import LtiTool

# TODO update the JSON string below
json = "{}"
# create an instance of LtiTool from a JSON string
lti_tool_instance = LtiTool.from_json(json)
# print the JSON string representation of the object
print(LtiTool.to_json())

# convert the object into a dict
lti_tool_dict = lti_tool_instance.to_dict()
# create an instance of LtiTool from a dict
lti_tool_from_dict = LtiTool.from_dict(lti_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


