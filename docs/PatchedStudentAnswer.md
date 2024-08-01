# PatchedStudentAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**math_student** | [**MathStudent**](MathStudent.md) |  | [optional] 
**question** | [**MathQuestionWithAnswer**](MathQuestionWithAnswer.md) |  | [optional] 
**answer** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**is_correct** | **bool** |  | [optional] 
**score** | **int** |  | [optional] 
**feedback** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_student_answer import PatchedStudentAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedStudentAnswer from a JSON string
patched_student_answer_instance = PatchedStudentAnswer.from_json(json)
# print the JSON string representation of the object
print(PatchedStudentAnswer.to_json())

# convert the object into a dict
patched_student_answer_dict = patched_student_answer_instance.to_dict()
# create an instance of PatchedStudentAnswer from a dict
patched_student_answer_from_dict = PatchedStudentAnswer.from_dict(patched_student_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


