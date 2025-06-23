# PaginatedUserLicenseAssignment

Response serializer for paginated user license assignment list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[UserLicenseAssignmentDetail]**](UserLicenseAssignmentDetail.md) | List of user license assignments | 

## Example

```python
from iblai.models.paginated_user_license_assignment import PaginatedUserLicenseAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserLicenseAssignment from a JSON string
paginated_user_license_assignment_instance = PaginatedUserLicenseAssignment.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserLicenseAssignment.to_json())

# convert the object into a dict
paginated_user_license_assignment_dict = paginated_user_license_assignment_instance.to_dict()
# create an instance of PaginatedUserLicenseAssignment from a dict
paginated_user_license_assignment_from_dict = PaginatedUserLicenseAssignment.from_dict(paginated_user_license_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


