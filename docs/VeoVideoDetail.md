# VeoVideoDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**id** | **int** |  | [readonly] 
**video_file** | **str** |  | [readonly] 
**generation_status** | **str** |  | [readonly] 
**prompt_text** | **str** |  | [optional] 
**prompt_image** | **str** |  | [readonly] 
**thumbnail_image** | **str** |  | [readonly] 

## Example

```python
from iblai.models.veo_video_detail import VeoVideoDetail

# TODO update the JSON string below
json = "{}"
# create an instance of VeoVideoDetail from a JSON string
veo_video_detail_instance = VeoVideoDetail.from_json(json)
# print the JSON string representation of the object
print(VeoVideoDetail.to_json())

# convert the object into a dict
veo_video_detail_dict = veo_video_detail_instance.to_dict()
# create an instance of VeoVideoDetail from a dict
veo_video_detail_from_dict = VeoVideoDetail.from_dict(veo_video_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


