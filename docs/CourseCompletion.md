# CourseCompletion

Serializer for course completion data used in both request and response. Inherits common completion fields from CompletableBaseSerializer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_percentage** | **float** | Completion percentage | [optional] 
**completed** | **bool** | Whether completable is completed | [optional] [default to False]
**last_updated** | **datetime** | Last update timestamp | [readonly] 
**completion_date** | **datetime** | Completion timestamp | [optional] 
**completion_data** | **object** | Completion metadata | [optional] 
**skill_points_computed** | **bool** | Whether skill points have been evaluated | [optional] [default to False]
**id** | **int** | Unique identifier for the completion record | [readonly] 
**user_id** | **int** | The user identifier | 
**username** | **str** | The username associated with the completion | [readonly] 
**course_id** | **str** | The course identifier (e.g., &#39;course-v1:org+code+run&#39;) | 
**org** | **str** | The organization identifier for the course | [readonly] 
**passed** | **bool** | Whether the user passed the course | [optional] 
**grading_percentage** | **float** | The user&#39;s grade in the course | [optional] 
**passed_date** | **datetime** | The date the course was passed (ISO format) | [optional] 
**grade_data** | **object** | Additional grading metadata | [optional] 

## Example

```python
from iblai.models.course_completion import CourseCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCompletion from a JSON string
course_completion_instance = CourseCompletion.from_json(json)
# print the JSON string representation of the object
print(CourseCompletion.to_json())

# convert the object into a dict
course_completion_dict = course_completion_instance.to_dict()
# create an instance of CourseCompletion from a dict
course_completion_from_dict = CourseCompletion.from_dict(course_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


