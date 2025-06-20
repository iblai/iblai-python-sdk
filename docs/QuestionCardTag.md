# QuestionCardTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**difficulty** | **int** |  | 
**total_cards** | **int** |  | [readonly] 
**correct_answers** | **int** |  | [readonly] 
**correct_rate** | **float** |  | [readonly] 

## Example

```python
from iblai.models.question_card_tag import QuestionCardTag

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionCardTag from a JSON string
question_card_tag_instance = QuestionCardTag.from_json(json)
# print the JSON string representation of the object
print(QuestionCardTag.to_json())

# convert the object into a dict
question_card_tag_dict = question_card_tag_instance.to_dict()
# create an instance of QuestionCardTag from a dict
question_card_tag_from_dict = QuestionCardTag.from_dict(question_card_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


