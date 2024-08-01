# TimeSpentPerCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeSpentPerCourseData]**](TimeSpentPerCourseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.time_spent_per_course import TimeSpentPerCourse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentPerCourse from a JSON string
time_spent_per_course_instance = TimeSpentPerCourse.from_json(json)
# print the JSON string representation of the object
print(TimeSpentPerCourse.to_json())

# convert the object into a dict
time_spent_per_course_dict = time_spent_per_course_instance.to_dict()
# create an instance of TimeSpentPerCourse from a dict
time_spent_per_course_from_dict = TimeSpentPerCourse.from_dict(time_spent_per_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


