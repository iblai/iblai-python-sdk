# ContentPagination

Serializer for content pagination metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of items | 
**next** | **str** | URL for next page | [optional] 
**previous** | **str** | URL for previous page | [optional] 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from iblai.models.content_pagination import ContentPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ContentPagination from a JSON string
content_pagination_instance = ContentPagination.from_json(json)
# print the JSON string representation of the object
print(ContentPagination.to_json())

# convert the object into a dict
content_pagination_dict = content_pagination_instance.to_dict()
# create an instance of ContentPagination from a dict
content_pagination_from_dict = ContentPagination.from_dict(content_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


