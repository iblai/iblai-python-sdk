# RetrieverRequestSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query for similarity search | 
**pathway** | **str** | The pathway of the docs | 

## Example

```python
from iblai.models.retriever_request_search import RetrieverRequestSearch

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverRequestSearch from a JSON string
retriever_request_search_instance = RetrieverRequestSearch.from_json(json)
# print the JSON string representation of the object
print(RetrieverRequestSearch.to_json())

# convert the object into a dict
retriever_request_search_dict = retriever_request_search_instance.to_dict()
# create an instance of RetrieverRequestSearch from a dict
retriever_request_search_from_dict = RetrieverRequestSearch.from_dict(retriever_request_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


