# TrainDocumentViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathway** | **str** | Pathway for document to be trained in | [optional] 
**url** | **str** | Url of the document to be trained | [optional] 
**text** | **str** | Search text for wikipedia | [optional] 
**type** | **str** | Type of document e.g file | 
**translate** | **bool** | If file should be translated | [optional] [default to False]
**file** | **bytearray** | File to be trained | [optional] 
**access** | **str** | Accessibilityto the file | [optional] [default to 'private']
**branch** | **str** | Branch of the repository | [optional] 
**google_drive_auth_data** | **object** | Authentication and scoped details of google drive | [optional] 
**dropbox_auth_data** | **object** | Authentication and scoped details of dropbox | [optional] 
**crawler_max_depth** | **int** | The max depth of the crawler | [optional] 
**crawler_max_pages_limit** | **int** | The max pages limit of the crawler | [optional] 
**crawler_max_concurrency** | **int** | The max concurrency of the crawler | [optional] 
**crawler_match_patterns** | **List[str]** | The patterns that the crawler should use to match urls. Patterns may be a glob pattern or a full regex pattern. Indicate the specified type in &#x60;crawler_pattern_type&#x60;. | [optional] 
**crawler_pattern_type** | [**CrawlerPatternTypeEnum**](CrawlerPatternTypeEnum.md) | Pattern type for the crawler  * &#x60;glob&#x60; - Glob * &#x60;regex&#x60; - Regex | [optional] 
**custom_metadata** | **object** | Custom metadata to attach to the trained document. Must be a flat JSON object with string keys and string, number, or boolean values. | [optional] 
**add_to_document_pool** | **bool** | Adds document to the pool or not. | [optional] [default to False]
**document_pool_only** | **bool** | Only adds document to document pool. Requires pathway to be empty. | [optional] [default to False]
**user_image_description** | **str** | Description of an image submitted by the user for RAG. | [optional] 

## Example

```python
from iblai.models.train_document_view_request import TrainDocumentViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrainDocumentViewRequest from a JSON string
train_document_view_request_instance = TrainDocumentViewRequest.from_json(json)
# print the JSON string representation of the object
print(TrainDocumentViewRequest.to_json())

# convert the object into a dict
train_document_view_request_dict = train_document_view_request_instance.to_dict()
# create an instance of TrainDocumentViewRequest from a dict
train_document_view_request_from_dict = TrainDocumentViewRequest.from_dict(train_document_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


