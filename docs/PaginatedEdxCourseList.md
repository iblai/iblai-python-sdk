# PaginatedEdxCourseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[EdxCourse]**](EdxCourse.md) |  | 

## Example

```python
from iblai.models.paginated_edx_course_list import PaginatedEdxCourseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEdxCourseList from a JSON string
paginated_edx_course_list_instance = PaginatedEdxCourseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEdxCourseList.to_json())

# convert the object into a dict
paginated_edx_course_list_dict = paginated_edx_course_list_instance.to_dict()
# create an instance of PaginatedEdxCourseList from a dict
paginated_edx_course_list_from_dict = PaginatedEdxCourseList.from_dict(paginated_edx_course_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


