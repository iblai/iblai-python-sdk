# PatchedUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**subsection** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [optional] [readonly] 
**type** | [**TypeC42Enum**](TypeC42Enum.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_unit import PatchedUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUnit from a JSON string
patched_unit_instance = PatchedUnit.from_json(json)
# print the JSON string representation of the object
print(PatchedUnit.to_json())

# convert the object into a dict
patched_unit_dict = patched_unit_instance.to_dict()
# create an instance of PatchedUnit from a dict
patched_unit_from_dict = PatchedUnit.from_dict(patched_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


