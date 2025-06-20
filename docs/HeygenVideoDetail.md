# HeygenVideoDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**script** | **str** |  | [optional] 
**id** | **int** |  | [readonly] 
**video_file** | **str** |  | [readonly] 
**generation_status** | **str** |  | [readonly] 

## Example

```python
from iblai.models.heygen_video_detail import HeygenVideoDetail

# TODO update the JSON string below
json = "{}"
# create an instance of HeygenVideoDetail from a JSON string
heygen_video_detail_instance = HeygenVideoDetail.from_json(json)
# print the JSON string representation of the object
print(HeygenVideoDetail.to_json())

# convert the object into a dict
heygen_video_detail_dict = heygen_video_detail_instance.to_dict()
# create an instance of HeygenVideoDetail from a dict
heygen_video_detail_from_dict = HeygenVideoDetail.from_dict(heygen_video_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


