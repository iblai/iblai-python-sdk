# LLMScoresViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**trace_id** | **str** |  | 
**name** | **str** |  | 
**value** | **float** |  | 
**observation_id** | **str** |  | 
**comment** | **str** |  | 

## Example

```python
from iblai.models.llm_scores_view_request import LLMScoresViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LLMScoresViewRequest from a JSON string
llm_scores_view_request_instance = LLMScoresViewRequest.from_json(json)
# print the JSON string representation of the object
print(LLMScoresViewRequest.to_json())

# convert the object into a dict
llm_scores_view_request_dict = llm_scores_view_request_instance.to_dict()
# create an instance of LLMScoresViewRequest from a dict
llm_scores_view_request_from_dict = LLMScoresViewRequest.from_dict(llm_scores_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


