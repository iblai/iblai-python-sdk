# PatchedDisclaimer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**scope** | [**ScopeEnum**](ScopeEnum.md) |  | [optional] 
**platform** | **int** | Platform to which the disclaimer applies.  | [optional] [readonly] 
**content** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**has_agreed** | **bool** |  | [optional] [readonly] 
**platform_key** | **str** |  | [optional] [readonly] 
**mentors** | **List[str]** |  | [optional] 

## Example

```python
from iblai.models.patched_disclaimer import PatchedDisclaimer

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDisclaimer from a JSON string
patched_disclaimer_instance = PatchedDisclaimer.from_json(json)
# print the JSON string representation of the object
print(PatchedDisclaimer.to_json())

# convert the object into a dict
patched_disclaimer_dict = patched_disclaimer_instance.to_dict()
# create an instance of PatchedDisclaimer from a dict
patched_disclaimer_from_dict = PatchedDisclaimer.from_dict(patched_disclaimer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


