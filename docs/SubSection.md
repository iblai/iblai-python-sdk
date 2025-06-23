# SubSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**section** | **int** |  | 
**display_name** | **str** |  | 
**status** | [**Status6eeEnum**](Status6eeEnum.md) |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.sub_section import SubSection

# TODO update the JSON string below
json = "{}"
# create an instance of SubSection from a JSON string
sub_section_instance = SubSection.from_json(json)
# print the JSON string representation of the object
print(SubSection.to_json())

# convert the object into a dict
sub_section_dict = sub_section_instance.to_dict()
# create an instance of SubSection from a dict
sub_section_from_dict = SubSection.from_dict(sub_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


