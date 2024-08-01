# PlayWrightScript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**platform** | **int** |  | [readonly] 
**student** | **int** | edX user ID | [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**script** | **str** |  | 
**is_public** | **bool** |  | [readonly] 

## Example

```python
from iblai.models.play_wright_script import PlayWrightScript

# TODO update the JSON string below
json = "{}"
# create an instance of PlayWrightScript from a JSON string
play_wright_script_instance = PlayWrightScript.from_json(json)
# print the JSON string representation of the object
print(PlayWrightScript.to_json())

# convert the object into a dict
play_wright_script_dict = play_wright_script_instance.to_dict()
# create an instance of PlayWrightScript from a dict
play_wright_script_from_dict = PlayWrightScript.from_dict(play_wright_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


