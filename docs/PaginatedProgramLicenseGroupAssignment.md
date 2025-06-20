# PaginatedProgramLicenseGroupAssignment

Response serializer for paginated program license group assignment list.  This serializer represents a paginated list of program license group assignments, with navigation links and metadata.  Fields:     count: Total number of results matching the query     next: URL for the next page of results (null if no next page)     previous: URL for the previous page of results (null if no previous page)     results: List of program license group assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[ProgramLicenseGroupAssignmentDetail]**](ProgramLicenseGroupAssignmentDetail.md) | List of program license group assignments | 

## Example

```python
from iblai.models.paginated_program_license_group_assignment import PaginatedProgramLicenseGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProgramLicenseGroupAssignment from a JSON string
paginated_program_license_group_assignment_instance = PaginatedProgramLicenseGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(PaginatedProgramLicenseGroupAssignment.to_json())

# convert the object into a dict
paginated_program_license_group_assignment_dict = paginated_program_license_group_assignment_instance.to_dict()
# create an instance of PaginatedProgramLicenseGroupAssignment from a dict
paginated_program_license_group_assignment_from_dict = PaginatedProgramLicenseGroupAssignment.from_dict(paginated_program_license_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


