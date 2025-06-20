# InputQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**difficulty_level** | **int** |  | [optional] 
**possible_answers** | [**List[IntialQuestionAnswer]**](IntialQuestionAnswer.md) |  | 

## Example

```python
from iblai.models.input_question import InputQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of InputQuestion from a JSON string
input_question_instance = InputQuestion.from_json(json)
# print the JSON string representation of the object
print(InputQuestion.to_json())

# convert the object into a dict
input_question_dict = input_question_instance.to_dict()
# create an instance of InputQuestion from a dict
input_question_from_dict = InputQuestion.from_dict(input_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


