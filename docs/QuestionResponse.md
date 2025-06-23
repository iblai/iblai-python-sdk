# QuestionResponse

Serializer for the response data that returns additional questions.  Attributes:     follow_up_questions (list[LLMQuestionSerializer]): List of generated follow-up questions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**questions** | [**List[LLMQuestion]**](LLMQuestion.md) |  | 

## Example

```python
from iblai.models.question_response import QuestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionResponse from a JSON string
question_response_instance = QuestionResponse.from_json(json)
# print the JSON string representation of the object
print(QuestionResponse.to_json())

# convert the object into a dict
question_response_dict = question_response_instance.to_dict()
# create an instance of QuestionResponse from a dict
question_response_from_dict = QuestionResponse.from_dict(question_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


