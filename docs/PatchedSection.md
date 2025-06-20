# PatchedSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**course** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_section import PatchedSection

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSection from a JSON string
patched_section_instance = PatchedSection.from_json(json)
# print the JSON string representation of the object
print(PatchedSection.to_json())

# convert the object into a dict
patched_section_dict = patched_section_instance.to_dict()
# create an instance of PatchedSection from a dict
patched_section_from_dict = PatchedSection.from_dict(patched_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


