# PaginatedCourseInvitation

Response serializer for paginated course invitation list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseInvitationDetail]**](CourseInvitationDetail.md) | List of course invitations | 

## Example

```python
from iblai.models.paginated_course_invitation import PaginatedCourseInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseInvitation from a JSON string
paginated_course_invitation_instance = PaginatedCourseInvitation.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseInvitation.to_json())

# convert the object into a dict
paginated_course_invitation_dict = paginated_course_invitation_instance.to_dict()
# create an instance of PaginatedCourseInvitation from a dict
paginated_course_invitation_from_dict = PaginatedCourseInvitation.from_dict(paginated_course_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


