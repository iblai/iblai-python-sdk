# VideosSpecificCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Course name | 
**id** | **str** | Video Id | 
**duration** | **int** | Video duration | 
**total_time** | **int** | Total time spent by users watching | 
**total_users** | **int** | Total users who have watched this video | 
**average_time** | **float** | Average time spent per learner | 

## Example

```python
from iblai.models.videos_specific_course_data import VideosSpecificCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of VideosSpecificCourseData from a JSON string
videos_specific_course_data_instance = VideosSpecificCourseData.from_json(json)
# print the JSON string representation of the object
print(VideosSpecificCourseData.to_json())

# convert the object into a dict
videos_specific_course_data_dict = videos_specific_course_data_instance.to_dict()
# create an instance of VideosSpecificCourseData from a dict
videos_specific_course_data_from_dict = VideosSpecificCourseData.from_dict(videos_specific_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


