# PerLearnerCourseVideosWatched


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PerLearnerCourseVideosWatchedData]**](PerLearnerCourseVideosWatchedData.md) |  | 
**total** | **int** | videos watched | 

## Example

```python
from iblai.models.per_learner_course_videos_watched import PerLearnerCourseVideosWatched

# TODO update the JSON string below
json = "{}"
# create an instance of PerLearnerCourseVideosWatched from a JSON string
per_learner_course_videos_watched_instance = PerLearnerCourseVideosWatched.from_json(json)
# print the JSON string representation of the object
print(PerLearnerCourseVideosWatched.to_json())

# convert the object into a dict
per_learner_course_videos_watched_dict = per_learner_course_videos_watched_instance.to_dict()
# create an instance of PerLearnerCourseVideosWatched from a dict
per_learner_course_videos_watched_from_dict = PerLearnerCourseVideosWatched.from_dict(per_learner_course_videos_watched_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


