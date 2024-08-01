# MathQuestion


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
**image** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**platform** | **int** |  | [optional] 

## Example

```python
from iblai.models.math_question import MathQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of MathQuestion from a JSON string
math_question_instance = MathQuestion.from_json(json)
# print the JSON string representation of the object
print(MathQuestion.to_json())

# convert the object into a dict
math_question_dict = math_question_instance.to_dict()
# create an instance of MathQuestion from a dict
math_question_from_dict = MathQuestion.from_dict(math_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


