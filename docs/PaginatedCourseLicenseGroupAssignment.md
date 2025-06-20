# PaginatedCourseLicenseGroupAssignment

Response serializer for paginated course license group assignment list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseLicenseGroupAssignmentDetail]**](CourseLicenseGroupAssignmentDetail.md) | List of course license group assignments | 

## Example

```python
from iblai.models.paginated_course_license_group_assignment import PaginatedCourseLicenseGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseLicenseGroupAssignment from a JSON string
paginated_course_license_group_assignment_instance = PaginatedCourseLicenseGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseLicenseGroupAssignment.to_json())

# convert the object into a dict
paginated_course_license_group_assignment_dict = paginated_course_license_group_assignment_instance.to_dict()
# create an instance of PaginatedCourseLicenseGroupAssignment from a dict
paginated_course_license_group_assignment_from_dict = PaginatedCourseLicenseGroupAssignment.from_dict(paginated_course_license_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


