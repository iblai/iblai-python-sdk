# MathStudent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**student** | **int** | edX user ID | [readonly] 
**level** | **int** |  | [readonly] 
**points** | **int** |  | [readonly] 
**correct_questions_for_level** | **int** | Number of correctly answered questions at the student&#39;s current level | [readonly] 
**no_incorrect_questions_for_level** | **int** | Number of incorrectly answered questions at the student&#39;s current level | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**acquired_skills** | **str** |  | [readonly] 

## Example

```python
from iblai.models.math_student import MathStudent

# TODO update the JSON string below
json = "{}"
# create an instance of MathStudent from a JSON string
math_student_instance = MathStudent.from_json(json)
# print the JSON string representation of the object
print(MathStudent.to_json())

# convert the object into a dict
math_student_dict = math_student_instance.to_dict()
# create an instance of MathStudent from a dict
math_student_from_dict = MathStudent.from_dict(math_student_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


