# MathQuestionWithAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**topic** | [**Topic**](Topic.md) |  | 
**sub_topic** | [**SubTopic**](SubTopic.md) |  | 
**skills_assessed** | [**List[Skill]**](Skill.md) |  | 
**content** | **str** |  | 
**difficulty** | **int** |  | [optional] 
**cognitive_skills** | [**MathQuestionCognitiveSkills**](MathQuestionCognitiveSkills.md) |  | [optional] 
**grade** | **int** |  | [optional] 
**expected_time_to_solve** | **str** |  | [optional] 
**related_concepts** | **str** |  | [optional] 
**hints_provided** | **str** |  | [optional] 
**learning_outcomes** | **str** |  | [optional] 
**prerequisites** | **str** |  | [optional] 
**recommended_grade_level** | **str** |  | [optional] 
**expected_answer** | **str** | The answer to the math problem | [optional] 
**image** | **str** |  | [optional] 
**answer_image** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**platform** | **int** |  | [optional] 

## Example

```python
from iblai.models.math_question_with_answer import MathQuestionWithAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of MathQuestionWithAnswer from a JSON string
math_question_with_answer_instance = MathQuestionWithAnswer.from_json(json)
# print the JSON string representation of the object
print(MathQuestionWithAnswer.to_json())

# convert the object into a dict
math_question_with_answer_dict = math_question_with_answer_instance.to_dict()
# create an instance of MathQuestionWithAnswer from a dict
math_question_with_answer_from_dict = MathQuestionWithAnswer.from_dict(math_question_with_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


