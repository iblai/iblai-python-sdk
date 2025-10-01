# GuidedPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**icon** | **str** |  | 

## Example

```python
from iblai.models.guided_prompt import GuidedPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of GuidedPrompt from a JSON string
guided_prompt_instance = GuidedPrompt.from_json(json)
# print the JSON string representation of the object
print(GuidedPrompt.to_json())

# convert the object into a dict
guided_prompt_dict = guided_prompt_instance.to_dict()
# create an instance of GuidedPrompt from a dict
guided_prompt_from_dict = GuidedPrompt.from_dict(guided_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


