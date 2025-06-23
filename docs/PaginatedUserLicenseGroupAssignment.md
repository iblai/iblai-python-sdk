# PaginatedUserLicenseGroupAssignment

Response serializer for paginated user license group assignment list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[UserLicenseGroupAssignmentDetail]**](UserLicenseGroupAssignmentDetail.md) | List of user license group assignments | 

## Example

```python
from iblai.models.paginated_user_license_group_assignment import PaginatedUserLicenseGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserLicenseGroupAssignment from a JSON string
paginated_user_license_group_assignment_instance = PaginatedUserLicenseGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserLicenseGroupAssignment.to_json())

# convert the object into a dict
paginated_user_license_group_assignment_dict = paginated_user_license_group_assignment_instance.to_dict()
# create an instance of PaginatedUserLicenseGroupAssignment from a dict
paginated_user_license_group_assignment_from_dict = PaginatedUserLicenseGroupAssignment.from_dict(paginated_user_license_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


