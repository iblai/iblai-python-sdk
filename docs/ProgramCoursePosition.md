# ProgramCoursePosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**position** | **int** |  | [readonly] 

## Example

```python
from iblai.models.program_course_position import ProgramCoursePosition

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramCoursePosition from a JSON string
program_course_position_instance = ProgramCoursePosition.from_json(json)
# print the JSON string representation of the object
print(ProgramCoursePosition.to_json())

# convert the object into a dict
program_course_position_dict = program_course_position_instance.to_dict()
# create an instance of ProgramCoursePosition from a dict
program_course_position_from_dict = ProgramCoursePosition.from_dict(program_course_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


