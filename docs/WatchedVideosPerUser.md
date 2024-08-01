# WatchedVideosPerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WatchedVideosPerUserData]**](WatchedVideosPerUserData.md) |  | [optional] 
**total** | **int** | Total rows | [optional] 

## Example

```python
from iblai.models.watched_videos_per_user import WatchedVideosPerUser

# TODO update the JSON string below
json = "{}"
# create an instance of WatchedVideosPerUser from a JSON string
watched_videos_per_user_instance = WatchedVideosPerUser.from_json(json)
# print the JSON string representation of the object
print(WatchedVideosPerUser.to_json())

# convert the object into a dict
watched_videos_per_user_dict = watched_videos_per_user_instance.to_dict()
# create an instance of WatchedVideosPerUser from a dict
watched_videos_per_user_from_dict = WatchedVideosPerUser.from_dict(watched_videos_per_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


