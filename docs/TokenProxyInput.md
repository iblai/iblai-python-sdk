# TokenProxyInput

Serializer for TokenProxyView POST request input data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Edx User ID | [optional] 
**username** | **str** | Edx Username | [optional] 
**email** | **str** | Edx Email | [optional] 
**platform_key** | **str** | Platform key axd token should belong to | 

## Example

```python
from iblai.models.token_proxy_input import TokenProxyInput

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProxyInput from a JSON string
token_proxy_input_instance = TokenProxyInput.from_json(json)
# print the JSON string representation of the object
print(TokenProxyInput.to_json())

# convert the object into a dict
token_proxy_input_dict = token_proxy_input_instance.to_dict()
# create an instance of TokenProxyInput from a dict
token_proxy_input_from_dict = TokenProxyInput.from_dict(token_proxy_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


