# ProviderBreakdown

Provider cost breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**cost** | **decimal.Decimal** |  | 
**percentage** | **decimal.Decimal** |  | 

## Example

```python
from iblai.models.provider_breakdown import ProviderBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderBreakdown from a JSON string
provider_breakdown_instance = ProviderBreakdown.from_json(json)
# print the JSON string representation of the object
print(ProviderBreakdown.to_json())

# convert the object into a dict
provider_breakdown_dict = provider_breakdown_instance.to_dict()
# create an instance of ProviderBreakdown from a dict
provider_breakdown_from_dict = ProviderBreakdown.from_dict(provider_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


