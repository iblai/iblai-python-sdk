# LLMModelForTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**llm_provider** | **str** |  | 
**llm_name** | **str** |  | 
**tenant** | **int** |  | [optional] 

## Example

```python
from iblai.models.llm_model_for_tenant import LLMModelForTenant

# TODO update the JSON string below
json = "{}"
# create an instance of LLMModelForTenant from a JSON string
llm_model_for_tenant_instance = LLMModelForTenant.from_json(json)
# print the JSON string representation of the object
print(LLMModelForTenant.to_json())

# convert the object into a dict
llm_model_for_tenant_dict = llm_model_for_tenant_instance.to_dict()
# create an instance of LLMModelForTenant from a dict
llm_model_for_tenant_from_dict = LLMModelForTenant.from_dict(llm_model_for_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


