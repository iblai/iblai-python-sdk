# SpacedRepetitionQuestionStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_questions** | **int** |  | [readonly] 
**success_rate** | **float** |  | [readonly] 
**reviewed_questions** | **int** |  | [readonly] 

## Example

```python
from iblai.models.spaced_repetition_question_stats import SpacedRepetitionQuestionStats

# TODO update the JSON string below
json = "{}"
# create an instance of SpacedRepetitionQuestionStats from a JSON string
spaced_repetition_question_stats_instance = SpacedRepetitionQuestionStats.from_json(json)
# print the JSON string representation of the object
print(SpacedRepetitionQuestionStats.to_json())

# convert the object into a dict
spaced_repetition_question_stats_dict = spaced_repetition_question_stats_instance.to_dict()
# create an instance of SpacedRepetitionQuestionStats from a dict
spaced_repetition_question_stats_from_dict = SpacedRepetitionQuestionStats.from_dict(spaced_repetition_question_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


