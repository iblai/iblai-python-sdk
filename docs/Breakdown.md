# Breakdown

Detailed breakdown of costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_provider** | [**List[ProviderBreakdown]**](ProviderBreakdown.md) |  | [optional] 
**by_mentor** | [**List[MentorBreakdown]**](MentorBreakdown.md) |  | [optional] 
**by_action** | [**List[ActionBreakdown]**](ActionBreakdown.md) |  | [optional] 

## Example

```python
from iblai.models.breakdown import Breakdown

# TODO update the JSON string below
json = "{}"
# create an instance of Breakdown from a JSON string
breakdown_instance = Breakdown.from_json(json)
# print the JSON string representation of the object
print(Breakdown.to_json())

# convert the object into a dict
breakdown_dict = breakdown_instance.to_dict()
# create an instance of Breakdown from a dict
breakdown_from_dict = Breakdown.from_dict(breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


