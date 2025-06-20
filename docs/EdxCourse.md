# EdxCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**run** | **str** |  | 
**number** | **str** |  | 
**description** | **str** |  | [optional] 
**xblock_id** | **str** |  | 
**task** | **int** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.edx_course import EdxCourse

# TODO update the JSON string below
json = "{}"
# create an instance of EdxCourse from a JSON string
edx_course_instance = EdxCourse.from_json(json)
# print the JSON string representation of the object
print(EdxCourse.to_json())

# convert the object into a dict
edx_course_dict = edx_course_instance.to_dict()
# create an instance of EdxCourse from a dict
edx_course_from_dict = EdxCourse.from_dict(edx_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


