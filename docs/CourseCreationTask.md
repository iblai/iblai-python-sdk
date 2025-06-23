# CourseCreationTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user_id** | **str** |  | [readonly] 
**student** | **int** | edX user ID | [readonly] 
**name** | **str** |  | 
**description** | **str** | Description of the course to create and its requirements | 
**target_audience** | **str** | The intended audience for the course. eg. Grade 11 students. | 
**platform** | **int** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**status** | [**CourseCreationTaskStatusEnum**](CourseCreationTaskStatusEnum.md) |  | [readonly] 
**publish_course** | **bool** |  | [optional] 
**course_data** | **object** |  | [readonly] 
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**desired_number_of_sections** | **int** |  | [optional] 
**logs** | **str** |  | [readonly] 
**files** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md) |  | [readonly] 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.course_creation_task import CourseCreationTask

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCreationTask from a JSON string
course_creation_task_instance = CourseCreationTask.from_json(json)
# print the JSON string representation of the object
print(CourseCreationTask.to_json())

# convert the object into a dict
course_creation_task_dict = course_creation_task_instance.to_dict()
# create an instance of CourseCreationTask from a dict
course_creation_task_from_dict = CourseCreationTask.from_dict(course_creation_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


