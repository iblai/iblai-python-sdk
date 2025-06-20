# WatchedVideosPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | 
**name** | **str** | Course Name | 
**count** | **int** | Number of watched videos | 
**percentage** | **float** | Percentage ... | 

## Example

```python
from iblai.models.watched_videos_per_course_data import WatchedVideosPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of WatchedVideosPerCourseData from a JSON string
watched_videos_per_course_data_instance = WatchedVideosPerCourseData.from_json(json)
# print the JSON string representation of the object
print(WatchedVideosPerCourseData.to_json())

# convert the object into a dict
watched_videos_per_course_data_dict = watched_videos_per_course_data_instance.to_dict()
# create an instance of WatchedVideosPerCourseData from a dict
watched_videos_per_course_data_from_dict = WatchedVideosPerCourseData.from_dict(watched_videos_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


