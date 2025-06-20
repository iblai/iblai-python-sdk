# CourseEnrollmentSearchResponse

Serializer for course enrollment search results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID associated with the enrollment | 
**username** | **str** | Username associated with the enrollment | 
**email** | **str** | Email of the user | 
**course_id** | **str** | Course ID associated with the enrollment | 
**active** | **bool** | Whether the enrollment is active | 
**created** | **datetime** | Date when enrollment began/activated | 
**started** | **datetime** | Date when enrollment started | 
**ended** | **datetime** | Date when enrollment ended/deactivated | 
**expired** | **datetime** | Date when enrollment expires | 
**metadata** | **object** | Enrollment specific metadata | 
**name** | **str** | Full name of the user | 
**course_name** | **str** | Name of the course | 

## Example

```python
from iblai.models.course_enrollment_search_response import CourseEnrollmentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEnrollmentSearchResponse from a JSON string
course_enrollment_search_response_instance = CourseEnrollmentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CourseEnrollmentSearchResponse.to_json())

# convert the object into a dict
course_enrollment_search_response_dict = course_enrollment_search_response_instance.to_dict()
# create an instance of CourseEnrollmentSearchResponse from a dict
course_enrollment_search_response_from_dict = CourseEnrollmentSearchResponse.from_dict(course_enrollment_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


