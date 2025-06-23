# PromptFacet

Serializer for prompt facets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of prompts in this facet | 
**terms** | **Dict[str, object]** | Terms and their counts in this facet | 
**other** | **int** | Count of prompts not in any term | 

## Example

```python
from iblai.models.prompt_facet import PromptFacet

# TODO update the JSON string below
json = "{}"
# create an instance of PromptFacet from a JSON string
prompt_facet_instance = PromptFacet.from_json(json)
# print the JSON string representation of the object
print(PromptFacet.to_json())

# convert the object into a dict
prompt_facet_dict = prompt_facet_instance.to_dict()
# create an instance of PromptFacet from a dict
prompt_facet_from_dict = PromptFacet.from_dict(prompt_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


