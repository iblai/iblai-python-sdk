# PaginatedPlatformLicense

Response serializer for paginated platform license list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Total number of results | 
**next_page** | **str** | URL for next page of results | 
**previous_page** | **str** | URL for previous page of results | 
**results** | [**List[PlatformLicenseDetail]**](PlatformLicenseDetail.md) | List of platform licenses | 

## Example

```python
from iblai.models.paginated_platform_license import PaginatedPlatformLicense

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlatformLicense from a JSON string
paginated_platform_license_instance = PaginatedPlatformLicense.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlatformLicense.to_json())

# convert the object into a dict
paginated_platform_license_dict = paginated_platform_license_instance.to_dict()
# create an instance of PaginatedPlatformLicense from a dict
paginated_platform_license_from_dict = PaginatedPlatformLicense.from_dict(paginated_platform_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


