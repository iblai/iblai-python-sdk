# Answer

Serializer for an individual answer choice for a question.  Attributes:     text (str): The text of the answer.     is_correct (Optional[bool]): Boolean indicating if this answer is correct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**is_correct** | **bool** |  | [optional] [default to False]

## Example

```python
from iblai.models.answer import Answer

# TODO update the JSON string below
json = "{}"
# create an instance of Answer from a JSON string
answer_instance = Answer.from_json(json)
# print the JSON string representation of the object
print(Answer.to_json())

# convert the object into a dict
answer_dict = answer_instance.to_dict()
# create an instance of Answer from a dict
answer_from_dict = Answer.from_dict(answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


