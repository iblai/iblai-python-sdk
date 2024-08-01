# PatchedMathQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**topic** | [**Topic**](Topic.md) |  | [optional] 
**sub_topic** | [**SubTopic**](SubTopic.md) |  | [optional] 
**skills_assessed** | [**List[Skill]**](Skill.md) |  | [optional] 
**content** | **str** |  | [optional] 
**difficulty** | **int** |  | [optional] 
**cognitive_skills** | [**MathQuestionCognitiveSkills**](MathQuestionCognitiveSkills.md) |  | [optional] 
**grade** | **int** |  | [optional] 
**expected_time_to_solve** | **str** |  | [optional] 
**related_concepts** | **str** |  | [optional] 
**hints_provided** | **str** |  | [optional] 
**learning_outcomes** | **str** |  | [optional] 
**prerequisites** | **str** |  | [optional] 
**recommended_grade_level** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**platform** | **int** |  | [optional] 

## Example

```python
from iblai.models.patched_math_question import PatchedMathQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMathQuestion from a JSON string
patched_math_question_instance = PatchedMathQuestion.from_json(json)
# print the JSON string representation of the object
print(PatchedMathQuestion.to_json())

# convert the object into a dict
patched_math_question_dict = patched_math_question_instance.to_dict()
# create an instance of PatchedMathQuestion from a dict
patched_math_question_from_dict = PatchedMathQuestion.from_dict(patched_math_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


