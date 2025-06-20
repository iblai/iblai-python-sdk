# PaginatedUserLicense

Response serializer for paginated user license list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[UserLicenseDetail]**](UserLicenseDetail.md) | List of user licenses | 

## Example

```python
from iblai.models.paginated_user_license import PaginatedUserLicense

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserLicense from a JSON string
paginated_user_license_instance = PaginatedUserLicense.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserLicense.to_json())

# convert the object into a dict
paginated_user_license_dict = paginated_user_license_instance.to_dict()
# create an instance of PaginatedUserLicense from a dict
paginated_user_license_from_dict = PaginatedUserLicense.from_dict(paginated_user_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


