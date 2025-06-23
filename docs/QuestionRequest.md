# QuestionRequest

Serializer for incoming request data that includes initial questions and the username.  Attributes:     username (str): Username of the requesting student or user.     initial_questions (list[InputQuestionSerializer]): List of initial questions provided by the LMS.     question_count (int): Number of questions the mentor (llm) should generate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**initial_questions** | [**List[InputQuestion]**](InputQuestion.md) |  | 
**question_count** | **int** |  | [optional] [default to 20]
**subject** | **str** |  | 

## Example

```python
from iblai.models.question_request import QuestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionRequest from a JSON string
question_request_instance = QuestionRequest.from_json(json)
# print the JSON string representation of the object
print(QuestionRequest.to_json())

# convert the object into a dict
question_request_dict = question_request_instance.to_dict()
# create an instance of QuestionRequest from a dict
question_request_from_dict = QuestionRequest.from_dict(question_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


