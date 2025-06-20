# MentorEvalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**passing_score** | **int** |  | [optional] 
**questions** | [**List[MentorEvalQuestionRequest]**](MentorEvalQuestionRequest.md) |  | [optional] 
**evaluation_prompt** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_eval_request import MentorEvalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentorEvalRequest from a JSON string
mentor_eval_request_instance = MentorEvalRequest.from_json(json)
# print the JSON string representation of the object
print(MentorEvalRequest.to_json())

# convert the object into a dict
mentor_eval_request_dict = mentor_eval_request_instance.to_dict()
# create an instance of MentorEvalRequest from a dict
mentor_eval_request_from_dict = MentorEvalRequest.from_dict(mentor_eval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


