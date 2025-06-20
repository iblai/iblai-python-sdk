# HeygenVideoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | 
**name** | **str** |  | 
**template_id** | **str** |  | [optional] 

## Example

```python
from iblai.models.heygen_video_request import HeygenVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeygenVideoRequest from a JSON string
heygen_video_request_instance = HeygenVideoRequest.from_json(json)
# print the JSON string representation of the object
print(HeygenVideoRequest.to_json())

# convert the object into a dict
heygen_video_request_dict = heygen_video_request_instance.to_dict()
# create an instance of HeygenVideoRequest from a dict
heygen_video_request_from_dict = HeygenVideoRequest.from_dict(heygen_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


