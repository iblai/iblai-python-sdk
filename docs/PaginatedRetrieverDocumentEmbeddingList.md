# PaginatedRetrieverDocumentEmbeddingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RetrieverDocumentEmbedding]**](RetrieverDocumentEmbedding.md) |  | 

## Example

```python
from iblai.models.paginated_retriever_document_embedding_list import PaginatedRetrieverDocumentEmbeddingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRetrieverDocumentEmbeddingList from a JSON string
paginated_retriever_document_embedding_list_instance = PaginatedRetrieverDocumentEmbeddingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRetrieverDocumentEmbeddingList.to_json())

# convert the object into a dict
paginated_retriever_document_embedding_list_dict = paginated_retriever_document_embedding_list_instance.to_dict()
# create an instance of PaginatedRetrieverDocumentEmbeddingList from a dict
paginated_retriever_document_embedding_list_from_dict = PaginatedRetrieverDocumentEmbeddingList.from_dict(paginated_retriever_document_embedding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


