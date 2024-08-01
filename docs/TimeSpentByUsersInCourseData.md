# TimeSpentByUsersInCourseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**full_name** | **str** | learner Name | 
**email** | **str** | learner email | 
**assessments** | **int** | Total assessments | 
**time_spent** | **str** | Time spent formatted in seconds | 

## Example

```python
from iblai.models.time_spent_by_users_in_course_data import TimeSpentByUsersInCourseData

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentByUsersInCourseData from a JSON string
time_spent_by_users_in_course_data_instance = TimeSpentByUsersInCourseData.from_json(json)
# print the JSON string representation of the object
print(TimeSpentByUsersInCourseData.to_json())

# convert the object into a dict
time_spent_by_users_in_course_data_dict = time_spent_by_users_in_course_data_instance.to_dict()
# create an instance of TimeSpentByUsersInCourseData from a dict
time_spent_by_users_in_course_data_from_dict = TimeSpentByUsersInCourseData.from_dict(time_spent_by_users_in_course_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


