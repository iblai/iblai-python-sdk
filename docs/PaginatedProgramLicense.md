# PaginatedProgramLicense

Response serializer for paginated program license list.  This serializer represents a paginated list of program licenses, with navigation links and metadata.  Fields:     count: Total number of results matching the query     next: URL for the next page of results (null if no next page)     previous: URL for the previous page of results (null if no previous page)     results: List of program licenses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[ProgramLicenseDetail]**](ProgramLicenseDetail.md) | List of program licenses | 

## Example

```python
from iblai.models.paginated_program_license import PaginatedProgramLicense

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProgramLicense from a JSON string
paginated_program_license_instance = PaginatedProgramLicense.from_json(json)
# print the JSON string representation of the object
print(PaginatedProgramLicense.to_json())

# convert the object into a dict
paginated_program_license_dict = paginated_program_license_instance.to_dict()
# create an instance of PaginatedProgramLicense from a dict
paginated_program_license_from_dict = PaginatedProgramLicense.from_dict(paginated_program_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


