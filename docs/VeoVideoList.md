# VeoVideoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**id** | **int** |  | [readonly] 
**generation_status** | **str** |  | [readonly] 

## Example

```python
from iblai.models.veo_video_list import VeoVideoList

# TODO update the JSON string below
json = "{}"
# create an instance of VeoVideoList from a JSON string
veo_video_list_instance = VeoVideoList.from_json(json)
# print the JSON string representation of the object
print(VeoVideoList.to_json())

# convert the object into a dict
veo_video_list_dict = veo_video_list_instance.to_dict()
# create an instance of VeoVideoList from a dict
veo_video_list_from_dict = VeoVideoList.from_dict(veo_video_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


