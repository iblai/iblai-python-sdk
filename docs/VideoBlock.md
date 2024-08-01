# VideoBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Video name | 
**id** | **str** | Video Id | 
**total_users** | **int** | Total users who have watched the video | [optional] 

## Example

```python
from iblai.models.video_block import VideoBlock

# TODO update the JSON string below
json = "{}"
# create an instance of VideoBlock from a JSON string
video_block_instance = VideoBlock.from_json(json)
# print the JSON string representation of the object
print(VideoBlock.to_json())

# convert the object into a dict
video_block_dict = video_block_instance.to_dict()
# create an instance of VideoBlock from a dict
video_block_from_dict = VideoBlock.from_dict(video_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


