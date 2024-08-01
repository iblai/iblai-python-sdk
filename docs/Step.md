# Step


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | [**StepStatusEnum**](StepStatusEnum.md) |  | [optional] 
**position** | **int** |  | 
**job** | **int** |  | 

## Example

```python
from iblai.models.step import Step

# TODO update the JSON string below
json = "{}"
# create an instance of Step from a JSON string
step_instance = Step.from_json(json)
# print the JSON string representation of the object
print(Step.to_json())

# convert the object into a dict
step_dict = step_instance.to_dict()
# create an instance of Step from a dict
step_from_dict = Step.from_dict(step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


