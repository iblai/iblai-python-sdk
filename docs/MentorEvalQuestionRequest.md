# MentorEvalQuestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**sample_answer** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_eval_question_request import MentorEvalQuestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorEvalQuestionRequest from a JSON string
mentor_eval_question_request_instance = MentorEvalQuestionRequest.from_json(json)
# print the JSON string representation of the object
print(MentorEvalQuestionRequest.to_json())

# convert the object into a dict
mentor_eval_question_request_dict = mentor_eval_question_request_instance.to_dict()
# create an instance of MentorEvalQuestionRequest from a dict
mentor_eval_question_request_from_dict = MentorEvalQuestionRequest.from_dict(mentor_eval_question_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


