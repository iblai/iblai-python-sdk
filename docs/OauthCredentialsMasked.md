# OauthCredentialsMasked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_global** | **bool** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from iblai.models.oauth_credentials_masked import OauthCredentialsMasked

# TODO update the JSON string below
json = "{}"
# create an instance of OauthCredentialsMasked from a JSON string
oauth_credentials_masked_instance = OauthCredentialsMasked.from_json(json)
# print the JSON string representation of the object
print(OauthCredentialsMasked.to_json())

# convert the object into a dict
oauth_credentials_masked_dict = oauth_credentials_masked_instance.to_dict()
# create an instance of OauthCredentialsMasked from a dict
oauth_credentials_masked_from_dict = OauthCredentialsMasked.from_dict(oauth_credentials_masked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


