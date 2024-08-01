# GuidedPromptsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_prompts** | **List[str]** |  | 

## Example

```python
from iblai.models.guided_prompts_response import GuidedPromptsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuidedPromptsResponse from a JSON string
guided_prompts_response_instance = GuidedPromptsResponse.from_json(json)
# print the JSON string representation of the object
print(GuidedPromptsResponse.to_json())

# convert the object into a dict
guided_prompts_response_dict = guided_prompts_response_instance.to_dict()
# create an instance of GuidedPromptsResponse from a dict
guided_prompts_response_from_dict = GuidedPromptsResponse.from_dict(guided_prompts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


