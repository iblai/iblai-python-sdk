# WatchedVideosPerUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**full_name** | **str** | learner fullname | 
**count** | **int** | Videos watched count | 
**percentage** | **float** | Percentage ... | 

## Example

```python
from iblai.models.watched_videos_per_user_data import WatchedVideosPerUserData

# TODO update the JSON string below
json = "{}"
# create an instance of WatchedVideosPerUserData from a JSON string
watched_videos_per_user_data_instance = WatchedVideosPerUserData.from_json(json)
# print the JSON string representation of the object
print(WatchedVideosPerUserData.to_json())

# convert the object into a dict
watched_videos_per_user_data_dict = watched_videos_per_user_data_instance.to_dict()
# create an instance of WatchedVideosPerUserData from a dict
watched_videos_per_user_data_from_dict = WatchedVideosPerUserData.from_dict(watched_videos_per_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


