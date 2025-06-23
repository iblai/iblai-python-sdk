# PaginatedAssertionsResponse

{         'next': self.get_next_link(),         'previous': self.get_previous_link(),         'count': self.page.paginator.count,         'data': data,         'num_pages': self.page.paginator.num_pages,         'page_number': self.page.number,         'max_page_size': self.max_page_size     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | 
**previous** | **str** |  | 
**count** | **int** |  | 
**num_pages** | **int** |  | 
**page_number** | **int** |  | 
**max_page_size** | **int** |  | 
**data** | [**List[Assertion]**](Assertion.md) |  | 

## Example

```python
from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssertionsResponse from a JSON string
paginated_assertions_response_instance = PaginatedAssertionsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedAssertionsResponse.to_json())

# convert the object into a dict
paginated_assertions_response_dict = paginated_assertions_response_instance.to_dict()
# create an instance of PaginatedAssertionsResponse from a dict
paginated_assertions_response_from_dict = PaginatedAssertionsResponse.from_dict(paginated_assertions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


