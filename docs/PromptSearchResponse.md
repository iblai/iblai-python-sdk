# PromptSearchResponse

Response serializer for PromptSearchView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Prompt]**](Prompt.md) | List of prompts matching the search criteria | 
**count** | **int** | Total number of prompts matching the search criteria | 
**next** | **str** | URL for the next page of results | 
**previous** | **str** | URL for the previous page of results | 
**current_page** | **int** | Current page number | 
**num_pages** | **int** | Total number of pages | 
**facets** | [**Dict[str, PromptFacet]**](PromptFacet.md) | Facet information for filtering | [optional] 

## Example

```python
from iblai.models.prompt_search_response import PromptSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSearchResponse from a JSON string
prompt_search_response_instance = PromptSearchResponse.from_json(json)
# print the JSON string representation of the object
print(PromptSearchResponse.to_json())

# convert the object into a dict
prompt_search_response_dict = prompt_search_response_instance.to_dict()
# create an instance of PromptSearchResponse from a dict
prompt_search_response_from_dict = PromptSearchResponse.from_dict(prompt_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


