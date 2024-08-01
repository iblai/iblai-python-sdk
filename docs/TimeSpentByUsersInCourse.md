# TimeSpentByUsersInCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeSpentByUsersInCourseData]**](TimeSpentByUsersInCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.time_spent_by_users_in_course import TimeSpentByUsersInCourse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentByUsersInCourse from a JSON string
time_spent_by_users_in_course_instance = TimeSpentByUsersInCourse.from_json(json)
# print the JSON string representation of the object
print(TimeSpentByUsersInCourse.to_json())

# convert the object into a dict
time_spent_by_users_in_course_dict = time_spent_by_users_in_course_instance.to_dict()
# create an instance of TimeSpentByUsersInCourse from a dict
time_spent_by_users_in_course_from_dict = TimeSpentByUsersInCourse.from_dict(time_spent_by_users_in_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


