# MentorBreakdown

Mentor cost breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor** | **str** |  | 
**cost** | **decimal.Decimal** |  | 
**sessions** | **int** |  | 
**mentor_name** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_breakdown import MentorBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of MentorBreakdown from a JSON string
mentor_breakdown_instance = MentorBreakdown.from_json(json)
# print the JSON string representation of the object
print(MentorBreakdown.to_json())

# convert the object into a dict
mentor_breakdown_dict = mentor_breakdown_instance.to_dict()
# create an instance of MentorBreakdown from a dict
mentor_breakdown_from_dict = MentorBreakdown.from_dict(mentor_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


