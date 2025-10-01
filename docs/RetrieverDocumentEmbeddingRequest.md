# RetrieverDocumentEmbeddingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_name** | **str** | The name of the document | [optional] 
**document_type** | **str** | The type of the document | [optional] 
**pathway** | **str** | The pathway to retrain the document in | 
**url** | **str** | The url of the document | [optional] 
**train** | **bool** | The type of the document | [optional] 
**crawler_max_depth** | **int** | The max depth of the crawler | [optional] 
**crawler_max_pages_limit** | **int** | The max pages limit of the crawler | [optional] 
**crawler_max_concurrency** | **int** | The max concurrency of the crawler | [optional] 
**crawler_match_patterns** | **List[str]** | The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in &#x60;crawler_pattern_type&#x60;. | [optional] 
**crawler_pattern_type** | [**CrawlerPatternTypeEnum**](CrawlerPatternTypeEnum.md) | Pattern type for the crawler  * &#x60;glob&#x60; - Glob * &#x60;regex&#x60; - Regex | [optional] 
**access** | [**AccessEnum**](AccessEnum.md) | The access of the document.  * &#x60;public&#x60; - Public * &#x60;private&#x60; - Private | [optional] 
**google_drive_auth_data** | **object** | Authentication and scoped details of google drive. | [optional] 
**dropbox_auth_data** | **object** | Authentication and scoped details of dropbox | [optional] 
**custom_metadata** | **object** | Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. | [optional] 

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


