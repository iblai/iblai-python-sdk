# CourseReviewRequest

Request serializer for CourseReviewUpdateView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course ID to review | 
**username** | **str** | The username of the reviewer | 
**user_id** | **int** | The user ID of the reviewer (alternative to username) | [optional] 
**rating** | **float** | The rating value (typically 1-5) | [optional] 
**title** | **str** | The review title | [optional] 
**content** | **str** | The review content/text | [optional] 
**visible** | **bool** | Whether the review is visible | [optional] [default to True]
**metadata** | **object** | Additional review metadata | [optional] 

## Example

```python
from iblai.models.course_review_request import CourseReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseReviewRequest from a JSON string
course_review_request_instance = CourseReviewRequest.from_json(json)
# print the JSON string representation of the object
print(CourseReviewRequest.to_json())

# convert the object into a dict
course_review_request_dict = course_review_request_instance.to_dict()
# create an instance of CourseReviewRequest from a dict
course_review_request_from_dict = CourseReviewRequest.from_dict(course_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


