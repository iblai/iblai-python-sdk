# PaginatedCourseLicenseAssignment

Response serializer for paginated course license assignment list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[CourseLicenseAssignmentDetail]**](CourseLicenseAssignmentDetail.md) | List of course license assignments | 

## Example

```python
from iblai.models.paginated_course_license_assignment import PaginatedCourseLicenseAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCourseLicenseAssignment from a JSON string
paginated_course_license_assignment_instance = PaginatedCourseLicenseAssignment.from_json(json)
# print the JSON string representation of the object
print(PaginatedCourseLicenseAssignment.to_json())

# convert the object into a dict
paginated_course_license_assignment_dict = paginated_course_license_assignment_instance.to_dict()
# create an instance of PaginatedCourseLicenseAssignment from a dict
paginated_course_license_assignment_from_dict = PaginatedCourseLicenseAssignment.from_dict(paginated_course_license_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


