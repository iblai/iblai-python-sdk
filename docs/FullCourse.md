# FullCourse


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
**sections** | [**List[SectionWithChildren]**](SectionWithChildren.md) |  | 

## Example

```python
from iblai.models.full_course import FullCourse

# TODO update the JSON string below
json = "{}"
# create an instance of FullCourse from a JSON string
full_course_instance = FullCourse.from_json(json)
# print the JSON string representation of the object
print(FullCourse.to_json())

# convert the object into a dict
full_course_dict = full_course_instance.to_dict()
# create an instance of FullCourse from a dict
full_course_from_dict = FullCourse.from_dict(full_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


