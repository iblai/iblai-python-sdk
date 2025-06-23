# PaginatedCourseAccessRequest

Response serializer for paginated access request list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseAccessRequestDetail]**](CourseAccessRequestDetail.md) | List of access requests | 

## Example

```python
from iblai.models.paginated_course_access_request import PaginatedCourseAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseAccessRequest from a JSON string
paginated_course_access_request_instance = PaginatedCourseAccessRequest.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseAccessRequest.to_json())

# convert the object into a dict
paginated_course_access_request_dict = paginated_course_access_request_instance.to_dict()
# create an instance of PaginatedCourseAccessRequest from a dict
paginated_course_access_request_from_dict = PaginatedCourseAccessRequest.from_dict(paginated_course_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


