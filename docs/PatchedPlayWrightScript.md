# PatchedPlayWrightScript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**platform** | **int** |  | [optional] [readonly] 
**student** | **int** | edX user ID | [optional] [readonly] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**script** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_play_wright_script import PatchedPlayWrightScript

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlayWrightScript from a JSON string
patched_play_wright_script_instance = PatchedPlayWrightScript.from_json(json)
# print the JSON string representation of the object
print(PatchedPlayWrightScript.to_json())

# convert the object into a dict
patched_play_wright_script_dict = patched_play_wright_script_instance.to_dict()
# create an instance of PatchedPlayWrightScript from a dict
patched_play_wright_script_from_dict = PatchedPlayWrightScript.from_dict(patched_play_wright_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


