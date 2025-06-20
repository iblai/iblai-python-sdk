# SectionWithChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**course** | **int** |  | 
**display_name** | **str** |  | 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [readonly] 
**subsections** | [**List[SubSectionWithChildren]**](SubSectionWithChildren.md) |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.section_with_children import SectionWithChildren

# TODO update the JSON string below
json = "{}"
# create an instance of SectionWithChildren from a JSON string
section_with_children_instance = SectionWithChildren.from_json(json)
# print the JSON string representation of the object
print(SectionWithChildren.to_json())

# convert the object into a dict
section_with_children_dict = section_with_children_instance.to_dict()
# create an instance of SectionWithChildren from a dict
section_with_children_from_dict = SectionWithChildren.from_dict(section_with_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


