# LLMScoresView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_scores_tracked** | **int** |  | 
**scores_summary** | [**List[ScoreSummary]**](ScoreSummary.md) |  | 
**scores** | [**List[Score]**](Score.md) |  | 

## Example

```python
from iblai.models.llm_scores_view import LLMScoresView

# TODO update the JSON string below
json = "{}"
# create an instance of LLMScoresView from a JSON string
llm_scores_view_instance = LLMScoresView.from_json(json)
# print the JSON string representation of the object
print(LLMScoresView.to_json())

# convert the object into a dict
llm_scores_view_dict = llm_scores_view_instance.to_dict()
# create an instance of LLMScoresView from a dict
llm_scores_view_from_dict = LLMScoresView.from_dict(llm_scores_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


