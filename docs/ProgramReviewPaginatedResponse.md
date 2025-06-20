# ProgramReviewPaginatedResponse

Paginated response serializer for ProgramReviewQueryView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of reviews | 
**next_page** | **int** | Next page number | 
**previous_page** | **int** | Previous page number | 
**results** | [**List[ProgramReview]**](ProgramReview.md) | List of program reviews | 

## Example

```python
from iblai.models.program_review_paginated_response import ProgramReviewPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramReviewPaginatedResponse from a JSON string
program_review_paginated_response_instance = ProgramReviewPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramReviewPaginatedResponse.to_json())

# convert the object into a dict
program_review_paginated_response_dict = program_review_paginated_response_instance.to_dict()
# create an instance of ProgramReviewPaginatedResponse from a dict
program_review_paginated_response_from_dict = ProgramReviewPaginatedResponse.from_dict(program_review_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


