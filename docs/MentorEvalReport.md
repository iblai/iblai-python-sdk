# MentorEvalReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**mentor_eval** | **str** |  | [readonly] 
**mentor** | **str** |  | [readonly] 
**conversation_ratings** | [**List[ConversationRating]**](ConversationRating.md) |  | [readonly] 
**overall_score** | **float** |  | [readonly] 
**is_passed** | **bool** |  | [readonly] 
**generated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.mentor_eval_report import MentorEvalReport

# TODO update the JSON string below
json = "{}"
# create an instance of MentorEvalReport from a JSON string
mentor_eval_report_instance = MentorEvalReport.from_json(json)
# print the JSON string representation of the object
print(MentorEvalReport.to_json())

# convert the object into a dict
mentor_eval_report_dict = mentor_eval_report_instance.to_dict()
# create an instance of MentorEvalReport from a dict
mentor_eval_report_from_dict = MentorEvalReport.from_dict(mentor_eval_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


