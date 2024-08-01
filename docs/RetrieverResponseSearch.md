# RetrieverResponseSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PageContent]**](PageContent.md) | Docs from similarity search | 

## Example

```python
from iblai.models.retriever_response_search import RetrieverResponseSearch

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverResponseSearch from a JSON string
retriever_response_search_instance = RetrieverResponseSearch.from_json(json)
# print the JSON string representation of the object
print(RetrieverResponseSearch.to_json())

# convert the object into a dict
retriever_response_search_dict = retriever_response_search_instance.to_dict()
# create an instance of RetrieverResponseSearch from a dict
retriever_response_search_from_dict = RetrieverResponseSearch.from_dict(retriever_response_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


