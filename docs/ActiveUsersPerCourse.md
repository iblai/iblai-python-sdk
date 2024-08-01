# ActiveUsersPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActiveUsersPerCourseData]**](ActiveUsersPerCourseData.md) |  | 
**total** | **int** | Total unique active users in this period | 
**meta** | [**OvertimeMeta**](OvertimeMeta.md) |  | 

## Example

```python
from iblai.models.active_users_per_course import ActiveUsersPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveUsersPerCourse from a JSON string
active_users_per_course_instance = ActiveUsersPerCourse.from_json(json)
# print the JSON string representation of the object
print(ActiveUsersPerCourse.to_json())

# convert the object into a dict
active_users_per_course_dict = active_users_per_course_instance.to_dict()
# create an instance of ActiveUsersPerCourse from a dict
active_users_per_course_from_dict = ActiveUsersPerCourse.from_dict(active_users_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


