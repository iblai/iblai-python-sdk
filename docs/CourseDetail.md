# CourseDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** |  | 
**name** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**enrollment** | [**EnrollmentInfo**](EnrollmentInfo.md) |  | 
**completion** | [**CourseCompletion**](CourseCompletion.md) |  | [optional] 
**time_spent** | **str** | Total time spent on this course in human-readable format (e.g., &#39;1h 30m&#39;) | [optional] 
**time_spent_secs** | **int** | Total time spent on this course in seconds | [optional] 

## Example

```python
from iblai.models.course_detail import CourseDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseDetail from a JSON string
course_detail_instance = CourseDetail.from_json(json)
# print the JSON string representation of the object
print(CourseDetail.to_json())

# convert the object into a dict
course_detail_dict = course_detail_instance.to_dict()
# create an instance of CourseDetail from a dict
course_detail_from_dict = CourseDetail.from_dict(course_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


