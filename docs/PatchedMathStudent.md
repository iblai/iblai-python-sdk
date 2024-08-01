# PatchedMathStudent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**student** | **int** | edX user ID | [optional] [readonly] 
**level** | **int** |  | [optional] [readonly] 
**points** | **int** |  | [optional] [readonly] 
**correct_questions_for_level** | **int** | Number of correctly answered questions at the student&#39;s current level | [optional] [readonly] 
**no_incorrect_questions_for_level** | **int** | Number of incorrectly answered questions at the student&#39;s current level | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**acquired_skills** | **str** |  | [optional] [readonly] 

## Example

```python
from iblai.models.patched_math_student import PatchedMathStudent

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMathStudent from a JSON string
patched_math_student_instance = PatchedMathStudent.from_json(json)
# print the JSON string representation of the object
print(PatchedMathStudent.to_json())

# convert the object into a dict
patched_math_student_dict = patched_math_student_instance.to_dict()
# create an instance of PatchedMathStudent from a dict
patched_math_student_from_dict = PatchedMathStudent.from_dict(patched_math_student_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


