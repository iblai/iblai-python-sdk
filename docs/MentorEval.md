# MentorEval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor** | **str** |  | [readonly] 
**questions** | [**List[MentorEvalQuestion]**](MentorEvalQuestion.md) |  | [readonly] 
**eval_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**passing_score** | **int** |  | [optional] 
**evaluation_prompt** | **str** |  | [optional] 
**question_set** | **int** |  | [optional] 

## Example

```python
from iblai.models.mentor_eval import MentorEval

# TODO update the JSON string below
json = "{}"
# create an instance of MentorEval from a JSON string
mentor_eval_instance = MentorEval.from_json(json)
# print the JSON string representation of the object
print(MentorEval.to_json())

# convert the object into a dict
mentor_eval_dict = mentor_eval_instance.to_dict()
# create an instance of MentorEval from a dict
mentor_eval_from_dict = MentorEval.from_dict(mentor_eval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


