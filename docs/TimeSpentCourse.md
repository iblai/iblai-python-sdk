# TimeSpentCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** |  | 
**course_name** | **str** |  | 
**platform** | **str** |  | 
**time_spent** | **str** |  | 
**time_spent_secs** | **int** |  | 

## Example

```python
from iblai.models.time_spent_course import TimeSpentCourse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpentCourse from a JSON string
time_spent_course_instance = TimeSpentCourse.from_json(json)
# print the JSON string representation of the object
print(TimeSpentCourse.to_json())

# convert the object into a dict
time_spent_course_dict = time_spent_course_instance.to_dict()
# create an instance of TimeSpentCourse from a dict
time_spent_course_from_dict = TimeSpentCourse.from_dict(time_spent_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


