# VeoVideoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_image** | **str** |  | [optional] 
**prompt_text** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from iblai.models.veo_video_request import VeoVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VeoVideoRequest from a JSON string
veo_video_request_instance = VeoVideoRequest.from_json(json)
# print the JSON string representation of the object
print(VeoVideoRequest.to_json())

# convert the object into a dict
veo_video_request_dict = veo_video_request_instance.to_dict()
# create an instance of VeoVideoRequest from a dict
veo_video_request_from_dict = VeoVideoRequest.from_dict(veo_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


