# VideoEngagementPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VideoEngagementPerCourseData]**](VideoEngagementPerCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.video_engagement_per_course import VideoEngagementPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of VideoEngagementPerCourse from a JSON string
video_engagement_per_course_instance = VideoEngagementPerCourse.from_json(json)
# print the JSON string representation of the object
print(VideoEngagementPerCourse.to_json())

# convert the object into a dict
video_engagement_per_course_dict = video_engagement_per_course_instance.to_dict()
# create an instance of VideoEngagementPerCourse from a dict
video_engagement_per_course_from_dict = VideoEngagementPerCourse.from_dict(video_engagement_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


