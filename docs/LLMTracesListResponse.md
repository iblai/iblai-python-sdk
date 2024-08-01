# LLMTracesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**var_date** | **datetime** |  | 

## Example

```python
from iblai.models.llm_traces_list_response import LLMTracesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LLMTracesListResponse from a JSON string
llm_traces_list_response_instance = LLMTracesListResponse.from_json(json)
# print the JSON string representation of the object
print(LLMTracesListResponse.to_json())

# convert the object into a dict
llm_traces_list_response_dict = llm_traces_list_response_instance.to_dict()
# create an instance of LLMTracesListResponse from a dict
llm_traces_list_response_from_dict = LLMTracesListResponse.from_dict(llm_traces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


