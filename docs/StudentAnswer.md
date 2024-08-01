# StudentAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**math_student** | [**MathStudent**](MathStudent.md) |  | 
**question** | [**MathQuestionWithAnswer**](MathQuestionWithAnswer.md) |  | 
**answer** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**is_correct** | **bool** |  | [optional] 
**score** | **int** |  | [optional] 
**feedback** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.student_answer import StudentAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of StudentAnswer from a JSON string
student_answer_instance = StudentAnswer.from_json(json)
# print the JSON string representation of the object
print(StudentAnswer.to_json())

# convert the object into a dict
student_answer_dict = student_answer_instance.to_dict()
# create an instance of StudentAnswer from a dict
student_answer_from_dict = StudentAnswer.from_dict(student_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


