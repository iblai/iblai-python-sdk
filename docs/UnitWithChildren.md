# UnitWithChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**subsection** | **int** |  | 
**display_name** | **str** |  | 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [readonly] 
**type** | [**TypeC42Enum**](TypeC42Enum.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**components** | [**List[ComponentBlock]**](ComponentBlock.md) |  | 

## Example

```python
from iblai.models.unit_with_children import UnitWithChildren

# TODO update the JSON string below
json = "{}"
# create an instance of UnitWithChildren from a JSON string
unit_with_children_instance = UnitWithChildren.from_json(json)
# print the JSON string representation of the object
print(UnitWithChildren.to_json())

# convert the object into a dict
unit_with_children_dict = unit_with_children_instance.to_dict()
# create an instance of UnitWithChildren from a dict
unit_with_children_from_dict = UnitWithChildren.from_dict(unit_with_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


