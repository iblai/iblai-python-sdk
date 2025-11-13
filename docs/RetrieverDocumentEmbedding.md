# RetrieverDocumentEmbedding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**metadata** | **object** |  | [optional] 
**document_name** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**username** | **str** |  | 
**training_status** | **str** |  | [optional] 
**pathway** | **str** |  | 
**url** | **str** |  | [optional] 
**tokens** | **int** |  | [optional] 
**platform_key** | **str** |  | 
**is_trained** | **bool** |  | [optional] 
**access** | **str** |  | [optional] 
**crawler_max_depth** | **int** |  | [optional] 
**crawler_max_pages_limit** | **int** |  | [optional] 
**crawler_max_concurrency** | **int** |  | [optional] 
**crawler_match_patterns** | **object** | List of patterns that the crawler should use to match urls.          Patterns may be a glob pattern or a full regex pattern.          Indicate the specified type in &#x60;crawler_pattern_type&#x60;. | [optional] 
**crawler_pattern_type** | **str** |  | [optional] 
**last_trained_at** | **datetime** |  | [readonly] 

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


