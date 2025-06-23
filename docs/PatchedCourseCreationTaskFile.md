# PatchedCourseCreationTaskFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**course_creation_task** | **int** |  | [optional] 
**file** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] [readonly] 
**last_modified** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_course_creation_task_file import PatchedCourseCreationTaskFile

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedCourseCreationTaskFile from a JSON string
patched_course_creation_task_file_instance = PatchedCourseCreationTaskFile.from_json(json)
# print the JSON string representation of the object
print(PatchedCourseCreationTaskFile.to_json())

# convert the object into a dict
patched_course_creation_task_file_dict = patched_course_creation_task_file_instance.to_dict()
# create an instance of PatchedCourseCreationTaskFile from a dict
patched_course_creation_task_file_from_dict = PatchedCourseCreationTaskFile.from_dict(patched_course_creation_task_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


