# LLMScoresViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**trace_id** | **str** |  | 
**name** | **str** |  | 
**value** | **float** |  | 
**observation_id** | **str** |  | 
**timestamp** | **datetime** |  | 
**comment** | **str** |  | 

## Example

```python
from iblai.models.llm_scores_view_response import LLMScoresViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LLMScoresViewResponse from a JSON string
llm_scores_view_response_instance = LLMScoresViewResponse.from_json(json)
# print the JSON string representation of the object
print(LLMScoresViewResponse.to_json())

# convert the object into a dict
llm_scores_view_response_dict = llm_scores_view_response_instance.to_dict()
# create an instance of LLMScoresViewResponse from a dict
llm_scores_view_response_from_dict = LLMScoresViewResponse.from_dict(llm_scores_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


