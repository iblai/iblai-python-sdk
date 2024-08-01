# VideosWatchedSubSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Subsection name | 
**id** | **str** | Subsection Id | 
**total_watch** | **str** | Total videos watched. N/A if no record found | 
**videos** | [**List[VideoBlock]**](VideoBlock.md) | Videos | [optional] 

## Example

```python
from iblai.models.videos_watched_sub_section import VideosWatchedSubSection

# TODO update the JSON string below
json = "{}"
# create an instance of VideosWatchedSubSection from a JSON string
videos_watched_sub_section_instance = VideosWatchedSubSection.from_json(json)
# print the JSON string representation of the object
print(VideosWatchedSubSection.to_json())

# convert the object into a dict
videos_watched_sub_section_dict = videos_watched_sub_section_instance.to_dict()
# create an instance of VideosWatchedSubSection from a dict
videos_watched_sub_section_from_dict = VideosWatchedSubSection.from_dict(videos_watched_sub_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


