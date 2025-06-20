# WatchedVideosPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WatchedVideosPerCourseData]**](WatchedVideosPerCourseData.md) |  | [optional] 
**total** | **int** | Total videos Watched for all rows | [optional] 

## Example

```python
from iblai.models.watched_videos_per_course import WatchedVideosPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of WatchedVideosPerCourse from a JSON string
watched_videos_per_course_instance = WatchedVideosPerCourse.from_json(json)
# print the JSON string representation of the object
print(WatchedVideosPerCourse.to_json())

# convert the object into a dict
watched_videos_per_course_dict = watched_videos_per_course_instance.to_dict()
# create an instance of WatchedVideosPerCourse from a dict
watched_videos_per_course_from_dict = WatchedVideosPerCourse.from_dict(watched_videos_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


