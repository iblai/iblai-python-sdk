# RetrieverDocumentEmbeddingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_name** | **str** | The name of the document | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**pathway** | **str** | The pathway to retrain the document in | 
**url** | **str** | The url of the document | [optional] 
**train** | **bool** | The type of the document | [optional] 

## Example

```python
from iblai.models.retriever_document_embedding_request import RetrieverDocumentEmbeddingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverDocumentEmbeddingRequest from a JSON string
retriever_document_embedding_request_instance = RetrieverDocumentEmbeddingRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieverDocumentEmbeddingRequest.to_json())

# convert the object into a dict
retriever_document_embedding_request_dict = retriever_document_embedding_request_instance.to_dict()
# create an instance of RetrieverDocumentEmbeddingRequest from a dict
retriever_document_embedding_request_from_dict = RetrieverDocumentEmbeddingRequest.from_dict(retriever_document_embedding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


