# LLMTraceDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace** | [**Trace**](Trace.md) |  | [optional] 

## Example

```python
from iblai.models.llm_trace_detail import LLMTraceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LLMTraceDetail from a JSON string
llm_trace_detail_instance = LLMTraceDetail.from_json(json)
# print the JSON string representation of the object
print(LLMTraceDetail.to_json())

# convert the object into a dict
llm_trace_detail_dict = llm_trace_detail_instance.to_dict()
# create an instance of LLMTraceDetail from a dict
llm_trace_detail_from_dict = LLMTraceDetail.from_dict(llm_trace_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


