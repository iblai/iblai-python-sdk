# PerlearnerEngagementVideosData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | Edx Course ID | 
**name** | **str** | Course Name | 
**total_videos** | **int** | Total course videos | 
**watched** | **int** | Total videos watched by student | 
**total_time_watch** | **int** | Total time user watched video | 
**average_class_watch** | **float** | Average videos watched by students in course | 
**class_time_average** | **float** | Average time spent by students on this course | 

## Example

```python
from iblai.models.perlearner_engagement_videos_data import PerlearnerEngagementVideosData

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerEngagementVideosData from a JSON string
perlearner_engagement_videos_data_instance = PerlearnerEngagementVideosData.from_json(json)
# print the JSON string representation of the object
print(PerlearnerEngagementVideosData.to_json())

# convert the object into a dict
perlearner_engagement_videos_data_dict = perlearner_engagement_videos_data_instance.to_dict()
# create an instance of PerlearnerEngagementVideosData from a dict
perlearner_engagement_videos_data_from_dict = PerlearnerEngagementVideosData.from_dict(perlearner_engagement_videos_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


