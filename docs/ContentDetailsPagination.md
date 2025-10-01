# ContentDetailsPagination

Serializer for pagination information in content details response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total learner records | 
**next** | **str** | Relative URL for the next page | [optional] 
**previous** | **str** | Relative URL for the previous page | [optional] 
**current_page** | **int** | Current page number | 
**total_pages** | **int** | Total number of pages | 

## Example

```python
from iblai.models.content_details_pagination import ContentDetailsPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDetailsPagination from a JSON string
content_details_pagination_instance = ContentDetailsPagination.from_json(json)
# print the JSON string representation of the object
print(ContentDetailsPagination.to_json())

# convert the object into a dict
content_details_pagination_dict = content_details_pagination_instance.to_dict()
# create an instance of ContentDetailsPagination from a dict
content_details_pagination_from_dict = ContentDetailsPagination.from_dict(content_details_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


