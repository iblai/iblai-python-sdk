# CourseCreationTaskFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**course_creation_task** | **int** |  | 
**file** | **str** |  | 
**date_created** | **datetime** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.course_creation_task_file import CourseCreationTaskFile

# TODO update the JSON string below
json = "{}"
# create an instance of CourseCreationTaskFile from a JSON string
course_creation_task_file_instance = CourseCreationTaskFile.from_json(json)
# print the JSON string representation of the object
print(CourseCreationTaskFile.to_json())

# convert the object into a dict
course_creation_task_file_dict = course_creation_task_file_instance.to_dict()
# create an instance of CourseCreationTaskFile from a dict
course_creation_task_file_from_dict = CourseCreationTaskFile.from_dict(course_creation_task_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


