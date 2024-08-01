# IssuerAuthority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**signature** | **str** |  | 

## Example

```python
from iblai.models.issuer_authority import IssuerAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of IssuerAuthority from a JSON string
issuer_authority_instance = IssuerAuthority.from_json(json)
# print the JSON string representation of the object
print(IssuerAuthority.to_json())

# convert the object into a dict
issuer_authority_dict = issuer_authority_instance.to_dict()
# create an instance of IssuerAuthority from a dict
issuer_authority_from_dict = IssuerAuthority.from_dict(issuer_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


