# TokenProxyOutputSerializerData

Core data for Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**TokenProxyUser**](TokenProxyUser.md) | User details | 
**axd_token** | [**AuthToken**](AuthToken.md) | Axd Token details | 
**dm_token** | [**ManagerAuthToken**](ManagerAuthToken.md) | DM Token details | 

## Example

```python
from iblai.models.token_proxy_output_serializer_data import TokenProxyOutputSerializerData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProxyOutputSerializerData from a JSON string
token_proxy_output_serializer_data_instance = TokenProxyOutputSerializerData.from_json(json)
# print the JSON string representation of the object
print(TokenProxyOutputSerializerData.to_json())

# convert the object into a dict
token_proxy_output_serializer_data_dict = token_proxy_output_serializer_data_instance.to_dict()
# create an instance of TokenProxyOutputSerializerData from a dict
token_proxy_output_serializer_data_from_dict = TokenProxyOutputSerializerData.from_dict(token_proxy_output_serializer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


