# TokenProxyOutput

The SPA expects this outer data key so we need to create an extra layer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TokenProxyOutputSerializerData**](TokenProxyOutputSerializerData.md) |  | 

## Example

```python
from iblai.models.token_proxy_output import TokenProxyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProxyOutput from a JSON string
token_proxy_output_instance = TokenProxyOutput.from_json(json)
# print the JSON string representation of the object
print(TokenProxyOutput.to_json())

# convert the object into a dict
token_proxy_output_dict = token_proxy_output_instance.to_dict()
# create an instance of TokenProxyOutput from a dict
token_proxy_output_from_dict = TokenProxyOutput.from_dict(token_proxy_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


