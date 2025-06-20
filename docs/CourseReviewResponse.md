# CourseReviewResponse

Response serializer for CourseReviewQueryView GET endpoint. Matches the actual structure returned by review.to_json()

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID of the reviewer | 
**course_id** | **str** |  | [optional] 
**username** | **str** | Username of the reviewer | 
**content** | **str** | Review content | 
**rating** | **float** | Review rating | 
**title** | **str** | Review title | 
**visible** | **bool** | Whether review is visible | 
**created** | **datetime** | Review creation date | 
**modified** | **datetime** | Review modification date | 
**metadata** | **object** |  | 

## Example

```python
from iblai.models.course_review_response import CourseReviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseReviewResponse from a JSON string
course_review_response_instance = CourseReviewResponse.from_json(json)
# print the JSON string representation of the object
print(CourseReviewResponse.to_json())

# convert the object into a dict
course_review_response_dict = course_review_response_instance.to_dict()
# create an instance of CourseReviewResponse from a dict
course_review_response_from_dict = CourseReviewResponse.from_dict(course_review_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


