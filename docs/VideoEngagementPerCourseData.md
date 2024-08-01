# VideoEngagementPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Course name | 
**course_id** | **str** | edx Course Id | 
**num_vids** | **int** | Number of videos in course | 
**num_watched** | **int** | Number of videos watched  | 
**time_watched** | **int** | Total time spent by all users watching videos | 
**avg_percent_watched** | **float** | Average percentage of videos watched per user per course | 
**avg_time_watched** | **float** | Average time spent per learner | 

## Example

```python
from iblai.models.video_engagement_per_course_data import VideoEngagementPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of VideoEngagementPerCourseData from a JSON string
video_engagement_per_course_data_instance = VideoEngagementPerCourseData.from_json(json)
# print the JSON string representation of the object
print(VideoEngagementPerCourseData.to_json())

# convert the object into a dict
video_engagement_per_course_data_dict = video_engagement_per_course_data_instance.to_dict()
# create an instance of VideoEngagementPerCourseData from a dict
video_engagement_per_course_data_from_dict = VideoEngagementPerCourseData.from_dict(video_engagement_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


