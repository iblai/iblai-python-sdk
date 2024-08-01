# RetrieverRequestSearchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The source url of the docuemnt | 
**confidence_level** | **float** | The percentge confidence level of the document retrieved | 

## Example

```python
from iblai.models.retriever_request_search_document import RetrieverRequestSearchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverRequestSearchDocument from a JSON string
retriever_request_search_document_instance = RetrieverRequestSearchDocument.from_json(json)
# print the JSON string representation of the object
print(RetrieverRequestSearchDocument.to_json())

# convert the object into a dict
retriever_request_search_document_dict = retriever_request_search_document_instance.to_dict()
# create an instance of RetrieverRequestSearchDocument from a dict
retriever_request_search_document_from_dict = RetrieverRequestSearchDocument.from_dict(retriever_request_search_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


