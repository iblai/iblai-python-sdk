# RetrieverDocumentEmbedding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**metadata** | **object** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**training_status** | [**RetrieverDocumentEmbeddingTrainingStatus**](RetrieverDocumentEmbeddingTrainingStatus.md) |  | [optional] 
**pathway** | **str** |  | 
**url** | **str** |  | [optional] 
**tokens** | **int** |  | [optional] 
**platform_key** | **str** |  | 
**is_trained** | **bool** |  | [optional] 

## Example

```python
from iblai.models.retriever_document_embedding import RetrieverDocumentEmbedding

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverDocumentEmbedding from a JSON string
retriever_document_embedding_instance = RetrieverDocumentEmbedding.from_json(json)
# print the JSON string representation of the object
print(RetrieverDocumentEmbedding.to_json())

# convert the object into a dict
retriever_document_embedding_dict = retriever_document_embedding_instance.to_dict()
# create an instance of RetrieverDocumentEmbedding from a dict
retriever_document_embedding_from_dict = RetrieverDocumentEmbedding.from_dict(retriever_document_embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


