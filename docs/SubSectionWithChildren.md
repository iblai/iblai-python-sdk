# SubSectionWithChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**section** | **int** |  | 
**display_name** | **str** |  | 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [readonly] 
**units** | [**List[UnitWithChildren]**](UnitWithChildren.md) |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.sub_section_with_children import SubSectionWithChildren

# TODO update the JSON string below
json = "{}"
# create an instance of SubSectionWithChildren from a JSON string
sub_section_with_children_instance = SubSectionWithChildren.from_json(json)
# print the JSON string representation of the object
print(SubSectionWithChildren.to_json())

# convert the object into a dict
sub_section_with_children_dict = sub_section_with_children_instance.to_dict()
# create an instance of SubSectionWithChildren from a dict
sub_section_with_children_from_dict = SubSectionWithChildren.from_dict(sub_section_with_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


