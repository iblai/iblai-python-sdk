# LearnerListPagination

Serializer for learner list pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Current page number | 
**limit** | **int** | Records per page | 
**total_pages** | **int** | Total number of pages | 
**total_records** | **int** | Total number of records | 
**has_next** | **bool** | Whether there is a next page | 
**has_previous** | **bool** | Whether there is a previous page | 
**next_page** | **int** | Next page number | 
**previous_page** | **int** | Previous page number | 

## Example

```python
from iblai.models.learner_list_pagination import LearnerListPagination

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerListPagination from a JSON string
learner_list_pagination_instance = LearnerListPagination.from_json(json)
# print the JSON string representation of the object
print(LearnerListPagination.to_json())

# convert the object into a dict
learner_list_pagination_dict = learner_list_pagination_instance.to_dict()
# create an instance of LearnerListPagination from a dict
learner_list_pagination_from_dict = LearnerListPagination.from_dict(learner_list_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


