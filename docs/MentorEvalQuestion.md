# MentorEvalQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**content** | **str** |  | 
**sample_answer** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_eval_question import MentorEvalQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of MentorEvalQuestion from a JSON string
mentor_eval_question_instance = MentorEvalQuestion.from_json(json)
# print the JSON string representation of the object
print(MentorEvalQuestion.to_json())

# convert the object into a dict
mentor_eval_question_dict = mentor_eval_question_instance.to_dict()
# create an instance of MentorEvalQuestion from a dict
mentor_eval_question_from_dict = MentorEvalQuestion.from_dict(mentor_eval_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


