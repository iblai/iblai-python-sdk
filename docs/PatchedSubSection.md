# PatchedSubSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**section** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_sub_section import PatchedSubSection

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSubSection from a JSON string
patched_sub_section_instance = PatchedSubSection.from_json(json)
# print the JSON string representation of the object
print(PatchedSubSection.to_json())

# convert the object into a dict
patched_sub_section_dict = patched_sub_section_instance.to_dict()
# create an instance of PatchedSubSection from a dict
patched_sub_section_from_dict = PatchedSubSection.from_dict(patched_sub_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


