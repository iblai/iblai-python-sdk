# LtiKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** | Name of the RSA Key | 
**public_key** | **str** | Public Key in PEM format | [readonly] 
**public_jwk** | **object** | Public key in JWK format | [readonly] 
**platform_key** | **str** | Platform Key | 

## Example

```python
from iblai.models.lti_key import LtiKey

# TODO update the JSON string below
json = "{}"
# create an instance of LtiKey from a JSON string
lti_key_instance = LtiKey.from_json(json)
# print the JSON string representation of the object
print(LtiKey.to_json())

# convert the object into a dict
lti_key_dict = lti_key_instance.to_dict()
# create an instance of LtiKey from a dict
lti_key_from_dict = LtiKey.from_dict(lti_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


