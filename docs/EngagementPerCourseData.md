# EngagementPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | edx Course Id | 
**course_start** | **str** | Course start date | 
**course_end** | **str** | Course end date | 
**average_days** | **int** | Average days spent by each learners on the course | 
**average_time_spent** | **float** | Average days spent by learner on the course | 
**name** | **str** | Course name | 

## Example

```python
from iblai.models.engagement_per_course_data import EngagementPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of EngagementPerCourseData from a JSON string
engagement_per_course_data_instance = EngagementPerCourseData.from_json(json)
# print the JSON string representation of the object
print(EngagementPerCourseData.to_json())

# convert the object into a dict
engagement_per_course_data_dict = engagement_per_course_data_instance.to_dict()
# create an instance of EngagementPerCourseData from a dict
engagement_per_course_data_from_dict = EngagementPerCourseData.from_dict(engagement_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


