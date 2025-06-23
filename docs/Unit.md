# Unit


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

## Example

```python
from iblai.models.unit import Unit

# TODO update the JSON string below
json = "{}"
# create an instance of Unit from a JSON string
unit_instance = Unit.from_json(json)
# print the JSON string representation of the object
print(Unit.to_json())

# convert the object into a dict
unit_dict = unit_instance.to_dict()
# create an instance of Unit from a dict
unit_from_dict = Unit.from_dict(unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


