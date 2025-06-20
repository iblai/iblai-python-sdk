# LLMQuestion

Serializer for individual question data, including possible answers.  Attributes:     question_id (str): Unique identifier for the question.     text (str): The text of the question.     difficulty_level (Optional[int]): An optional difficulty level for the question.     options (list[AnswerSerializer]): List of possible answers for the question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**difficulty_level** | **int** |  | [optional] 
**options** | [**List[Answer]**](Answer.md) |  | 

## Example

```python
from iblai.models.llm_question import LLMQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of LLMQuestion from a JSON string
llm_question_instance = LLMQuestion.from_json(json)
# print the JSON string representation of the object
print(LLMQuestion.to_json())

# convert the object into a dict
llm_question_dict = llm_question_instance.to_dict()
# create an instance of LLMQuestion from a dict
llm_question_from_dict = LLMQuestion.from_dict(llm_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


