# LLMResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**resource_ids** | **object** |  | [optional] 
**tags** | **object** |  | [optional] 
**overview** | **str** |  | [optional] 
**use_cases** | **str** |  | [optional] 
**documentation** | **str** |  | [optional] 
**sdk_samples** | **str** |  | [optional] 
**chat_models** | **object** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from iblai.models.llm_response import LLMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LLMResponse from a JSON string
llm_response_instance = LLMResponse.from_json(json)
# print the JSON string representation of the object
print(LLMResponse.to_json())

# convert the object into a dict
llm_response_dict = llm_response_instance.to_dict()
# create an instance of LLMResponse from a dict
llm_response_from_dict = LLMResponse.from_dict(llm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


