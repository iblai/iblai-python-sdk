# CourseReviewPaginatedResponse

Paginated response serializer for CourseReviewQueryView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of reviews | 
**next_page** | **int** | Next page number | 
**previous_page** | **int** | Previous page number | 
**results** | **List[Dict[str, object]]** |  | 

## Example

```python
from iblai.models.course_review_paginated_response import CourseReviewPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseReviewPaginatedResponse from a JSON string
course_review_paginated_response_instance = CourseReviewPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(CourseReviewPaginatedResponse.to_json())

# convert the object into a dict
course_review_paginated_response_dict = course_review_paginated_response_instance.to_dict()
# create an instance of CourseReviewPaginatedResponse from a dict
course_review_paginated_response_from_dict = CourseReviewPaginatedResponse.from_dict(course_review_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


