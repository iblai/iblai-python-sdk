# CourseReviewInfoResponse

Serializer for course review info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course ID associated with the reviews | 
**avg_rating** | **float** | Average rating of the course | 
**count** | **int** | Total number of reviews for the course | 

## Example

```python
from iblai.models.course_review_info_response import CourseReviewInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseReviewInfoResponse from a JSON string
course_review_info_response_instance = CourseReviewInfoResponse.from_json(json)
# print the JSON string representation of the object
print(CourseReviewInfoResponse.to_json())

# convert the object into a dict
course_review_info_response_dict = course_review_info_response_instance.to_dict()
# create an instance of CourseReviewInfoResponse from a dict
course_review_info_response_from_dict = CourseReviewInfoResponse.from_dict(course_review_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


