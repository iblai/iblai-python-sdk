# VideosCountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | Total videos (videos watched / Total Course Videos) | 

## Example

```python
from iblai.models.videos_count_data import VideosCountData

# TODO update the JSON string below
json = "{}"
# create an instance of VideosCountData from a JSON string
videos_count_data_instance = VideosCountData.from_json(json)
# print the JSON string representation of the object
print(VideosCountData.to_json())

# convert the object into a dict
videos_count_data_dict = videos_count_data_instance.to_dict()
# create an instance of VideosCountData from a dict
videos_count_data_from_dict = VideosCountData.from_dict(videos_count_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


