# ActionBreakdown

Action/trace name cost breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**cost** | **decimal.Decimal** |  | 
**sessions** | **int** |  | 
**trace_count** | **int** |  | 
**unique_users** | **int** |  | [optional] 

## Example

```python
from iblai.models.action_breakdown import ActionBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBreakdown from a JSON string
action_breakdown_instance = ActionBreakdown.from_json(json)
# print the JSON string representation of the object
print(ActionBreakdown.to_json())

# convert the object into a dict
action_breakdown_dict = action_breakdown_instance.to_dict()
# create an instance of ActionBreakdown from a dict
action_breakdown_from_dict = ActionBreakdown.from_dict(action_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


