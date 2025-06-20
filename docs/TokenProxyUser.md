# TokenProxyUser

Serializer for User model for TokenProxyOutputSerializerData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Edx User ID | 
**user_email** | **str** | User&#39;s Edx Email | 
**user_nicename** | **str** | Username | 
**user_display_name** | **str** | User&#39;s display name | 
**user_fullname** | **str** | Edx Full Name | [readonly] 

## Example

```python
from iblai.models.token_proxy_user import TokenProxyUser

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProxyUser from a JSON string
token_proxy_user_instance = TokenProxyUser.from_json(json)
# print the JSON string representation of the object
print(TokenProxyUser.to_json())

# convert the object into a dict
token_proxy_user_dict = token_proxy_user_instance.to_dict()
# create an instance of TokenProxyUser from a dict
token_proxy_user_from_dict = TokenProxyUser.from_dict(token_proxy_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


