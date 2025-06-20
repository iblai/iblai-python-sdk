# WhitelistedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**is_active** | **bool** |  | [optional] 

## Example

```python
from iblai.models.whitelisted_domain import WhitelistedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistedDomain from a JSON string
whitelisted_domain_instance = WhitelistedDomain.from_json(json)
# print the JSON string representation of the object
print(WhitelistedDomain.to_json())

# convert the object into a dict
whitelisted_domain_dict = whitelisted_domain_instance.to_dict()
# create an instance of WhitelistedDomain from a dict
whitelisted_domain_from_dict = WhitelistedDomain.from_dict(whitelisted_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


