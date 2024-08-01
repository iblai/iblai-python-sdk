# TimeSpentPerCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Course name | 
**course_id** | **str** | Edx Course Id | 
**time_spent** | **int** | Total time spent | 
**course_start** | **str** | Course Start | 
**course_end** | **str** | Course End | 
**average_time** | **float** | Average time spent | 

## Example

```python
from iblai.models.time_spent_per_course_data import TimeSpentPerCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentPerCourseData from a JSON string
time_spent_per_course_data_instance = TimeSpentPerCourseData.from_json(json)
# print the JSON string representation of the object
print(TimeSpentPerCourseData.to_json())

# convert the object into a dict
time_spent_per_course_data_dict = time_spent_per_course_data_instance.to_dict()
# create an instance of TimeSpentPerCourseData from a dict
time_spent_per_course_data_from_dict = TimeSpentPerCourseData.from_dict(time_spent_per_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


