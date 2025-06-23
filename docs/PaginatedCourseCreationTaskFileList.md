# PaginatedCourseCreationTaskFileList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md) |  | 

## Example

```python
from iblai.models.paginated_course_creation_task_file_list import PaginatedCourseCreationTaskFileList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseCreationTaskFileList from a JSON string
paginated_course_creation_task_file_list_instance = PaginatedCourseCreationTaskFileList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseCreationTaskFileList.to_json())

# convert the object into a dict
paginated_course_creation_task_file_list_dict = paginated_course_creation_task_file_list_instance.to_dict()
# create an instance of PaginatedCourseCreationTaskFileList from a dict
paginated_course_creation_task_file_list_from_dict = PaginatedCourseCreationTaskFileList.from_dict(paginated_course_creation_task_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


