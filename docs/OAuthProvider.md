# OAuthProvider

Read-only serializer for OAuth providers, including the services they expose.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**description** | **str** |  | [readonly] 
**url** | **str** |  | [readonly] 
**image** | **str** |  | [readonly] 
**scope_map** | **object** |  | [readonly] 
**auth_url** | **str** |  | [readonly] 
**token_url** | **str** |  | [readonly] 
**is_enabled** | **bool** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**services** | [**List[OAuthService]**](OAuthService.md) |  | [readonly] 
**credentials** | [**OauthCredentialsMasked**](OauthCredentialsMasked.md) |  | [readonly] 
**use_basic_auth** | **bool** | Whether to use basic authentication for the OAuth provider. By default client id and client secret are sent to the Authorization server as post data. | [readonly] 

## Example

```python
from iblai.models.o_auth_provider import OAuthProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProvider from a JSON string
o_auth_provider_instance = OAuthProvider.from_json(json)
# print the JSON string representation of the object
print(OAuthProvider.to_json())

# convert the object into a dict
o_auth_provider_dict = o_auth_provider_instance.to_dict()
# create an instance of OAuthProvider from a dict
o_auth_provider_from_dict = OAuthProvider.from_dict(o_auth_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


